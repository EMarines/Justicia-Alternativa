---
tags:
  - bitacora
  - pendientes
  - sich
  - masc
updated: 2026-10-28
status: activo
---

# 📋 Bitácora Central de Pendientes y Tareas
**Ecosistema:** Soluciones Inmobiliarias Chihuahua & Agentes IA  
**Orquestación:** [[Maya_Orquestadora]] | **Memoria Ejecutiva:** [[Mina_Memoria_Viva]]  
**Última sincronización:** 2026-10-28  

---

## 🟡 Pendientes Activos

| ID | Fecha | Módulo / Responsable | Observación / Detalle | Prioridad |
| **#042** | 2026-10-28 | MASC Pactum & Marketing / Podcast Redes ([[Nexo_Copywriting]] / [[Kino_Audiovisual]]) | **Prototipos Construidos para Podcast NotebookLM (`07:24`):** 1) **Micro-Presentación Web Interactiva:** `podcast/index.html` + `podcast_masc_pactum.mp3` (audio al clic, 6 láminas sincronizadas, swipe de carrusel y onda dorada en vivo). 2) **Video Audiograma Vertical 9:16 (1080×1920):** `04_Flyers_Semanales/Prototipo_Reel_Audiograma_Pactum_66s.mp4` (66s: *Juicio 2 Años vs. Desalojo Express y Pólizas*). Ambos integran fijo **Sala PACTUM** (`WhatsApp: (614) 551-0188` y `C. Miguel Ahumada #153, Col. Industrial, Chihuahua`). | **Prototipos Listos** |
| **#041** | 2026-10-28 | MASC Pactum & Ecosistema / Hub Maestro ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Unificación Integral de todo el Ecosistema JA en `Justicia-Alternativa`:** Centralizado el 100% de MASC en `Operaciones en Curso/Justicia-Alternativa` (Landing Page, Mina Voice HUD PWA, `04_Flyers_Semanales`, Plática Gremio, Fuente de Verdad y Workflows), retirando carpetas duplicadas a `Operaciones Concluidas`. | **Resuelto** |
| **#040** | 2026-10-07 | Mina Core & Realtime Voice ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **Actualización a Gemini 3.8 Live y Extended Thinking:** 1) Verificado que opera bajo la cuota oficial sin costo adicional en Google AI Studio. 2) Integrado modelo `models/gemini-3.8-live-extended-thinking` en `MinaVoiceClient.ts`, `voiceSession.ts` y `VoiceHUD.svelte`. 3) Implementada configuración adaptativa de `thinkingConfig` (`thinkingLevel: LOW`) requerida por la API para respuestas conversacionales inmediatas y cero latencia. 4) Validado handshake exitoso por WebSocket y build limpio de producción en Vite. | **Resuelto** |
| **#039** | 2026-10-07 | ATAIR CRM / Ecosistema ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Integración y Despliegue de Organigrama Jerárquico en ATAIR CRM (`/admin/squad`):** Incorporada la ruta protegida de administración con visualizador interactivo (pan/zoom, pantalla completa, copiar código Miro), acceso directo en Navbar (`Squad IA` con tono ámbar) y alias estáticos aislados en `static/organigrama_squad_elite.html` sin interferencia con estilos base. | **Resuelto** |
| **#038** | 2026-10-07 | ATAIR CRM / Ecosistema ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Evaluación de Integración de Organigrama en ATAIR CRM:** Análisis de factibilidad para portar el organigrama jerárquico como vista/módulo administrativo nativo en SvelteKit (`/admin/squad`). Registrado en backlog diferido sin intervenir código de ATAIR actualmente. | **Resuelto (Superado por #039)** |
| **#037** | 2026-10-07 | Gobernanza & UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Corrección y Enlace de Líneas de Mando Jerárquicas:** Solucionado bug de renderizado SVG (filtros en líneas ortogonales) que ocultaba las vigas y troncos de mando. Conectados de punta a punta: Tronco Enrique $\rightarrow$ Maya/Mina $\rightarrow$ Viga de Despacho $\rightarrow$ 8 Especialistas; enlace de retorno Mina $\rightarrow$ Clara y asesoría Enrique $\leftrightarrow$ Marco. | **Resuelto** |
| **#036** | 2026-10-07 | Gobernanza & UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Rediseño Jerárquico Top-Down y Ratificación de Flujo Operativo:** Transición de organigrama circular a estructura corporativa en árbol estándar (Director $\rightarrow$ Maya/Mina $\rightarrow$ Squad Especialistas $\rightarrow$ Clara en Gabinete; Marco como mentor directo). Flujo canónico de delegación y consolidación formalizado en `organigrama_squad_elite.html`. | **Resuelto** |
| **#035** | 2026-10-07 | Ecosistema UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Reconexión y Calibración Visual de Enlaces en Organigrama (`organigrama_squad_elite.html`):** Corregido recorte SVG (`overflow: visible`), eliminados cruces de pantalla y asignadas alas operativas naturales: Ala Izquierda coordinada por Maya (Argos, Lince, Apolo, Wero); Ala Derecha coordinada por Mina (Clara, Beto, Eva, Kino, Nexo); y enlace directo de Marco al Director Enrique como mentor personal. Líneas de fibra óptica neón al 90% de opacidad y glow activo. | **Resuelto** |
| **#034** | 2026-10-07 | Ecosistema UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Mapa Mental y Organigrama Radial Interactivo Élite (`organigrama_squad_elite.html`):** Construcción de dashboard visual interactivo con Enrique Marines al centro (logo Match Home), Maya y Mina como estado mayor, y squad periférico (Argos, Lince, Eva, Kino, Nexo, Apolo, Wero, Clara, Marco). Clic en agente despliega ficha y clic en habilidad abre desglose pericial profundo. Listo para embed en Miro. | **Alta** |
| **#033** | 2026-10-07 | I+D & Innovación ([[Argos_Arquitecto]] / [[Maya_Orquestadora]]) | **Activación de Pipeline de Vigilancia Tecnológica y Radar de Avances:** Configurar a Argos como el agente responsable de monitorear nuevos lanzamientos tecnológicos e IA para someterlos a la mesa técnica de mejoras del sistema, con apoyo de Lince en auditoría de viabilidad/seguridad. | **Media-Alta** |
| **#032** | 2026-10-07 | Innovación & Estrategia ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Radar de Proyecciones a Futuro (Icebox Tecnológico):** Estructurar e inicializar un módulo formal de 'Proyecciones a Futuro' para salvaguardar tecnologías e ideas de alto potencial (ej. Gemini Enterprise, Google Business Profile automatizado, Routine Stacking en Workspace) sin desviar el foco crítico actual de ATAIR CRM y MASC. | **Media (Diferido)** |
| **#031** | 2026-09-18 | Ecosistema & UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Command Center / Interfaz Central con Chat Unificado y Motor Gemini:** Desarrollar dashboard web interactivo con organigrama del squad (Maya, Mina, Eva, Kino, Nexo, Lince, Apolo), fichas de agente al hacer clic, chat integrado con motor Gemini/Antigravity en el backend para ejecución de órdenes en tiempo real y sincronización bidireccional con notas/bitácoras de Obsidian. | **Media** |
| **#030** | 2026-09-17 | Infraestructura & Migración Cloud ([[Mina_Memoria_Viva]]) | **Migración Integral de Office 365 a Google Workspace / Drive y Cancelación de Suscripción:** Ejecutar por etapas la transferencia de archivos (OneDrive a Google Drive), correos/contactos (Outlook a Gmail), notas OneNote a Drive y posterior cancelación de la suscripción de Microsoft 365. Recordar a Enrique mañana a primera hora. | **Alta (Recordatorio 18-Sep)** |
| **#029** | 2026-09-17 | Telegram & Despacho Mina ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **Envío Autónomo de Archivos Locales por Telegram (sendDocument):** Configurar webhook/sub-flujo en n8n y script en Mina para enviar documentos generados (.docx, .pdf, contratos, expedientes) directamente como archivos descargables al chat de Telegram de Enrique Marines usando su Chat ID. | **Alta** |
| **#028** | 2026-09-17 | Negociaciones & Captación ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **Contacto y Entrevista Estratégica con Don Sergio Armendáriz (Predio Nombre de Dios - 8,413 m²):** Aplicación de cuestionario diagnóstico de 5 bloques (motivación, estatus Century 21, maderera/negocio en marcha, capacidad eléctrica/arroyo y esquemas de aportación/micro-bodegas) para definir plan comercial. | **Alta (18-Sep)** |
| **#027** | 2026-09-17 | Arquitectura Multi-Agente ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Protocolo de Despacho Multi-Agente (Mina Despachadora -> Maya/Antigravity Ejecutor):** Crear canal de órdenes en n8n/Supabase (`mina_dispatched_tasks`) para que las peticiones técnicas recibidas por voz en Mina se deleguen a Maya/Antigravity para su ejecución real. | **Alta** |
| **#026** | 2026-09-17 | Mina Live Voice / UI Visualizer ([[Mina_Memoria_Viva]]) | **Visualizador y Vibración Dinámica de Entrada de Voz:** Implementar en el orbe central de la app de voz una animación de pulsación/vibración en tiempo real que reaccione al volumen y captura del micrófono para confirmar visualmente el ingreso de audio. | **Alta** |
| **#025** | 2026-09-17 | Mina Live Voice / Audio App ([[Mina_Memoria_Viva]]) | **Selector y Priorización Automática de Auriculares / Bluetooth:** En la app de voz local, detectar automáticamente si hay auriculares Bluetooth conectados (PC/Celular), seleccionarlos como micrófono/altavoz principal y proveer botón/selector de conmutación de dispositivo. | **Alta** |
| **#024** | 2026-09-17 | Memoria & Supabase ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **Arquitectura de Memoria de 2 Niveles (Prontuario Semanal / Hot Cache vs Cold Storage):** Buffer rápido de contexto activo de 7 días para respuestas inmediatas de corto plazo y auto-archivado/rotación en Supabase para búsqueda profunda de largo plazo. | **Alta** |
| **#023** | 2026-09-17 | Telegram / Audio ([[Lince_Auditor_Web]] / [[Mina_Memoria_Viva]]) | **Fallback de Transcripción con Groq Whisper en Mina:** Mantener en el radar de contingencia la integración de Groq API (Whisper `whisper-large-v3` free tier <300ms) como respaldo en caso de falla, saturación o latencia con Google Gemini. | Media (Contingencia) |
| **#022** | 2026-09-15 | n8n / Google Hub ([[Maya_Orquestadora]]) | **Sub-Workflow Centralizado de Google Hub (Contacts, Calendar, Tasks):** Subrutina única en n8n para que Mina, ATAIR SGI y Eva sincronicen contactos, eventos y tareas en Google Workspace. | **Alta** |
| **#021** | 2026-09-15 | Telegram / Mina ([[Mina_Memoria_Viva]]) | **Enlace Telegram Directo a Obsidian:** Activar listener de Telegram con Whisper/OpenAI para que notas de voz y textos desde el celular se inserten automáticamente en la bitácora de Obsidian. | **Alta (Productividad)** |
| **#020** | 2026-09-15 | Expansión / CANACO ([[Mina_Memoria_Viva]]) | **Contacto Clave CANACO (Judith Hermosillo):** Presidenta/Secretaria Sección Inmobiliaria CANACO Chihuahua. Pendiente recabar teléfono directo para agendar presentación MASC junto con Arq. Alejandro Lazzaroto. | Media (Prospección) |
| **#019** | 2026-09-15 | Alianzas Pactum ([[Mina_Memoria_Viva]]) | **Desayuno Estratégico con Lic. Ricardo Gutiérrez (Pactum):** Confirmado contacto previo ayer 14-Sep; programado posible desayuno mañana miércoles 16-Sep para afianzar esquema comercial, comisiones y conferencia MASC. | **Alta (16 Sep)** |
| **#011** | 2026-09-15 | Alianzas AMPI | **Seguimiento Fecha Plática AMPI:** Sin confirmación ni resultados aún por parte de Ever Sepúlveda (Presidente AMPI Chihuahua). Mantener presión o preparar vía directa con inmobiliarias / CANACO. | **Alta (Seguimiento)** |
| **#001** | 2026-08-20 | Telegram / Whisper ([[Eva_Ventas_WhatsApp]]) | **Soporte para notas de voz:** Integrar transcripción con Whisper para audios en Telegram y WhatsApp. | Media |
| **#006** | 2026-08-27 | Plática Gremio / Presentación | **Ajuste Sala Particular Autorizada MASC:** Reflejar esquema privado/bufete vs CEJA público en presentación y web. *(Fase final).* | Baja (Fase Final) |
| **#009** | 2026-08-27 | Flyers / Logos ([[Nexo_Copywriting]]) | **Inserción de Logotipos Oficiales:** Recabar e insertar logos de AMPI Chihuahua, Pactum, TSJE y Soluciones Inmobiliarias. | Media |
| **#010** | 2026-08-27 | Logística / Azenzo | **Programación y Reserva de Salón Azenzo:** Sujeta a definición de fecha de evento. | Media (En espera) |
| **#012** | 2026-08-27 | Expansión / CANACO | **Segunda Etapa de Pláticas con Sección Inmobiliaria CANACO:** Contacto clave: Arq. Alejandro Lazzaroto Rodríguez. | Media |
| **#013** | 2026-08-27 | Automatizaciones n8n ([[Maya_Orquestadora]]) | **Reporte Diario por Correo (7:00 AM):** Workflow cron en n8n Cloud para envío autónomo de resumen matutino. | Media |
| **#017** | 2026-08-31 | Demo Kit / Web | **Pruebas de Demo Kit y Presentación Pactum:** Plataforma en Vercel (https://mascsite.vercel.app) lista para demostración en el desayuno. | Media |

