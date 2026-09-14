---
title: Configuración en tiempo de ejecución
source_url: https://www.php.net/manual/es/sqlsrv.configuration.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86330
---

## Configuración en tiempo de ejecución

El comportamiento de estas funciones es afectado por la configuración en el archivo `php.ini`.

La tabla siguiente lista las opciones de configuración disponibles para la extensión. Para más información sobre estas opciones, consúltese el capítulo sobre la [gestión de errores y alertas SQLSRV](http://msdn.microsoft.com/en-us/library/cc626302.aspx).

| Nombre | Por defecto | Cambiable | Historial de cambios |
|----|----|----|----|
| sqlsrv.WarningsReturnAsErrors | 1 (`true`) | `INI_ALL` | Disponible a partir de SQLSRV 1.0 |
| sqlsrv.LogSubsystems | 0 | `INI_ALL` | Disponible a partir de SQLSRV 1.0 |
| sqlsrv.LogSeverity | 1 | `INI_ALL` | Disponible a partir de SQLSRV 1.0 |

Opciones de configuración SQLSRV
