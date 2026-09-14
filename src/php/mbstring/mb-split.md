---
title: mb_split
description: Divide una string en un array utilizando una expresión regular multibyte
source_url: https://www.php.net/manual/es/function.mb-split.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-split.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: bb66ce4d4
order: 45390
---

mb_split

Divide una string en un array utilizando una expresión regular multibyte

## Descripción

```php
mb_split(string $pattern, string $string, [int $limit]): array
```php

Divide la string multibyte `string` utilizando la expresión regular `pattern` y devuelve el resultado en forma de array.

## Parámetros

`pattern`  
La máscara de la expresión regular.

`string`  
La string a dividir.

`limit`  
Si el argumento opcional `limit` es especificado, la string será dividida en un máximo de `limit` elementos.

## Valores devueltos

El resultado, en forma de un `array`, o `false` si ocurre un error.

## Notas

> [!NOTE]
> La codificación de caracteres especificada por `mb_regex_encoding` se utilizará como codificación de caracteres para esta función de forma predeterminada.

## Véase también

`mb_regex_encoding`, `mb_ereg`, `explode`
