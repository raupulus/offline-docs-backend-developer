---
title: SeasLog::flushBuffer
description: Vacía el buffer de registros, lo vierte en el fichero del appender o
  lo envía a la API remota con TCP/UDP
source_url: https://www.php.net/manual/es/seaslog.flushbuffer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/flushbuffer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73230
---

SeasLog::flushBuffer

Vacía el buffer de registros, lo vierte en el fichero del appender o lo envía a la API remota con TCP/UDP

## Descripción

```php
public static SeasLog::flushBuffer(): bool
```php

Vacía el buffer de registros por [seaslog.appender](#ini.seaslog.appender): vierte en el fichero, o envía a la API remota con TCP/UDP.

> [!NOTE]
> Ver también: [seaslog.appender_retry](#ini.seaslog.appender-retry) [seaslog.remote_host](#ini.seaslog.remote-host) [seaslog.remote_port](#ini.seaslog.remote-port)

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve TRUE en caso de éxito del vaciado del buffer, FALSE en caso de fallo.

## Ejemplos

Ejemplo de `SeasLog::flushBuffer`

```
<?php

SeasLog::info('info log');
SeasLog::debug('debug log');
var_dump(SeasLog::getBuffer());
var_dump(SeasLog::flushBuffer());
var_dump(SeasLog::getBuffer());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(1) {
      ["/var/log/www/default/20180707.log"]=>
      array(2) {
        [0]=>
        string(79) "2018-07-07 10:47:58 | INFO | 71910 | 5b4029ded6009 | 1530931678.877 | info log
    "
        [1]=>
        string(81) "2018-07-07 10:47:58 | DEBUG | 71910 | 5b4029ded6009 | 1530931678.877 | debug log
    "
      }
    }
    bool(true)
    array(0) {
    }

## Véase también

seaslog.use_buffer

seaslog.buffer_size

seaslog.buffer_disabled_in_cli

SeasLog::getBufferEnabled

SeasLog::getBuffer
