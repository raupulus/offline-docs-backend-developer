---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/pdo.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 61800
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre                     | Por defecto | Cambiable      | Historial de cambios |
|----------------------------|-------------|----------------|----------------------|
| [pdo.dsn.\*](#ini.pdo.dsn) |             | `php.ini` sólo |                      |

Opciones de configuración de PDO

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`pdo.dsn.*` `string`  
Define un alias DSN. Véase PDO::\_\_construct para una explicación completa.
