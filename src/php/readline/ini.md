---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/readline.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_revision: 53208f9bd
order: 68840
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre                        | Por defecto | Cambiable | Historial de cambios |
|-------------------------------|-------------|-----------|----------------------|
| [cli.pager](#ini.cli.pager)   | ""          | `INI_ALL` |                      |
| [cli.prompt](#ini.cli.prompt) | "\\b \\\> " | `INI_ALL` |                      |

Opciones de configuración Readline

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`cli.pager` `string`  
Herramienta externa para mostrar la salida de la [línea de comandos](#features.commandline).

`cli.prompt` `string`  
Véase [Línea de Comandos](#features.commandline).