---

## 🔵 En Progreso / En Fase de Pruebas

| ID | Fecha Inicio | Módulo | Detalle | Estado |
|:---|:---|:---|:---|:---|
| **#033** | 2026-09-28 | Soporte Psicológico / Confidente Privado ([[Marco_Mentor_Confidente]]) | **Activación de Marco (Mentor Estoico & Psicólogo de Trinchera):** Implementación del skill `mentor-psicologo-marco` y creación de su bitácora confidencial privada (`00_Marco_Confidente/BITACORA_MARCO.md`) para descompresión emocional, escucha activa, enfoque y custodia de meditaciones de Enrique. | **Activo** |
| **#007** | 2026-08-31 | [[Eva_Ventas_WhatsApp]] + Landing | **Pruebas Activas Multi-usuario:** Landing Page y Widget Chatbot Eva en producción (https://mascsite.vercel.app). | **En Pruebas** |
| **#015** | 2026-08-31 | Supabase Vector + RAG | **Calibración Base de Conocimiento:** Validación de respuestas sobre precios, honorarios y ley MASC. | **En Pruebas** |
| **#016** | 2026-08-31 | Contenido / Q&A | **Evaluación de Preguntas Frecuentes:** Banco de preguntas y respuestas en test con usuarios reales. | **En Pruebas** |

