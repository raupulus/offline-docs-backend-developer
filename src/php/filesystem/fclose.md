---
title: fclose
description: Cierra un fichero
source_url: https://www.php.net/manual/es/function.fclose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fclose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23380
---

fclose

Cierra un fichero

## Descripción

```php
fclose(resource $stream): bool
```php

Cierra el fichero representado por el puntero `stream`.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y debe haber sido correctamente abierto por la función `fopen` o la función `fsockopen`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `fclose`

```
<?php

$handle = fopen('somefile.txt', 'r');

fclose($handle);

?>

    
```php

## Véase también

`fopen`, `fsockopen`
