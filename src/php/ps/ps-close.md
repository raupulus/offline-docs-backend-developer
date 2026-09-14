---
title: ps_close
description: Cerrar un documento PostScript
source_url: https://www.php.net/manual/es/function.ps-close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65680
---

ps_close

Cerrar un documento PostScript

## Descripción

```php
ps_close(resource $psdoc): bool
```php

Cierra el documento PostScript.

Esta función escribe el tráiler del documento PostScript. También escribe el árbol de marcapáginas. `ps_close` no libera ningún recurso, lo que se realiza mediante la función `ps_delete`.

Esta función también es llamda por la función `ps_delete` si no ha sido llamada antes.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_open_file`, `ps_delete`
