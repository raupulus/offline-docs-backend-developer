---
title: gzclose
description: Cierra el apuntador de un archivo gz abierto
source_url: https://www.php.net/manual/es/function.gzclose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzclose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: 02ba67b51
order: 108730
---

gzclose

Cierra el apuntador de un archivo gz abierto

## Descripción

```php
gzclose(resource $stream): bool
```php

Cierra el apuntador del archivo gz dado.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `gzclose`

```
<?php
$gz = gzopen('somefile.gz','w9');
gzputs ($gz, 'I was added to somefile.gz');
gzclose($gz);
?>

    
```php

## Véase también

`gzopen`
