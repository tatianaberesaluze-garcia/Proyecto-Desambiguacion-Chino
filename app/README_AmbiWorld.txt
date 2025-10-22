# AmbiWorld App

AmbiWorld es una demo interactiva desarrollada en Streamlit que visualiza los diferentes significados de palabras ambiguas en chino mandarín mediante un sistema inspirado en órbitas planetarias.

Esta app es parte de un proyecto de investigación sobre desambiguación semántica en chino, combinando procesamiento del lenguaje natural, clasificación contextual y visualización interactiva.

---

¿Qué hace?

- Permite seleccionar una palabra china ambigua.
- Muestra sus significados como planetas orbitando alrededor del término central.
- Al pasar el ratón sobre cada significado, se muestra:
  - Una frase de ejemplo en chino.
  - Su traducción al español.
  - El pinyin (pronunciación).
Y el audio

---

 Tecnologías utilizadas

- Python 3.8+
- Streamlit
- Plotly
- Pandas
- NumPy

---

## Estructura del proyecto

ambiworld_app.py         # Código principal de la app
datos.csv                # Dataset de palabras ambiguas y ejemplos
Audio                    # carpeta de audios generados
imagenes/                #  futuras extensiones visuales

## 🧠 Archivos del modelo entrenado

El proyecto incluye dos archivos esenciales para el funcionamiento de la aplicación **AmbiWorld**, ubicados en la carpeta `/app/`:

| Archivo | Descripción | Función |
|----------|--------------|----------|
| `modelo_clase_gr.pkl` | Modelo de IA entrenado mediante técnicas de *Machine Learning* para predecir el significado contextual de palabras chinas ambiguas. | Realiza la clasificación semántica en la aplicación. |
| `vectorizer_clase_gr.pkl` | Vectorizador de texto (TF-IDF o similar) utilizado durante el entrenamiento. Convierte las frases en vectores numéricos compatibles con el modelo. | Preprocesa los textos de entrada antes de la predicción. |

⚠️ Ambos archivos son **necesarios** para que la aplicación funcione correctamente.
---

 Requisitos de instalación

pip install streamlit plotly pandas numpy

---

## ¿Cómo ejecutar la aplicación?

1. Coloca el archivo ambiworld_app.py y archivos con datos.csv en el mismo directorio.
2. Abre tu terminal o consola.
3. Ejecuta:

streamlit run ambiworld_app.py

4. Se abrirá automáticamente en el navegador predeterminado (http://localhost:8501).

---

Objetivo del proyecto

AmbiWorld busca hacer accesible y visual la comprensión de las múltiples acepciones de palabras ambiguas en chino, utilizando una representación gráfica intuitiva y educativa.
Apoya tanto a estudiantes de chino como a investigadores en procesamiento de lenguaje natural.

---
## 🔊 Archivos de audio

La aplicación incluye audios de pronunciación en chino mandarín asociados a cada palabra ambigua.  
Los detalles técnicos (formato, estructura y descarga) están documentados en:

👉 [readme-audios](app/audios/readme-audios)

Solo se incluyen cien audios de ejemplo.
Los audios completos utilizados en la versión original del proyecto pueden solicitarse a la autora.

🔍 Posibles Aplicaciones
	•	Aprendizaje de idiomas asistido por IA.
	•	Mejora de traductores automáticos multilingües.
	•	Clasificación semántica de texto.
	•	Modelos de comprensión del lenguaje aplicados a la educación.

⸻

👩‍💻 Autora

Tatiana Beresaluze García
Estratega en Inteligencia Artificial, Innovación y Marketing Digital
📧 tatiana.beresaluze@gmail.com


⸻

🧭 Licencia

Este proyecto se publica con fines educativos y de investigación.
Licencia: MIT License © 2025 Tatiana Beresaluze

