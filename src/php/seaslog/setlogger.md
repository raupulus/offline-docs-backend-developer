---
title: SeasLog::setLogger
description: Define el nombre del registrador de SeasLog
source_url: https://www.php.net/manual/es/seaslog.setlogger.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/setlogger.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73360
---

SeasLog::setLogger

Define el nombre del registrador de SeasLog

## Descripción

```php
public static SeasLog::setLogger(string $logger): bool
```php

Utilizar la función SeasLog::setLogger para definir el valor de la función SeasLog::getLastLogger. Esto significa que SeasLog registrará la información del registro en el directorio del registrador.

## Parámetros

`logger`  
El nombre del registrador.

## Valores devueltos

Devuelve TRUE en caso de éxito en la creación del directorio del registrador, FALSE en caso de fallo.

## Ejemplos

Ejemplo de `SeasLog::setLogger`

```
<?php

var_dump(SeasLog::setLogger('testModule/testLogger'));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)

## Véase también

SeasLog::getLastLogger

SeasLog::closeLoggerStream
