---
title: mysqli_stmt::$error_list
description: Devuelve una lista de errores para la última consulta ejecutada
source_url: https://www.php.net/manual/es/mysqli-stmt.error-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_stmt/error-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 55810
---

mysqli_stmt::\$error_list

mysqli_stmt_error_list

Devuelve una lista de errores para la última consulta ejecutada

## Descripción

Estilo orientado a objetos

array

mysqli_stmt-\>error_list

Estilo procedimental

```php
mysqli_stmt_error_list(mysqli_stmt $statement): array
```php

Devuelve un array de errores desde la última consulta ejecutada, haya tenido éxito o no.

## Parámetros

`statement`  
Solo estilo procedimental: Un objeto `mysqli_stmt` devuelto por `mysqli_stmt_init`.

## Valores devueltos

Una lista de errores, cada uno en forma de array asociativo que contiene el número de error (errno), el mensaje de error (error) y el estado SQL (sqlstate).

## Ejemplos

Estilo orientado a objetos

```
<?php
/* Abre una conexión */
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo al conectar: %s\n", mysqli_connect_error());
    exit();
}

$mysqli->query("CREATE TABLE myCountry LIKE Country");
$mysqli->query("INSERT INTO myCountry SELECT * FROM Country");

$query = "SELECT Name, Code FROM myCountry ORDER BY Name";
if ($stmt = $mysqli->prepare($query)) {

    /* Elimina la tabla */
    $mysqli->query("DROP TABLE myCountry");

    /* Ejecuta la consulta */
    $stmt->execute();

    echo "Error:\n";
    print_r($stmt->error_list);

    /* Cierra la consulta */
    $stmt->close();
}

/* Cierra la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
/* Abre una conexión */
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verifica la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo al conectar: %s\n", mysqli_connect_error());
    exit();
}

mysqli_query($link, "CREATE TABLE myCountry LIKE Country");
mysqli_query($link, "INSERT INTO myCountry SELECT * FROM Country");

$query = "SELECT Name, Code FROM myCountry ORDER BY Name";
if ($stmt = mysqli_prepare($link, $query)) {

    /* Elimina la tabla */
    mysqli_query($link, "DROP TABLE myCountry");

    /* Ejecuta la consulta */
    mysqli_stmt_execute($stmt);

    echo "Error:\n";
    print_r(mysqli_stmt_error_list($stmt));

    /* Cierra la consulta */
    mysqli_stmt_close($stmt);
}

/* Cierra la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Error:
    Array
    (
        [0] => Array
            (
                [errno] => 1146
                [sqlstate] => 42S02
                [error] => Table 'world.myCountry' doesn't exist
            )

    )

## Véase también

`mysqli_stmt_error`, `mysqli_stmt_errno`, `mysqli_stmt_sqlstate`
