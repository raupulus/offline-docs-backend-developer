---
title: mysqli_stmt::$param_count
description: Devuelve el número de parámetros de un comando SQL
source_url: https://www.php.net/manual/es/mysqli-stmt.param-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/param-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 7e5d0d1bb
order: 55930
---

mysqli_stmt::\$param_count

mysqli_stmt_param_count

Devuelve el número de parámetros de un comando SQL

## Descripción

Estilo orientado a objetos

int

mysqli_stmt-\>param_count

Estilo procedimental

```php
mysqli_stmt_param_count(mysqli_stmt $statement): int
```php

Devuelve el número de variables esperadas por el comando preparado `stmt`.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Devuelve un `int` que representa el número de parámetros.

## Ejemplos

Estilo orientado a objetos

```
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

if ($stmt = $mysqli->prepare("SELECT Name FROM Country WHERE Name=? OR Code=?")) {

    $marker = $stmt->param_count;
    printf("La consulta tiene %d variables.\n", $marker);

    /* Cierre del comando */
    $stmt->close();
}

/* Cierre de la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

if ($stmt = mysqli_prepare($link, "SELECT Name FROM Country WHERE Name=? OR Code=?")) {

    $marker = mysqli_stmt_param_count($stmt);
    printf("La consulta tiene %d variables.\n", $marker);

    /* Cierre del comando */
    mysqli_stmt_close($stmt);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    La consulta tiene 2 variables.

## Véase también

`mysqli_prepare`
