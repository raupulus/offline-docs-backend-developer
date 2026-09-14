---
title: chunk_split
description: Divide un string
source_url: https://www.php.net/manual/es/function.chunk-split.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/chunk-split.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 88640
---

chunk_split

Divide un string

## Descripción

```php
chunk_split(string $string, [int $length], [string $separator]): string
```php

Divide el string `body` en segmentos de `length` bytes de longitud. Esta función es muy útil para convertir los resultados de `base64_encode` al formato de la RFC 2045. Inserta el parámetro `separator` cada `length` caracteres.

## Parámetros

`string`  
El string a dividir.

`length`  
El tamaño de la porción.

`separator`  
El carácter de fin de la secuencia.

## Valores devueltos

Devuelve el string dividido.

## Ejemplos

Ejemplo con `chunk_split`

```
<?php
$data = 'This is quite a long string, which will get broken up because the line is going to be too long after base64 encoding it.';

// Formatear datos para seguir la norma RFC 2045
$new_string = chunk_split(base64_encode($data));
echo $new_string, PHP_EOL;
?>

    
```php

## Véase también

`str_split`, `explode`, `wordwrap`, [RFC 2045](https://datatracker.ietf.org/doc/html/rfc2045)
