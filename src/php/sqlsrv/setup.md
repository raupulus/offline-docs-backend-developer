---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/sqlsrv.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sqlsrv/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sqlsrv
translation_status: ready
translation_reviewed: false
translation_revision: c758e862c
order: 86340
---

## Instalación/Configuración

## Requisitos

La extensión SQLSRV puede ser utilizada en los siguientes sistemas operativos: Windows Vista Service Pack 2 o superior, Windows Server 2008 Service Pack 2 o superior, Windows Server 2008 R2, Windows 7

La extensión SQLSRV requiere que el cliente nativo Microsoft SQL Server 2012 esté instalado en la misma máquina que la que ejecuta PHP. Si el cliente nativo Microsoft SQL Server 2012 no está instalado, haga clic en el enlace apropiado a continuación para descargarlo: [Descarga del paquete x86](http://go.microsoft.com/fwlink/?LinkID=239647), [Descarga del paquete x64](http://go.microsoft.com/fwlink/?LinkID=239648)

La descarga SQLSRV viene con 8 controladores, de los cuales 4 están dedicados al soporte de PDO.

La versión más reciente del controlador está disponible para descargar aquí: [descarga de SQLSRV](http://msdn.microsoft.com/en-us/sqlserver/ff657782.aspx).

Para más información sobre los requisitos previos de SQLSRV, consulte el capítulo sobre los [requisitos del sistema SQLSRV](http://msdn.microsoft.com/en-us/library/cc296170.aspx).

## Tipos de recursos

### Recurso de conexión

Un recurso de conexión devuelto por la función `sqlsrv_connect`.

### Recurso de consulta

Un recurso de consulta devuelto por la función `sqlsrv_query` o la función `sqlsrv_prepare`.
