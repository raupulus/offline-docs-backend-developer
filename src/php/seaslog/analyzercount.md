---
title: SeasLog::analyzerCount
description: Devuelve el número de registros por nivel, ruta de acceso del registro
  y palabra clave
source_url: https://www.php.net/manual/es/seaslog.analyzercount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/analyzercount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73140
---

SeasLog::analyzerCount

Devuelve el número de registros por nivel, ruta de acceso del registro y palabra clave

## Descripción

```php
public static SeasLog::analyzerCount(string $level, [string $log_path], [string $key_word]): mixed
```php

\`SeasLog\` obtiene el valor del contador de \`grep -ai '{level}' \| grep -aic '{key_word}'\` utiliza el pipe del sistema y devuelve a PHP (array o integer).

## Parámetros

`level`  
String. El nivel de información del registro.

`log_path`  
String. La ruta de acceso de la información del registro.

`key_word`  
String. La palabra clave de búsqueda para la información del registro.

## Valores devueltos

Si \`level\` es SEASLOG_ALL o está vacío, devuelve todos los niveles contados como \`array\`. Si \`level\` es SEASLOG_INFO o cualquier otro nivel, devuelve el contador como \`integer\`.

## Ejemplos

Ejemplo de `SeasLog::analyzerCount`

```
<?php

$countResult1 = SeasLog::analyzerCount();

//con `level`
$countResult2 = SeasLog::analyzerCount(SEASLOG_DEBUG);

//con `level` y `log_path`
$countResult3 = SeasLog::analyzerCount(SEASLOG_ERROR,date('Ymd',time()));

//con `level` y `key_word`
$countResult4 = SeasLog::analyzerCount(SEASLOG_DEBUG,NULL,'accessToken');

var_dump($countResult1,$countResult2,$countResult3,$countResult4);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(8) {
      ["DEBUG"]=>
      int(180)
      ["INFO"]=>
      int(214)
      ["NOTICE"]=>
      int(0)
      ["WARNING"]=>
      int(0)
      ["ERROR"]=>
      int(228)
      ["CRITICAL"]=>
      int(244)
      ["ALERT"]=>
      int(1)
      ["EMERGENCY"]=>
      int(0)
    }

    int(180)

    int(228)

    int(29)

## Véase también

SeasLog::analyzerDetail
