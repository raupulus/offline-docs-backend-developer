---
title: mysqli_stmt::$affected_rows
description: Devuelve el número total de filas modificadas, eliminadas, insertadas
  o coincidentes por la última consulta
source_url: https://www.php.net/manual/es/mysqli-stmt.affected-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/affected-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 2d5c6bed3
order: 55720
---

mysqli_stmt::\$affected_rows

mysqli_stmt_affected_rows

Devuelve el número total de filas modificadas, eliminadas, insertadas o coincidentes por la última consulta

## Descripción

Estilo orientado a objetos

int

string

mysqli_stmt-\>affected_rows

Estilo procedimental

```php
mysqli_stmt_affected_rows(mysqli_stmt $statement): int
```php

Devuelve el número de filas afectadas por una consulta `INSERT`, `UPDATE` o `DELETE`.

Funciona como `mysqli_stmt_num_rows` para las consultas `SELECT`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Un entero mayor que cero indica el número de filas afectadas o recuperadas. Cero indica que ningún registro fue modificado por una consulta de tipo `UPDATE`, ninguna fila coincide con la cláusula `WHERE` en la consulta o que ninguna consulta fue ejecutada. `-1` indica que la consulta devolvió un error o que, para una consulta `SELECT`, `mysqli_stmt_affected_rows` fue llamado antes de llamar `mysqli_stmt_store_result`.

> [!NOTE]
> Si el número de filas afectadas es mayor que el valor máximo de un entero PHP, el número de filas afectadas será devuelto como una cadena de caracteres.

## Ejemplos

Ejemplo de mysqli_stmt_affected_rows

Estilo orientado a objetos

```
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Creación de una tabla temporal */
$mysqli->query("CREATE TEMPORARY TABLE myCountry LIKE Country");

$query = "INSERT INTO myCountry SELECT * FROM Country WHERE Code LIKE ?";

/* Preparación de la consulta */
$stmt = $mysqli->prepare($query);

/* Vincula una variable a un parámetro ficticio */
$code = 'A%';
$stmt->bind_param("s", $code);

/* Ejecución de la consulta */
$stmt->execute();

printf("Filas insertadas: %d\n", $stmt->affected_rows);
?>

   
```php

Estilo procedimental

```
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Creación de una tabla temporal */
mysqli_query($link, "CREATE TEMPORARY TABLE myCountry LIKE Country");

$query = "INSERT INTO myCountry SELECT * FROM Country WHERE Code LIKE ?";

/* Preparación de la consulta */
$stmt = mysqli_prepare($link, $query);

/* Vincula una variable a un parámetro ficticio */
$code = 'A%';
mysqli_stmt_bind_param($stmt, "s", $code);

/* Ejecución de la consulta */
mysqli_stmt_execute($stmt);

printf("Filas insertadas: %d\n", mysqli_stmt_affected_rows($stmt));
?>

   
```php

El ejemplo anterior mostrará:

    Filas insertadas: 17

## Véase también

`mysqli_stmt_num_rows`, `mysqli_stmt_store_result`
