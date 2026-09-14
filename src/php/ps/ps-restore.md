---
title: ps_restore
description: Restaurar un contexto previamente guardado
source_url: https://www.php.net/manual/es/function.ps-restore.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-restore.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65950
---

ps_restore

Restaurar un contexto previamente guardado

## Descripción

```php
ps_restore(resource $psdoc): bool
```php

Restaura un conexto de gráficos previamente guardado. Cualquier llamada a la función `ps_save` debe estar acompañada por una llamada a `ps_restore`. Todas las transformaciones de coordenadas, ajustes de estilos de línea, ajustes de color, etc., son restauradas al estado anterior de la llamada a la función `ps_save`.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`ps_save`
