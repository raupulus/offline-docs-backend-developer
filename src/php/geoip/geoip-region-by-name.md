---
title: geoip_region_by_name
description: Recupera el código del país y la región
source_url: https://www.php.net/manual/es/function.geoip-region-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-region-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26250
---

geoip_region_by_name

Recupera el código del país y la región

## Descripción

```php
geoip_region_by_name(string $hostname): array
```php

La función `geoip_region_by_name` devuelve el país y la región correspondientes al nombre del host o a la dirección IP.

Esta función está actualmente disponible únicamente para los usuarios que han adquirido una licencia comercial `GeoIP Region Edition`. Se emitirá una alerta si la base de datos no ha podido ser encontrada.

Los nombres de las diferentes claves del array devuelto son los siguientes:

- "country_code" : Las dos letras del código del país (Ver la función `geoip_country_code_by_name`)

- "region" : El código de la región (ej: CA para California)

## Parámetros

`hostname`  
El nombre del host o la dirección IP

## Valores devueltos

Devuelve un array asociativo en caso de éxito, o `false` si la dirección no ha podido ser encontrada en la base de datos.

## Ejemplos

Ejemplo con `geoip_region_by_name`

Este ejemplo muestra el array que contiene el código del país y la región del host example.com.

```
<?php
$region = geoip_region_by_name('www.example.com');
if ($region) {
    print_r($region);
}
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [country_code] => US
        [region] => CA
    )
