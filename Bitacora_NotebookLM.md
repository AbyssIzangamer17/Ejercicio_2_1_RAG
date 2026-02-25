# Bitácora de Desarrollo: NotebookLM Industrial

## Ejercicio 2.1 — Sistema RAG de Investigación Asistida por IA

---

### Descripción del Proyecto

El proyecto consiste en crear una herramienta de investigación basada en IA similar a Google NotebookLM. Permite cargar documentos de texto de cualquier tipo y realizar consultas inteligentes sobre su contenido. Utiliza Pollinations AI para proporcionar inteligencia artificial sin necesidad de API key.

---

### Prompt de Origen (Contexto General)

**Fuente:** Conversación inicial del proyecto - Antigravity

**Prompt principal del proyecto:**
> "Usa la skill @find-skills para explorar tu ecosistema de 60.000 herramientas y seleccionar, en cada paso, la habilidad más avanzada y adecuada para cumplir este flujo de trabajo:
> Extracción Multimodal: Busca y ejecuta la mejor herramienta de OCR y visión artificial para analizar la imagen/PDF dentro de la carpeta 'PDF DE EJERCICIOS' y extraer las instrucciones de texto.
> Deducción de Objetivos: Si el texto extraído es impreciso o incompleto, busca una skill de agentes autónomos o planificación estratégica capaz de comprender el contexto, deducir el objetivo final del trabajo y 'apañárselas' de forma independiente para descomponer la meta en tareas ejecutables.
> Documentación Académica: Localiza la skill de creación de documentos más robusta que garantice compatibilidad total con LibreOffice. El documento final debe seguir un estilo académico riguroso.
> Estilización y Pie de Página: Identifica una herramienta de diseño de temas o estilización para configurar un pie de página obligatorio con el texto: 'Documento realizado por Izan Urios de 3R de Automatización y Robótica industrial'. Es indispensable que este pie de página incluya un borde superior nítido que lo separe visualmente del cuerpo del documento.
> Ejecuta todo el proceso de forma autónoma, priorizando la precisión técnica y el rigor en el formato final.
> Ve poco a poco y ve diferenciando los ejercicios de forma estructurada y organizada. Haz una carpeta por cada uno y trabaja adecuadamente siendo ordenado."

**Interpretación:** Este prompt establece el flujo de trabajo completo del proyecto. Se buscaba utilizar el ecosistema de habilidades de IA para procesar las instrucciones del PDF y generar una solución organizada y profesional para cada ejercicio.

---

### Prompt de Origen (Ejercicio Específico)

**Fuente:** PDF de Instrucciones del Ejercicio (Captura 2026-02-24)

**Contexto del ejercicio:**
El Ejercicio 2.1 forma parte del bloque "Habilidades del Ecosistema IA" del módulo. Este ejercicio se enmarca dentro del contexto de investigación de herramientas de inteligencia artificial aplicadas al ámbito industrial.

**Prompt original extraído del PDF:**
> "Exercici 2.1. Recerca RAG. Investigar sobre els sistemes RAG per a manuals industrials."

**Interpretación y desarrollo:**
Este prompt establece como objetivo la investigación sobre sistemas RAG (Retrieval Augmented Generation) aplicados a manuales industriales. Los sistemas RAG combinan la recuperación de información con generación de texto, permitiendo que los modelos de IA respondan preguntas basándose en documentos específicos sin necesidad de reentrenamiento.

En el contexto industrial, esto es especialmente útil para:
- Consultar manuales de mantenimiento sin conocer el documento exacto
- Extraer información de procedimientos operativos (SOPs)
- Resolver dudas sobre configuraciones de equipos
- Crear bases de conocimiento consultables mediante lenguaje natural

La investigación debe cubrir:
- Fundamentos teóricos de RAG
- Arquitecturas de embedding y recuperación
- Aplicaciones prácticas en entornos industriales
- Integración con sistemas existentes

**Nota del desarrollo:** El sistema final implementa una versión funcional de NotebookLM industrial que permite cargar cualquier documento y realizar consultas inteligentes sobre su contenido, con capacidad de citar las fuentes exactas de cada respuesta.

---

### Prompts Utilizados

#### Prompt #1
**Prompt:** "El ejercicio de RAG tiene que funcionar como si fuera un NotebookLM. No tal y como lo has planta

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

#### Prompt #8
**Prompt:** "Actualiza el Python de Rag y los sincroniza con el formato HTML. Quiero que sea capaz de todo lo que dice, de ser un NotebookLM en todo su esplendor pero de forma LOCAL."

**Para qué sirve:** Se actualizó completamente rag_prototype.py para que sea idéntico en funcionalidades a research_notebook.html:
- Sistema de gestión de fuentes (añadir/eliminar documentos)
- Integración real con Pollinations AI (sin simulación)
- Memoria de conversación (últimas 6 interacciones)
- Citas automáticas de fuentes en respuestas
- Acciones rápidas (resumen global, relaciones, guía de estudio, FAQ, conclusiones)
- Interfaz de terminal mejorada con menús interactivos
- Compatible 100% con el HTML - mismo motor de IA

**Corrección:** No — Este prompt fue para sincronizar Python con HTML y añadir modo local.

---

### Resumen de Funcionalidades (Versión Python + HTML Sincronizadas)

| Funcionalidad | Descripción |
|--------------|-------------|
| Gestión de Fuentes | Añadir y eliminar fuentes dinámicamente (Python CLI + HTML) |
| Chat con IA | Consultas sobre documentos cargados (Pollinations AI real) |
| Citas Automáticas | Indica el documento fuente de cada respuesta |
| Memoria de Conversación | Mantiene contexto de las últimas 6 interacciones |
| Resumen Global | Resume todas las fuentes conjuntamente |
| Guía de Estudio | Genera contenido educativo |
| FAQ | Crea preguntas y respuestas automáticas |
| Relaciones | Encuentra conexiones entre documentos |
| Pollinations AI | Motor de IA sin API key (mismo en Python y HTML) |
| Modo Local Python | Interfaz de terminal completa, funcional sin navegador |
| Interfaz HTML | Versión web con UI idéntica a NotebookLM real |

---

### Conclusión

NotebookLM Industrial se convirtió en una herramienta de investigación versátil y potente, capaz de funcionar con cualquier tipo de documento y tema. Permite cargar fuentes personalizadas, mantener contexto de conversación y generar contenido automáticamente.

---

*Documento realizado por Izan Urios — 3R de Automatización y Robótica Industrial*
