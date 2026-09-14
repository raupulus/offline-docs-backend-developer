---
title: cubrid_client_encoding
description: Devuelve el actual conjunto de caracteres de la conexión a CUBRID
source_url: https://www.php.net/manual/es/function.cubrid-client-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/cubridmysql/cubrid-client-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_revision: 22492de2e
order: 8600
---

cubrid_client_encoding

Devuelve el actual conjunto de caracteres de la conexión a CUBRID

## Descripción

```php
cubrid_client_encoding([resource $conn_identifier]): string
```php

Esta función devuelve el actual conjunto de caracteres de conexión a CUBRID y es similar a la función CUBRID `cubrid_get_charset`.

## Parámetros

`conn_identifier`  
Conexión CUBRID. Si no se especifica el identificador de conexión, se asumirá el último enlace abierto por `cubrid_connect`.

## Valores devueltos

Cadena que representa el conjunto de caracteres de la conexión a CUBRID; en caso de éxito.

`false` en caso de falla.

## Ejemplos

Ejemplo de `cubrid_client_encoding`

```
<?php

$con = cubrid_connect("localhost", 33000, "demodb");
if (!$con)
{
    die('No se pudo conectar.');
}

printf("Conjunto actual de caracteres de CUBRID: %s\n", cubrid_client_encoding($con));

?>

   
```php

El ejemplo anterior mostrará:

    CUBRID current charset: iso8859-1

## Véase también

cubrid_get_charset
