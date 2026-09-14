---
title: mysqli::$affected_rows
description: Devuelve el número de filas afectadas por la última operación MySQL
source_url: https://www.php.net/manual/es/mysqli.affected-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/affected-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 9ed7c3ebf
order: 54890
---

mysqli::\$affected_rows

mysqli_affected_rows

Devuelve el número de filas afectadas por la última operación MySQL

## Descripción

Estilo orientado a objetos

int

string

mysqli-\>affected_rows

Estilo procedimental

```php
mysqli_affected_rows(mysqli $mysql): int
```php

Devuelve el número de filas afectadas por la última consulta `INSERT`, `UPDATE`, `REPLACE` o `DELETE` asociada al argumento `link`.

Funciona como `mysqli_num_rows` para las consultas `SELECT`.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un entero mayor que cero indica el número de filas afectadas o recuperadas. Cero indica que ningún registro fue modificado por una consulta del tipo `UPDATE`, ninguna fila coincide con la cláusula `WHERE` en la consulta o que ninguna consulta fue ejecutada. `-1` indica que la consulta devolvió un error o que `mysqli_affected_rows` fue llamado sobre una consulta `SELECT` no almacenada en búfer.

> [!NOTE]
> Si el número de filas afectadas es mayor que el valor máximo (`PHP_INT_MAX`) que puede tomar un entero, el número de filas afectadas será devuelto como un string.

## Ejemplos

Ejemplo con `$mysqli->affected_rows`

Estilo orientado a objetos

```
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Inserción de una fila */
$mysqli->query("CREATE TABLE Language SELECT * from CountryLanguage");
printf("Número de filas afectadas (INSERT): %d\n", $mysqli->affected_rows);

$mysqli->query("ALTER TABLE Language ADD Status int default 0");

/* Modificación de una fila */
$mysqli->query("UPDATE Language SET Status=1 WHERE Percentage > 50");
printf("Número de filas afectadas (UPDATE): %d\n", $mysqli->affected_rows);

/* Eliminación de una fila */
$mysqli->query("DELETE FROM Language WHERE Percentage < 50");
printf("Número de filas afectadas (DELETE): %d\n", $mysqli->affected_rows);

/* Selección de todas las filas */
$result = $mysqli->query("SELECT CountryCode FROM Language");
printf("Número de filas afectadas (SELECT): %d\n", $mysqli->affected_rows);

/* Eliminación de la tabla Language */
$mysqli->query("DROP TABLE Language");
?>

   
```php

Estilo procedimental

```
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Inserción de una fila */
mysqli_query($link, "CREATE TABLE Language SELECT * from CountryLanguage");
printf("Número de filas afectadas (INSERT): %d\n", mysqli_affected_rows($link));

mysqli_query($link, "ALTER TABLE Language ADD Status int default 0");

/* Modificación de una fila */
mysqli_query($link, "UPDATE Language SET Status=1 WHERE Percentage > 50");
printf("Número de filas afectadas (UPDATE): %d\n", mysqli_affected_rows($link));

/* Eliminación de una fila */
mysqli_query($link, "DELETE FROM Language WHERE Percentage < 50");
printf("Número de filas afectadas (DELETE): %d\n", mysqli_affected_rows($link));

/* Selección de todas las filas */
$result = mysqli_query($link, "SELECT CountryCode FROM Language");
printf("Número de filas afectadas (SELECT): %d\n", mysqli_affected_rows($link));

/* Eliminación de la tabla "language" */
mysqli_query($link, "DROP TABLE Language");
?>

   
```php

Los ejemplos anteriores mostrarán:

    Número de filas afectadas (INSERT): 984
    Número de filas afectadas (UPDATE): 168
    Número de filas afectadas (DELETE): 815
    Número de filas afectadas (SELECT): 169

## Véase también

`mysqli_num_rows`, `mysqli_info`
