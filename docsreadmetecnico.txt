
README - PARTE 1: Procesamiento de Palabras Ambiguas del CC-CEDICT
==================================================================

Objetivo:
---------
Extraer palabras ambiguas del diccionario chino-inglés CC-CEDICT para entrenar modelos de desambiguación semántica.

Metodología:
------------
1. Descarga y descompresión del diccionario CC-CEDICT.
2. Filtrado de palabras ambiguas (con más de un significado).
3. Opcionalmente traducir al español.

Requisitos:
-----------
- Python 3.x, pandas, wget, gzip.

Resultados:
-----------
- CSV con palabras ambiguas.

Aplicaciones:
-------------
- Modelos PLN para desambiguación.
- Educación en chino.



PARTE 2: Extracción de Frases con Palabras Ambiguas
=============================================================

Objetivo:
---------
Extraer frases en chino que contengan palabras ambiguas desde un corpus paralelo.

Metodología:
------------
1. Cargar corpus bilingüe.
2. Filtrar frases en chino.
3. Detectar palabras ambiguas en frases.
4. Exportar frases contextualizadas.

Requisitos:
-----------
- Python 3.x, pandas, json.

Resultados:
-----------
- CSV con frases chinas, traducción y palabras ambiguas.

Aplicaciones:
-------------
- Modelos de PLN contextuales.
- Material didáctico para aprendizaje.



PARTE 3: Fusión y Entreno (fusion_archivos_y_entreno2)
================================================================

Objetivo:
---------
Generar un dataset etiquetado combinando frases traducidas con palabras ambiguas, y entrenar un modelo de clasificación para desambiguar palabras chinas en contexto.

Metodología:
------------
1. Fusionar datasets.
2. Etiquetar automáticamente el significado correcto.
3. Generar embeddings multilingües.
4. Entrenar un clasificador (LogisticRegression).

Requisitos:
-----------
- Python 3.8+, pandas, spacy, sentence-transformers, scikit-learn.

Resultados:
-----------
- CSV final con etiquetas.
- Modelo clasificador (joblib).

Aplicaciones:
-------------
- Desambiguación semántica automática en textos chinos.

Conclusión:
-----------
Desambiguar automáticamente palabras en chino según contexto.

