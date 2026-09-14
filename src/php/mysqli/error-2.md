---
title: mysqli_stmt::$error
description: Devuelve una descripción del último error de procesamiento
source_url: https://www.php.net/manual/es/mysqli-stmt.error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 7e5d0d1bb
order: 55820
---

mysqli_stmt::\$error

mysqli_stmt_error

Devuelve una descripción del último error de procesamiento

## Descripción

Estilo orientado a objetos

string

mysqli_stmt-\>error

Estilo procedimental

```php
mysqli_stmt_error(mysqli_stmt $statement): string
```php

Devuelve un string que representa el mensaje de error más reciente llamado por una función de procesamiento, haya tenido éxito o no.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Un `string` que describe el error. Una cadena vacía si no ha ocurrido ningún error.

## Ejemplos

Estilo orientado a objetos

```
<?php
/* Abre la conexión */
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$mysqli->query("CREATE TABLE myCountry LIKE Country");
$mysqli->query("INSERT INTO myCountry SELECT * FROM Country");

$query = "SELECT Name, Code FROM myCountry ORDER BY Name";
if ($stmt = $mysqli->prepare($query)) {

    /* Borrado de la tabla */
    $mysqli->query("DROP TABLE myCountry");

    /* Ejecuta la consulta */
    $stmt->execute();

    printf("Error: %s.\n", $stmt->error);

    /* Cierra la sentencia */
    $stmt->close();
}

/* Cierra la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
/* Abre la conexión */
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

mysqli_query($link, "CREATE TABLE myCountry LIKE Country");
mysqli_query($link, "INSERT INTO myCountry SELECT * FROM Country");

$query = "SELECT Name, Code FROM myCountry ORDER BY Name";
if ($stmt = mysqli_prepare($link, $query)) {

    /* Borrado de la tabla */
    mysqli_query($link, "DROP TABLE myCountry");

    /* Ejecuta la consulta */
    mysqli_stmt_execute($stmt);

    printf("Error: %s.\n", mysqli_stmt_error($stmt));

    /* Cierra la sentencia */
    mysqli_stmt_close($stmt);
}

/* Cierra la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Error: Table 'world.myCountry' doesn't exist.

## Véase también

`mysqli_stmt_errno`, `mysqli_stmt_sqlstate`
