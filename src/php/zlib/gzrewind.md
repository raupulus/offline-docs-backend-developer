---
title: gzrewind
description: Reinicia la posición del apuntador a un archivo gz
source_url: https://www.php.net/manual/es/function.gzrewind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zlib/functions/gzrewind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zlib
translation_status: ready
translation_revision: 02ba67b51
order: 108880
---

gzrewind

Reinicia la posición del apuntador a un archivo gz

## Descripción

```php
gzrewind(resource $stream): bool
```php

Coloca el indicador de posición del apuntador al archivo gz dado al comienzo del flujo del archivo.

## Parámetros

`stream`  
El apuntador al archivo gz. Debe ser válido y debe apuntar a un archivo abierto exitosamente por `gzopen`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`gzseek`, `gztell`
