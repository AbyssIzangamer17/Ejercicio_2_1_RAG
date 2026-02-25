# Bitácora de Desarrollo: MindCore Industrial

## Ejercicio 2.1 — Sistema RAG de Investigación Asistida por IA

---

### Descripción del Proyecto

El proyecto consiste en crear una herramienta de investigación basada en IA llamada MindCore Industrial. Permite cargar documentos de texto de cualquier tipo y realizar consultas inteligentes sobre su contenido. Utiliza Pollinations AI para proporcionar inteligencia artificial sin necesidad de API key.

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

**Nota del desarrollo:** El sistema final implementa una versión funcional de MindCore Industrial que permite cargar cualquier documento y realizar consultas inteligentes sobre su contenido, con capacidad de citar las fuentes exactas de cada respuesta.

---

### Prompts Utilizados

#### Prompt #1
**Prompt:** "El ejercicio de RAG tiene que funcionar como si fuera un NotebookLM..."

**Para qué sirve:** Se rediseñó completamente la interfaz para emulate MindCore Industrial (antes NotebookLM): panel de fuentes lateral, área de chat central, citas en tiempo real con etiquetas azules indicando el documento fuente, e interfaz minimalista inspirada en Google Research.

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

#### Prompt #9
**Prompt:** "Mejora su aspecto en HTML, quiero un toque de colores negro y rojizo."

**Para qué sirve:** Se rediseñó completamente la interfaz HTML con un tema oscuro profesional:
- Fondo principal #0d0d0d (negro profundo)
- Sidebar y tarjetas en tonos gris oscuro (#1a1a1a, #1e1e1e)
- Color de acento principal #e63946 (rojo brillante)
- Gradientes sutiles con tinte rojizo en el fondo
- Efectos glow rojo en hover y elementos activos
- Scrollbars personalizadas
- Mensajes de chat con tarjetas oscuras y bordes sutiles
- Botón de envío con gradiente rojo y sombra

**Corrección:** No — Este prompt fue para mejorar el diseño visual.

---

#### Prompt #10
**Prompt:** "Perfecto, el Rag ya funciona, Ahora quiero que sepa guardar mis fuentes para que si yo me salgo al volver entrar siga ahí. También quiero poder tener diversos cuadernos para tener diversas conversaciones que no tengan nada que ver entre si como si fuera un historial de conversaciones."

**Para qué sirve:** Se implementó un sistema completo de persistencia y múltiples cuadernos:
- **Persistencia local (localStorage):** Todas las fuentes y conversaciones se guardan automáticamente
- **Múltiples cuadernos:** Cada cuaderno tiene sus propias fuentes y conversación independiente
- **Panel de cuadernos:** Interfaz lateral para gestionar cuadernos
- **Crear/renombrar/eliminar cuadernos:** Funcionalidad completa de CRUD
- **Cambio rápido:** Se puede cambiar entre cuadernos instantáneamente
- **Título dinámico:** El nombre del cuaderno actual aparece en el header
- **Metadatos:** Cada cuaderno muestra número de fuentes, mensajes y fecha de creación

**Corrección:** No — Este prompt fue para añadir nuevas funcionalidades de persistencia y organización.

---

#### Prompt #11
**Prompt:** "Mejora el formato y arregla las cosas que no funcionan como el boton de nuevo cuaderno, También la vista del HTML se ve rara no está bien alineada arreglalo."

**Para qué sirve:** Se corrigieron bugs y problemas de diseño:
- Arreglado el botón "Nuevo Cuaderno" que no funcionaba
- Corregida la alineación del layout con contenedor flexbox
- Reorganizado el header del sidebar
- Mejorada la experiencia de usuario general

**Corrección:** Sí — Este prompt corrigió bugs de funcionamiento.

---

#### Prompt #12
**Prompt:** "Quiero que se vea más visible lo de los cuadrenos, si no pasa desapercibido por lo demás es genial."

**Para qué sirve:** Se hizo el botón de cuadernos mucho más visible:
- Botón grande con gradiente rojo
- Texto blanco "📚 Cuadernos"
- Sombra glow rojiza
- Efecto de escala en hover
- Posicionado prominentemente en el header del sidebar

**Corrección:** No — Este prompt fue para mejorar la visibilidad.

---

### Resumen de Funcionalidades (Versión Final v10)

| Funcionalidad | Descripción |
|--------------|-------------|
| Gestión de Fuentes | Añadir y eliminar fuentes dinámicamente |
| Chat con IA | Consultas sobre documentos cargados (Pollinations AI real) |
| Citas Automáticas | Indica el documento fuente de cada respuesta |
| Memoria de Conversación | Mantiene contexto de las últimas 6 interacciones |
| Resumen Global | Resume todas las fuentes conjuntamente |
| Guía de Estudio | Genera contenido educativo |
| FAQ | Crea preguntas y respuestas automáticas |
| Relaciones | Encuentra conexiones entre documentos |
| Pollinations AI | Motor de IA sin API key |
| Múltiples Cuadernos | Varios cuadernos con conversaciones independientes |
| Persistencia Local | Fuentes y conversaciones se guardan automáticamente |
| Tema Oscuro | Diseño negro y rojizo profesional |
| Versión Python | Interfaz de terminal completa para uso local |
| Versión HTML | Interfaz web con UI similar a NotebookLM |

---

### Conclusión

NotebookLM Industrial ha evolucionado hasta convertirse en una herramienta de investigación versátil y potente, capaz de funcionar con cualquier tipo de documento y tema. Sus características principales incluyen:

- **Persistencia total:** Fuentes y conversaciones se mantienen al salir y volver a entrar
- **Múltiples cuadernos:** Organiza diferentes proyectos o temas en cuadernos separados
- **IA avanzada:** Integración con Pollinations AI para respuestas inteligentes con citas
- **Diseño profesional:** Tema oscuro con acentos rojos, inspirado en el ámbito industrial
- **Dualidad:** Disponible tanto en versión HTML (navegador) como Python (terminal)

El sistema permite cargar cualquier documento, realizar consultas inteligentes, generar resúmenes, guías de estudio y contenido educativo, manteniendo siempre el contexto de la conversación y la trazabilidad de las fuentes utilizadas.

---

*Documento realizado por Izan Urios — 3R de Automatización y Robótica Industrial*
