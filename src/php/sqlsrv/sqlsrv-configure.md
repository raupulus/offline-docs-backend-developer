---
title: sqlsrv_configure
description: Cambia la configuración de los drivers del gestionador de errores y de
  log
source_url: https://www.php.net/manual/es/function.sqlsrv-configure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/functions/sqlsrv-configure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86120
---

sqlsrv_configure

Cambia la configuración de los drivers del gestionador de errores y de log

## Descripción

```php
sqlsrv_configure(string $setting, mixed $value): bool
```php

Cambia la configuración de los drivers del gestionador de errores y de log.

## Parámetros

`setting`  
El nombre de la propiedad a configurar. Los valores posibles son "WarningsReturnAsErrors", "LogSubsystems", and "LogSeverity".

`value`  
El valor de la propiedad especificada. La tabla siguiente muestra los valores posibles:

| Propiedades | Opciones |
|----|----|
| WarningsReturnAsErrors | 1 (`true`) o 0 (`false`) |
| LogSubsystems | SQLSRV_LOG_SYSTEM_ALL (-1) SQLSRV_LOG_SYSTEM_CONN (2) SQLSRV_LOG_SYSTEM_INIT (1) SQLSRV_LOG_SYSTEM_OFF (0) SQLSRV_LOG_SYSTEM_STMT (4) SQLSRV_LOG_SYSTEM_UTIL (8) |
| LogSeverity | SQLSRV_LOG_SEVERITY_ALL (-1) SQLSRV_LOG_SEVERITY_ERROR (1) SQLSRV_LOG_SEVERITY_NOTICE (4) SQLSRV_LOG_SEVERITY_WARNING (2) |

Opciones de configuración de la gestión de errores y log

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

Gestionador de errores SQLSRV

.

Actividad de log de SQLSRV

.
