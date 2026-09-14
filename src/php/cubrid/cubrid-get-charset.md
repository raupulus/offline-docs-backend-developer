---
title: cubrid_get_charset
description: Devolver el conjunto de caracteres de la conexión CUBRID actual
source_url: https://www.php.net/manual/es/function.cubrid-get-charset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/functions/cubrid-get-charset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9060
---

cubrid_get_charset

Devolver el conjunto de caracteres de la conexión CUBRID actual

## Descripción

```php
cubrid_get_charset(resource $conn_identifier): string
```php

Esta función devuelve el conjunto de caracteres de la conexión CUBRID actual y es similar a la función de CUBRID compatible con MySQL `cubrid_client_encoding`.

## Parámetros

`conn_identifier`  
La conexión CUBRID.

## Valores devueltos

Una cadena que representa el conjunto de caracteres de la conexión CUBRID; en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo de `cubrid_get_charset`

```
<?php

$con = cubrid_connect("localhost", 33000, "demodb");
if (!$con)
{
    die('No se pudo realizar la conexión.');
}

printf("Conjunto de caracteres actual de CUBRID: %s\n", cubrid_get_charset($con));

?>

   
```php

El ejemplo anterior mostrará:

    CUBRID current charset: iso8859-1

## Véase también

cubrid_client_encoding
