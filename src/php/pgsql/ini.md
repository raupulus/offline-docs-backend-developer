---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/pgsql.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pgsql/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pgsql
translation_status: ready
translation_revision: d4d5216e7
order: 63820
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [pgsql.allow_persistent](#ini.pgsql.allow-persistent) | "1" | `INI_SYSTEM` |  |
| [pgsql.max_persistent](#ini.pgsql.max-persistent) | "-1" | `INI_SYSTEM` |  |
| [pgsql.max_links](#ini.pgsql.max-links) | "-1" | `INI_SYSTEM` |  |
| [pgsql.auto_reset_persistent](#ini.pgsql.auto-reset-persistent) | "0" | `INI_SYSTEM` |  |
| [pgsql.ignore_notice](#ini.pgsql.ignore-notice) | "0" | `INI_ALL` |  |
| [pgsql.log_notice](#ini.pgsql.log-notice) | "0" | `INI_ALL` |  |

Opciones de configuración PostgreSQL

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`pgsql.allow_persistent` `bool`  
Si se permiten conexiones Postgres persistentes.

`pgsql.max_persistent` `int`  
El número máximo de conexiones Postgres persistentes por proceso.

`pgsql.max_links` `int`  
El número máximo de conexiones Postgres por proceso, incluyendo conexiones persistentes.

`pgsql.auto_reset_persistent` `int`  
Detectar conexiones persitentes rotas con `pg_pconnect`. Necesita un breve tiempo adicional.

`pgsql.ignore_notice` `int`  
Hacer caso o no a los mensajes de avisos del backend PostgreSQL.

`pgsql.log_notice` `int`  
Registrar o no los mensajes de aviso del backend PostgreSQL. La directiva PHP [ pgsql.ignore_notice](#ini.pgsql.ignore-notice) debe estar apagada para registrar los mensajes de aviso
