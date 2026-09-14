---
title: mysqli_result::fetch_fields
description: Devuelve un array de objetos que representan los campos en el resultado
source_url: https://www.php.net/manual/es/mysqli-result.fetch-fields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli_result/fetch-fields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: 5152c78db
order: 55600
---

mysqli_result::fetch_fields

mysqli_fetch_fields

Devuelve un array de objetos que representan los campos en el resultado

## Descripción

Estilo orientado a objetos

```php
public mysqli_result::fetch_fields(): array
```php

Estilo procedimental

```php
mysqli_fetch_fields(mysqli_result $result): array
```

Esta función opera como `mysqli_fetch_field` con la diferencia de que, en lugar de devolver un objeto a la vez para cada campo, las columnas son devueltas como un array de objetos.

## Parámetros

`result`  
Solo estilo procedimental: Un objeto `mysqli_result` devuelto por `mysqli_query`, `mysqli_store_result`, `mysqli_use_result` o `mysqli_stmt_get_result`.

## Valores devueltos

Devuelve un array de objetos que contiene información sobre la definición de los campos.

| Propiedad | Descripción |
|----|----|
| name | El nombre de la columna |
| orgname | El nombre original de la columna si se ha especificado un alias |
| table | El nombre de la tabla a la que pertenece este campo (si no ha sido calculado) |
| orgtable | El nombre original de la tabla si se ha especificado un alias |
| def | No utilizado. Siempre una string vacía |
| db | El nombre de la base de datos |
| catalog | No utilizado. Siempre `"def"` |
| max_length | La longitud máxima del campo para el conjunto de resultados. A partir de PHP 8.1, este valor es siempre `0`. |
| length | El ancho del campo en bytes. Para las columnas de tipo string, el valor de longitud varía en función del juego de caracteres de la conexión. Por ejemplo, si el juego de caracteres es `latin1`, un juego de caracteres de un byte, el valor de longitud para una consulta `SELECT 'abc'` es 3. Si el juego de caracteres es `utf8mb4`, un juego de caracteres multibyte en el que los caracteres ocupan hasta 4 bytes, el valor de longitud es 12. |
| charsetnr | El número del juego de caracteres para este campo |
| flags | Un integer que representa los bit-flags para este campo |
| type | El tipo de datos utilizados para este campo |
| decimals | El número de decimales para los campos numéricos y la precisión de los segundos fraccionarios para los campos temporales. |

Propiedades del objeto

## Ejemplos

Estilo orientado a objetos

```php
<?php
$mysqli = new mysqli("127.0.0.1", "root", "foofoo", "sakila");

/* verificación de la conexión */
if ($mysqli->connect_errno) {
    printf("Fallo en la conexión: %s\n", $mysqli->connect_error);
    exit();
}

foreach (array('latin1', 'utf8') as $charset) {

    // Establecer el juego de caracteres, para mostrar su impacto en ciertos valores (por ejemplo, longitudes en bytes)
    $mysqli->set_charset($charset);

    $query = "SELECT actor_id, last_name from actor ORDER BY actor_id";

    echo "============================\n";
    echo "Juego de caracteres: $charset\n";
    echo "============================\n";

    if ($result = $mysqli->query($query)) {

        /* Obtiene la información de los campos para todas las columnas */
        $finfo = $result->fetch_fields();

        foreach ($finfo as $val) {
            printf("Name:      %s\n",   $val->name);
            printf("Table:     %s\n",   $val->table);
            printf("Max. Len:  %d\n",   $val->max_length);
            printf("Length:    %d\n",   $val->length);
            printf("charsetnr: %d\n",   $val->charsetnr);
            printf("Flags:     %d\n",   $val->flags);
            printf("Type:      %d\n\n", $val->type);
        }
        $result->free();
    }
}
$mysqli->close();
?>

   
```

Estilo procedimental

```php
<?php
$link = mysqli_connect("127.0.0.1", "my_user", "my_password", "sakila");

/* verificación de la conexión */
if (mysqli_connect_errno()) {
    printf("Fallo en la conexión: %s\n", mysqli_connect_error());
    exit();
}

foreach (array('latin1', 'utf8') as $charset) {

    // Establecer el juego de caracteres, para mostrar su impacto en ciertos valores (por ejemplo, longitudes en bytes)
    mysqli_set_charset($link, $charset);

    $query = "SELECT actor_id, last_name from actor ORDER BY actor_id";

    echo "============================\n";
    echo "Juego de caracteres: $charset\n";
    echo "============================\n";

    if ($result = mysqli_query($link, $query)) {

        /* Obtiene la información de los campos para todas las columnas */
        $finfo = mysqli_fetch_fields($result);

        foreach ($finfo as $val) {
            printf("Name:      %s\n",   $val->name);
            printf("Table:     %s\n",   $val->table);
            printf("Max. Len:  %d\n",   $val->max_length);
            printf("Length:    %d\n",   $val->length);
            printf("charsetnr: %d\n",   $val->charsetnr);
            printf("Flags:     %d\n",   $val->flags);
            printf("Type:      %d\n\n", $val->type);
        }
        mysqli_free_result($result);
    }
}

mysqli_close($link);
?>

   
```

Los ejemplos anteriores mostrarán:

    ============================
    Juego de caracteres: latin1
    ============================
    Name:      actor_id
    Table:     actor
    Max. Len:  3
    Length:    5
    charsetnr: 63
    Flags:     49699
    Type:      2

    Name:      last_name
    Table:     actor
    Max. Len:  12
    Length:    45
    charsetnr: 8
    Flags:     20489
    Type:      253

    ============================
    Juego de caracteres: utf8
    ============================
    Name:      actor_id
    Table:     actor
    Max. Len:  3
    Length:    5
    charsetnr: 63
    Flags:     49699
    Type:      2

    Name:      last_name
    Table:     actor
    Max. Len:  12
    Length:    135
    charsetnr: 33
    Flags:     20489

## Véase también

`mysqli_num_fields`, `mysqli_fetch_field_direct`, `mysqli_fetch_field`
