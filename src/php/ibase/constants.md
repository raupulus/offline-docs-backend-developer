---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/ibase.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 4d8da4190
order: 29610
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

Las constantes siguientes pueden ser pasadas a `ibase_trans` para especificar el comportamiento de las transacciones.

| Constante | Descripción |
|----|----|
| IBASE_DEFAULT | Define el comportamiento por omisión. Este comportamiento es determinado por la biblioteca cliente, que es definida como IBASE_WRITE\|IBASE_CONCURRENCY\|IBASE_WAIT en la mayoría de los casos. |
| IBASE_READ | Inicia una transacción en modo de solo lectura |
| IBASE_WRITE | Inicia una transacción en modo de lectura / escritura |
| IBASE_CONSISTENCY | Inicia una transacción con el nivel de aislamiento definido a 'consistency', lo que significa que la transacción actual no puede leer desde tablas que han sido modificadas por otras transacciones. |
| IBASE_CONCURRENCY | Inicia una transacción con el nivel de aislamiento definido a 'concurrency' (o 'snapshot'), lo que significa que la transacción puede acceder a todas las tablas, pero no puede ver las modificaciones realizadas por otras transacciones una vez que la transacción ha comenzado. |
| IBASE_COMMITTED | Inicia una transacción con el nivel de aislamiento definido a 'read committed'. Este flag debe ser asociado con la constante `IBASE_REC_VERSION` o la constante `IBASE_REC_NO_VERSION`. Este nivel de aislamiento permite acceder a las modificaciones realizadas después del inicio de la transacción. Si la constante `IBASE_REC_NO_VERSION` es especificada, solo la última versión de las filas podrá ser leída. Si la constante `IBASE_REC_VERSION` es especificada, una fila puede ser leída siempre que una modificación esté pendiente en una transacción concurrente. |
| IBASE_WAIT | Indica que la transacción puede esperar y luego reintentar cuando aparece un conflicto. |
| IBASE_NOWAIT | Indica que la transacción fallará inmediatamente cuando aparece un conflicto. |

Constantes Firebird/InterBase

Las constantes siguientes pueden ser pasadas a las funciones `ibase_fetch_row`, `ibase_fetch_assoc` o `ibase_fetch_object` para especificar sus comportamientos.

| Constante | Descripción |
|----|----|
| IBASE_FETCH_BLOBS | También disponible bajo el nombre `IBASE_TEXT` por razones de compatibilidad ascendente. Permite leer el contenido de un BLOB "inline" en lugar de recorrerlo utilizando un identificador de BLOB. |
| IBASE_FETCH_ARRAYS | Permite leer un array "inline". De lo contrario, los identificadores de arrays son devueltos. Los identificadores de arrays solo pueden ser pasados como argumentos a las consultas INSERT, ya que ninguna función para manejar los identificadores de arrays está actualmente disponible. |
| IBASE_UNIXTIME | Permite devolver los campos de fecha y hora no como strings sino como timestamps UNIX (el número de segundos desde la época UNIX, que es el 1-Jan-1970 0:00 UTC). Esto puede ser problemático si se utilizan fechas anteriores a 1970 en algunos sistemas. |

Constantes Firebird/InterBase

Las constantes siguientes son utilizadas para pasar consultas y opciones a la API (`ibase_server_info`, `ibase_db_info`, `ibase_backup`, `ibase_restore` y `ibase_maintain_db`). Consulte el manual de Firebird/InterBase para más información sobre el significado de estas opciones.

`IBASE_BKP_IGNORE_CHECKSUMS`  
Opciones para `ibase_backup`

`IBASE_BKP_IGNORE_LIMBO`  
Opciones para `ibase_backup`

`IBASE_BKP_METADATA_ONLY`  
Opciones para `ibase_backup`

`IBASE_BKP_NO_GARBAGE_COLLECT`  
Opciones para `ibase_backup`

`IBASE_BKP_OLD_DESCRIPTIONS`  
Opciones para `ibase_backup`

`IBASE_BKP_NON_TRANSPORTABLE`  
Opciones para `ibase_backup`

`IBASE_BKP_CONVERT`  
Opciones para `ibase_backup`

`IBASE_RES_DEACTIVATE_IDX`  
Opciones para `ibase_restore`

`IBASE_RES_NO_SHADOW`  
Opciones para `ibase_restore`

`IBASE_RES_NO_VALIDITY`  
Opciones para `ibase_restore`

`IBASE_RES_ONE_AT_A_TIME`  
Opciones para `ibase_restore`

`IBASE_RES_REPLACE`  

`IBASE_RES_CREATE`  
Opciones para `ibase_restore`

`IBASE_RES_USE_ALL_SPACE`  
Opciones para `ibase_restore`

`IBASE_PRP_PAGE_BUFFERS`  

`IBASE_PRP_SWEEP_INTERVAL`  

`IBASE_PRP_SHUTDOWN_DB`  

`IBASE_PRP_DENY_NEW_TRANSACTIONS`  

`IBASE_PRP_DENY_NEW_ATTACHMENTS`  

`IBASE_PRP_RESERVE_SPACE`  

`IBASE_PRP_RES_USE_FULL`  

`IBASE_PRP_RES`  

`IBASE_PRP_WRITE_MODE`  

`IBASE_PRP_WM_ASYNC`  

`IBASE_PRP_WM_SYNC`  

`IBASE_PRP_ACCESS_MODE`  

`IBASE_PRP_AM_READONLY`  

`IBASE_PRP_AM_READWRITE`  

`IBASE_PRP_SET_SQL_DIALECT`  

`IBASE_PRP_ACTIVATE`  

`IBASE_PRP_DB_ONLINE`  

`IBASE_RPR_CHECK_DB`  

`IBASE_RPR_IGNORE_CHECKSUM`  

`IBASE_RPR_KILL_SHADOWS`  

`IBASE_RPR_MEND_DB`  

`IBASE_RPR_VALIDATE_DB`  

`IBASE_RPR_FULL`  

`IBASE_RPR_SWEEP_DB`  
Opciones de `ibase_maintain_db`

`IBASE_STS_DATA_PAGES`  

`IBASE_STS_DB_LOG`  

`IBASE_STS_HDR_PAGES`  

`IBASE_STS_IDX_PAGES`  

`IBASE_STS_SYS_RELATIONS`  
Opciones de `ibase_db_info`

`IBASE_SVC_SERVER_VERSION`  
Opciones para `ibase_server_info`

`IBASE_SVC_IMPLEMENTATION`  
Opciones para `ibase_server_info`

`IBASE_SVC_GET_ENV`  
Opciones para `ibase_server_info`

`IBASE_SVC_GET_ENV_LOCK`  

`IBASE_SVC_GET_ENV_MSG`  

`IBASE_SVC_USER_DBPATH`  

`IBASE_SVC_SVR_DB_INFO`  

`IBASE_SVC_GET_USERS`  
Opciones para `ibase_server_info`
