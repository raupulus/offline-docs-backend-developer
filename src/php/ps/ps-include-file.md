---
title: ps_include_file
description: Leer un fichero externo con código PostScript sin tratar
source_url: https://www.php.net/manual/es/function.ps-include-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-include-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 9c3786643
order: 65840
---

ps_include_file

Leer un fichero externo con código PostScript sin tratar

## Descripción

```php
ps_include_file(resource $psdoc, string $file): bool
```php

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`file`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
