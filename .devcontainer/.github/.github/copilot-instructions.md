# Agente Gastronómico Colombiano

## Objetivo del proyecto

Este repositorio contiene una aplicación Streamlit llamada "Agente Gastronómico Colombiano".

La aplicación tiene como objetivo funcionar como un asistente de consulta sobre gastronomía colombiana utilizando una base de conocimiento estructurada.

## Archivos importantes

- `app.py`: aplicación principal de Streamlit.
- `recetas_completas.json`: base de conocimiento principal.
- `recetas.json`: archivo anterior de recetas. No reemplazar ni eliminar.
- `requirements.txt`: dependencias del proyecto.

## Base de conocimiento

La base `recetas_completas.json` contiene información relacionada mediante el campo `ID receta`.

La información está organizada conceptualmente en:

- recetas
- ingredientes
- preparación
- técnicas
- errores y soluciones
- fuentes

El identificador de relación entre los datos es `ID receta`.

## Reglas importantes

1. No eliminar archivos existentes.
2. No reemplazar `recetas_completas.json`.
3. No modificar ni perder información de la base de conocimiento.
4. Antes de modificar `app.py`, revisar su estructura actual.
5. Mantener compatibilidad con Streamlit.
6. Mantener la aplicación sencilla y adecuada para usuarios principiantes.
7. Las respuestas del agente deben basarse prioritariamente en la información disponible en `recetas_completas.json`.
8. Si una información no está disponible en la base de conocimiento, indicarlo claramente.
9. No inventar recetas, ingredientes, cantidades, tiempos o técnicas como si fueran datos de la base.
10. Conservar la información de las fuentes asociadas a cada receta.

## Objetivo funcional

La aplicación debe evolucionar desde un buscador simple hacia un asistente gastronómico conversacional.

El usuario debería poder realizar preguntas como:

- ¿Cómo preparo un ajiaco santafereño?
- ¿Qué ingredientes necesito para preparar un ajiaco?
- Tengo pollo, papa y mazorca, ¿qué puedo preparar?
- ¿Qué técnicas se utilizan en esta receta?
- ¿Qué hago si la papa quedó dura?
- ¿Qué hago si la preparación quedó muy salada?
- ¿De qué región es esta preparación?
- ¿Cuántas porciones produce?
- ¿Cuál es el tiempo de preparación?

El sistema debe identificar la receta o recetas relacionadas y utilizar la información disponible en la base de conocimiento para responder.

## Desarrollo

Cuando se propongan cambios:

1. Revisar primero los archivos existentes.
2. Mantener la base de datos intacta.
3. Realizar cambios pequeños y verificables.
4. Evitar reescribir innecesariamente toda la aplicación.
5. Mantener una interfaz clara.
6. Mantener la posibilidad de consultar directamente las recetas.
7. Mostrar las fuentes cuando sean relevantes.
