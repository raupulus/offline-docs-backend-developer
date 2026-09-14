---
title: SeasLog::getLastLogger
description: Define el último registrador de SeasLog
source_url: https://www.php.net/manual/es/seaslog.getlastlogger.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/getlastlogger.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73280
---

SeasLog::getLastLogger

Define el último registrador de SeasLog

## Descripción

```php
public static SeasLog::getLastLogger(): string
```php

Utiliza la función SeasLog::getLastLogger para obtener el valor de [seaslog.default_logger](#ini.seaslog.default-logger) configurado en php.ini (seaslog.ini).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Utiliza la función SeasLog::setLogger para modificar el valor de la función SeasLog::getLastLogger.

## Ejemplos

Ejemplo de `SeasLog::getLastLogger`

```
<?php

var_dump(SeasLog::getLastLogger());
SeasLog::setLogger('theNewLogger');
var_dump(SeasLog::getLastLogger());
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(7) "default"
    string(12) "theNewLogger"

## Véase también

SeasLog::setLogger
