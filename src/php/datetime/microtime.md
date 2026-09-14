---
title: microtime
description: Devuelve el timestamp UNIX actual con microsegundos
source_url: https://www.php.net/manual/es/function.microtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/microtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11300
---

microtime

Devuelve el timestamp UNIX actual con microsegundos

## Descripción

```php
microtime([bool $as_float]): string
```php

`microtime` devuelve el timestamp Unix, con microsegundos. Esta función está únicamente disponible en los sistemas que soportan la función gettimeofday().

Para medir el rendimiento, se recomienda el uso de `hrtime`.

## Parámetros

`as_float`  
Si se utiliza y se define como `true`, `microtime` devolverá un `float` en lugar de un `string`, tal como se describe en la sección de valores devueltos a continuación.

## Valores devueltos

Por omisión, `microtime` devuelve un `string` en el formato "msec sec", donde `sec` es el número de segundos desde la época Unix (1 de Enero de 1970, 00:00:00 GMT), y `msec` es el número de microsegundos que han transcurrido desde `sec`, expresado en segundos en forma de fracción decimal.

Si `as_float` se define como `true`, entonces `microtime` devuelve un `float`, que representa el tiempo actual, en segundos, desde la época Unix, con precisión de microsegundo.

## Ejemplos

Duración de ejecución de un script en PHP

```
<?php
$time_start = microtime(true);

// Espera durante un momento
usleep(10_000);

$time_end = microtime(true);
$time = $time_end - $time_start;

print "No hacer nada durante $time segundos\n";

    
```php

Ejemplo con `microtime` y `REQUEST_TIME_FLOAT`

```
<?php
// Duración de espera aleatoria
usleep(random_int(10_000, 1_000_000));

// REQUEST_TIME_FLOAT está disponible en el array superglobal $_SERVER.
// Contiene el timestamp del inicio de la petición, con precisión de microsegundo.
$time = microtime(true) - $_SERVER["REQUEST_TIME_FLOAT"];

echo "No hacer nada durante $time segundos\n";

    
```php

## Véase también

`time`, `hrtime`
