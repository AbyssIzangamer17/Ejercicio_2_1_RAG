#!/usr/bin/env python3
"""
NotebookLM Industrial - Python Edition
Sistema RAG de Investigación Asistida por IA
==========================================
Compatible con research_notebook.html - Funcionalidades sincronizadas
"""

import os
import sys
import time
import json
import hashlib
import re
from collections import Counter

try:
    import requests
except ImportError:
    print(
        "Error: Se requiere la biblioteca 'requests'. Instálala con: pip install requests"
    )
    sys.exit(1)


class NotebookLM_Industrial:
    def __init__(self):
        self.sources = []
        self.conversation_history = []
        self.knowledge_index = {}
        self.api_url = "https://text.pollinations.ai/openai"

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def print_header(self):
        self.clear_screen()
        print("=" * 70)
        print("📔 NOTEBOOKLM INDUSTRIAL - Python Edition v9.0")
        print("   Motor: Pollinations AI (Sin API Key)")
        print("   Autor: Izan Urios · 3R Automatización")
        print("=" * 70)

    def print_sources(self):
        print("\n📂 FUENTES CARGADAS:")
        print("-" * 50)
        if not self.sources:
            print("   (No hay fuentes cargadas)")
            return

        for i, source in enumerate(self.sources, 1):
            word_count = len(source["text"].split())
            preview = source["text"][:80].replace("\n", " ")
            print(f"   [{i}] {source['name']}")
            print(f"       📝 {word_count} palabras")
            print(f"       📄 {preview}...")
            print()

    def print_chips(self):
        print("\n🎯 ACCIONES RÁPIDAS:")
        print("-" * 50)
        print("   [1] 📝 Resumen global de todas las fuentes")
        print("   [2] 🔗 Relaciones entre documentos")
        print("   [3] 📚 Generar guía de estudio")
        print("   [4] ❓ Crear FAQ (Preguntas Frecuentes)")
        print("   [5] 💡 Extraer conclusiones")

        for i, source in enumerate(self.sources[:2], 6):
            short_name = source["name"][:25]
            print(f"   [{i + 5}] 📄 Resumir: {short_name}")

        print(f"   [9] ➕ Añadir nueva fuente")
        print("   [0] 💬 Consulta libre (sin fuentes)")
        print("-" * 50)

    def add_source(self):
        print("\n" + "=" * 50)
        print("📥 AÑADIR NUEVA FUENTE")
        print("=" * 50)

        name = input("   Nombre del documento: ").strip()
        if not name:
            name = f"Documento_{len(self.sources) + 1}"

        print(
            "\n   Pega el contenido del documento (termina con Ctrl+D en Linux/Mac o Ctrl+Z en Windows):"
        )
        print("   (Escribe 'cancelar' en una línea nueva para salir)")
        print("-" * 50)

        lines = []
        try:
            while True:
                try:
                    line = input()
                    if line.strip().lower() == "cancelar":
                        print("\n❌ Operación cancelada.")
                        return
                    lines.append(line)
                except EOFError:
                    break
        except KeyboardInterrupt:
            print("\n\n❌ Operación cancelada.")
            return

        text = "\n".join(lines).strip()
        if not text:
            print("\n❌ No se añadió ningún texto.")
            return

        source = {"name": name, "text": text, "added_at": time.time()}

        self.sources.append(source)
        word_count = len(text.split())
        print(f"\n✅ '{name}' añadido correctamente ({word_count} palabras)")
        print("   La IA ya tiene acceso a este documento.")

        input("\n   Presiona Enter para continuar...")

    def remove_source(self):
        if not self.sources:
            print("\n❌ No hay fuentes para eliminar.")
            return

        self.print_sources()

        try:
            idx = int(input("\n   Número de fuente a eliminar (0 para cancelar): "))
            if idx == 0:
                return
            if 1 <= idx <= len(self.sources):
                removed = self.sources.pop(idx - 1)
                print(f"\n✅ Fuente '{removed['name']}' eliminada.")
            else:
                print("\n❌ Número inválido.")
        except ValueError:
            print("\n❌ Por favor, introduce un número.")

        input("\n   Presiona Enter para continuar...")

    def build_context(self):
        if not self.sources:
            return ""

        context_parts = []
        for source in self.sources:
            context_parts.append(f'[DOCUMENTO: "{source["name"]}"]\n{source["text"]}')

        return "\n\n===\n\n".join(context_parts)

    def build_prompt(self, user_query, include_sources=True):
        system_prompt = """Eres un asistente de investigación avanzado, similar a NotebookLM de Google.
Tu trabajo es ayudar al usuario a entender, analizar y trabajar con sus documentos.

INSTRUCCIONES OBLIGATORIAS:
1. Responde SIEMPRE en español.
2. Si la pregunta está relacionada con los documentos, BASA tu respuesta en ellos y CITA el nombre del documento entre corchetes, ejemplo: [Manual_PLC.pdf].
3. Si la pregunta NO está relacionada con los documentos, responde con tu conocimiento general.
4. Puedes generar: resúmenes, guías de estudio, preguntas frecuentes (FAQ), comparaciones, y cualquier análisis que se pida.
5. Sé detallado pero estructurado. Usa listas y formato claro.
6. Si no hay fuentes cargadas, informa al usuario amablemente y ofrece ayuda general."""

        if include_sources and self.sources:
            source_context = self.build_context()
            system_prompt += f"""

DOCUMENTOS DEL USUARIO ({len(self.sources)} fuentes cargadas):

{source_context}

Nota: El usuario tiene {len(self.sources)} documento(s) cargado(s). Utilízalos como referencia principal para tus respuestas."""

        return system_prompt

    def query_ai(self, user_query, include_sources=True):
        print("\n🤔 Analizando y razonando...")

        messages = [
            {
                "role": "system",
                "content": self.build_prompt(user_query, include_sources),
            }
        ]

        for msg in self.conversation_history[-6:]:
            messages.append(msg)

        messages.append({"role": "user", "content": user_query})

        try:
            response = requests.post(
                self.api_url,
                json={"model": "openai", "messages": messages, "temperature": 0.7},
                timeout=60,
            )

            if response.status_code == 200:
                data = response.json()
                answer = (
                    data.get("choices", [{}])[0].get("message", {}).get("content", "")
                )
                return answer
            else:
                return f"❌ Error de API: Código {response.status_code}"

        except requests.exceptions.Timeout:
            return "❌ Tiempo de espera agotado. La IA tardó demasiado en responder."
        except requests.exceptions.ConnectionError:
            return "❌ Error de conexión. Verifica tu conexión a internet."
        except Exception as e:
            return f"❌ Error: {str(e)}"

    def find_cited_sources(self, answer):
        cited = []
        for source in self.sources:
            if source["name"] in answer:
                cited.append(source["name"])
        return cited

    def execute_chip_action(self, chip_num):
        actions = {
            1: (
                "Resumen global",
                "Haz un resumen global y completo de todas mis fuentes, extrayendo los puntos más importantes de cada documento.",
            ),
            2: (
                "Relaciones",
                "¿Qué relaciones y conexiones encuentras entre todos mis documentos? ¿Qué temas comunes hay?",
            ),
            3: (
                "Guía de estudio",
                "Genera una guía de estudio completa basada en mis documentos. Incluye temas, subtemas y puntos clave.",
            ),
            4: (
                "FAQ",
                "Crea 5 preguntas frecuentes (FAQ) con respuestas basadas en mis documentos.",
            ),
            5: (
                "Conclusiones",
                "¿Qué conclusiones principales puedo extraer de mis documentos?",
            ),
        }

        if chip_num in actions:
            chip_name, prompt = actions[chip_num]
            return self.process_query(prompt)

        source_idx = chip_num - 6
        if 0 <= source_idx < len(self.sources[:2]):
            source = self.sources[source_idx]
            prompt = f"Explica los conceptos más importantes del documento '{source['name']}'. Resume sus puntos clave."
            return self.process_query(prompt)

        return None

    def process_query(self, query):
        if not query.strip():
            return

        self.print_header()
        self.print_sources()

        print("\n" + "=" * 70)
        print(f"👤 CONSULTA: {query}")
        print("=" * 70)

        self.conversation_history.append({"role": "user", "content": query})

        include_sources = len(self.sources) > 0
        answer = self.query_ai(query, include_sources)

        print("\n" + "=" * 70)
        print("🤖 RESPUESTA:")
        print("=" * 70)

        if include_sources:
            cited = self.find_cited_sources(answer)
            if cited:
                print("\n📑 CITAS:")
                for src in cited:
                    print(f"   📄 [{src}]")

        print()
        print(answer)
        print()

        self.conversation_history.append({"role": "assistant", "content": answer})

        print("-" * 70)
        input("   Presiona Enter para continuar...")

    def show_welcome(self):
        self.print_header()
        print("""
📌 BIENVENIDO A NOTEBOOKLM INDUSTRIAL - Python Edition
   
Esta herramienta te permite:
   
   ✅ Cargar documentos de cualquier tipo (manuales, artículos, apuntes...)
   ✅ Realizar consultas inteligentes sobre tu contenido
   ✅ Obtener respuestas con citas de las fuentes exactas
   ✅ Generar resúmenes globales, guías de estudio, FAQ
   ✅ Mantener contexto de conversación
   ✅ Funcionar SIN necesidad de API key (usa Pollinations AI)
   
📌 CÓMO USAR:
   
   1. Añade fuentes con la opción 9
   2. Selecciona una acción rápida (1-5) o haz una consulta personalizada
   3. La IA analizará tus documentos y responderá con citas
   
💡 NOTA: Si no hay fuentes cargadas, la IA responderá con conocimiento general.

""")
        print("-" * 70)
        input("   Presiona Enter para continuar...")

    def main_loop(self):
        if not self.sources:
            self.show_welcome()

        while True:
            self.print_header()
            self.print_sources()
            self.print_chips()

            try:
                choice = input("\n🎯 Selecciona una opción: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 ¡Hasta luego!")
                break

            if choice.lower() in ["salir", "exit", "quit", "q"]:
                print("\n👋 ¡Hasta luego! Gracias por usar NotebookLM Industrial.")
                break

            if choice == "9":
                self.add_source()
                continue

            if choice == "8":
                self.remove_source()
                continue

            if choice == "0":
                query = input("\n💬 Escribe tu consulta libre: ").strip()
                if query:
                    self.process_query(query)
                continue

            try:
                chip_num = int(choice)
                if 1 <= chip_num <= 11:
                    if chip_num >= 6 and not self.sources:
                        print(
                            "\n❌ No hay fuentes cargadas. Añade primero un documento."
                        )
                        input("\n   Presiona Enter para continuar...")
                        continue

                    result = self.execute_chip_action(chip_num)
                    if result is None:
                        print("\n❌ Opción no válida.")
                        input("\n   Presiona Enter para continuar...")
                else:
                    query = input("\n💬 Escribe tu consulta: ").strip()
                    if query:
                        self.process_query(query)
            except ValueError:
                query = choice.strip()
                if query:
                    self.process_query(query)


def main():
    app = NotebookLM_Industrial()
    app.main_loop()


if __name__ == "__main__":
    main()
