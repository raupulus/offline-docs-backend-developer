---
title: quoted_printable_decode
description: Convierte una string quoted-printable en una string de 8 bits
source_url: https://www.php.net/manual/es/function.quoted-printable-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/quoted-printable-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 6330e4d73
order: 88990
---

quoted_printable_decode

Convierte una string quoted-printable en una string de 8 bits

## Descripción

```php
quoted_printable_decode(string $string): string
```php

`quoted_printable_decode` devuelve la string `str`, después de convertirla del formato `quoted printable` binario de 8 bits (de acuerdo con la [RFC2045](https://datatracker.ietf.org/doc/html/rfc2045), sección 6.7, y no la [RFC2821](https://datatracker.ietf.org/doc/html/rfc2821), sección 4.5.2, para que las comas adicionales no sean eliminadas del inicio de la línea).

Esta función es similar a `imap_qprint`, excepto que no requiere el módulo IMAP para funcionar.

## Parámetros

`string`  
La string de entrada.

## Valores devueltos

Devuelve la string, convertida al formato de 8 bits.

## Ejemplos

Ejemplo con `quoted_printable_decode`

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

`quoted_printable_encode`
