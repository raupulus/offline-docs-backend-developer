---
title: ps_delete
description: Borrar todos los recursos de un documento PostScript
source_url: https://www.php.net/manual/es/function.ps-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65730
---

ps_delete

Borrar todos los recursos de un documento PostScript

## Descripción

```php
ps_delete(resource $psdoc): bool
```php

Principalmente libera la memoria usada por el documento. También cierra un fichero, si no fue cerrado antes con la función `ps_close`. En cualquier caso, antes se debería cerrar el fichero con la función `ps_close`, ya que `ps_close` no sólo cierra el fichero, sino que también imprime un tráiler que contiene comentarios de PostScript, como el número de páginas del documento, y añade la jerarquía de marcapáginas.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_close`
