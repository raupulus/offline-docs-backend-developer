---
title: quoted_printable_encode
description: Convierte un string de 8 bits en un string quoted-printable
source_url: https://www.php.net/manual/es/function.quoted-printable-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/quoted-printable-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 6330e4d73
order: 89000
---

quoted_printable_encode

Convierte un string de 8 bits en un string quoted-printable

## Descripción

```php
quoted_printable_encode(string $string): string
```php

Devuelve un string quoted printable creado siguiendo las reglas de [RFC2045](https://datatracker.ietf.org/doc/html/rfc2045), sección 6.7.

Esta función es similar a `imap_8bit`, salvo que no requiere de un módulo IMAP para funcionar.

## Parámetros

`string`  
El string a procesar.

## Valores devueltos

El string codificado.

## Ejemplos

Ejemplo con `quoted_printable_encode`

```
<?php

$encoded = quoted_printable_encode('Möchten Sie ein paar Äpfel?');

var_dump($encoded);
var_dump(quoted_printable_decode($encoded));
?>

    
```php

El ejemplo anterior mostrará:

    string(37) "M=C3=B6chten Sie ein paar =C3=84pfel?"
    string(29) "Möchten Sie ein paar Äpfel?"

## Véase también

`quoted_printable_decode`, `iconv_mime_encode`
