---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/taint.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/taint/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: taint
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 93820
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [taint.enable](#ini.taint.enable) | 0 | `INI_SYSTEM` |  |
| [taint.error_level](#ini.taint.error-level) | E_WARNING | `INI_ALL` |  |

Opciones de configuración de taint

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`taint.enable` `int`  
Si habilitar taint.

`taint.error_level` `int`  
El tipo del error del que taint informará cuando encuentre una cadena corrupta.
