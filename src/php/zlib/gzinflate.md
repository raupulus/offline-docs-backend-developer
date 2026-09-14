---
title: gzinflate
description: Descomprime una cadena comprimida
source_url: https://www.php.net/manual/es/function.gzinflate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzinflate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: b9d23bbb9
order: 108830
---

gzinflate

Descomprime una cadena comprimida

## Descripción

```php
gzinflate(string $data, [int $max_length]): string
```php

Esta función descomprime una cadena comprimida.

## Parámetros

`data`  
Los datos comprimidos con `gzdeflate`.

`max_length`  
La longitud máxima de los datos descodificados.

## Valores devueltos

Los datos originales descomprimidos o `false` en caso de error.

La función retornará un error si los datos descomprimidos son más de 32768 veces la longitud de la `data` de entrada o, a menos que `max_length` sea `0`, mayores que el parámetro opcional `max_length`.

## Ejemplos

Ejemplo de `gzinflate`

```
<?php
$compressed   = gzdeflate('Compress me', 9);
$uncompressed = gzinflate($compressed);
echo $uncompressed;
?>

    
```php

## Véase también

`gzdeflate`, `gzcompress`, `gzuncompress`, `gzencode`
