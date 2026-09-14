---
title: imap_mime_header_decode
description: Decodifica los elementos MIME de un encabezado
source_url: https://www.php.net/manual/es/function.imap-mime-header-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-mime-header-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: e2f50c240
order: 38350
---

imap_mime_header_decode

Decodifica los elementos MIME de un encabezado

## Descripción

```php
imap_mime_header_decode(string $string): array
```php

Decodifica un mensaje MIME que contiene datos no ASCII (ver [RFC2047](https://datatracker.ietf.org/doc/html/rfc2047)).

## Parámetros

`string`  
El texto MIME

## Valores devueltos

Los elementos decodificados se devuelven en un array de objetos. Cada uno de estos objetos tiene dos propiedades: `charset` y `text`.

Si el elemento no ha sido codificado, o, en otras palabras, si está en claro (plain US_ASCII), la propiedad `charset` se establece en `default`.

Esta función devuelve `false` en caso de fallo.

## Ejemplos

Ejemplo con `imap_mime_header_decode`

```
<?php
$text = "=?ISO-8859-1?Q?Keld_J=F8rn_Simonsen?= <keld@example.com>";

$elements = imap_mime_header_decode($text);
for ($i=0; $i<count($elements); $i++) {
    echo "Charset : {$elements[$i]->charset}\n";
    echo "Texto : {$elements[$i]->text}\n\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    Charset: ISO-8859-1
    Texto: Keld Jørn Simonsen

    Charset: default
    Texto:  <keld@example.com>

En el ejemplo anterior, se encuentran dos elementos: el primero ha sido codificado en ISO-8859-1, y el segundo está en claro.

## Véase también

`imap_utf8`
