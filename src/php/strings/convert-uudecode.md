---
title: convert_uudecode
description: Decodifica un string en formato uuencode
source_url: https://www.php.net/manual/es/function.convert-uudecode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/convert-uudecode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 88660
---

convert_uudecode

Decodifica un string en formato uuencode

## Descripción

```php
convert_uudecode(string $string): string
```php

`convert_uudecode` decodifica un string en formato uuencode.

> [!NOTE]
> `convert_uudecode` no acepta ni la línea `begin` ni la línea `end`, que forman parte de los ficheros *files* codificados en uuencode.

## Parámetros

`string`  
Los datos, en formato uuencode.

## Valores devueltos

Devuelve los datos decodificados, como un string, o false en caso de fallo.

## Ejemplos

Ejemplo con `convert_uudecode`

```
<?php
echo convert_uudecode("+22!L;W9E(%!(4\"$`\n`");
?>

    
```php

El ejemplo anterior mostrará:

    I love PHP!

## Véase también

`convert_uuencode`
