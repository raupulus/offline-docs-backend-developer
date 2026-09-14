---
title: SeasLog::getBuffer
description: Devuelve el búfer de registros en memoria como un array
source_url: https://www.php.net/manual/es/seaslog.getbuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/getbuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73250
---

SeasLog::getBuffer

Devuelve el búfer de registros en memoria como un array

## Descripción

```php
public static SeasLog::getBuffer(): array
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array del búfer de registros en memoria.

## Ejemplos

Ejemplo de `SeasLog::getBuffer`

```
<?php

var_dump(SeasLog::info('info log'));
var_dump(SeasLog::debug('debug log'));
var_dump(SeasLog::getBuffer());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    array(1) {
      ["/var/log/www/default/20180707.log"]=>
      array(2) {
        [0]=>
        string(79) "2018-07-07 10:43:32 | INFO | 71785 | 5b4028d4c58d5 | 1530931412.810 | info log
    "
        [1]=>
        string(81) "2018-07-07 10:43:32 | DEBUG | 71785 | 5b4028d4c58d5 | 1530931412.810 | debug log
    "
      }
    }

## Véase también

seaslog.use_buffer

seaslog.buffer_size

seaslog.buffer_disabled_in_cli

SeasLog::getBufferEnabled

SeasLog::flushBuffer
