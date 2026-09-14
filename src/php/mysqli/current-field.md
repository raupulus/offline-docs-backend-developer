---
title: mysqli_result::$current_field
description: Obtiene la posición actual de un campo en un puntero de resultado
source_url: https://www.php.net/manual/es/mysqli-result.current-field.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/current-field.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 0d604bbc9
order: 55520
---

mysqli_result::\$current_field

mysqli_field_tell

Obtiene la posición actual de un campo en un puntero de resultado

## Descripción

Estilo orientado a objetos

int

mysqli_result-\>current_field

Estilo procedimental

```php
mysqli_field_tell(mysqli_result $result): int
```php

Devuelve la posición del cursor de campo utilizado por la última llamada a la función `mysqli_fetch_field`. Este valor puede ser utilizado como argumento de la función `mysqli_field_seek`.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Devuelve la posición actual del cursor de campo.

## Ejemplos

Estilo orientado a objetos

```
<?php
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT Name, SurfaceArea from Country ORDER BY Code LIMIT 5";

if ($result = $mysqli->query($query)) {

    /* Obtención de información sobre el campo para todas las columnas */
    while ($finfo = $result->fetch_field()) {

        /* Obtención de la posición del puntero de campo */
        $currentfield = $result->current_field;

        printf("Columna %d:\n", $currentfield);
        printf("Nombre: %s\n", $finfo->name);
        printf("Tabla: %s\n", $finfo->table);
        printf("Longitud máx.: %d\n", $finfo->max_length);
        printf("Flags: %d\n", $finfo->flags);
        printf("Tipo: %d\n\n", $finfo->type);
    }
    $result->close();
}

/* Cierre de la conexión */
$mysqli->close();
?>

   
```php

Estilo procedimental

```
<?php
$link = mysqli_connect("localhost", "my_user", "my_password", "world");

/* Verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT Name, SurfaceArea from Country ORDER BY Code LIMIT 5";

if ($result = mysqli_query($link, $query)) {

    /* Obtención de información sobre el campo para todas las columnas */
    while ($finfo = mysqli_fetch_field($result)) {

        /* Obtención de la posición del puntero de campo */
        $currentfield = mysqli_field_tell($result);

        printf("Columna %d:\n", $currentfield);
        printf("Nombre: %s\n", $finfo->name);
        printf("Tabla: %s\n", $finfo->table);
        printf("Longitud máx.: %d\n", $finfo->max_length);
        printf("Flags: %d\n", $finfo->flags);
        printf("Tipo: %d\n\n", $finfo->type);
    }
    mysqli_free_result($result);
}

/* Cierre de la conexión */
mysqli_close($link);
?>

   
```php

Los ejemplos anteriores mostrarán:

    Columna 1:
    Nombre: Name
    Tabla: Country
    Longitud máx.: 11
    Flags: 1
    Tipo: 254

    Columna 2:
    Nombre: SurfaceArea
    Tabla: Country
    Longitud máx.: 10
    Flags: 32769
    Tipo: 4

## Véase también

`mysqli_fetch_field`, `mysqli_field_seek`
