---
title: urldecode
description: Decodifica una cadena cifrada como URL
source_url: https://www.php.net/manual/es/function.urldecode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/urldecode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 100270
---

urldecode

Decodifica una cadena cifrada como URL

## Descripción

```php
urldecode(string $string): string
```php

Decodifica cualquier cifrado tipo `%##` en la cadena dada. Los símbolos ('`+`') son decodificados como el caracter espacio.

## Parámetros

`string`  
La cadena a ser decodificada.

## Valores devueltos

Devuelve la cadena decodificada.

## Ejemplos

Ejemplo de `urldecode`

```
<?php
$query = "my=apples&are=green+and+red";

foreach (explode('&', $query) as $chunk) {
    $param = explode("=", $chunk);

    if ($param) {
        printf("Value for parameter \"%s\" is \"%s\"<br/>\n", urldecode($param[0]), urldecode($param[1]));
    }
}
?>

    
```php

## Notas

> [!WARNING]
> Las superglobales `$_GET` y `$_REQUEST` ya están decodificadas. El uso de `urldecode` en un elemento en `$_GET` o `$_REQUEST` puede tener resultados inesperados y peligrosos.

## Véase también

`urlencode`, `rawurlencode`, `rawurldecode`, [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
