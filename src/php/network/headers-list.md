---
title: headers_list
description: Devuelve la lista de los encabezados de respuesta del script actual
source_url: https://www.php.net/manual/es/function.headers-list.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/headers-list.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: eecf09080
order: 56400
---

headers_list

Devuelve la lista de los encabezados de respuesta del script actual

## Descripción

```php
headers_list(): array
```php

`headers_list` devuelve un array con la lista de los encabezados que serán transmitidos al navegador. Para determinar si estos encabezados han sido ya enviados o no, utilice la función `headers_sent`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array de encabezados indexado numéricamente.

## Ejemplos

Ejemplo con `headers_list`

```
<?php

/* setcookie() va añadir un encabezado */
setcookie('foo', 'bar');

/* Define un encabezado de respuesta
Será ignorado por la mayoría de los navegadores */
header("Example-Test: foo");

/* Especificación de la respuesta en texto simple */
header('Content-Type: text/plain; charset=UTF-8');

/* ¿Cuáles son los encabezados que serán enviados? */
var_dump(headers_list());

?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(4) {
      [0]=>
      string(19) "Set-Cookie: foo=bar"
      [1]=>
      string(17) "Example-Test: foo"
      [2]=>
      string(39) "Content-Type: text/plain; charset=UTF-8"
    }

## Notas

> [!NOTE]
> Los encabezados solo serán accesibles y se mostrarán cuando se utilice un SAPI que los soporte.

## Véase también

`headers_sent`, `header`, `setcookie`, `apache_response_headers`, `http_response_code`
