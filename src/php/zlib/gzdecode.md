---
title: gzdecode
description: Decodifica una cadena comprimida con gzip
source_url: https://www.php.net/manual/es/function.gzdecode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzdecode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_reviewed: false
translation_revision: 7fc84e37b
order: 108750
---

gzdecode

Decodifica una cadena comprimida con gzip

## Descripción

```php
gzdecode(string $data, [int $max_length]): string
```php

Está función retorna una versión decodificada de la entrada `data`.

## Parámetros

`data`  
Los datos para decodificar, codificados con `gzencode`.

`max_length`  
La longitud máxima de datos que decodificar.

## Valores devueltos

La cadena decodificada, o o `false` si ocurre un error.

## Errores/Excepciones

En caso de fallo, se emite un error de nivel `E_WARNING`.

## Véase también

`gzencode`
