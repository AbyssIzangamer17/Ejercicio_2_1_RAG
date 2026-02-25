# Bitácora de Desarrollo: NotebookLM Industrial

## Ejercicio 2.1 — Sistema RAG de Investigación Asistida por IA

---

### Descripción del Proyecto

El proyecto consiste en crear una herramienta de investigación basada en IA similar a Google NotebookLM. Permite cargar documentos de texto de cualquier tipo y realizar consultas inteligentes sobre su contenido. Utiliza Pollinations AI para proporcionar inteligencia artificial sin necesidad de API key.

---

### Prompt de Origen

**Fuente:** PDF de Instrucciones del Ejercicio (Captura 2026-02-24)

**Prompt original:**
> "Exercici 2.1. Recerca RAG. Investigar sobre els sistemes RAG per a manuals industrials."

Este prompt establece la investigación sobre sistemas RAG aplicados a manuales industriales como objetivo del ejercicio.

---

### Prompts Utilizados

#### Prompt #1
**Prompt:** "El ejercicio de RAG tiene que funcionar como si fuera un NotebookLM. No tal y como lo has planteado."

**Para qué sirve:** Se rediseñó completamente la interfaz para emulate NotebookLM: panel de fuentes lateral, área de chat central, citas en tiempo real con etiquetas azules indicando el documento fuente, e interfaz minimalista inspirada en Google Research.

**Corrección:** Sí — Se utilizó para corregir el enfoque inicial del RAG que no funcionaba como NotebookLM.

---

#### Prompt #2
**Prompt:** "Tienes que separar los ejercicios, una HTML por cada uno y que sean diferentes."

**Para qué sirve:** Se separó el RAG en su propio archivo research_notebook.html con identidad visual única dentro del Ejercicio 2.1.

**Corrección:** No — Este prompt fue para organizar la estructura del proyecto.

---

#### Prompt #3
**Prompt:** "El RAG no deja subir fuentes y no tiene la capacidad de IA para poder interpretar cosas que no tenga definidas."

**Para qué sirve:** Se implementó la gestión de fuentes: botón "+ Añadir fuente" para pegar texto de cualquier documento, sistema de eliminación de fuentes, y metadatos por fuente (conteo de palabras).

**Corrección:** Sí — Se utilizó para corregir la falta de gestión de fuentes y capacidades de IA.

---

#### Prompt #4
**Prompt:** "El RAG no tiene ningún tipo de libre albedrío, está centrado en un proyecto y yo quiero usarlo para lo que me dé la gana."

**Para qué sirve:** Se eliminaron los datos predefinidos. El sistema ahora empieza vacío y el usuario puede pegar cualquier texto (apuntes, manuales, artículos). La IA busca en todas las fuentes pegadas usando coincidencia de frases y funciona con cualquier tema.

**Corrección:** Sí — Se utilizó para corregir la limitación del sistema a un solo tema predefinido.

---

#### Prompt #5
**Prompt:** "Del RAG no es capaz de hacer resúmenes globales o de interpretar preguntas fuera de lugar, añádele un asistente IA para que pueda usarlo en muchos ámbitos."

**Para qué sirve:** Se añadieron capacidades avanzadas de IA: chip "Resumen global" para resumir todas las fuentes conjuntamente, chip "Relaciones" para encontrar conexiones entre documentos, chip "Guía de estudio" para generar contenido educativo, chip "FAQ" para crear preguntas frecuentes, y chip "Conclusiones" para extraer conclusiones principales.

**Corrección:** Sí — Se utilizó para corregir la falta de capacidades de IA avanzada y resúmenes globales.

---

#### Prompt #6
**Prompt:** "El Rag que funcione con OpenCode sin API alguna, mejóralo."

**Para qué sirve:** Se integró Pollinations AI (URL: https://text.pollinations.ai/openai) que acepta peticiones OpenAI-compatibles sin autenticación. Es un motor gratuito sin necesidad de API key.

**Corrección:** No — Este prompt fue para añadir una nueva funcionalidad.

---

#### Prompt #7
**Prompt:** "Del RAG sigue sin funcionar como NotebookLM, no tiene capacidades de IA, ni de fuentes ni nada. Arreglado."

**Para qué sirve:** Se implementó NotebookLM v9 con características completas: memoria de conversación (últimas 6 interacciones), renderizado markdown en respuestas, UI refinada más similar a NotebookLM real, metadatos por fuente, y spinner animado durante procesamiento.

**Corrección:** Sí — Este prompt se usó para corregir múltiples deficiencias anteriores y unificar todas las mejoras en una versión cohesiva.

---

### Resumen de Funcionalidades

| Funcionalidad | Descripción |
|--------------|-------------|
| Gestión de Fuentes | Añadir y eliminar fuentes dinámicamente |
| Chat con IA | Consultas sobre documentos cargados |
| Citas Automáticas | Indica el documento fuente de cada respuesta |
| Memoria de Conversación | Mantiene contexto de las últimas 6 interacciones |
| Resumen Global | Resume todas las fuentes conjuntamente |
| Guía de Estudio | Genera contenido educativo |
| FAQ | Crea preguntas y respuestas automáticas |
| Relaciones | Encuentra conexiones entre documentos |
| Pollinations AI | Motor de IA sin API key |

---

### Conclusión

NotebookLM Industrial se convirtió en una herramienta de investigación versátil y potente, capaz de funcionar con cualquier tipo de documento y tema. Permite cargar fuentes personalizadas, mantener contexto de conversación y generar contenido automáticamente.

---

*Documento realizado por Izan Urios — 3R de Automatización y Robótica Industrial*
