---
title: mb_strcut
description: Corta una parte de string
source_url: https://www.php.net/manual/es/function.mb-strcut.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strcut.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 911fe79de
order: 45420
---

mb_strcut

Corta una parte de string

## Descripción

```php
mb_strcut(string $string, int $start, [int $length], [string $encoding]): string
```php

`mb_strcut` extrae un substring desde un string, de manera similar a la función `mb_substr`, pero opera sobre los bytes en lugar de los caracteres. Si el corte ocurre entre 2 bytes de un carácter multibyte, el corte se realizará al inicio del primer byte de ese carácter. Esta es también la diferencia con la función `substr` que cortará el string en medio de los bytes, resultando en una secuencia de bytes mal formada.

## Parámetros

`string`  
El string a cortar.

`start`  
Si `start` es positivo, el string devuelto comenzará en el *byte* número `start`, en el string `string`. El primer carácter está numerado cero. En efecto, en el string '`abcdef`', el byte en la posición `0` es '`a`', el byte en la posición `2` es '`c`', y así sucesivamente.

Si `start` es negativo, el string devuelto comenzará en el byte número `start` contando desde el final del string `string`. Sin embargo, si el número negativo pasado como argumento `start` es mayor que la longitud del string, la porción devuelta comenzará desde el inicio del string `string`.

`length`  
Longitud en *bytes*. Si este argumento es omitido, o vale `null`, todos los bytes hasta el final del string serán extraídos.

Si `length` es negativo, el string devuelto terminará en la posición `length` contando desde el final del string `string`. Sin embargo, si el número negativo pasado al argumento `length` es mayor que el número de caracteres después de la posición `start`, un string vacío será devuelto.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

`mb_strcut` devuelve la porción del string `string` que comienza en el carácter `start` y tiene la longitud de `length` caracteres.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El comportamiento ahora es más consistente con las cadenas `UTF-8` y `UTF-16` inválidas. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Véase también

`mb_substr`, `mb_internal_encoding`
