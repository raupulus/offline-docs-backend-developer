---
title: mysqli_result::fetch_field_direct
description: Obtiene los metadatos de un campo único
source_url: https://www.php.net/manual/es/mysqli-result.fetch-field-direct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-field-direct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 5152c78db
order: 55580
---

mysqli_result::fetch_field_direct

mysqli_fetch_field_direct

Obtiene los metadatos de un campo único

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_field_direct(int $index): object
```php

Estilo procedimental

```php
mysqli_fetch_field_direct(mysqli_result $result, int $index): object
```

Devuelve un objeto que contiene los metadatos de un campo en el conjunto de resultados especificado.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

`index`  
El número del campo. Este valor debe estar en el intervalo `0` a `número de campos - 1`.

## Valores devueltos

Devuelve un objeto que contiene los metadatos de un campo o `false` si no se especifican metadatos para el campo `index`.

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

$query = "SELECT Name, SurfaceArea from Country ORDER BY Name LIMIT 5";

if ($result = $mysqli->query($query)) {

    /* Obtener información del campo para la columna 'SurfaceArea' */
    $finfo = $result->fetch_field_direct(1);

    printf("Nombre      : %s\n", $finfo->name);
    printf("Tabla       : %s\n", $finfo->table);
    printf("Tamaño máx : %d\n", $finfo->max_length);
    printf("Flags       : %d\n", $finfo->flags);
    printf("Tipo        : %d\n", $finfo->type);

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

$query = "SELECT Name, SurfaceArea from Country ORDER BY Name LIMIT 5";

if ($result = mysqli_query($link, $query)) {

    /* Obtener información del campo para la columna 'SurfaceArea' */
    $finfo = mysqli_fetch_field_direct($result, 1);

    printf("Nombre      : %s\n", $finfo->name);
    printf("Tabla       : %s\n", $finfo->table);
    printf("Tamaño máx : %d\n", $finfo->max_length);
    printf("Flags       : %d\n", $finfo->flags);
    printf("Tipo        : %d\n", $finfo->type);

    mysqli_free_result($result);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    Nombre      : SurfaceArea
    Tabla       : Country
    Tamaño máx : 10
    Flags       : 32769
    Tipo        : 4

## Véase también

`mysqli_num_fields`, `mysqli_fetch_field`, `mysqli_fetch_fields`
