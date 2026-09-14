---
title: mysqli::$field_count
description: Devuelve el número de columnas para la última consulta
source_url: https://www.php.net/manual/es/mysqli.field-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/field-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 7e5d0d1bb
order: 55050
---

mysqli::\$field_count

mysqli_field_count

Devuelve el número de columnas para la última consulta

## Descripción

Estilo orientado a objetos

int

mysqli-\>field_count

Estilo procedimental

```php
mysqli_field_count(mysqli $mysql): int
```php

Devuelve el número de columnas para la última consulta en la conexión especificada por el parámetro `mysql`. Esta función puede ser útil al utilizar `mysqli_store_result` para determinar si la consulta debería haber devuelto un resultado vacío o no, sin conocer su naturaleza.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Un entero que representa el número de campos en un conjunto de resultados.

## Ejemplos

Ejemplo con `$mysqli->field_count`

Estilo orientado a objetos

```
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "test");

$mysqli->query( "DROP TABLE IF EXISTS friends");
$mysqli->query( "CREATE TABLE friends (id int, name varchar(20))");

$mysqli->query( "INSERT INTO friends VALUES (1,'Hartmut'), (2, 'Ulf')");

$mysqli->real_query("SELECT * FROM friends");

if ($mysqli->field_count) {
    /* Una consulta SELECT, SHOW o DESCRIBE */
    $result = $mysqli->store_result();

    /* Obtención del conjunto de resultados */
    $row = $result->fetch_row();

    /* Liberación del conjunto de resultados */
    $result->close();
}

/* Cierre de la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "test");

mysqli_query($link, "DROP TABLE IF EXISTS friends");
mysqli_query($link, "CREATE TABLE friends (id int, name varchar(20))");

mysqli_query($link, "INSERT INTO friends VALUES (1,'Hartmut'), (2, 'Ulf')");

mysqli_real_query($link, "SELECT * FROM friends");

if (mysqli_field_count($link)) {
    /* Una consulta SELECT, SHOW o DESCRIBE */
    $result = mysqli_store_result($link);

    /* Obtención del conjunto de resultados */
    $row = mysqli_fetch_row($result);

    /* Liberación del conjunto de resultados */
    mysqli_free_result($result);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```php
