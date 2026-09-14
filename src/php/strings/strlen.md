---
title: strlen
description: Calcula el tamaño de un string
source_url: https://www.php.net/manual/es/function.strlen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strlen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89340
---

strlen

Calcula el tamaño de un string

## Descripción

```php
strlen(string $string): int
```php

Devuelve el tamaño del string `string`.

## Parámetros

`string`  
El `string` a medir.

## Valores devueltos

El tamaño del string `string` en bytes.

## Ejemplos

Ejemplo con `strlen`

```
<?php
$str = 'abcdef';
echo strlen($str), PHP_EOL; // 6

$str = ' ab cd ';
echo strlen($str), PHP_EOL; // 7
?>

    
```php

## Notas

> [!NOTE]
> `strlen` devuelve el número de bytes en lugar del número de caracteres en un string.

## Véase también

`count`, `grapheme_strlen`, `iconv_strlen`, `mb_strlen`
