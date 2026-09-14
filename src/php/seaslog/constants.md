---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/seaslog.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: ed0559b36
order: 73080
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

`SEASLOG_VERSION` (`string`)  

`SEASLOG_AUTHOR` (`string`)  

`SEASLOG_ALL` (`string`)  
"ALL"

`SEASLOG_DEBUG` (`string`)  
"DEBUG" - Información detallada de depuración. Información detallada sobre los eventos.

`SEASLOG_INFO` (`string`)  
"INFO" - Eventos interesantes. Énfasis en el proceso de ejecución de la aplicación.

`SEASLOG_NOTICE` (`string`)  
"NOTICE" - Eventos normales pero significativos. Información más importante que el nivel INFO durante la ejecución.

`SEASLOG_WARNING` (`string`)  
"WARNING" - Ocurrencias excepcionales que no son errores. Información aberrante potencial que requiere atención y debe ser reparada.

`SEASLOG_ERROR` (`string`)  
"ERROR" - Errores de funcionamiento que no requieren acción inmediata pero que deberían necesitarla típicamente.

`SEASLOG_CRITICAL` (`string`)  
"CRITICAL" - Condiciones críticas. Requiere reparación inmediata, y el componente del programa está indisponible.

`SEASLOG_ALERT` (`string`)  
"ALERT" - Acción debe ser tomada inmediatamente. Atención inmediata debe ser prestada al personal concernido para las reparaciones de emergencia.

`SEASLOG_EMERGENCY` (`string`)  
"EMERGENCY" - Sistema inutilizable.

`SEASLOG_DETAIL_ORDER_ASC` (`int`)  
1

`SEASLOG_DETAIL_ORDER_DESC` (`int`)  
2

`SEASLOG_APPENDER_FILE` (`int`)  
1

`SEASLOG_APPENDER_TCP` (`int`)  
2

`SEASLOG_APPENDER_UDP` (`int`)  
3

`SEASLOG_CLOSE_LOGGER_STREAM_MOD_ALL` (`int`)  
1

`SEASLOG_CLOSE_LOGGER_STREAM_MOD_ASSIGN` (`int`)  
2

`SEASLOG_REQUEST_VARIABLE_DOMAIN_PORT` (`int`)  
1

`SEASLOG_REQUEST_VARIABLE_REQUEST_URI` (`int`)  
2

`SEASLOG_REQUEST_VARIABLE_REQUEST_METHOD` (`int`)  
3

`SEASLOG_REQUEST_VARIABLE_CLIENT_IP` (`int`)  
4
