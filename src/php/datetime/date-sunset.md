---
title: date_sunset
description: Devuelve la hora de puesta del sol para un día y un lugar dados
source_url: https://www.php.net/manual/es/function.date-sunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/date-sunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11160
---

date_sunset

Devuelve la hora de puesta del sol para un día y un lugar dados

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 8.1.0. Depender de esta función está altamente desaconsejo. Use `date_sun_info` en su lugar.

## Descripción

```php
#[\Deprecated] date_sunset(int $timestamp, [int $returnFormat], [float $latitude], [float $longitude], [float $zenith], [float $utcOffset]): string
```php

La función `date_sunset` devuelve la hora de puesta del sol para un día (especificado como `timestamp` Unix) y un lugar dados.

## Parámetros

`timestamp`  
El `timestamp` Unix del día para el cual se proporciona la hora de puesta del sol.

`returnFormat`  
| Constante | Descripción | Ejemplo |
|----|----|----|
| SUNFUNCS_RET_STRING | Devuelve el resultado en forma de `string` | 16:46 |
| SUNFUNCS_RET_DOUBLE | Devuelve el resultado en forma de `float` | 16.78243132 |
| SUNFUNCS_RET_TIMESTAMP | Devuelve el resultado en forma de `int` (timestamp) | 1095034606 |

Constantes para el parámetro `returnFormat`

`latitude`  
Por omisión, es el Norte. Pase un valor negativo para el Sur. Ver también [date.default_latitude](#ini.date.default-latitude).

`longitude`  
Por omisión, es el Este. Pase un valor negativo para el Oeste. Ver también [date.default_longitude](#ini.date.default-longitude).

`zenith`  
`zenith` es el ángulo entre el centro del sol y la línea perpendicular a la superficie de la tierra. Por omisión [date.sunset_zenith](#ini.date.sunset-zenith)

| Ángulo | Descripción |
|----|----|
| 90°50' | Puesta del sol: El punto donde el sol se vuelve invisible. |
| 96° | Crepúsculo civil: convencionalmente utilizado para significar el fin del crepúsculo. |
| 102° | Crepúsculo náutico: el punto de fin del horizonte siendo visible en el mar. |
| 108° | Crepúsculo astronómico: el punto donde el sol deja de ser la fuente de toda iluminación. |

Valores comunes de ángulo `zenith`

`utcOffset`  
Especificado en horas. El `utcOffset` es ignorado, si `returnFormat` es `SUNFUNCS_RET_TIMESTAMP`.

## Valores devueltos

Devuelve la hora de puesta del sol en el `returnFormat` especificado o `false` si ocurre un error. Una razón posible del fallo es que el sol no se pone, lo cual ocurre dentro de los círculos polares durante parte del año.

## Errores/Excepciones

Cada llamada a una función de fecha/hora generará un diagnóstico de tipo `E_WARNING` si la zona horaria no es válida. Ver también `date_default_timezone_set`

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Esta función ha sido marcada como obsoleta en favor de `date_sun_info`. |
| 8.0.0 | `latitude`, `longitude`, `zenith` y `utcOffset` ahora son nullable. |

## Ejemplos

Ejemplo con `date_sunset`

```
<?php

     /* Calcula la hora de puesta del sol para Lisboa, Portugal
Latitud: 38.4 Norte
Longitud: 9 Oeste
Zenith ~= 90
offset:1 GMT
*/

echo date("D M d Y"). ', hora de puesta del sol : ' .date_sunset(time(), SUNFUNCS_RET_STRING, 38.4, -9, 90, 1);

    
```php

Resultado del ejemplo anterior es similar a:

    Deprecated: Constant SUNFUNCS_RET_STRING is deprecated in script on line 10
    Deprecated: Function date_sunset() is deprecated since 8.1, use date_sun_info() instead in script on line 10
    Mon Dec 20 2004, sunset time : 18:13

Sin puesta de sol

```
<?php
$solstice = strtotime('2017-12-21');
var_dump(date_sunset($solstice, SUNFUNCS_RET_STRING, 69.245833, -53.537222));

    
```php

El ejemplo anterior mostrará:

    Deprecated: Constant SUNFUNCS_RET_STRING is deprecated in script on line 3
    Deprecated: Function date_sunset() is deprecated since 8.1, use date_sun_info() instead in script on line 3
    bool(false)

## Véase también

`date_sun_info`
