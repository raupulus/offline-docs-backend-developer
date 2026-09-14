---
title: ps_end_page
description: Finaliza una página
source_url: https://www.php.net/manual/es/function.ps-end-page.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-end-page.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 72880807a
order: 65740
---

ps_end_page

Finaliza una página

## Descripción

```php
ps_end_page(resource $psdoc): bool
```php

Finaliza una página que ha sido iniciada con `ps_begin_page`. Finalizar una página deja el contexto de dibujo actual, lo que por ejemplo requiere recargar las fuentes si fueron cargadas con la página y fija varios otros parámetros de dibujo como el grosor de las líneas, el color.

## Parámetros

`psdoc`  
Identificador de un archivo postscript devuelto por `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_begin_page`
