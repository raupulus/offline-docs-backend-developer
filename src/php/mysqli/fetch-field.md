---
title: mysqli_result::fetch_field
description: Devuelve el siguiente campo en el conjunto de resultados
source_url: https://www.php.net/manual/es/mysqli-result.fetch-field.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-field.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 5152c78db
order: 55590
---

mysqli_result::fetch_field

mysqli_fetch_field

Devuelve el siguiente campo en el conjunto de resultados

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_field(): object
```php

Estilo procedimental

```php
mysqli_fetch_field(mysqli_result $result): object
```

Devuelve los atributos de la siguiente columna en el conjunto de resultados representado por el parámetro `result` como un objeto. Llame a esta función de forma repetitiva para recuperar la información de todas las columnas.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Devuelve un objeto que contiene la información de un campo o `false` si no hay información disponible para este campo.

## Ejemplos

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT Name, SurfaceArea from Country ORDER BY Code LIMIT 5";

if ($result = $mysqli->query($query)) {

    /* Recupera la información de un campo para todas las columnas */
    while ($finfo = $result->fetch_field()) {

        printf("Name:     %s\n", $finfo->name);
        printf("Table:    %s\n", $finfo->table);
        printf("max. Len: %d\n", $finfo->max_length);
        printf("Flags:    %d\n", $finfo->flags);
        printf("Type:     %d\n\n", $finfo->type);
    }
    $result->close();
}

/* Cierre de la conexión */
$mysqli->close();
?>

   
```

Estilo procedimental

```php
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT Name, SurfaceArea from Country ORDER BY Code LIMIT 5";

if ($result = mysqli_query($link, $query)) {

    /* Recupera la información de un campo para todas las columnas */
    while ($finfo = mysqli_fetch_field($result)) {

        printf("Name:     %s\n", $finfo->name);
        printf("Table:    %s\n", $finfo->table);
        printf("max. Len: %d\n", $finfo->max_length);
        printf("Flags:    %d\n", $finfo->flags);
        printf("Type:     %d\n\n", $finfo->type);
    }
    mysqli_free_result($result);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    Name:     Name
    Table:    Country
    max. Len: 11
    Flags:    1
    Type:     254

    Name:     SurfaceArea
    Table:    Country
    max. Len: 10
    Flags:    32769
    Type:     4

## Véase también

`mysqli_num_fields`, `mysqli_fetch_field_direct`, `mysqli_fetch_fields`, `mysqli_field_seek`
