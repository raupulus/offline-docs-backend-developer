---
title: gzuncompress
description: Descomprime una cadena comprimida
source_url: https://www.php.net/manual/es/function.gzuncompress.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzuncompress.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 02ba67b51
order: 108910
---

gzuncompress

Descomprime una cadena comprimida

## Descripción

```php
gzuncompress(string $data, [int $max_length]): string
```php

Está función descomprime una cadena comprimida

## Parámetros

`data`  
Los datos comprimidos con `gzcompress`.

`max_length`  
La longitud máxima de datos a decodificar.

## Valores devueltos

Los datos originales sin comprimir o `false` en caso de error.

La función retornará un error si los datos descomprimidos son más de 32768 veces la longitud de la entrada comprimida `data` o mayores que el parámetro opcional `max_length`.

## Ejemplos

Ejemplo de `gzuncompress`

```
<?php
$compressed   = gzcompress('Compress me', 9);
$uncompressed = gzuncompress($compressed);
echo $uncompressed;
?>

    
```php

## Véase también

`gzcompress`, `gzinflate`, `gzdeflate`, `gzencode`
