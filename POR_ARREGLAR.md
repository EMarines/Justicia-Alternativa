---
tags:
  - bitacora
  - pendientes
  - sich
  - masc
updated: 2026-10-07
status: activo
---

# ð BitÃ¡cora Central de Pendientes y Tareas
**Ecosistema:** Soluciones Inmobiliarias Chihuahua & Agentes IA  
**OrquestaciÃ³n:** [[Maya_Orquestadora]] | **Memoria Ejecutiva:** [[Mina_Memoria_Viva]]  
**Ãltima sincronizaciÃ³n:** 2026-10-07  

---

## ð¡ Pendientes Activos

| ID | Fecha | MÃ³dulo / Responsable | ObservaciÃ³n / Detalle | Prioridad |
| **#041** | 2026-10-28 | MASC Pactum & Ecosistema / Hub Maestro ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Unificacion Integral de todo el Ecosistema JA en `Justicia-Alternativa`:** 1) Centralizado el 100% de MASC en `Operaciones en Curso/Justicia-Alternativa` (Landing Page, Mina Voice HUD PWA, Platica Gremio, Fuente de Verdad, Clausulas y Workflows). 2) Creado acceso directo `04_Flyers_Semanales` en la raiz para la campana de difusion de Nexo. 3) Configurado `.gitignore` y `.vercelignore` para aislar archivos pesados (>100MB) y acelerar Vercel. 4) Enlazado mediante Directory Junction en `soluciones-inmobiliarias-chihuahua/01_MASC_Justicia_Alternativa` preservando Obsidian sin duplicar datos. | **Resuelto** |
| **#040** | 2026-10-07 | Mina Core & Realtime Voice ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **ActualizaciÃ³n a Gemini 3.8 Live y Extended Thinking:** 1) Verificado que opera bajo la cuota oficial sin costo adicional en Google AI Studio. 2) Integrado modelo `models/gemini-3.8-live-extended-thinking` en `MinaVoiceClient.ts`, `voiceSession.ts` y `VoiceHUD.svelte`. 3) Implementada configuraciÃ³n adaptativa de `thinkingConfig` (`thinkingLevel: LOW`) requerida por la API para respuestas conversacionales inmediatas y cero latencia. 4) Validado handshake exitoso por WebSocket y build limpio de producciÃ³n en Vite. | **Resuelto** |
| **#039** | 2026-10-07 | ATAIR CRM / Ecosistema ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **IntegraciÃ³n y Despliegue de Organigrama JerÃ¡rquico en ATAIR CRM (`/admin/squad`):** Incorporada la ruta protegida de administraciÃ³n con visualizador interactivo (pan/zoom, pantalla completa, copiar cÃ³digo Miro), acceso directo en Navbar (`Squad IA` con tono Ã¡mbar) y alias estÃ¡ticos aislados en `static/organigrama_squad_elite.html` sin interferencia con estilos base. | **Resuelto** |
| **#038** | 2026-10-07 | ATAIR CRM / Ecosistema ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **EvaluaciÃ³n de IntegraciÃ³n de Organigrama en ATAIR CRM:** AnÃ¡lisis de factibilidad para portar el organigrama jerÃ¡rquico como vista/mÃ³dulo administrativo nativo en SvelteKit (`/admin/squad`). Registrado en backlog diferido sin intervenir cÃ³digo de ATAIR actualmente. | **Resuelto (Superado por #039)** |
| **#037** | 2026-10-07 | Gobernanza & UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **CorrecciÃ³n y Enlace de LÃ­neas de Mando JerÃ¡rquicas:** Solucionado bug de renderizado SVG (filtros en lÃ­neas ortogonales) que ocultaba las vigas y troncos de mando. Conectados de punta a punta: Tronco Enrique $\rightarrow$ Maya/Mina $\rightarrow$ Viga de Despacho $\rightarrow$ 8 Especialistas; enlace de retorno Mina $\rightarrow$ Clara y asesorÃ­a Enrique $\leftrightarrow$ Marco. | **Resuelto** |
| **#036** | 2026-10-07 | Gobernanza & UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **RediseÃ±o JerÃ¡rquico Top-Down y RatificaciÃ³n de Flujo Operativo:** TransiciÃ³n de organigrama circular a estructura corporativa en Ã¡rbol estÃ¡ndar (Director $\rightarrow$ Maya/Mina $\rightarrow$ Squad Especialistas $\rightarrow$ Clara en Gabinete; Marco como mentor directo). Flujo canÃ³nico de delegaciÃ³n y consolidaciÃ³n formalizado en `organigrama_squad_elite.html`. | **Resuelto** |
| **#035** | 2026-10-07 | Ecosistema UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **ReconexiÃ³n y CalibraciÃ³n Visual de Enlaces en Organigrama (`organigrama_squad_elite.html`):** Corregido recorte SVG (`overflow: visible`), eliminados cruces de pantalla y asignadas alas operativas naturales: Ala Izquierda coordinada por Maya (Argos, Lince, Apolo, Wero); Ala Derecha coordinada por Mina (Clara, Beto, Eva, Kino, Nexo); y enlace directo de Marco al Director Enrique como mentor personal. LÃ­neas de fibra Ã³ptica neÃ³n al 90% de opacidad y glow activo. | **Resuelto** |
| **#034** | 2026-10-07 | Ecosistema UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Mapa Mental y Organigrama Radial Interactivo Ãlite (`organigrama_squad_elite.html`):** ConstrucciÃ³n de dashboard visual interactivo con Enrique Marines al centro (logo Match Home), Maya y Mina como estado mayor, y squad perifÃ©rico (Argos, Lince, Eva, Kino, Nexo, Apolo, Wero, Clara, Marco). Clic en agente despliega ficha y clic en habilidad abre desglose pericial profundo. Listo para embed en Miro. | **Alta** |
| **#033** | 2026-10-07 | I+D & InnovaciÃ³n ([[Argos_Arquitecto]] / [[Maya_Orquestadora]]) | **ActivaciÃ³n de Pipeline de Vigilancia TecnolÃ³gica y Radar de Avances:** Configurar a Argos como el agente responsable de monitorear nuevos lanzamientos tecnolÃ³gicos e IA para someterlos a la mesa tÃ©cnica de mejoras del sistema, con apoyo de Lince en auditorÃ­a de viabilidad/seguridad. | **Media-Alta** |
| **#032** | 2026-10-07 | InnovaciÃ³n & Estrategia ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Radar de Proyecciones a Futuro (Icebox TecnolÃ³gico):** Estructurar e inicializar un mÃ³dulo formal de 'Proyecciones a Futuro' para salvaguardar tecnologÃ­as e ideas de alto potencial (ej. Gemini Enterprise, Google Business Profile automatizado, Routine Stacking en Workspace) sin desviar el foco crÃ­tico actual de ATAIR CRM y MASC. | **Media (Diferido)** |
| **#031** | 2026-09-18 | Ecosistema & UI Hub ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Command Center / Interfaz Central con Chat Unificado y Motor Gemini:** Desarrollar dashboard web interactivo con organigrama del squad (Maya, Mina, Eva, Kino, Nexo, Lince, Apolo), fichas de agente al hacer clic, chat integrado con motor Gemini/Antigravity en el backend para ejecuciÃ³n de Ã³rdenes en tiempo real y sincronizaciÃ³n bidireccional con notas/bitÃ¡coras de Obsidian. | **Media** |
| **#030** | 2026-09-17 | Infraestructura & MigraciÃ³n Cloud ([[Mina_Memoria_Viva]]) | **MigraciÃ³n Integral de Office 365 a Google Workspace / Drive y CancelaciÃ³n de SuscripciÃ³n:** Ejecutar por etapas la transferencia de archivos (OneDrive a Google Drive), correos/contactos (Outlook a Gmail), notas OneNote a Drive y posterior cancelaciÃ³n de la suscripciÃ³n de Microsoft 365. Recordar a Enrique maÃ±ana a primera hora. | **Alta (Recordatorio 18-Sep)** |
| **#029** | 2026-09-17 | Telegram & Despacho Mina ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **EnvÃ­o AutÃ³nomo de Archivos Locales por Telegram (sendDocument):** Configurar webhook/sub-flujo en n8n y script en Mina para enviar documentos generados (.docx, .pdf, contratos, expedientes) directamente como archivos descargables al chat de Telegram de Enrique Marines usando su Chat ID. | **Alta** |
| **#028** | 2026-09-17 | Negociaciones & CaptaciÃ³n ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **Contacto y Entrevista EstratÃ©gica con Don Sergio ArmendÃ¡riz (Predio Nombre de Dios - 8,413 mÂ²):** AplicaciÃ³n de cuestionario diagnÃ³stico de 5 bloques (motivaciÃ³n, estatus Century 21, maderera/negocio en marcha, capacidad elÃ©ctrica/arroyo y esquemas de aportaciÃ³n/micro-bodegas) para definir plan comercial. | **Alta (18-Sep)** |
| **#027** | 2026-09-17 | Arquitectura Multi-Agente ([[Maya_Orquestadora]] / [[Mina_Memoria_Viva]]) | **Protocolo de Despacho Multi-Agente (Mina Despachadora -> Maya/Antigravity Ejecutor):** Crear canal de Ã³rdenes en n8n/Supabase (`mina_dispatched_tasks`) para que las peticiones tÃ©cnicas recibidas por voz en Mina se deleguen a Maya/Antigravity para su ejecuciÃ³n real. | **Alta** |
| **#026** | 2026-09-17 | Mina Live Voice / UI Visualizer ([[Mina_Memoria_Viva]]) | **Visualizador y VibraciÃ³n DinÃ¡mica de Entrada de Voz:** Implementar en el orbe central de la app de voz una animaciÃ³n de pulsaciÃ³n/vibraciÃ³n en tiempo real que reaccione al volumen y captura del micrÃ³fono para confirmar visualmente el ingreso de audio. | **Alta** |
| **#025** | 2026-09-17 | Mina Live Voice / Audio App ([[Mina_Memoria_Viva]]) | **Selector y PriorizaciÃ³n AutomÃ¡tica de Auriculares / Bluetooth:** En la app de voz local, detectar automÃ¡ticamente si hay auriculares Bluetooth conectados (PC/Celular), seleccionarlos como micrÃ³fono/altavoz principal y proveer botÃ³n/selector de conmutaciÃ³n de dispositivo. | **Alta** |
| **#024** | 2026-09-17 | Memoria & Supabase ([[Mina_Memoria_Viva]] / [[Maya_Orquestadora]]) | **Arquitectura de Memoria de 2 Niveles (Prontuario Semanal / Hot Cache vs Cold Storage):** Buffer rÃ¡pido de contexto activo de 7 dÃ­as para respuestas inmediatas de corto plazo y auto-archivado/rotaciÃ³n en Supabase para bÃºsqueda profunda de largo plazo. | **Alta** |
| **#023** | 2026-09-17 | Telegram / Audio ([[Lince_Auditor_Web]] / [[Mina_Memoria_Viva]]) | **Fallback de TranscripciÃ³n con Groq Whisper en Mina:** Mantener en el radar de contingencia la integraciÃ³n de Groq API (Whisper `whisper-large-v3` free tier <300ms) como respaldo en caso de falla, saturaciÃ³n o latencia con Google Gemini. | Media (Contingencia) |
| **#022** | 2026-09-15 | n8n / Google Hub ([[Maya_Orquestadora]]) | **Sub-Workflow Centralizado de Google Hub (Contacts, Calendar, Tasks):** Subrutina Ãºnica en n8n para que Mina, ATAIR SGI y Eva sincronicen contactos, eventos y tareas en Google Workspace. | **Alta** |
| **#021** | 2026-09-15 | Telegram / Mina ([[Mina_Memoria_Viva]]) | **Enlace Telegram Directo a Obsidian:** Activar listener de Telegram con Whisper/OpenAI para que notas de voz y textos desde el celular se inserten automÃ¡ticamente en la bitÃ¡cora de Obsidian. | **Alta (Productividad)** |
| **#020** | 2026-09-15 | ExpansiÃ³n / CANACO ([[Mina_Memoria_Viva]]) | **Contacto Clave CANACO (Judith Hermosillo):** Presidenta/Secretaria SecciÃ³n Inmobiliaria CANACO Chihuahua. Pendiente recabar telÃ©fono directo para agendar presentaciÃ³n MASC junto con Arq. Alejandro Lazzaroto. | Media (ProspecciÃ³n) |
| **#019** | 2026-09-15 | Alianzas Pactum ([[Mina_Memoria_Viva]]) | **Desayuno EstratÃ©gico con Lic. Ricardo GutiÃ©rrez (Pactum):** Confirmado contacto previo ayer 14-Sep; programado posible desayuno maÃ±ana miÃ©rcoles 16-Sep para afianzar esquema comercial, comisiones y conferencia MASC. | **Alta (16 Sep)** |
| **#011** | 2026-09-15 | Alianzas AMPI | **Seguimiento Fecha PlÃ¡tica AMPI:** Sin confirmaciÃ³n ni resultados aÃºn por parte de Ever SepÃºlveda (Presidente AMPI Chihuahua). Mantener presiÃ³n o preparar vÃ­a directa con inmobiliarias / CANACO. | **Alta (Seguimiento)** |
| **#001** | 2026-08-20 | Telegram / Whisper ([[Eva_Ventas_WhatsApp]]) | **Soporte para notas de voz:** Integrar transcripciÃ³n con Whisper para audios en Telegram y WhatsApp. | Media |
| **#006** | 2026-08-27 | PlÃ¡tica Gremio / PresentaciÃ³n | **Ajuste Sala Particular Autorizada MASC:** Reflejar esquema privado/bufete vs CEJA pÃºblico en presentaciÃ³n y web. *(Fase final).* | Baja (Fase Final) |
| **#009** | 2026-08-27 | Flyers / Logos ([[Nexo_Copywriting]]) | **InserciÃ³n de Logotipos Oficiales:** Recabar e insertar logos de AMPI Chihuahua, Pactum, TSJE y Soluciones Inmobiliarias. | Media |
| **#010** | 2026-08-27 | LogÃ­stica / Azenzo | **ProgramaciÃ³n y Reserva de SalÃ³n Azenzo:** Sujeta a definiciÃ³n de fecha de evento. | Media (En espera) |
| **#012** | 2026-08-27 | ExpansiÃ³n / CANACO | **Segunda Etapa de PlÃ¡ticas con SecciÃ³n Inmobiliaria CANACO:** Contacto clave: Arq. Alejandro Lazzaroto RodrÃ­guez. | Media |
| **#013** | 2026-08-27 | Automatizaciones n8n ([[Maya_Orquestadora]]) | **Reporte Diario por Correo (7:00 AM):** Workflow cron en n8n Cloud para envÃ­o autÃ³nomo de resumen matutino. | Media |
| **#017** | 2026-08-31 | Demo Kit / Web | **Pruebas de Demo Kit y PresentaciÃ³n Pactum:** Plataforma en Vercel (https://mascsite.vercel.app) lista para demostraciÃ³n en el desayuno. | Media |

