---
title: ps_get_buffer
description: Obtener el buffer completo que contiene la información generada de PS
source_url: https://www.php.net/manual/es/function.ps-get-buffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-get-buffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 65800
---

ps_get_buffer

Obtener el buffer completo que contiene la información generada de PS

## Descripción

```php
ps_get_buffer(resource $psdoc): string
```php

Esta función aún no está implementada. Siempre devolverá una cadena vacía. La idea para una implementación posterior es escribir el contenido del fichero postscript en un buffer interno si se solicita la creación en memoria, y recuperar el contenifo del buffer con esta función. Actualmente, los documentos creados en memoria son enviados al visualizador sin la participación de un buffer.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`psdoc`  
El identificador de recursos del fichero postscript, como el devuelto por la función `ps_new`.

## Véase también

`ps_open_file`
