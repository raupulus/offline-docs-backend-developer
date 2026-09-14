---
title: convert_uuencode
description: Codifica un string utilizando el algoritmo uuencode
source_url: https://www.php.net/manual/es/function.convert-uuencode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/convert-uuencode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 88670
---

convert_uuencode

Codifica un string utilizando el algoritmo uuencode

## Descripción

```php
convert_uuencode(string $string): string
```php

`convert_uuencode` codifica un string utilizando el algoritmo uuencode.

Uuencode traduce todos los strings (incluyendo datos binarios) en caracteres imprimibles, para asegurar su transmisión por Internet. Los datos en formato uuencode son aproximadamente un 35 % más grandes que los originales.

> [!NOTE]
> `convert_uuencode` no produce ni la línea `begin` ni la línea `end`, que forman parte de los ficheros *files* codificados en uuencoded.

## Parámetros

`string`  
Los datos a codificar.

## Valores devueltos

Devuelve los datos en formato uuencode.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Antes de esta versión, intentar convertir un string vacío devolvía `false` sin ninguna razón en particular. |

## Ejemplos

Ejemplo con `convert_uuencode`

```
<?php
$some_string = "test\ntext text\r\n";

echo convert_uuencode($some_string);
?>

    
```php

El ejemplo anterior mostrará:

    0=&5S=`IT97AT('1E>'0-"@``
    `

## Véase también

`convert_uudecode`, `base64_encode`