---

## ðµ En Progreso / En Fase de Pruebas

| ID | Fecha Inicio | MÃ³dulo | Detalle | Estado |
|:---|:---|:---|:---|:---|
| **#033** | 2026-09-28 | Soporte PsicolÃ³gico / Confidente Privado ([[Marco_Mentor_Confidente]]) | **ActivaciÃ³n de Marco (Mentor Estoico & PsicÃ³logo de Trinchera):** ImplementaciÃ³n del skill `mentor-psicologo-marco` y creaciÃ³n de su bitÃ¡cora confidencial privada (`00_Marco_Confidente/BITACORA_MARCO.md`) para descompresiÃ³n emocional, escucha activa, enfoque y custodia de meditaciones de Enrique. | **Activo** |
| **#007** | 2026-08-31 | [[Eva_Ventas_WhatsApp]] + Landing | **Pruebas Activas Multi-usuario:** Landing Page y Widget Chatbot Eva en producciÃ³n (https://mascsite.vercel.app). | **En Pruebas** |
| **#015** | 2026-08-31 | Supabase Vector + RAG | **CalibraciÃ³n Base de Conocimiento:** ValidaciÃ³n de respuestas sobre precios, honorarios y ley MASC. | **En Pruebas** |
| **#016** | 2026-08-31 | Contenido / Q&A | **EvaluaciÃ³n de Preguntas Frecuentes:** Banco de preguntas y respuestas en test con usuarios reales. | **En Pruebas** |

