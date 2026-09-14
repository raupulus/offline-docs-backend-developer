---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/mysql-xdevapi.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: d4d5216e7
order: 52580
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [xmysqlnd.collect_memory_statistics](#ini.xmysqlnd.collect-memory-statistics) | 0 | `INI_SYSTEM` |  |
| [xmysqlnd.collect_statistics](#ini.xmysqlnd.collect-statistics) | 1 | `INI_ALL` |  |
| [xmysqlnd.debug](#ini.xmysqlnd.debug) |  | `INI_SYSTEM` |  |
| [xmysqlnd.mempool_default_size](#ini.xmysqlnd.mempool-default-size) | 16000 | `INI_ALL` |  |
| [xmysqlnd.net_read_timeout](#ini.xmysqlnd.net-read-timeout) | 31536000 | `INI_SYSTEM` |  |
| [xmysqlnd.trace_alloc](#ini.xmysqlnd.trace-alloc) |  | `INI_SYSTEM` |  |

Opciones de configuración Mysql_xdevapi {#mysql-xdevapi.configuration.configuration}

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`xmysqlnd.collect_memory_statistics` `int`  

`xmysqlnd.collect_statistics` `int`  

`xmysqlnd.debug` `string`  

`xmysqlnd.mempool_default_size` `int`  

`xmysqlnd.net_read_timeout` `int`  

`xmysqlnd.trace_alloc` `string`