---

## 🟢 Resueltos Recientes

| ID | Fecha | Módulo | Solución Aplicada |
|:---|:---|:---|:---|
| **#018** | 2026-08-31 | Landing Page MASC | Rediseño Glassmorphic Sapphire/Cobalt en mascsite/index.html, sincronizado en GitHub y desplegado en Vercel. |
| **#008** | 2026-08-27 | Branding & Skill | Estilo corporativo Glassmorphic Legal-Tech establecido. |
| **#005** | 2026-08-22 | Parsear Lead | Disparo determinístico de lead solo al completar caso/cierre en n8n. |
| **#004** | 2026-08-22 | Eva RAG | Corrección de bucle de despedida post-cierre. |
| **#003** | 2026-08-20 | Extractor JSON | Reemplazo de LangChain parser frágil por nodo JavaScript a prueba de fallos. |
| **#034** | 2026-10-03 | MASC Pactum & Marketing / Nexo | Campaña Semanal de Flyers de JA: Selección de dolor visceral y diseño de flyer para postear la próxima semana con rotación semanal continua. |
| **#035** | 2026-10-03 | MASC Pactum & Marketing / Nexo | Flyer Semanal JA (Semana 1): Generado flyer oficial 'El miedo del dueño no debería costarte tu comisión' con identidad Pactum y WhatsApp (614 540 4003). Guardado en `platica-gremio/04_Flyers_Historicos_Difusion/Flyer_MASC_Semana1_Miedo_Dueno_Pactum.jpg`. |
| **#036** | 2026-10-03 | MASC Pactum & Difusión / Contacto | Actualización Canónica de Línea de WhatsApp MASC / Pactum: Se fija como número oficial único de WhatsApp el '614 551 0188' (en sustitución del 614 540 4003) para todos los flyers, copys, campañas y canales de contacto de Justicia Alternativa. | **Resuelto y Desplegado** |
