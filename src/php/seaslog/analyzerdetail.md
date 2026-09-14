---
title: SeasLog::analyzerDetail
description: Devuelve los detalles del registro por nivel, ruta de registro, palabra
  clave, inicio, límite, orden
source_url: https://www.php.net/manual/es/seaslog.analyzerdetail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/seaslog/seaslog/analyzerdetail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: seaslog
translation_status: ready
translation_reviewed: false
translation_revision: 60f4ad429
order: 73150
---

SeasLog::analyzerDetail

Devuelve los detalles del registro por nivel, ruta de registro, palabra clave, inicio, límite, orden

## Descripción

```php
public static SeasLog::analyzerDetail(string $level, [string $log_path], [string $key_word], [int $start], [int $limit], [int $order]): mixed
```php

\`SeasLog\` obtiene los resultados \`grep -ai '{level}' \| grep -ai '{key_word}' \| sed -n '{start},{limit}'p\` utiliza el pipe del sistema y devuelve un array a PHP.

## Parámetros

`level`  
String. El nivel de información del registro.

`log_path`  
String. La ruta de la información del registro.

`key_word`  
String. La palabra clave de búsqueda para la información del registro.

`start`  
Integer. Por omisión, \`1\`.

`limit`  
Integer. Por omisión, \`20\`.

`order`  
Integer. Por omisión, [SEASLOG_DETAIL_ORDER_ASC](#constant.seaslog-detail-order-asc). Ver también: [SEASLOG_DETAIL_ORDER_ASC](#constant.seaslog-detail-order-asc), [SEASLOG_DETAIL_ORDER_DESC](#constant.seaslog-detail-order-desc)

## Valores devueltos

Devuelve los resultados en forma de array.

> [!NOTE]
> Cuando \`start\`,\`limit\` no es NULL y en Windows, SeasLog lanzará una excepción con el mensaje 'Param start and limit don't support Windows'.

## Ejemplos

Ejemplo de `SeasLog::analyzerDetail`

```
<?php

$result1 = SeasLog::analyzerDetail(SEASLOG_ERROR);

//con `logger` y `key_word`
$result2 = SeasLog::analyzerDetail(SEASLOG_ERROR,'test/logger/','neeke');

//con `start` y `limit`
$result3 = SeasLog::analyzerDetail(SEASLOG_ERROR,'test/logger/','neeke',1,2);

var_dump($result1,$result2,$result3);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    array(20) {
      [0]=>
      string(93) "2018-07-09 12:52:53 | ERROR | 12247 | 5b42ea2580e51 | 1531111973.528 | log message from neeke"
      [1]=>
      string(93) "2018-07-09 12:52:54 | ERROR | 12256 | 5b42ea26d6657 | 1531111974.878 | log message from neeke"
      [2]=>
      string(93) "2018-07-09 12:52:55 | ERROR | 12265 | 5b42ea277b8d4 | 1531111975.506 | log message from neeke"
      [3]=>
      string(104) "2018-07-09 12:52:55 | ERROR | 12274 | 5b42ea27db5dc | 1531111975.898 | log message from the other people"
    ...
    }

    array(3) {
      [0]=>
      string(93) "2018-07-09 12:52:53 | ERROR | 12247 | 5b42ea2580e51 | 1531111973.528 | log message from neeke"
      [1]=>
      string(93) "2018-07-09 12:52:54 | ERROR | 12256 | 5b42ea26d6657 | 1531111974.878 | log message from neeke"
      [2]=>
      string(93) "2018-07-09 12:52:55 | ERROR | 12265 | 5b42ea277b8d4 | 1531111975.506 | log message from neeke"
    }

    array(2) {
      [0]=>
      string(93) "2018-07-09 12:52:53 | ERROR | 12247 | 5b42ea2580e51 | 1531111973.528 | log message from neeke"
      [1]=>
      string(93) "2018-07-09 12:52:54 | ERROR | 12256 | 5b42ea26d6657 | 1531111974.878 | log message from neeke"
    }

## Véase también

SeasLog::analyzerCount
