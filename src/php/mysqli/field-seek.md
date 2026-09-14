---
title: mysqli_result::field_seek
description: Desplaza el puntero de resultado al campo especificado
source_url: https://www.php.net/manual/es/mysqli-result.field-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/field-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: c5ccd084c
order: 55640
---

mysqli_result::field_seek

mysqli_field_seek

Desplaza el puntero de resultado al campo especificado

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::field_seek(int $index): true
```php

Estilo procedimental

```php
mysqli_field_seek(mysqli_result $result, int $index): true
```

Coloca el cursor en el campo especificado por el número `index`. La próxima llamada a la función `mysqli_fetch_field` devolverá la definición del campo de la columna asociada a esta posición.

> [!NOTE]
> Para moverse al inicio de una fila, pase una posición con valor cero.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

`index`  
El número del campo. Este valor debe estar en el intervalo `0` a `número de campos - 1`.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función devuelve ahora siempre `true`. Anteriormente, devolvía `false` en caso de fallo. |

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

    /* Obtención de información del campo para la 2ª columna */
    $result->field_seek(1);
    $finfo = $result->fetch_field();

    printf("Name:     %s\n", $finfo->name);
    printf("Table:    %s\n", $finfo->table);
    printf("max. Len: %d\n", $finfo->max_length);
    printf("Flags:    %d\n", $finfo->flags);
    printf("Type:     %d\n\n", $finfo->type);

    $result->close();
}

/* Cierra la conexión */
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

    /* Obtención de información del campo para la 2ª columna */
    mysqli_field_seek($result, 1);
    $finfo = mysqli_fetch_field($result);

    printf("Name:     %s\n", $finfo->name);
    printf("Table:    %s\n", $finfo->table);
    printf("max. Len: %d\n", $finfo->max_length);
    printf("Flags:    %d\n", $finfo->flags);
    printf("Type:     %d\n\n", $finfo->type);

    mysqli_free_result($result);
}

/* Cierra la conexión */
mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    Name:     SurfaceArea
    Table:    Country
    max. Len: 10
    Flags:    32769
    Type:     4

## Véase también

`mysqli_fetch_field`
