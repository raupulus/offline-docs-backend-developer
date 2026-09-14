---
title: gettimeofday
description: Devuelve la hora actual
source_url: https://www.php.net/manual/es/function.gettimeofday.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/gettimeofday.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11240
---

gettimeofday

Devuelve la hora actual

## Descripción

```php
gettimeofday([bool $as_float]): array
```php

Es una interfaz con gettimeofday(2). Devuelve un array asociativo que contiene las informaciones devueltas por el sistema.

## Parámetros

`as_float`  
Cuando se define como `true`, se devuelve un `float` en lugar de un array.

## Valores devueltos

Por omisión, se devuelve un `array`. Si el argumento `as_float` está definido, entonces se devolverá un `float`.

Claves del array :

- "sec" : segundos desde la época Unix

- "usec" : microsegundos

- "minuteswest" : minutos de desfase respecto a Greenwich, hacia el Oeste.

- "dsttime" : tipo de corrección dst

## Ejemplos

Ejemplo con `gettimeofday`

```
<?php
print_r(gettimeofday());

echo gettimeofday(true);

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
       [sec] => 1073504408
       [usec] => 238215
       [minuteswest] => 0
       [dsttime] => 1
    )
    1073504408.23910
