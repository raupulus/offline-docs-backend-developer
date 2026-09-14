---
title: md5_file
description: Calcula el md5 de un fichero
source_url: https://www.php.net/manual/es/function.md5-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/md5-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 88880
---

md5_file

Calcula el md5 de un fichero

## Descripción

```php
md5_file(string $filename, [bool $binary]): string
```php

`md5_file` calcula el MD5 del fichero `filename` utilizando el algoritmo [`RSA Data Security, Inc. MD5 Message-Digest Algorithm`](https://datatracker.ietf.org/doc/html/rfc1321), luego devuelve el valor calculado. El resultado es un número de 32 caracteres hexadecimales.

## Parámetros

`filename`  
El nombre del fichero.

`binary`  
Cuando `true`, devuelve el preprocesamiento en formato binario sin tratar con un tamaño de 16.

## Valores devueltos

Devuelve un string en caso de éxito, `false` en caso contrario.

## Ejemplos

Ejemplo de uso de `md5_file`

```
<?php
$file = '/examples/book.xml';

echo 'La firma MD5 del fichero ' . $file . ' es ' . md5_file($file);
?>

    
```php

## Véase también

`hash_file`, `hash_init`, `md5`
