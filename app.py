import streamlit as st
import json
from pathlib import Path

st.set_page_config(
    page_title="Agente Gastronómico",
    page_icon="🍳",
    layout="wide"
)

st.title("🍳 Agente Gastronómico Colombiano")

st.write(
    "Consulta recetas, ingredientes, técnicas, procedimientos "
    "y soluciones a problemas comunes de la cocina colombiana."
)

# ---------------------------------------------------------
# CARGAR BASE DE CONOCIMIENTO
# ---------------------------------------------------------

RUTA_RECETAS = Path(__file__).parent / "recetas.json"


@st.cache_data
def cargar_recetas():

    if not RUTA_RECETAS.exists():
        return []

    try:

        with open(
            RUTA_RECETAS,
            "r",
            encoding="utf-8"
        ) as archivo:

            datos = json.load(archivo)

            if isinstance(datos, list):
                return datos
            return datos.get("recetas", [])

    except Exception as error:

        st.error(
            f"Error al cargar la base de conocimiento: {error}"
        )

        return []


recetas = cargar_recetas()


# ---------------------------------------------------------
# INFORMACIÓN DE LA BASE
# ---------------------------------------------------------

st.sidebar.header("📚 Base de conocimiento")

st.sidebar.metric(
    "Recetas disponibles",
    len(recetas)
)


# ---------------------------------------------------------
# BUSCADOR
# ---------------------------------------------------------

st.subheader("🔎 Buscar en la base gastronómica")

pregunta = st.text_input(
    "¿Qué quieres consultar?",
    placeholder=(
        "Ejemplo: arroz, arepa, ajiaco, "
        "pollo, Costa Caribe..."
    )
)


# ---------------------------------------------------------
# BÚSQUEDA
# ---------------------------------------------------------

if pregunta:

    texto_busqueda = pregunta.lower().strip()

    resultados = []

    for receta in recetas:

        texto_receta = json.dumps(
            receta,
            ensure_ascii=False
        ).lower()

        if texto_busqueda in texto_receta:

            resultados.append(receta)


    # -----------------------------------------------------
    # MOSTRAR RESULTADOS
    # -----------------------------------------------------

    if resultados:

        st.success(
            f"Encontré {len(resultados)} resultado(s)."
        )

        for receta in resultados:

            st.divider()

            st.header(
                f"🍽️ {receta.get('plato', 'Sin nombre')}"
            )


            # Información general

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"**Región:** "
                    f"{receta.get('region', 'No registrada')}"
                )

            with col2:

                st.write(
                    f"**Categoría:** "
                    f"{receta.get('categoria', 'No registrada')}"
                )

            with col3:

                st.write(
                    f"**Porciones:** "
                    f"{receta.get('porciones', 'No registradas')}"
                )


            # Descripción

            if receta.get("descripcion"):

                st.write(
                    f"**Descripción:** "
                    f"{receta['descripcion']}"
                )


            # -------------------------------------------------
            # INGREDIENTES
            # -------------------------------------------------

            st.subheader("🥕 Ingredientes")

            for ingrediente in receta.get(
                "ingredientes",
                []
            ):

                nombre = ingrediente.get(
                    "ingrediente",
                    ""
                )

                cantidad = ingrediente.get(
                    "cantidad",
                    ""
                )

                unidad = ingrediente.get(
                    "unidad",
                    ""
                )

                observacion = ingrediente.get(
                    "observacion",
                    ""
                )

                texto = (
                    f"- **{nombre}**: "
                    f"{cantidad} {unidad}"
                )

                if observacion:

                    texto += (
                        f" — {observacion}"
                    )

                st.markdown(texto)


            # -------------------------------------------------
            # PREPARACIÓN
            # -------------------------------------------------

            st.subheader("👨‍🍳 Preparación")

            pasos = receta.get(
                "preparacion",
                []
            )

            for paso in pasos:

                numero = paso.get(
                    "paso",
                    ""
                )

                instruccion = paso.get(
                    "instruccion",
                    ""
                )

                st.markdown(
                    f"**Paso {numero}:** "
                    f"{instruccion}"
                )


            # -------------------------------------------------
            # TÉCNICAS
            # -------------------------------------------------

            tecnicas = receta.get(
                "tecnicas",
                []
            )

            if tecnicas:

                st.subheader(
                    "🔪 Técnicas culinarias"
                )

                for tecnica in tecnicas:

                    nombre = tecnica.get(
                        "tecnica",
                        ""
                    )

                    descripcion = tecnica.get(
                        "descripcion",
                        ""
                    )

                    st.markdown(
                        f"**{nombre}:** "
                        f"{descripcion}"
                    )


            # -------------------------------------------------
            # ERRORES Y SOLUCIONES
            # -------------------------------------------------

            errores = receta.get(
                "errores_y_soluciones",
                []
            )

            if errores:

                st.subheader(
                    "⚠️ Problemas y soluciones"
                )

                for error in errores:

                    problema = error.get(
                        "problema",
                        ""
                    )

                    causa = error.get(
                        "posible_causa",
                        ""
                    )

                    solucion = error.get(
                        "solucion",
                        ""
                    )

                    st.markdown(
                        f"**Problema:** {problema}"
                    )

                    st.markdown(
                        f"**Posible causa:** {causa}"
                    )

                    st.markdown(
                        f"**Solución:** {solucion}"
                    )


            # -------------------------------------------------
            # FUENTES
            # -------------------------------------------------

            fuentes = receta.get(
                "fuentes",
                []
            )

            if fuentes:

                with st.expander(
                    "📚 Fuente de información"
                ):

                    for fuente in fuentes:

                        st.write(
                            f"**Fuente:** "
                            f"{fuente.get('fuente', '')}"
                        )

                        st.write(
                            f"**Tipo:** "
                            f"{fuente.get('tipo', '')}"
                        )


    else:

        st.warning(
            "No encontré una coincidencia. "
            "Prueba con el nombre de un plato, "
            "un ingrediente o una región."
        )


# ---------------------------------------------------------
# LISTA DE RECETAS
# ---------------------------------------------------------

with st.expander(
    "📖 Ver las recetas disponibles"
):

    if recetas:

        for receta in recetas:

            st.write(
                f"• {receta.get('id', '')} — "
                f"{receta.get('plato', 'Sin nombre')}"
            )

    else:

        st.write(
            "No hay recetas cargadas."
        )


# ---------------------------------------------------------
# PIE DE PÁGINA
# ---------------------------------------------------------

st.caption(
    "Agente Gastronómico Colombiano — "
    "Base de conocimiento inicial de 100 recetas."
)
