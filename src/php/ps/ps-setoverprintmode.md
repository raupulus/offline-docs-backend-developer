---
title: ps_setoverprintmode
description: Establecer el modo de sobreimpresión
source_url: https://www.php.net/manual/es/function.ps-setoverprintmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-setoverprintmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 9c3786643
order: 66150
---

ps_setoverprintmode

Establecer el modo de sobreimpresión

## Descripción

```php
ps_setoverprintmode(resource $psdoc, int $mode): bool
```php

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

`mode`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
