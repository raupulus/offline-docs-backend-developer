---
title: SeasLog::getDatetimeFormat
description: Devuelve el formato de fecha y hora de SeasLog
source_url: https://www.php.net/manual/es/seaslog.getdatetimeformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/getdatetimeformat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73270
---

SeasLog::getDatetimeFormat

Devuelve el formato de fecha y hora de SeasLog

## Descripción

```php
public static SeasLog::getDatetimeFormat(): string
```php

Devuelve el formato de fecha y hora de SeasLog. Utilice la función SeasLog::getDatetimeFormat para obtener el valor de [seaslog.default_datetime_format](#ini.seaslog.default-datetime-format) configurado en php.ini (seaslog.ini).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el formato de fecha y hora de SeasLog [seaslog.default_datetime_format](#ini.seaslog.default-datetime-format). Utilice la función SeasLog::setDatetimeFormat para modificar este valor.

## Ejemplos

Ejemplo de `SeasLog::getDatetimeFormat`

```
<?php

var_dump(SeasLog::getDateTimeFormat());
var_dump(SeasLog::setDateTimeFormat('Ymd His'));
var_dump(SeasLog::getDateTimeFormat());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(11) "Y-m-d H:i:s"
    bool(true)
    string(7) "Ymd His"

## Véase también

SeasLog::setDatetimeFormat
