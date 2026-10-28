# PROMPT: EXTRACTOR DE DATOS ESTRUCTURADOS
**Workflow:** Justicia Alternativa Bot 2.4  
**Nodo:** `Extractor de Datos Estructurados` → `Parsear Lead` (Code Node)  
**Tipo:** Basic LLM Chain (`@n8n/n8n-nodes-langchain.chainLlm`)  
**Modelo:** OpenAI `gpt-4o-mini` (Temperature: 0)  

---

```text
# TAREA
Analiza TODA la conversación entre el usuario y Eva (incluyendo el último turno).
Extrae los siguientes 8 datos en formato JSON.
No inventes información. Solo usa lo que el usuario dijo explícita o implícitamente.

# CONVERSACIÓN COMPLETA A ANALIZAR

{{ $json.historial_conversacion }}

Último mensaje del usuario:
{{ $json.original_text }}

Respuesta que Eva generó en este turno:
{{ $json.agent_response }}

# INSTRUCCIONES DE EXTRACCIÓN

1. nombre
   - Extrae el nombre completo (nombre + apellidos) del cliente.
   - Si viene pegado al teléfono (ej. "Pancho Villa 6141231234"), sepáralos: los últimos 10 dígitos consecutivos son el teléfono, el resto alfabético es el nombre.
   - Nunca incluyas dígitos en este campo.
   - Si no hay nombre claro, devuelve "".

2. telefono
   - Busca cualquier número de celular mexicano en toda la conversación, sin importar el formato (espacios, guiones, paréntesis, prefijo +52, 044, 01, letras mezcladas).
   - Devuelve exactamente 10 dígitos numéricos puros, sin ningún otro carácter.
   - Si no hay una secuencia válida de 10 dígitos, devuelve "".
   - Nunca incluyas letras ni el nombre del usuario en este campo.

3. tipo_problema
   - Sintetiza en 2 a 5 palabras el asunto legal o inmobiliario del cliente.
   - Ejemplos válidos: "Contrato de arrendamiento", "Inquilino moroso", "Convenio preventivo".
   - Basarte en TODA la conversación, no solo en el último mensaje.
   - Si no hay problema identificado, devuelve "".

4. resumen_caso
   - Redacta 1 a 2 líneas que capturen la situación específica del cliente: qué quiere resolver, qué le preocupa, qué solicitó.
   - Basarte en toda la conversación acumulada.
   - Si no hay caso identificado, devuelve "".

5. observacion_cobertura
   - Si el cliente mencionó una colonia, municipio o ciudad concreta, anótala.
   - Si no mencionó ninguna ubicación, devuelve "Chihuahua".

6. solicitar_contacto
   - true si en cualquier punto de la conversación el usuario:
     (a) pidió una cita o asesoría,
     (b) preguntó dónde están las oficinas o cómo contactarlos,
     (c) ya comenzó a proporcionar su nombre o teléfono.
   - false en cualquier otro caso.

7. datos_completos
   - true si se cuentan con nombre (>= 2 caracteres), telefono (10 dígitos) y resumen_caso. De lo contrario false.

8. respuesta_usuario
   - Copia EXACTAMENTE la respuesta que Eva dio en este turno.

# REGLAS CRÍTICAS DE SALIDA
Responde ÚNICAMENTE con el objeto JSON con estas 8 keys:
nombre, telefono, tipo_problema, resumen_caso, observacion_cobertura, solicitar_contacto, datos_completos, respuesta_usuario
```
