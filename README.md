# MindCore Industrial — Asistente de Investigación con IA

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/es/docs/Web/JavaScript)
[![Pollinations AI](https://img.shields.io/badge/AI-Pollinations%20OpenCode-blueviolet)](https://pollinations.ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Ejercicio 2.1** — Sistema RAG (Retrieval-Augmented Generation) de investigación asistida por IA.

MindCore Industrial v10.0 es una herramienta de investigación que permite cargar cualquier documento de texto y realizar consultas inteligentes sobre su contenido. Utiliza **Pollinations AI** (OpenCode, 100% gratuito, sin necesidad de API key) para proporcionar inteligencia artificial real capaz de resumir, analizar, comparar y razonar sobre cualquier tema.

---

## 🎯 Objetivo del Proyecto

Recrear la experiencia de un asistente de investigación con IA en un entorno independiente, proporcionando a estudiantes e ingenieros una herramienta de investigación con IA que:
- Permita trabajar con **cualquier tipo de texto** (apuntes, manuales, artículos, normativas).
- Ofrezca razonamiento real mediante IA generativa.
- No requiera instalación, cuenta o clave de API.

---

## 🚀 Características Principales

### Novedades v10.0
- **📚 Múltiples Cuadernos:** Crea diferentes cuadernos para distintos proyectos o temas
- **💾 Persistencia Local:** Todo se guarda automáticamente - fuentes y conversaciones
- **🎨 Tema Oscuro:** Diseño profesional negro y rojizo

### Motor de IA (Pollinations AI - OpenCode)
- Integración con la API gratuita de **Pollinations AI** (`text.pollinations.ai/openai`).
- **Sin API key necesaria**: Funciona directamente desde el navegador.
- Modelo OpenAI-compatible con temperatura configurable.
- Respuestas en español con citación automática de fuentes.

### Gestión de Fuentes
- **Añadir fuentes**: Pega cualquier texto (apuntes, manuales, informes, artículos).
- **Eliminar fuentes**: Botón de eliminación individual por fuente.
- **Metadatos**: Muestra el conteo de palabras de cada documento.
- **Vista previa**: Preview del contenido de cada fuente en la barra lateral.
- Sin límite de fuentes ni de tamaño de texto.

### Capacidades de Análisis
| Función | Descripción |
|---------|-------------|
| 📝 **Resumen global** | Resume todas las fuentes de forma conjunta |
| 🔗 **Relaciones** | Encuentra conexiones y temas comunes entre documentos |
| 📚 **Guía de estudio** | Genera una guía de estudio personalizada |
| ❓ **FAQ** | Crea preguntas frecuentes con respuestas basadas en las fuentes |
| 💡 **Conclusiones** | Extrae conclusiones principales de los documentos |
| 📄 **Análisis individual** | Analiza un documento específico en detalle |

### Memoria de Conversación
- Guarda las **últimas 6 interacciones** para mantener el contexto.
- La IA recuerda lo que habéis discutido y puede hacer referencias cruzadas.
- Permite preguntas de seguimiento sin repetir contexto.

### Interfaz tipo Google
- **Diseño limpio** inspirado en Google NotebookLM.
- Barra lateral con panel de fuentes.
- Chips de acción rápida dinámicos.
- Spinner de carga durante el procesamiento.
- Animaciones suaves de aparición de mensajes.

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| **HTML5** | Estructura de la aplicación |
| **CSS3** | Interfaz tipo Google con Google Sans |
| **JavaScript ES6+** | Lógica RAG, gestión de fuentes, llamadas a API |
| **Pollinations AI** | Motor de IA generativa (gratuito, sin API key) |
| **Fetch API** | Comunicación asíncrona con el motor de IA |

---

## 🚀 Inicio Rápido

### Opción 1: Versión Python (Terminal - Recomendado para uso local)
```
# Requiere Python 3.7+ y la biblioteca requests
pip install requests
python rag_prototype.py
```

### Opción 2: Versión HTML (Navegador)
```
Abrir research_notebook.html en cualquier navegador moderno
```

### Opción 2: Clonar repositorio
```bash
git clone https://github.com/AbyssIzangamer17/Ejercicio_2_1_RAG.git
cd Ejercicio_2_1_RAG
# Abrir research_notebook.html en el navegador
```

### Uso Paso a Paso
1. **Abre** `research_notebook.html` en tu navegador.
2. **Añade fuentes**: Haz clic en "+ Añadir fuente", pon un nombre y pega el texto del documento.
3. **Consulta**: Escribe tu pregunta en la barra inferior o usa los chips sugeridos.
4. **Analiza**: La IA procesará tus fuentes y responderá con citas.
5. **Itera**: Añade más fuentes, elimina las que no necesites, haz preguntas de seguimiento.

### Ejemplos de Preguntas
- *"Haz un resumen global de todas mis fuentes"*
- *"¿Qué relación hay entre el documento A y el documento B?"*
- *"Genera una guía de estudio basada en estos apuntes"*
- *"Crea 5 preguntas de examen con respuestas"*
- *"¿Qué conclusiones puedo sacar de esto?"*
- *"Explica el concepto X que aparece en mis fuentes"*

---

## 📁 Estructura del Proyecto

```
Ejercicio_2_1_RAG/
├── research_notebook.html   # Aplicación web (interfaz + IA - versión navegador)
├── rag_prototype.py        # Versión Python (terminal - 100% funcional)
├── Bitacora_NotebookLM.md # Bitácora de desarrollo
└── README.md               # Este archivo
```

---

## ⚙️ Requisitos

### Versión Python (Terminal):
- **Python 3.7+** instalado
- **Biblioteca requests**: `pip install requests`
- Conexión a internet para Pollinations AI

### Versión HTML (Navegador):
- **Navegador moderno**: Chrome, Firefox, Edge o Safari (versión reciente).
- Conexión a internet para Pollinations AI.
- Sin instalación: No requiere Node.js ni backend.

---

## 🔒 Privacidad

- Las fuentes que pegas se procesan **en el navegador** y se envían únicamente al motor de IA para generar respuestas.
- No se almacena ningún dato en servidores externos de forma persistente.
- Al cerrar la pestaña, todos los datos se eliminan.

---

## 👤 Autor

**Izan Urios** — 3R de Automatización y Robótica Industrial

---

## 📄 Licencia

Proyecto de código abierto bajo licencia **MIT**.
