---
title: date_sun_info
description: Retorna un array con las informaciones sobre el amanecer/atardecer así
  como el inicio y el fin del amanecer
source_url: https://www.php.net/manual/es/function.date-sun-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-sun-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11140
---

date_sun_info

Retorna un array con las informaciones sobre el amanecer/atardecer así como el inicio y el fin del amanecer

## Descripción

```php
date_sun_info(int $timestamp, float $latitude, float $longitude): array
```php

## Parámetros

`timestamp`  
Timestamp Unix.

`latitude`  
Latitud, en grados.

`longitude`  
Longitud, en grados.

## Valores devueltos

Retorna un array cuya estructura del array se detalla en la lista siguiente:

`sunrise`  
El timestamp del amanecer (ángulo de zenit = 90°35').

`sunset`  
El timestamp del atardecer (ángulo de zenit = 90°35').

`transit`  
El timestamp donde el sol está en su cenit, es decir ha alcanzado su punto más alto.

`civil_twilight_begin`  
El inicio del amanecer civil (ángulo de zenit = 96°). Termina en el `sunrise`.

`civil_twilight_end`  
El fin del crepúsculo civil (ángulo de zenit = 96°). Comienza en el `sunset`.

`nautical_twilight_begin`  
El inicio del amanecer náutico (ángulo de zenit = 102°). Termina en el `civil_twilight_begin`.

`nautical_twilight_end`  
El fin del crepúsculo náutico (ángulo de zenit = 102°). Comienza en `civil_twilight_end`.

`astronomical_twilight_begin`  
El inicio del amanecer astronómico (ángulo de zenit = 108°). Termina en el `nautical_twilight_begin`.

`astronomical_twilight_end`  
El fin del crepúsculo astronómico (ángulo de zenit = 108°). Comienza en `nautical_twilight_end`.

Los valores de los elementos del array son timestamps UNIX, `false`, si el sol está bajo el zenit respectivo durante todo el día, o `true`, si el sol está sobre el zenit respectivo durante todo el día.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | El cálculo ha sido corregido teniendo en cuenta la medianoche local en lugar del mediodía local, lo que modifica ligeramente los resultados. |

## Ejemplos

Ejemplo con `date_sun_info`

```
<?php
$sun_info = date_sun_info(strtotime("2006-12-12"), 31.7667, 35.2333);
foreach ($sun_info as $key => $val) {
  echo "$key: " . date("H:i:s", $val) . "\n";
}

    
```php

El ejemplo anterior mostrará:

    sunrise: 05:52:11
    sunset: 15:41:21
    transit: 10:46:46
    civil_twilight_begin: 05:24:08
    civil_twilight_end: 16:09:24
    nautical_twilight_begin: 04:52:25
    nautical_twilight_end: 16:41:06
    astronomical_twilight_begin: 04:21:32
    astronomical_twilight_end: 17:12:00

Noche polar con un poco de tratamiento

```
<?php
$tz = new \DateTimeZone('America/Anchorage');

$si = date_sun_info(strtotime("2022-12-21"), 70.21, -148.51);
foreach ($si as $key => $value) {
    echo
        match ($value) {
            true => 'always',
            false => 'never',
            default => date_create("@{$value}")->setTimeZone($tz)->format( 'H:i:s T' ),
        },
        ": {$key}",
        "\n";
}

    
```php

El ejemplo anterior mostrará:

    never: sunrise
    never: sunset
    12:52:18 AKST: transit
    10:53:19 AKST: civil_twilight_begin
    14:51:17 AKST: civil_twilight_end
    09:01:47 AKST: nautical_twilight_begin
    16:42:48 AKST: nautical_twilight_end
    07:40:47 AKST: astronomical_twilight_begin
    18:03:49 AKST: astronomical_twilight_end

Sol de medianoche (Tromso, Noruega)

```
<?php
$si = date_sun_info(strtotime("2022-06-26"), 69.68, 18.94);
print_r($si);

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [sunrise] => 1
        [sunset] => 1
        [transit] => 1656240426
        [civil_twilight_begin] => 1
        [civil_twilight_end] => 1
        [nautical_twilight_begin] => 1
        [nautical_twilight_end] => 1
        [astronomical_twilight_begin] => 1
        [astronomical_twilight_end] => 1
    )

Cálculo de la duración del día (Kiev)

```
<?php
$si = date_sun_info(strtotime('2022-08-26'), 50.45, 30.52);
$diff = $si['sunset'] - $si['sunrise'];
echo "Duración del día: ",
    floor($diff / 3600), "h ",
    floor(($diff % 3600) / 60), "s\n";

    
```php

El ejemplo anterior mostrará:

    Duración del día: 13h 56s
