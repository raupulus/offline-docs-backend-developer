---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/phpdbg.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phpdbg/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phpdbg
translation_status: ready
translation_reviewed: true
translation_revision: 06f14554e
order: 65060
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [phpdbg.eol](#ini.phpdbg.eol) | 2 | `INI_ALL` | Eliminada a partir de PHP 8.1.0 |
| [phpdbg.path](#ini.phpdbg.path) |  | 6 | Eliminada a partir de PHP 8.1.0 |

Opciones de configuración de phpdbg

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`phpdbg.eol` `mixed`  
El tipo de fin de línea a utilizar para la salida. Para definir el valor, se debe utilizar uno de los alias de string.

| `int` Valor | `string` Alias               |
|-------------|------------------------------|
| `0`         | `CRLF`, `crlf`, `DOS`, `dos` |
| `1`         | `LF`, `lf`, `UNIX`, `unix`   |
| `2`         | `CR`, `cr`, `MAC`, `mac`     |

`phpdbg.path` `string`
