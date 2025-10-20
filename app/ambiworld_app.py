
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

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
        if pd.notna(row['audio_url']):
            st.audio(row['audio_url'], format="audio/mp3")
