---
title: SeasLog::critical
description: Registra la información de registro crítica
source_url: https://www.php.net/manual/es/seaslog.critical.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/critical.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73180
---

SeasLog::critical

Registra la información de registro crítica

## Descripción

```php
public static SeasLog::critical(string $message, [array $content], [string $logger]): bool
```php

Registra la información de registro crítica.

> [!NOTE]
> "CRITICAL" - Condiciones críticas. Deben ser reparadas de inmediato, y el componente del programa no está disponible.

## Parámetros

`message`  
El mensaje de registro.

`content`  
El \`message\` contiene marcadores de posición que los implementadores reemplazan con valores del array de contenido. Por ejemplo, si \`message\` es \`log info from {NAME}\` y \`content\` es \`array('NAME' =\> neeke)\`, la información de registro será \`log info from neeke\`.

`logger`  
El \`registro\` pasado por el tercer parámetro sería utilizado ahora, como un registro temporal, cuando la función SeasLog::setLogger() es llamada en el contenido anterior. Si \`logger\` es NULL o "", SeasLog utilizará el último registro definido por SeasLog::setLogger.

## Valores devueltos

Devuelve TRUE en caso de éxito en el registro de la información de registro, FALSE en caso de fallo.

## Ejemplos

Ejemplo de `SeasLog::critical`

```
<?php

var_dump(SeasLog::critical('log message'));

//con contenido
var_dump(SeasLog::critical('log message from {NAME}',array('NAME' => 'neeke')));

//con registro temporal
var_dump(SeasLog::critical('log message from {NAME}',array('NAME' => 'neeke'),'tmp_logger'));

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
        string(81) "2018-07-07 11:45:49 | CRITICAL | 73263 | 5b40376d1067c | 1530935149.68 | log message
    "
        [1]=>
        string(92) "2018-07-07 11:45:49 | CRITICAL | 73263 | 5b40376d1067c | 1530935149.68 | log message from neeke
    "
      }
      ["/var/log/www/tmp_logger/20180707.log"]=>
      array(1) {
        [0]=>
        string(92) "2018-07-07 11:45:49 | CRITICAL | 73263 | 5b40376d1067c | 1530935149.68 | log message from neeke
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

SeasLog::alert

SeasLog::emergency

SeasLog::log
