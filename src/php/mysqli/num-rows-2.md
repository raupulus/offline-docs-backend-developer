---
title: mysqli_stmt::$num_rows
description: Devuelve el número de filas recuperadas del servidor
source_url: https://www.php.net/manual/es/mysqli-stmt.num-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/num-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 035c126c0
order: 55920
---

mysqli_stmt::\$num_rows

mysqli_stmt::num_rows

mysqli_stmt_num_rows

Devuelve el número de filas recuperadas del servidor

## Descripción

Estilo orientado a objetos

int

string

mysqli_stmt-\>num_rows

```php
public mysqli_stmt::num_rows(): int
```php

Estilo procedimental

```php
mysqli_stmt_num_rows(mysqli_stmt $statement): int
```

Devuelve el número de filas almacenadas en el búfer en la instrucción. Esta función solo funcionará después de llamar a `mysqli_stmt_store_result` para almacenar en el búfer el conjunto completo de resultados en el gestor de la instrucción.

Esta función devuelve `0` a menos que todas las filas hayan sido recuperadas del servidor.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Un `int` que representa el número de filas almacenadas en el búfer. Devuelve `0` en modo no almacenado en búfer, excepto si todas las filas han sido recuperadas del servidor.

> [!NOTE]
> Si el número de filas es mayor que `PHP_INT_MAX`, el número será devuelto como un `string`.

## Ejemplos

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name LIMIT 20";

$stmt = $mysqli->prepare($query);
$stmt->execute();

/* Almacenar el resultado en un búfer interno */
$stmt->store_result();

printf("Número de filas: %d.\n", $stmt->num_rows);
?>

   
```

Estilo procedimental

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

$query = "SELECT Name, CountryCode FROM City ORDER BY Name LIMIT 20";

$stmt = mysqli_prepare($link, $query);
mysqli_stmt_execute($stmt);

/* Almacenar el resultado en un búfer interno */
mysqli_stmt_store_result($stmt);

printf("Número de filas: %d.\n", mysqli_stmt_num_rows($stmt));
?>

   
```

Los ejemplos anteriores mostrarán:

    Número de filas: 20.

## Véase también

`mysqli_stmt_store_result`, `mysqli_stmt_affected_rows`, `mysqli_prepare`
