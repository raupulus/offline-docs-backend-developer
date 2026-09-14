---
title: La clase mysqli_driver
source_url: https://www.php.net/manual/es/class.mysqli-driver.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_driver.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 55500
---

## Introducción

La clase `mysqli_driver` es una instancia del patrón monostate, es decir, solo hay un driver que puede ser accedido a través de un número arbitrario de instancias `mysqli_driver`.

## Sinopsis de la clase

final

mysqli_driver

Propiedades

public

readonly

string

client_info

public

readonly

int

client_version

public

readonly

int

driver_version

public

int

report_mode

## Propiedades

`client_info`  
La versión del encabezado de la API del cliente

`client_version`  
La versión del cliente

`driver_version`  
La versión del driver MySQLi

> [!WARNING]
> Esta propiedad está *obsoleta* a partir de PHP 8.1.0. Se desaconseja encarecidamente depender de esta propiedad.

`embedded`  
Si el soporte "MySQLi Embedded" está activado

> [!WARNING]
> Esta propiedad ha sido *eliminada* a partir de PHP 8.0.0.

`reconnect`  
Permite o no la reconexión (ver la directiva INI [mysqli.reconnect](#ini.mysqli.reconnect))

> [!WARNING]
> Esta propiedad ha sido *eliminada* junto con la directiva INI [mysqli.reconnect](#ini.mysqli.reconnect) a partir de PHP 8.2.0.

`report_mode`  
Se establece en `MYSQLI_REPORT_OFF`, `MYSQLI_REPORT_ALL` o cualquier combinación de `MYSQLI_REPORT_STRICT` (lanza excepciones en caso de errores), `MYSQLI_REPORT_ERROR` (reporta errores) y `MYSQLI_REPORT_INDEX` (errores en los índices). Ver también `mysqli_report`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | mysqli_driver::\$reconnect fue eliminada. |
| 8.1.0 | mysqli_driver::\$driver_version ha sido marcada como obsoleta. |
| 8.0.0 | mysqli_driver::\$embedded fue eliminada. |
| 7.4.0 | mysqli_driver::embedded_server_start y mysqli_driver:embedded_server_end fueron eliminadas. |
