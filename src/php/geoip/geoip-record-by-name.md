---
title: geoip_record_by_name
description: Recupera la información registrada correspondiente al nombre del host
  o a la dirección IP, encontrada en la base de datos GeoIP
source_url: https://www.php.net/manual/es/function.geoip-record-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-record-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26240
---

geoip_record_by_name

Recupera la información registrada correspondiente al nombre del host o a la dirección IP, encontrada en la base de datos GeoIP

## Descripción

```php
geoip_record_by_name(string $hostname): array
```php

La función `geoip_record_by_name` devuelve la información registrada correspondiente al nombre del host o a la dirección IP.

Esta función está disponible para las bases de datos `GeoLite City Edition` y la versión comercial `GeoIP City Edition`. Se emitirá una alerta si la base de datos no ha podido ser encontrada.

Los nombres de las diferentes claves del array asociativo devuelto son los siguientes:

- `"continent_code"` : Código del continente en 2 letras (disponible desde la versión 1.0.4 con libgeoip 1.4.3 o superior)

- `"country_code"` : Las dos letras del código del país (Véase `geoip_country_code_by_name`)

- `"country_code3"` : Código del país en 3 letras (Véase la función `geoip_country_code3_by_name`)

- `"country_name"` : Nombre del país (Véase la función `geoip_country_name_by_name`)

- `"region"` : El código de la región (ej: CA para California)

- `"city"` : La ciudad.

- `"postal_code"` : El código postal, FSA o Zip.

- `"latitude"` : La latitud como `float` firmado.

- `"longitude"` : La longitud como `float` firmado.

- `"dma_code"` : Código de la zona de mercado (Solo para EE.UU. y Canadá)

- `"area_code"` : El código PSTN (ej: 212)

## Parámetros

`hostname`  
El nombre del host o la dirección IP

## Valores devueltos

Devuelve un array asociativo en caso de éxito, o `false` si la dirección no ha podido ser encontrada en la base de datos.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL geoip 1.0.4 | Adición de continent_code con la biblioteca GeoIP 1.4.3 o superior únicamente |
| PECL geoip 1.0.3 | Adición de country_code3 y de country_name |

## Ejemplos

Ejemplo con `geoip_record_by_name`

Este ejemplo muestra el array que contiene el registro del host example.com.

```
<?php
$record = geoip_record_by_name('www.example.com');
if ($record) {
    print_r($record);
}
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [continent_code] => NA
        [country_code] => US
        [country_code3] => USA
        [country_name] => United States
        [region] => CA
        [city] => Marina Del Rey
        [postal_code] =>
        [latitude] => 33.9776992798
        [longitude] => -118.435096741
        [dma_code] => 803
        [area_code] => 310
    )
