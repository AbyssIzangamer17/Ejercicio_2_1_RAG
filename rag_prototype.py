import os

def create_rag_prototype():
    # Simulación de una base de datos de conocimientos industriales
    knowledge_base = {
        "mantenimiento": "El mantenimiento preventivo del motor M101 debe realizarse cada 5000 horas de operación.",
        "seguridad": "El protocolo de parada de emergencia (E-Stop) requiere la activación del relé de seguridad K1.",
        "configuracion": "La dirección IP estática del PLC Siemens S7-1200 es por defecto 192.168.0.1.",
        "error_f01": "El error F01 indica una sobrecarga térmica en el variador de frecuencia VFD-02."
    }

    def retrieve_info(query):
        query = query.lower()
        # Simulación de búsqueda semántica simple
        for key in knowledge_base:
            if key in query:
                return knowledge_base[key]
        return "No se encontró información relevante en los manuales indexados."

    def generate_response(query, context):
        if context == "No se encontró información relevante en los manuales indexados.":
            return context
        
        # Simulación de agente IA que procesa el contexto
        return f"Basado en los manuales técnicos: Para resolver su consulta sobre '{query}', el sistema indica que: {context}"

    # Ejemplo de uso
    queries = ["¿Cuándo es el mantenimiento del motor?", "¿Qué significa el error F01?", "¿Cómo configurar la IP del PLC?"]
    
    print("--- Prototipo RAG Industrial (Simulación) ---")
    for q in queries:
        context = retrieve_info(q)
        response = generate_response(q, context)
        print(f"\nUsuario: {q}")
        print(f"Agente RAG: {response}")

if __name__ == "__main__":
    create_rag_prototype()