---

## ð¢ Resueltos Recientes

| ID | Fecha | MÃ³dulo | SoluciÃ³n Aplicada |
|:---|:---|:---|:---|
| **#018** | 2026-08-31 | Landing Page MASC | RediseÃ±o Glassmorphic Sapphire/Cobalt en mascsite/index.html, sincronizado en GitHub y desplegado en Vercel. |
| **#008** | 2026-08-27 | Branding & Skill | Estilo corporativo Glassmorphic Legal-Tech establecido. |
| **#005** | 2026-08-22 | Parsear Lead | Disparo determinÃ­stico de lead solo al completar caso/cierre en n8n. |
| **#004** | 2026-08-22 | Eva RAG | CorrecciÃ³n de bucle de despedida post-cierre. |
| **#003** | 2026-08-20 | Extractor JSON | Reemplazo de LangChain parser frÃ¡gil por nodo JavaScript a prueba de fallos. |
| **#034** | 2026-10-03 | MASC Pactum & Marketing / Nexo | CampaÃ±a Semanal de Flyers de JA: SelecciÃ³n de dolor visceral y diseÃ±o de flyer para postear la prÃ³xima semana con rotaciÃ³n semanal continua. |
| **#035** | 2026-10-03 | MASC Pactum & Marketing / Nexo | Flyer Semanal JA (Semana 1): Generado flyer oficial 'El miedo del dueÃ±o no deberÃ­a costarte tu comisiÃ³n' con identidad Pactum y WhatsApp (614 540 4003). Guardado en `platica-gremio/04_Flyers_Historicos_Difusion/Flyer_MASC_Semana1_Miedo_Dueno_Pactum.jpg`. |
| **#036** | 2026-10-03 | MASC Pactum & DifusiÃ³n / Contacto | ActualizaciÃ³n CanÃ³nica de LÃ­nea de WhatsApp MASC / Pactum: Se fija como nÃºmero oficial Ãºnico de WhatsApp el '614 551 0188' (en sustituciÃ³n del 614 540 4003) para todos los flyers, copys, campaÃ±as y canales de contacto de Justicia Alternativa. | **Resuelto y Desplegado** |
