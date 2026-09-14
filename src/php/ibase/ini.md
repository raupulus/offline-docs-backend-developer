---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/ibase.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30580
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| [ibase.allow_persistent](#ini.ibase.allow-persistent) | "1" | `INI_SYSTEM` |  |
| [ibase.max_persistent](#ini.ibase.max-persistent) | "-1" | `INI_SYSTEM` |  |
| [ibase.max_links](#ini.ibase.max-links) | "-1" | `INI_SYSTEM` |  |
| [ibase.default_db](#ini.ibase.default-db) | NULL | `INI_SYSTEM` |  |
| [ibase.default_user](#ini.ibase.default-user) | NULL | `INI_ALL` |  |
| [ibase.default_password](#ini.ibase.default-password) | NULL | `INI_ALL` |  |
| [ibase.default_charset](#ini.ibase.default-charset) | NULL | `INI_ALL` |  |
| [ibase.timestampformat](#ini.ibase.timestampformat) | "%Y-%m-%d %H:%M:%S" | `INI_ALL` |  |
| [ibase.dateformat](#ini.ibase.dateformat) | "%Y-%m-%d" | `INI_ALL` |  |
| [ibase.timeformat](#ini.ibase.timeformat) | "%H:%M:%S" | `INI_ALL` |  |

Opciones de configuración iBase

Para más detalles sobre los modos INI\_\*, refiérase a [???](#configuration.changes.modes).

Aquí hay una aclaración sobre el uso de las directivas de configuración.

`ibase.allow_persistent` `bool`  
Acepta o no las [conexiones persistentes](#features.persistent-connections) a Firebird/Interbase.

`ibase.max_persistent` `int`  
El número máximo de conexiones persistentes Firebird/Interbase por proceso. Las nuevas conexiones con `ibase_pconnect` no serán persistentes si se alcanza este número máximo.

`ibase.max_links` `int`  
El número máximo de conexiones Firebird/Interbase por proceso, incluyendo las conexiones persistentes.

`ibase.default_db` `string`  
El nombre de la base de datos por defecto cuando ibase\_\[p\]connect() es llamado sin una base de datos específica. Si este valor está definido y el modo seguro SQL está activado, no se permitirá la conexión a otras bases de datos que no sean esta.

`ibase.default_user` `string`  
El nombre de usuario utilizado al conectar a la base de datos cuando no se especifica ninguno.

`ibase.default_password` `string`  
La contraseña utilizada al conectar a la base de datos cuando no se especifica ninguna.

`ibase.default_charset` `string`  
El conjunto de caracteres utilizado al conectar a la base de datos cuando no se especifica ninguno.

`ibase.timestampformat` `string`  

`ibase.dateformat` `string`  

`ibase.timeformat` `string`  
Estas directivas se utilizan para definir los formatos de fechas y horas que serán utilizados cuando las fechas/horas sean devueltas de un conjunto de resultados, o cuando se procesen argumentos en parámetros de fechas/horas.
