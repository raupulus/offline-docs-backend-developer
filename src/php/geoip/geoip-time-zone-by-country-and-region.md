---
title: geoip_time_zone_by_country_and_region
description: Devuelve la zona horaria de ciertos países y regiones del mundo
source_url: https://www.php.net/manual/es/function.geoip-time-zone-by-country-and-region.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-time-zone-by-country-and-region.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26280
---

geoip_time_zone_by_country_and_region

Devuelve la zona horaria de ciertos países y regiones del mundo

## Descripción

```php
geoip_time_zone_by_country_and_region(string $country_code, [string $region_code]): string
```php

`geoip_time_zone_by_country_and_region` devuelve la zona horaria correspondiente a un país y una región.

En los Estados Unidos de América, la región corresponde a la abreviatura de dos letras del estado. En Canadá, esta región corresponde a la abreviatura de la provincia o del territorio, tal como lo asigna Correos de Canadá.

Para el resto del mundo, GeoIP utiliza los códigos FIPS 10-4 para representar las regiones. Se puede verificar el sitio <http://www.maxmind.com/app/fips10_4> para una lista detallada de los códigos FIPS 10-4.

Esta función está siempre disponible si se utiliza GeoIP Library versión 1.4.1 o más reciente. Los datos provienen directamente de GeoIP Library y no de una tabla de referencia.

## Parámetros

`country_code`  
El código del país, en dos letras (véase `geoip_country_code_by_name`)

`region_code`  
El código de región en dos letras (véase `geoip_region_by_name`)

## Valores devueltos

Devuelve la zona horaria en caso de éxito, y `false` si el país, la región o la combinación de ambos no se encuentra.

## Ejemplos

Ejemplo con `geoip_time_zone_by_country_and_region` para EE.UU. y Canadá

Este script mostrará la zona horaria de Quebec, Canadá.

```
<?php
$timezone = geoip_time_zone_by_country_and_region('CA', 'QC');
if ($timezone) {
    echo 'Zona horaria de CA/QC : ' . $timezone;
}
?>

    
```php

El ejemplo anterior mostrará:

    Zona horaria de CA/QC : America/Montreal

Ejemplo con `geoip_time_zone_by_country_and_region` y los códigos FIPS

Este script mostrará la zona horaria de Japón, región 01 (Aichi).

```
<?php
$timezone = geoip_time_zone_by_country_and_region('JP', '01');
if ($timezone) {
    echo 'Zona horaria de JP/01 : ' . $timezone;
}
?>

    
```php

El ejemplo anterior mostrará:

    Zona horaria de JP/01 : Asia/Tokyo
