import streamlit as st
import json
from pathlib import Path

st.set_page_config(
    page_title="Agente Gastronómico",
    page_icon="🍳",
    layout="centered"
)

st.title("🍳 Agente Gastronómico")
st.write(
    "Tu asistente para consultar recetas, "
    "ingredientes y procedimientos culinarios."
)

RUTA_RECETAS = Path(__file__).parent / "recetas.json"

def cargar_recetas():
    if RUTA_RECETAS.exists():
        with open(RUTA_RECETAS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

recetas = cargar_recetas()

pregunta = st.text_input(
    "¿Qué receta o técnica culinaria quieres consultar?",
    placeholder="Ejemplo: ¿Cómo preparo arroz con pollo?"
)

if pregunta:
    resultados = [
        receta for receta in recetas
        if pregunta.lower() in json.dumps(
            receta, ensure_ascii=False
        ).lower()
    ]

    if resultados:
        for receta in resultados:
            st.subheader(receta["nombre"])
            st.write("**Ingredientes:**")
            for ingrediente in receta["ingredientes"]:
                st.write(f"- {ingrediente}")

            st.write("**Preparación:**")
            for paso in receta["preparacion"]:
                st.write(f"- {paso}")
    else:
        st.info(
            "No encontré una coincidencia exacta en la "
            "base de recetas. Prueba con el nombre del plato "
            "o un ingrediente."
        )

with st.expander("Ver recetas disponibles"):
    for receta in recetas:
        st.write(f"- {receta['nombre']}")

st.caption(
    "Versión inicial de prueba. "
    "Las respuestas provienen de las recetas registradas."
)
