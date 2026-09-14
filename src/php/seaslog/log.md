---
title: SeasLog::log
description: La función de registro de la grabación común
source_url: https://www.php.net/manual/es/seaslog.log.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/log.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73320
---

SeasLog::log

La función de registro de la grabación común

## Descripción

```php
public static SeasLog::log(string $level, [string $message], [array $content], [string $logger]): bool
```php

La función de registro de la grabación común.

## Parámetros

`level`  
Utilizar los niveles en: [SEASLOG_DEBUG](#constant.seaslog-debug), [SEASLOG_INFO](#constant.seaslog-info), [SEASLOG_NOTICE](#constant.seaslog-notice), [SEASLOG_WARNING](#constant.seaslog-warning), [SEASLOG_ERROR](#constant.seaslog-error), [SEASLOG_CRITICAL](#constant.seaslog-critical), [SEASLOG_ALERT](#constant.seaslog-alert), [SEASLOG_EMERGENCY](#constant.seaslog-emergency) O se puede crear un nuevo nivel de autoayuda.

`message`  
El mensaje del registro.

`content`  
El \`message\` contiene marcadores de posición que los implementadores reemplazan con valores del array de contenido. Por ejemplo, si \`message\` es \`log info from {NAME}\` y \`content\` es \`array('NAME' =\> neeke)\`, la información de registro será \`log info from neeke\`.

`logger`  
El \`registro\` pasado por el tercer argumento sería utilizado a partir de ahora, como un registro temporal, cuando la función SeasLog::setLogger() es llamada en el contenido anterior. Si \`logger\` es NULL o "", SeasLog utilizará el último registro definido por SeasLog::setLogger.

## Valores devueltos

Devuelve TRUE en caso de éxito en el registro de la información de registro, FALSE en caso de fallo.

## Ejemplos

Ejemplo de `SeasLog::log`

```
<?php

var_dump(SeasLog::log(SEASLOG_INFO,'info log'));
var_dump(SeasLog::getBuffer());

//crear un nuevo nivel de autoayuda.
var_dump(SeasLog::log('MySelfLevel','info log'));
var_dump(SeasLog::getBuffer());

//con `content`
var_dump(SeasLog::log('MySelfLevel','info log {NAME}',array('NAME' => 'neeke')));
var_dump(SeasLog::getBuffer());

//con `logger`
var_dump(SeasLog::log('MySelfLevel','info log {NAME}',array('NAME' => 'neeke'),'tmp_logger'));
var_dump(SeasLog::getBuffer());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    array(1) {
      ["/var/log/www/default/20180707.log"]=>
      array(1) {
        [0]=>
        string(79) "2018-07-07 11:12:37 | INFO | 72427 | 5b402fa56a2ea | 1530933157.436 | info log
    "
      }
    }

    bool(true)
    array(1) {
      ["/var/log/www/default/20180707.log"]=>
      array(1) {
        [0]=>
        string(86) "2018-07-07 11:13:59 | MySelfLevel | 72470 | 5b402ff781c5e | 1530933239.532 | info log
    "
      }
    }

    bool(true)
    array(1) {
      ["/var/log/www/tmp_logger/20180707.log"]=>
      array(1) {
        [0]=>
        string(92) "2018-07-07 11:28:12 | MySelfLevel | 72833 | 5b40334ce6a2f | 1530934092.946 | info log neeke
    "
      }
    }

    bool(true)
    array(1) {
      ["/var/log/www/default/20180707.log"]=>
      array(1) {
        [0]=>
        string(86) "2018-07-07 11:20:12 | INFO | 72616 | 5b40316c3641e | 1530933612.222 | info log neeke
    "
      }
    }

## Véase también

seaslog.default_template

SeasLog::debug

SeasLog::info

SeasLog::notice

SeasLog::warning

SeasLog::error

SeasLog::critical

SeasLog::alert

SeasLog::emergency
