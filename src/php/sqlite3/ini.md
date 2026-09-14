---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/sqlite3.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlite3/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlite3
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 85600
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [sqlite3.extension_dir](#ini.sqlite3.extension-dir) | "" | `INI_SYSTEM` |  |
| [sqlite3.defensive](#ini.sqlite3.defensive) | 1 | `INI_USER` | Disponible a partir de PHP 7.2.17 y 7.3.4 para libsqlite ≥ 3.26.0. Anterior a PHP 8.2.0 este parámetro solo podía ser modificado como `INI_SYSTEM`. |

Opciones de configuración Sqlite3

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`sqlite3.extension_dir` `string`  
Ruta hacia el directorio donde se encuentran las extensiones cargables para SQLite.

`sqlite3.defensive` `bool`  
Cuando el flag defensivo está activado, las funcionalidades del lenguaje que permiten a SQL ordinario corromper deliberadamente los archivos de la base de datos son desactivadas. Esto impide escribir directamente en el esquema, las tablas sombra (como las tablas de datos FTS) o la tabla virtual sqlite_dbpage. Este parámetro `php.ini` solo es efectivo para libsqlite ≥ 3.26.0.
