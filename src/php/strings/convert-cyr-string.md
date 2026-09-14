---
title: convert_cyr_string
description: Convierte un string de un juego de caracteres cirílico a otro
source_url: https://www.php.net/manual/es/function.convert-cyr-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/convert-cyr-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: f112cc1ec
order: 88650
---

convert_cyr_string

Convierte un string de un juego de caracteres cirílico a otro

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
convert_cyr_string(string $str, string $from, string $to): string
```php

Convierte un string de un juego de caracteres cirílico a otro.

## Parámetros

`str`  
El string a convertir.

`from`  
El juego de caracteres cirílico, como un solo carácter.

`to`  
El juego de caracteres cirílico de destino, como un solo carácter.

Los caracteres admitidos son:

- `k` : `koi8-r`

- `w` : `windows-1251`

- `i` : `iso8859-5`

- `a` : `x-cp866`

- `d` : `x-cp866`

- `m` : `x-mac-cyrillic`

## Valores devueltos

Devuelve el string convertido.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido eliminada. |
| 7.4.0   | Esta función está obsoleta.     |

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`mb_convert_encoding`, `iconv`
