---
title: SeasLog::setDatetimeFormat
description: Define el formato de fecha y hora de SeasLog
source_url: https://www.php.net/manual/es/seaslog.setdatetimeformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/setdatetimeformat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73350
---

SeasLog::setDatetimeFormat

Define el formato de fecha y hora de SeasLog

## Descripción

```php
public static SeasLog::setDatetimeFormat(string $format): bool
```php

Define el estilo de formato de fecha y hora de SeasLog.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`format`  
String. Como \`Y-m-d H:i:s\` o \`Ymd His\`. Ver también el primer argumento \`format\` en `date`.

## Valores devueltos

Devuelve TRUE en caso de éxito al definir el formato de fecha y hora, FALSE en caso de fallo.

## Ejemplos

Ejemplo de `SeasLog::setDatetimeFormat`

```
<?php

var_dump(SeasLog::setDateTimeFormat('Ymd His'));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)

## Véase también

SeasLog::getDateTimeFormat
