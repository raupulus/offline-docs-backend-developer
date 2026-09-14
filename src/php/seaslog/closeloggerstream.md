---
title: SeasLog::closeLoggerStream
description: Libera manualmente el flujo de registro del registro
source_url: https://www.php.net/manual/es/seaslog.closeloggerstream.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/closeloggerstream.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73160
---

SeasLog::closeLoggerStream

Libera manualmente el flujo de registro del registro

## Descripción

```php
public static SeasLog::closeLoggerStream(int $model, string $logger): bool
```php

Libera manualmente el flujo de registro del registro. SeasLog almacena en caché el gestor de flujo abierto por el registro para ahorrar en la carga adicional de la creación de un flujo. El gestor será liberado automáticamente al final de la petición. Si en modo CLI, el proceso también liberará automáticamente cuando termine. O se pueden utilizar las siguientes funciones para liberar manualmente (la función de liberación manual debe actualizar SeasLog 1.8.6 o versión posterior).

## Parámetros

`model`  
Una constante de entero. [SEASLOG_CLOSE_LOGGER_STREAM_MOD_ALL](#constant.seaslog-close-logger-stream-mod-all), [SEASLOG_CLOSE_LOGGER_STREAM_MOD_ASSIGN](#constant.seaslog-close-logger-stream-mod-assign)

`logger`  
El nombre del registro.

## Valores devueltos

Devuelve TRUE en caso de éxito del flujo de registro liberado, FALSE en caso de fallo.

## Ejemplos

Ejemplo de SeasLog::closeLoggerStream

```
<?php

var_dump(SeasLog::closeLoggerStream());
var_dump(SeasLog::closeLoggerStream(SEASLOG_CLOSE_LOGGER_STREAM_MOD_ALL));
var_dump(SeasLog::closeLoggerStream(SEASLOG_CLOSE_LOGGER_STREAM_MOD_ASSIGN, 'logger_name'));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    bool(true)

## Véase también

SeasLog::setLogger

SeasLog::getLastLogger
