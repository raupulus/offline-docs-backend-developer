---
title: mysqli::$sqlstate
description: Devuelve el error SQLSTATE de la última operación MySQL
source_url: https://www.php.net/manual/es/mysqli.sqlstate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/sqlstate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: d9de192ba
order: 55370
---

mysqli::\$sqlstate

mysqli_sqlstate

Devuelve el error SQLSTATE de la última operación MySQL

## Descripción

Estilo orientado a objetos

string

mysqli-\>sqlstate

Estilo procedimental

```php
mysqli_sqlstate(mysqli $mysql): string
```php

Devuelve un string que contiene el código de error SQLSTATE del último error. El código de error `'00000'` significa: "sin errores". Los valores están especificados por los estándares ANSI SQL y ODBC. Para una lista de los valores posibles, consulte: <http://dev.mysql.com/doc/mysql/en/error-handling.html>.

> [!NOTE]
> Tenga en cuenta que no todos los errores de MySQL tienen aún una correspondencia con los errores SQLSTATE. El valor `HY000` (error general) se utiliza para los errores sin correspondencia.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Devuelve un string que contiene el código de error SQLSTATE del último error. El código está compuesto por 5 caracteres: `'00000'` representa la ausencia de errores.

## Ejemplos

Ejemplo con `$mysqli->sqlstate`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* La tabla Ciudad ya existe, deberíamos tener un error */
try {
    $mysqli->query("CREATE TABLE City (ID INT, Name VARCHAR(30))");
} catch (mysqli_sql_exception) {
    printf("Error - SQLSTATE %s.\n", $mysqli->sqlstate);
}

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* La tabla Ciudad ya existe, deberíamos tener un error */
try {
    mysqli_query($link, "CREATE TABLE City (ID INT, Name VARCHAR(30))");
} catch (mysqli_sql_exception) {
    printf("Error - SQLSTATE %s.\n", mysqli_sqlstate($link));
}

   
```php

Los ejemplos anteriores mostrarán:

    Error - SQLSTATE 42S01.

## Véase también

`mysqli_errno`, `mysqli_error`
