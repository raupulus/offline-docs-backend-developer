---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/pdo-mysql.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_mysql/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_mysql
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 62380
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable |
|----|----|----|
| [pdo_mysql.default_socket](#ini.pdo-mysql.default-socket) | "/tmp/mysql.sock" | `INI_SYSTEM` |
| [pdo_mysql.debug](#ini.pdo-mysql.debug) | NULL | `INI_SYSTEM` |

Opciones de configuración del controlador PDO_MYSQL

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`pdo_mysql.default_socket` `string`  
Se define un socket de dominio Unix. El valor puede ser también definido en el momento de la compilación si se encuentra un socket de dominio Unix durante la configuración. Esta configuración INI solo está disponible bajo Unix.

`pdo_mysql.debug` `bool`  
Se activa el depurado para el controlador PDO_MYSQL. Esta configuración solo está disponible cuando el controlador PDO_MYSQL es compilado con mysqlnd y en modo de depurado PDO.
