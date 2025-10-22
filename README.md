# Proyecto-Desambiguacion-Chino
Modelo de IA para predecir el significado contextual de palabras chinas usando NLP y embeddings multilingües.

# 🧠 Desambiguación de Palabras Chinas con un Modelo de Inteligencia Artificial  

## 📖 Descripción del Proyecto  
Este proyecto tiene como objetivo resolver la **ambigüedad semántica** de palabras chinas mediante técnicas de **Procesamiento del Lenguaje Natural (NLP)**.  
Se desarrolló un modelo capaz de **predecir el significado correcto de una palabra ambigua según el contexto**, utilizando *embeddings* multilingües y clasificación supervisada.

El proyecto culmina con **AmbiWorld**, una aplicación interactiva desarrollada en **Streamlit** que permite probar el modelo en tiempo real.

---

## 🎯 Objetivos Principales  
- Analizar y predecir el significado contextual de palabras chinas con múltiples traducciones.  
- Entrenar un modelo de *Machine Learning supervisado* utilizando *Sentence Embeddings*.  
- Crear una interfaz visual sencilla para demostrar el funcionamiento del modelo.  

---

## 🧩 Pipeline del Proyecto  

1. **Recolección de Datos**  
   - Fuente: [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict)  
   - Extracción de 300 palabras chinas con múltiples significados.  
   - Traducción al español para generar un corpus multilingüe.  

2. **Preprocesamiento y Limpieza**  
   - Normalización de caracteres chinos.  
   - Etiquetado manual de significados.  
   - Eliminación de duplicados y desbalanceo de clases.  

3. **Vectorización Semántica**  
   - Uso de *SentenceTransformers* para generar *embeddings* multilingües (chino–español).  
   - Representación numérica de cada frase contextualizada.  

4. **Entrenamiento del Modelo**  
   - Clasificación mediante **Regresión Logística (Scikit-learn)**.  
   - Evaluación con *Accuracy* y *F1-score*.  
   - Guardado del modelo con *Joblib* para uso posterior.  

5. **Despliegue de la Aplicación**  
   - Creación de la app **AmbiWorld** en *Streamlit*.  
   - Interfaz que permite seleccionar una palabra y obtener su significado más probable según el contexto.  

---

## 🧠 Tecnologías Utilizadas  

| Categoría | Herramientas |
|------------|---------------|
| Lenguaje | Python 🐍 |
| Librerías principales | Pandas, NumPy, Scikit-learn, SentenceTransformers |
| Deep Learning | TensorFlow, Keras |
| Visualización | Matplotlib, Seaborn |
| App / Despliegue | Streamlit |
| Control de versiones | Git & GitHub |
| Guardado de modelo | Joblib |

---

## 📁 Estructura del Repositorio  
Proyecto-Desambiguacion-Chino/
├── app/                                ← Aplicación Streamlit (AmbiWorld)
│   ├── ambiworld_app.py                ← Código principal de la app
│   └── audio/                          ← Audios de ejemplo (100)
│       data/                               ← Archivos de datos
│   ├── app_data/                       ← Datos que usa la app AmbiWorld
│   │   └── datos.csv
├── project_data/                   ← Datasets para entrenamiento y validación
│   │   ├── top_300_ambiguas_completo.csv
│   │   ├── frases_enriquecidas.csv
│   │   ├── frases_etiquetadas.csv
│   │   ├── frases_etiquetadas_corregidas.csv
│   │   ├── frases_traducidas_500.csv
│   │   └── frases_fusionadas.csv
 │   │   └── sentences.csv              ← Archivo original del corpus multilingüe **Tatoeba**, con millones de frases y metadatos de idioma. Debido a su gran tamaño, **no se incluye en este repositorio**, pero se utilizó como fuente principal de datos para el filtrado. | Fuente de datos original (no incluida por limitaciones de tamaño). 
> Se encuentra disponible públicamente en [https://tatoeba.org](https://tatoeba.org) y fue utilizado únicamente como fuente de extracción.
 │   │   └── sentences_es_300.csv       ←  Subconjunto con frases exclusivamente en **español**. 
│   │   └── sentences_zh_300.csv        ← Subconjunto con frases exclusivamente en **chino mandarín**.  del archivo original del corpus multilingüe **Tatoeba**
		
│   └── dictionaries/                   ← Diccionarios base
│       ├── cedict_0_0_ts_utf-8_mdbg_20250424_130919.txt
│       └── dict.txt
│
├── notebooks/                          ← Notebooks de desarrollo
│   ├── 1_preprocesamiento_y_limpieza.ipynb
│   ├── 2_extraccion_frases_ambiguas.ipynb
│   └── 3_fusion_y_entrenamiento_modelo.ipynb
│
├── models/                             ← Modelos entrenados
│   └── modelo_desambiguacion.joblib
│   └── modelo_clase_gr.pkl            ← Modelo de IA entrenado mediante técnicas de *Machine Learning* para predecir el significado contextual de palabras chinas ambiguas. | Realiza la clasificación semántica en la aplicación. 
│   └── vectorizer_clase_gr.pkl       ← Vectorizador de texto (TF-IDF o similar) utilizado durante el entrenamiento. Convierte las frases en vectores numéricos compatibles con el modelo. | Preprocesa los textos de entrada antes de la predicción. |
⚠️ Ambos archivos son **necesarios** para que la aplicación funcione correctamente.
│
├── docs/                               ← Presentaciones y documentación 
│   ├── Presentacion_Proyecto.pdf  **no se incluye en este repositorio**,
│   └── README_TECNICO.md
│
├── requirements.txt                    ← Dependencias del proyecto
├── README.md                           ← Este archivo
└── LICENSE                             ← Licencia MIT

---


 
Requisitos de instalación:

pip install streamlit plotly pandas numpy

---

## ¿Cómo ejecutar la aplicación?

1. Coloca el archivo ambiworld_app.py y archivos con datos.csv en el mismo directorio.
2. Abre tu terminal o consola.
3. Ejecuta:

streamlit run ambiworld_app.py

4. Se abrirá automáticamente en el navegador predeterminado (http://localhost:8501).




🎧 Archivos de audio

La aplicación incluye audios en formato `.mp3` con pronunciaciones en **chino mandarín**, asociados a cada palabra ambigua.  
Estos archivos permiten escuchar la palabra y su pinyin dentro de la app AmbiWorld.

📂 Carpeta: `/app/audio/`  
🎧 Detalles técnicos y enlace de descarga: [readme-audios](app/audio/readme-audios)
Se incluyen cien audios de ejemplo.
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

