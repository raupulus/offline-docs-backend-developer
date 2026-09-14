---
title: DateTimeZone::getLocation
description: Devuelve las informaciones geográficas de una zona horaria
source_url: https://www.php.net/manual/es/datetimezone.getlocation.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/datetimezone/getlocation.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10850
---

DateTimeZone::getLocation

timezone_location_get

Devuelve las informaciones geográficas de una zona horaria

## Descripción

Estilo orientado a objetos

```php
public DateTimeZone::getLocation(): array
```php

Estilo procedimental

```php
timezone_location_get(DateTimeZone $object): array
```

Devuelve las informaciones geográficas de una zona horaria, incluyendo el código del país, la latitud y longitud, y comentarios.

## Parámetros

`object`  
Solo en estilo procedimental: un objeto `DateTimeZone` retornado por `timezone_open`

## Valores devueltos

Array que contiene las informaciones de localización de la zona horaria o `false` si ocurre un error.

## Ejemplos

Ejemplo con `DateTimeZone::getLocation`

```php
<?php
$tz = new DateTimeZone("Asia/Jakarta");
print_r($tz->getLocation());
print_r(timezone_location_get($tz));

    
```

El ejemplo anterior mostrará:

    Array
    (
        [country_code] => ID
        [latitude] => -6.16667
        [longitude] => 106.8
        [comments] => Java, Sumatra
    )
    Array
    (
        [country_code] => ID
        [latitude] => -6.16667
        [longitude] => 106.8
        [comments] => Java, Sumatra
    )

Los elementos `country_code` contienen el código de país ISO 3166-1 alfa-2 correspondiente a cada entrada. Los elementos `latitude` y `longitude` indican las coordenadas de la ciudad nombrada en el identificador de zona horaria, y `comments` incluye (cuando no es `false`) una indicación de la región del país a la que se aplica dicha zona horaria. Esta información es adecuada para ser presentada a usuarios finales.

## Véase también

DateTimeZone::listIdentifiers

para obtener una lista completa o parcial de todos los identificadores de zonas horarias soportadas
