---
title: base64_encode
description: Codifica datos con MIME base64
source_url: https://www.php.net/manual/es/function.base64-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/base64-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 100200
---

base64_encode

Codifica datos con MIME base64

## Descripción

```php
base64_encode(string $string): string
```php

Codifica `string` en base64.

Este tipo de codificación está diseñado para que datos binarios sobrepasen capas de transporte que no son de 8-bits 100%, como por ejemplo el cuerpo de un E-Mail.

La codificación en Base64 hace que los datos sean un 33% más largos que los datos originales.

## Parámetros

`string`  
Datos a codificar.

## Valores devueltos

Los datos codificados, como un string.

## Ejemplos

Ejemplo de `base64_encode`

```
<?php
$str = 'This is an encoded string';
echo base64_encode($str);
?>

    
```php

El ejemplo anterior mostrará:

    VGhpcyBpcyBhbiBlbmNvZGVkIHN0cmluZw==

## Véase también

`base64_decode`, `chunk_split`, `convert_uuencode`, [RFC 2045](https://datatracker.ietf.org/doc/html/rfc2045) sección 6.8
