---
title: MongoDB\BSON\UTCDateTime::__construct
description: Construye un nuevo objeto UTCDateTime
source_url: https://www.php.net/manual/es/mongodb-bson-utcdatetime.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/bson/utcdatetime/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: 9f4cb232d
order: 48600
---

MongoDB\BSON\UTCDateTime::\_\_construct

Construye un nuevo objeto UTCDateTime

## Descripción

```php
final public MongoDB\BSON\UTCDateTime::__construct([int $milliseconds])
```php

## Parámetros

`milliseconds` (`intMongoDB\BSON\Int64DateTimeInterfacenull`)  
Número de milisegundos transcurridos desde la época Unix (1 de enero de 1970). Los valores negativos representan fechas anteriores a 1970. Este valor puede proporcionarse como un `int` de 64 bits. Para compatibilidad en sistemas de 32 bits, este parámetro también puede proporcionarse como un `MongoDB\BSON\Int64`.

Si el argumento es un `DateTimeInterface`, el número de milisegundos transcurridos desde la época Unix se derivará de ese valor.

Si este argumento es `null`, por omisión se utilizará la hora actual.

## Errores/Excepciones

Lanza una excepción

MongoDB\Driver\Exception\InvalidArgumentException

en caso de error durante el análisis de un argumento.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL mongodb 2.0.0 | El parámetro `milliseconds` ya no acepta un argumento de tipo `string` o `float`. |
| PECL mongodb 1.20.0 | El argumento `milliseconds` ahora acepta un objeto `MongoDB\BSON\Int64` (para compatibilidad en plataformas de 32 bits). Especificar un `string` o `float` está obsoleto. |
| PECL mongodb 1.2.0 | El argumento `milliseconds` es opcional y por omisión es `null` (es decir, hora actual). El argumento también acepta un `DateTimeInterface`, que puede usarse para derivar el número de milisegundos transcurridos desde la época Unix. Anteriormente, solo se aceptaban tipos `int`, `float` y `string`. |

## Ejemplos

Ejemplo de `MongoDB\BSON\UTCDateTime::__construct`

```
<?php

var_dump(new MongoDB\BSON\UTCDateTime);

var_dump(new MongoDB\BSON\UTCDateTime(new DateTime));

var_dump(new MongoDB\BSON\UTCDateTime(1416445411987));

?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(MongoDB\BSON\UTCDateTime)#1 (1) {
      ["milliseconds"]=>
      string(13) "1484852905560"
    }
    object(MongoDB\BSON\UTCDateTime)#1 (1) {
      ["milliseconds"]=>
      string(13) "1484852905560"
    }
    object(MongoDB\BSON\UTCDateTime)#1 (1) {
      ["milliseconds"]=>
      string(13) "1416445411987"
    }

## Véase también

Tipos BSON: Fecha
