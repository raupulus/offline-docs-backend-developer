---
title: mysqli_driver::$report_mode
description: Define el modo de informe de errores de mysqli
source_url: https://www.php.net/manual/es/mysqli-driver.report-mode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_driver/report-mode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: c8ba91f7e
order: 55490
---

mysqli_driver::\$report_mode

mysqli_report

Define el modo de informe de errores de mysqli

## Descripción

Estilo orientado a objetos

int

mysqli_driver-\>report_mode

Estilo procedimental

```php
mysqli_report(int $flags): true
```php

Según los flags, esto define el modo de informe de errores de mysqli a excepción, advertencia o ninguno. Cuando se define como `MYSQLI_REPORT_ALL` o `MYSQLI_REPORT_INDEX` esto también informará sobre consultas que no utilizan un índice (o un índice incorrecto).

A partir de PHP 8.1.0, el valor por omisión es `MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT`. Anteriormente, era `MYSQLI_REPORT_OFF`.

## Parámetros

`flags`  
| Nombre | Descripción |
|----|----|
| `MYSQLI_REPORT_OFF` | Desactiva los informes (valor por omisión) |
| `MYSQLI_REPORT_ERROR` | Informa sobre errores desde llamadas a funciones mysqli |
| `MYSQLI_REPORT_STRICT` | Lanza una excepción `mysqli_sql_exception` para errores, en lugar de emitir alertas |
| `MYSQLI_REPORT_INDEX` | Informa si no se utiliza ningún índice o un índice incorrecto en una consulta |
| `MYSQLI_REPORT_ALL` | Define todas las opciones (informa sobre todo) |

Flags admitidos {#mysqli-driver.report-mode.parameters}

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El valor por omisión es ahora `MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT`. Anteriormente, era `MYSQLI_REPORT_OFF`. |

## Ejemplos

Estilo orientado a objetos

```
<?php

/* Activación del informe de errores */
$driver = new mysqli_driver();
$driver->report_mode = MYSQLI_REPORT_ALL;

try {
    /* si la conexión falla, se lanzará una mysqli_sql_exception */
    $mysqli = new mysqli("localhost", "my_user", "my_password", "my_db");

    /* esta consulta debería informar sobre un error */
    $result = $mysqli->query("SELECT Name FROM Nonexistingtable WHERE population > 50000");

    /* esta consulta debería informar sobre un índice incorrecto, si la columna population no tiene un índice */
    $result = $mysqli->query("SELECT Name FROM City WHERE population > 50000");
} catch (mysqli_sql_exception $e) {
    error_log($e->__toString());
}

   
```php

Estilo procedimental

```
<?php

/* Activación del informe de errores */
mysqli_report(MYSQLI_REPORT_ALL);

try {
    /* si la conexión falla, se lanzará una excepción mysqli_sql_exception */
    $link = mysqli_connect("localhost", "my_user", "my_password", "my_db");

    /* esta consulta debería informar sobre un error */
    $result = mysqli_query($link, "SELECT Name FROM Nonexistingtable WHERE population > 50000");

    /* esta consulta debería informar sobre un índice incorrecto, si la columna population no tiene un índice */
    $result = mysqli_query($link, "SELECT Name FROM City WHERE population > 50000");
} catch (mysqli_sql_exception $e) {
    error_log($e->__toString());
}

   
```php

Informe de errores a excepción de errores de índice incorrecto

```
<?php

/* Activación del informe de errores */
$driver = new mysqli_driver();
$driver->report_mode = MYSQLI_REPORT_ALL;

try {
    /* si la conexión falla, se lanzará una mysqli_sql_exception */
    $mysqli = new mysqli("localhost", "my_user", "my_password", "my_db");

    /* esta consulta debería informar sobre un error */
    $result = $mysqli->query("SELECT Name FROM Nonexistingtable WHERE population > 50000");

    /* esto NO emitirá un error incluso si no hay ningún índice disponible */
    $result = $mysqli->query("SELECT Name FROM City WHERE population > 50000");
} catch (mysqli_sql_exception $e) {
    error_log($e->__toString());
}

   
```php

## Véase también

`mysqli_sql_exception`, `set_exception_handler`, `error_reporting`
