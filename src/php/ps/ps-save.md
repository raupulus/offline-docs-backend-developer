---
title: ps_save
description: Guardar el contexto actual
source_url: https://www.php.net/manual/es/function.ps-save.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-save.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65970
---

ps_save

Guardar el contexto actual

## Descripción

```php
ps_save(resource $psdoc): bool
```php

Guarda el contexto de gráficos actual, conteniendo ajustes de color, de traslación y de rotación, y algunos más. Un contexto guardado puede ser restaurado con `ps_restore`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_restore`
