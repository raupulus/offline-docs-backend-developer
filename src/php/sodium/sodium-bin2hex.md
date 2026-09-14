---
title: sodium_bin2hex
description: Codificar en hexadecimal
source_url: https://www.php.net/manual/es/function.sodium-bin2hex.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sodium/functions/sodium-bin2hex.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sodium
translation_status: ready
translation_reviewed: false
translation_revision: 96a8863cc
order: 75990
---

sodium_bin2hex

Codificar en hexadecimal

## Descripción

```php
#[\SensitiveParameter] sodium_bin2hex(string $string): string
```php

Convierte una cadena binaria bruta en una cadena codificada en hexadecimal. A diferencia de la función de codificación hexadecimal estándar, `sodium_bin2hex` es de tiempo constante (una propiedad importante para cualquier código que manipule entradas criptográficas, como textos sin formato o claves).

## Parámetros

`string`  
Una cadena binaria bruta.

## Valores devueltos

Una cadena codificada en hexadecimal.
