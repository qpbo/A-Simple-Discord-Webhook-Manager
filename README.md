<div align="center">

```
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                        MULTITOOL V.1.0
```

# 🛠️ Discord Webhook Multitool

### *Herramienta profesional de línea de comandos para la gestión, análisis y control de Webhooks de Discord*

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Production-success?style=for-the-badge)](https://github.com/tu-usuario/discord-webhook-multitool)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey?style=for-the-badge)](https://github.com/tu-usuario/discord-webhook-multitool)

---

<img src="https://img.shields.io/badge/Maintained-Yes-brightgreen?style=flat-square" alt="Maintained">
<img src="https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square" alt="Version">
<img src="https://img.shields.io/badge/Built%20with-❤️-red?style=flat-square" alt="Built with Love">

</div>

---

## 📖 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características Principales](#-características-principales)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Funcionalidades Detalladas](#-funcionalidades-detalladas)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Dependencias](#-dependencias)
- [Advertencia Legal](#%EF%B8%8F-advertencia-legal)
- [Roadmap](#-roadmap)
- [Contribuciones](#-contribuciones)
- [Créditos](#-créditos)
- [Licencia](#-licencia)

---

## 📝 Descripción

**Discord Webhook Multitool** es una herramienta CLI (Command Line Interface) avanzada desarrollada en **Python 3.8+**, diseñada para administradores de servidores, desarrolladores y auditores de seguridad que necesiten gestionar y analizar Webhooks de Discord de manera eficiente y profesional.

Con una interfaz colorida e intuitiva, este multitool ofrece funcionalidades completas para inspeccionar, probar y administrar webhooks sin necesidad de herramientas externas o APIs complejas.

> **💡 Ideal para:** Testing de integraciones, auditorías de seguridad, análisis forense de webhooks, y gestión automatizada de notificaciones.

---

## ✨ Características Principales

<table>
<tr>
<td width="50%">

### 🔍 **Inspector Avanzado**
- Extracción completa de metadatos del webhook
- Cálculo automático de fecha de creación (desde Snowflake ID)
- Información de servidor (Guild ID) y canal
- Visualización de avatares y tokens (parcialmente ocultados)
- Detección de tipo de webhook (Bot/Webhook estándar)

</td>
<td width="50%">

### 📨 **Sistema de Mensajería**
- Envío rápido de mensajes de texto
- Soporte para contenido personalizado
- Manejo inteligente de errores
- Feedback visual inmediato
- Compatible con rate limits de Discord

</td>
</tr>
<tr>
<td width="50%">

### 🚀 **Stress Testing**
- Herramienta de spam controlado
- Pruebas de resistencia a rate limits
- Control de cantidad de mensajes
- Capacidad de interrupción (Ctrl+C)
- Delay configurable entre mensajes

</td>
<td width="50%">

### 🗑️ **Gestión Segura**
- Eliminación permanente de webhooks
- Sistema de confirmación de seguridad
- Logging detallado de operaciones
- Manejo robusto de errores
- Validación de URLs en tiempo real

</td>
</tr>
</table>

### 🎨 **Características Adicionales**

| Característica | Descripción |
|:--------------|:------------|
| **CLI Colorida** | Interfaz con `colorama` que mejora la legibilidad y experiencia de usuario |
| **Banner ASCII** | Diseño profesional con arte ASCII personalizado |
| **Multiplataforma** | Compatible con Windows, Linux y macOS |
| **Código Limpio** | Arquitectura orientada a objetos, extensible y mantenible |
| **Zero Config** | Funciona inmediatamente después de instalar dependencias |
| **Session Manager** | Reutilización de conexiones HTTP para mejor rendimiento |

---

## 📸 Capturas de Pantalla

<div align="center">

### 🖥️ Menú Principal

```
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝ 
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗ 
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                        MULTITOOL V.1.0
                        By: Carliyo

Selecciona una operación:

[1] Obtener Info (Inspector)
[2] Enviar Mensaje Simple
[3] Spammer (Posible Rate-Limit si se abusa)
[4] Eliminar Webhook
[5] Creditos
[6] Salir

-----------------------------------
root@carliyo's-webhook-tool:~# _
```

### 🔍 Inspector de Webhook

```
--- REPORTE DE WEBHOOK ---
 Estado:      ACTIVO
 Nombre:      Mi Webhook Test
 ID:          123456789012345678
 Guild ID:    987654321098765432
 Channel ID:  111222333444555666
 Creado:      2025-01-15 10:30:45
 Token:       AbCdEfGhIj... (Oculto)
 Avatar:      https://cdn.discordapp.com/avatars/...
```

</div>

---

## 🚀 Instalación

### Prerrequisitos

Asegúrate de tener instalado **Python 3.8** o superior en tu sistema:

```bash
python --version
```

### Método 1: Instalación Rápida (Recomendado)

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/discord-webhook-multitool.git

# 2. Accede al directorio
cd discord-webhook-multitool

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Ejecuta la herramienta
python webhook_manager.py
```

### Método 2: Instalación Manual

```bash
# Instala las dependencias manualmente
pip install requests colorama python-dotenv
```

### Verificación de Instalación

Para verificar que todo está correctamente instalado:

```bash
python webhook_manager.py
```

Si ves el banner ASCII y el menú principal, ¡la instalación fue exitosa! 🎉

---

## 💻 Uso

### Inicio Rápido

1. **Ejecuta el script:**
   ```bash
   python webhook_manager.py
   ```

2. **Selecciona una opción** del menú numérico (1-6)

3. **Introduce la URL del webhook** cuando se te solicite

4. **Sigue las instrucciones** en pantalla para cada funcionalidad

### Ejemplo de Uso - Inspector

```bash
# Paso 1: Ejecutar
python webhook_manager.py

# Paso 2: Seleccionar opción 1
[?] root@carliyo's-webhook-tool:~# 1

# Paso 3: Pegar URL del webhook
[?] Ingresa la URL del Webhook: https://discord.com/api/webhooks/YOUR_WEBHOOK_URL

# Resultado: Se mostrará toda la información del webhook
```

### Ejemplo de Uso - Enviar Mensaje

```bash
# Opción 2 en el menú
[?] URL del Webhook: https://discord.com/api/webhooks/YOUR_WEBHOOK_URL
[?] Mensaje a enviar: ¡Hola desde Webhook Multitool!

[+] ÉXITO: Mensaje enviado correctamente.
```

---

## 🛠️ Funcionalidades Detalladas

### 1️⃣ Inspector de Webhooks

Analiza en profundidad cualquier webhook de Discord y extrae información valiosa:

**Información Extraída:**
- ✅ Estado (Activo/Inactivo)
- ✅ Nombre del webhook
- ✅ ID único (Snowflake)
- ✅ Guild ID (Servidor)
- ✅ Channel ID (Canal)
- ✅ **Fecha de creación calculada** desde el Snowflake ID
- ✅ Token (parcialmente oculto por seguridad)
- ✅ URL del avatar (si existe)
- ✅ Tipo de webhook

**Casos de uso:**
- Auditoría de webhooks existentes
- Análisis forense de webhooks sospechosos
- Verificación de configuración de webhooks

---

### 2️⃣ Envío de Mensajes

Envía mensajes rápidamente a través de cualquier webhook:

**Características:**
- Envío instantáneo
- Soporte para texto plano
- Manejo de errores de red
- Detección de rate limits

**Ejemplo:**
```python
URL: https://discord.com/api/webhooks/123/ABC
Mensaje: "Notificación automática del sistema"
```

---

### 3️⃣ Spammer / Stress Testing

Herramienta de testing para comprobar límites y estabilidad:

> ⚠️ **ADVERTENCIA:** Úsalo solo en webhooks de tu propiedad o con permiso explícito.

**Configuración:**
- Cantidad de mensajes personalizables
- Delay de 0.5 segundos entre mensajes (respeta rate limits básicos)
- Interrupción con `Ctrl+C`
- Contador de mensajes enviados/fallidos

**Rate Limits de Discord:**
- **5 mensajes / 2 segundos** por webhook
- **30 mensajes / 60 segundos** por webhook

---

### 4️⃣ Eliminación de Webhooks

Borra permanentemente un webhook de los servidores de Discord:

**Seguridad:**
- Requiere confirmación escribiendo `DELETE`
- Operación irreversible
- Logging de operación
- Validación antes de eliminar

**Proceso:**
```
[?] URL del Webhook a ELIMINAR: [Tu URL]
[?] Escribe 'DELETE' para confirmar: DELETE

[+] ÉXITO: Webhook eliminado permanentemente.
```

---

### 5️⃣ Créditos e Información

Muestra información sobre el desarrollador, versión y enlaces:

- Nombre del desarrollador
- Versión actual
- Repositorio de GitHub
- Año de desarrollo
- Disclaimer legal

---

## 📂 Estructura del Proyecto

```
discord-webhook-multitool/
│
├── 📄 webhook_manager.py      # Script principal (246 líneas)
│   ├── Clase: DiscordWebhookManager
│   ├── Funciones de menú
│   ├── Utilidades visuales
│   └── Loop principal
│
├── 📄 requirements.txt        # Dependencias del proyecto
│   ├── requests
│   ├── colorama
│   └── python-dotenv
│
├── 📄 README.md               # Documentación completa
│
└── 📄 LICENSE                 # Licencia MIT (opcional)
```

### Arquitectura del Código

```
webhook_manager.py
│
├── [Imports y Configuración]
│   ├── requests (HTTP)
│   ├── colorama (Colores CLI)
│   └── datetime (Cálculo de fechas)
│
├── [Clase DiscordWebhookManager]    # Backend de operaciones
│   ├── validate_url()               # Validación de URLs
│   ├── get_info()                   # Obtener información
│   ├── delete()                     # Eliminar webhook
│   ├── send_message()               # Enviar mensajes
│   └── modify()                     # Modificar webhook (Futuro)
│
├── [Utilidades Visuales]
│   ├── clear()                      # Limpiar consola
│   ├── print_log()                  # Sistema de logging
│   └── pause()                      # Pausar ejecución
│
├── [Funciones de Menú]
│   ├── menu_info()                  # Inspector
│   ├── menu_send()                  # Enviar mensaje
│   ├── menu_spam()                  # Spammer
│   ├── menu_delete()                # Eliminar
│   └── action_credits()             # Créditos
│
└── [main()]                         # Loop principal
```

---

## 📦 Dependencias

El proyecto utiliza las siguientes librerías de Python:

| Librería | Versión | Propósito |
|:---------|:--------|:----------|
| **requests** | `>=2.31.0` | Realización de peticiones HTTP a la API de Discord |
| **colorama** | `>=0.4.6` | Colores y estilización de la interfaz CLI |
| **python-dotenv** | `>=1.0.0` | Gestión de variables de entorno (opcional) |

### requirements.txt

```txt
requests>=2.31.0
colorama>=0.4.6
python-dotenv>=1.0.0
```

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

O instalar individualmente:

```bash
pip install requests colorama python-dotenv
```

---

## ⚖️ Advertencia Legal

> **⚠️ IMPORTANTE - LEE ESTO ANTES DE USAR**

Esta herramienta ha sido desarrollada **exclusivamente con fines educativos, de aprendizaje y auditoría de seguridad personal**.

### 📜 Disclaimer

- ✅ **Uso permitido:** Webhooks de tu propiedad, entornos de testing, auditorías autorizadas
- ❌ **Uso prohibido:** Webhooks ajenos sin permiso, ataques DoS, spam malicioso, violación de ToS

### 🚨 Responsabilidad

- El autor (**Carliyo**) **NO se hace responsable** del mal uso, daños o consecuencias derivadas del uso indebido de este software.
- El uso de funciones como **Spammer** o **Eliminación** en webhooks que no sean de tu propiedad puede **violar los Términos de Servicio de Discord** y leyes locales/internacionales.
- Al utilizar esta herramienta, aceptas toda la responsabilidad sobre tus acciones.

### 📋 Términos de Servicio de Discord

El uso indebido de webhooks puede resultar en:
- Suspensión de tu cuenta de Discord
- Baneo permanente del servidor
- Acciones legales en casos graves

### 🛡️ Buenas Prácticas

1. **Úsalo solo en webhooks de tu propiedad**
2. Respeta los rate limits de Discord
3. No lo utilices para spam o acoso
4. Infórmate sobre las leyes locales relacionadas con ciberseguridad
5. Mantén tus tokens y URLs privadas

---

## 🗺️ Roadmap

### Versión 1.0.0 (Actual) ✅
- [x] Inspector de webhooks
- [x] Envío de mensajes
- [x] Spammer/stress testing
- [x] Eliminación de webhooks
- [x] Interfaz CLI colorida

### Versión 1.1.0 (Próxima) 🚧
- [ ] Soporte para embeds personalizados
- [ ] Modificación de avatar y nombre del webhook
- [ ] Exportación de reportes a JSON/TXT
- [ ] Modo batch (múltiples webhooks desde archivo)
- [ ] Historial de operaciones

### Versión 2.0.0 (Futuro) 💡
- [ ] Interfaz gráfica (GUI) opcional
- [ ] Programación de mensajes
- [ ] Sistema de plantillas para mensajes
- [ ] Análisis de rendimiento y estadísticas
- [ ] Integración con APIs de terceros
- [ ] Modo silencioso para scripts automatizados

¿Tienes una sugerencia? ¡[Abre un issue](https://github.com/qpbo/A-Simple-Discord-Webhook-Manager/issues)!

---

## 🤝 Contribuciones

Las contribuciones son **bienvenidas** y se agradecen enormemente. Si deseas contribuir:

### Cómo Contribuir

1. **Fork** el repositorio
2. Crea una **rama** para tu feature (`git checkout -b feature/AmazingFeature`)
3. Haz **commit** de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. **Push** a la rama (`git push origin feature/AmazingFeature`)
5. Abre un **Pull Request**

### Código de Conducta

- Sé respetuoso con otros contribuidores
- Reporta bugs de manera constructiva
- Documenta tus cambios claramente
- Sigue el estilo de código existente

### Reportar Bugs

Si encuentras un bug, por favor abre un [issue](https://github.com/tu-usuario/discord-webhook-multitool/issues) con:
- Descripción del problema
- Pasos para reproducirlo
- Comportamiento esperado vs. actual
- Screenshots (si aplica)
- Información del sistema (OS, versión de Python)

---

## 👨‍💻 Créditos

<div align="center">

### Desarrollado con ❤️ por **Carliyo**

[![GitHub](https://img.shields.io/badge/GitHub-@Carliyo-181717?style=for-the-badge&logo=github)](https://github.com/qpbo)
[![Discord](https://img.shields.io/badge/Discord-Carliyo%230000-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com)

**Versión:** 1.0.0  
**Año:** 2025  
**Mantenido:** Sí ✅

</div>

### Agradecimientos

- Comunidad de Python por las excelentes librerías
- Documentación oficial de Discord API
- Todos los contribuidores futuros

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2025 Carliyo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

### 🌟 Si este proyecto te fue útil, considera darle una estrella! ⭐

[![Star on GitHub](https://img.shields.io/github/stars/tu-usuario/discord-webhook-multitool?style=social)](https://github.com/tu-usuario/discord-webhook-multitool)

---

**Made with Python 🐍 | Powered by Discord API 💬 | Styled with Colorama 🎨**

*Última actualización: Diciembre 2025*

</div>
