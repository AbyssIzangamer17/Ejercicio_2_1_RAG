import os
import sys

def simulate_rag_engine():
    # Base de conocimientos extendida
    knowledge_base = {
        "mantenimiento": "El mantenimiento preventivo del motor M101 debe realizarse cada 5000 horas de operación para evitar fallos térmicos.",
        "seguridad": "El protocolo de parada de emergencia (E-Stop) requiere la activación del relé de seguridad K1 en el panel principal.",
        "ip": "La dirección IP estática del PLC Siemens S7-1200 es por defecto 192.168.0.1 en la subred 255.255.255.0.",
        "error f01": "El error F01 indica una sobrecarga térmica en el variador de frecuencia VFD-02. Verifique la ventilación.",
        "stop": "Para una parada controlada, use la instrucción de software 'HALT' antes de cortar la potencia.",
        "agv": "Los robots AGV operan en el canal 6 de radiofrecuencia (2.4GHz) para evitar interferencias con el WiFi de planta."
    }

    print("="*60)
    print("🚀 MOTOR RAG INDUSTRIAL - SISTEMA DE CONSULTA TÉCNICA")
    print("="*60)
    print("Instrucciones: Escribe tu consulta técnica (ej: 'mantenimiento', 'error f01').")
    print("Escribe 'salir' para finalizar.\n")

    while True:
        try:
            query = input("🛠️ CONSULTA > ").strip().lower()
            if query == 'salir':
                break
            if not query:
                continue

            # Simulación de recuperación de fragmentos relevantes
            found = False
            for key, content in knowledge_base.items():
                if key in query:
                    print(f"\n🔍 [RECUPERADO]: {content}")
                    print(f"🤖 [AGENTE IA]: Según el manual técnico indexado, {content.lower()}")
                    found = True
                    break
            
            if not found:
                print("\n❌ [ERROR]: No se encontró información en la base de conocimientos para esa consulta.")
            
            print("-" * 30)
        except EOFError:
            break

if __name__ == "__main__":
    simulate_rag_engine()
