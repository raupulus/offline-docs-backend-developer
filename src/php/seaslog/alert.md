---
title: SeasLog::alert
description: Registra la información del registro de alerta
source_url: https://www.php.net/manual/es/seaslog.alert.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/alert.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73130
---

SeasLog::alert

Registra la información del registro de alerta

## Descripción

```php
public static SeasLog::alert(string $message, [array $content], [string $logger]): bool
```php

Registra la información del registro de alerta.

> [!NOTE]
> "ALERT" - Se debe tomar una acción inmediatamente. Se debe prestar atención inmediata al personal concernido para reparaciones de emergencia.

## Parámetros

`message`  
El mensaje del registro.

`content`  
El \`message\` contiene marcadores de posición que los implementadores reemplazan con valores del array de contenido. Por ejemplo, si el \`message\` es 'log info desde {NAME}' y el 'content' es 'array('NAME' =\> neeke)', la información del registro será 'log info desde neeke'.

`logger`  
El \`logger\` causado por el tercer argumento sería utilizado a partir de ahora, como un registro temporal, cuando la función SeasLog::setLogger() es llamada en el contenido anterior. Si \`logger\` es NULL o "", SeasLog utilizará el último registro definido por SeasLog::setLogger.

## Valores devueltos

Retorna TRUE en caso de éxito en el registro de la información del registro, FALSE en caso de fallo.

## Ejemplos

Ejemplo de `SeasLog::alert`

```
<?php

var_dump(SeasLog::alert('log message'));

//con contenido
var_dump(SeasLog::alert('log message from {NAME}',array('NAME' => 'neeke')));

//con registro temporal
var_dump(SeasLog::alert('log message from {NAME}',array('NAME' => 'neeke'),'tmp_logger'));

var_dump(SeasLog::getBuffer());

?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)
    bool(true)
    array(2) {
      ["/var/log/www/default/20180707.log"]=>
      array(2) {
        [0]=>
        string(81) "2018-07-07 11:45:49 | ALERT | 73263 | 5b40376d1067c | 1530935149.68 | log message
    "
        [1]=>
        string(92) "2018-07-07 11:45:49 | ALERT | 73263 | 5b40376d1067c | 1530935149.68 | log message from neeke
    "
      }
      ["/var/log/www/tmp_logger/20180707.log"]=>
      array(1) {
        [0]=>
        string(92) "2018-07-07 11:45:49 | ALERT | 73263 | 5b40376d1067c | 1530935149.68 | log message from neeke
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

SeasLog::emergency

SeasLog::log
