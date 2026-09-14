---
title: mysqli_stmt::$errno
description: Devuelve un código de error para la última consulta
source_url: https://www.php.net/manual/es/mysqli-stmt.errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_revision: 614d77598
order: 55800
---

mysqli_stmt::\$errno

mysqli_stmt_errno

Devuelve un código de error para la última consulta

## Descripción

Estilo orientado a objetos

int

mysqli_stmt-\>errno

Estilo procedimental

```php
mysqli_stmt_errno(mysqli_stmt $statement): int
```php

Devuelve el código de error para la última consulta llamada en el procesamiento que tuvo éxito o falló.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Un valor que representa un código de error. `0` significa que no ocurrió ningún error.

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

    printf("Error: %d.\n", $stmt->errno);

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

    printf("Error: %d.\n", mysqli_stmt_errno($stmt));

    /* Cierra la sentencia */
    mysqli_stmt_close($stmt);
}

/* Cierra la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Error: 1146.

## Véase también

`mysqli_stmt_error`, `mysqli_stmt_sqlstate`
