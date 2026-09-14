---
title: base64_decode
description: Decodifica datos codificados con MIME base64
source_url: https://www.php.net/manual/es/function.base64-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/base64-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 100190
---

base64_decode

Decodifica datos codificados con MIME base64

## Descripción

```php
base64_decode(string $string, [bool $strict]): string
```php

Decodifica los datos en `string` codificados en base64.

## Parámetros

`string`  
Los datos codificados.

`strict`  
Si el parámetro `strict` está establecido a `true`, la función `base64_decode` devolverá `false` si la entrada contiene algún carácter que no es del alfabeto de base64. De lo contrario, los caracteres no válidos serán descartados silenciosamente.

## Valores devueltos

Devuelve los datos decodificados o `false` si ocurre un error. Los datos devueltos pueden estar en formato binario.

## Ejemplos

Ejemplo de `base64_decode`

```
<?php
$str = 'VGhpcyBpcyBhbiBlbmNvZGVkIHN0cmluZw==';
echo base64_decode($str);
?>

    
```php

El ejemplo anterior mostrará:

    Estos datos son una cadena codificada.

## Véase también

`base64_encode`, [RFC 2045](https://datatracker.ietf.org/doc/html/rfc2045) sección 6.8
