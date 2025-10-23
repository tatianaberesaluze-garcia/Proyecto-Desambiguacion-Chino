
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

from pathlib import Path


APP_DIR = Path(__file__).parent

AUDIO_DIR = APP_DIR / "audio"

def try_play_audio(row):
    """
    Busca <palabra>.mp3 en:
      - AmbiWorld_appDemo copia 2/audio/<palabra>.mp3
      - Y en todas las subcarpetas (audios1/, audios2/, audios3/)
    """
    if "palabra" not in row or not isinstance(row["palabra"], str) or not row["palabra"].strip():
        st.info("🔇 No hay 'palabra' válida para buscar audio.")
        return

    fname = f"{row['palabra']}.mp3"

    # 1) audio/<palabra>.mp3
    direct = AUDIO_DIR / fname
    if direct.exists():
        etiqueta = row.get('pinyin', row['palabra'])
        st.caption(f"🔊 Pronunciación: {etiqueta}")
        st.audio(str(direct), format="audio/mp3")
        return

    # 2) Cualquier subcarpeta dentro de audio/ (audios1, audios2, audios3…)
    if AUDIO_DIR.exists():
        for encontrado in APP_DIR.rglob(fname):
            etiqueta = row.get('pinyin', row['palabra'])
            st.caption(f"🔊 Pronunciación: {etiqueta}")
            st.audio(str(encontrado), format="audio/mp3")
            return

    st.info(f"🔇 No encuentro `{fname}` en la carpeta `audio/`.")


@st.cache_data
def cargar_datos():
    return pd.read_csv("datos.csv")

df = cargar_datos()

st.title("🌍 AmbiWorld: Visualizador de Palabras Chinas Ambiguas")

# Lista de palabras ordenadas por score
palabras = df[['palabra', 'score']].drop_duplicates().sort_values(by='score', ascending=False)['palabra']
palabra = st.selectbox("Selecciona una palabra ambigua:", palabras)

# Filtrar significados por palabra
df_filtrado = df[df['palabra'] == palabra]

def mostrar_orbitas(df):
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers+text',
        marker=dict(size=30, color='blue'),
        text=[df.iloc[0]['palabra']],
        textposition="top center",
        name="Palabra central"
    ))

    angulos = np.linspace(0, 2 * np.pi, len(df), endpoint=False)
    radio = 3

    for i, (index, row) in enumerate(df.iterrows()):
        x = radio * np.cos(angulos[i])
        y = radio * np.sin(angulos[i])
        fig.add_trace(go.Scatter(
            x=[x], y=[y],
            mode='markers+text',
            marker=dict(size=20),
            text=[row['sentido']],
            textposition="top center",
            name=row['sentido'],
            hovertext=f"{row['ejemplo']} ({row['traduccion']})\nPinyin: {row['pinyin']}",
            hoverinfo="text"
        ))

    fig.update_layout(
        showlegend=False,
        margin=dict(t=20, l=20, r=20, b=20),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        height=500,
        title=f"Visualización Semántica de '{df.iloc[0]['palabra']}'"
    )

    st.plotly_chart(fig)

mostrar_orbitas(df_filtrado)

st.subheader("Detalles de los significados:")
for i, row in df_filtrado.iterrows():
    with st.expander(row['sentido']):
        st.markdown(f"**Ejemplo:** {row['ejemplo']}")
        st.markdown(f"**Traducción:** {row['traduccion']}")
        st.markdown(f"**Pinyin:** {row['pinyin']}")
        try_play_audio(row)
