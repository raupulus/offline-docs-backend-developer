---
title: SeasLog::getBufferEnabled
description: Determina si el búfer está activado
source_url: https://www.php.net/manual/es/seaslog.getbufferenabled.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/getbufferenabled.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73260
---

SeasLog::getBufferEnabled

Determina si el búfer está activado

## Descripción

```php
public static SeasLog::getBufferEnabled(): bool
```php

Resulta de la combinación de [seaslog.use_buffer](#ini.seaslog.use-buffer) y [seaslog.buffer_disabled_in_cli](#ini.seaslog.buffer-disabled-in-cli).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve TRUE si [seaslog.use_buffer](#ini.seaslog.use-buffer) está activado. Si [seaslog.buffer_disabled_in_cli](#ini.seaslog.buffer-disabled-in-cli) está activado, y el script se ejecuta en CLI, el parámetro seaslog.use_buffer será ignorado, Seaslog escribirá en el almacén de datos INMEDIATAMENTE.

## Ejemplos

Ejemplo de `SeasLog::getBufferEnabled`

```
<?php

var_dump(SeasLog::getBufferEnabled());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(false)

## Véase también

seaslog.use_buffer

seaslog.buffer_size

seaslog.buffer_disabled_in_cli

SeasLog::getBuffer

SeasLog::flushBuffer
