---
title: geoip_region_name_by_code
description: Devuelve el nombre de la región para un país y un código de región
source_url: https://www.php.net/manual/es/function.geoip-region-name-by-code.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-region-name-by-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26260
---

geoip_region_name_by_code

Devuelve el nombre de la región para un país y un código de región

## Descripción

```php
geoip_region_name_by_code(string $country_code, string $region_code): string
```php

`geoip_region_name_by_code` devuelve el nombre de la región correspondiente a un par país y región.

En los Estados Unidos de América, la región corresponde a la abreviatura de dos letras del estado. En Canadá, esta región corresponde a la abreviatura de la provincia o del territorio, tal como lo asigna Correos de Canadá.

Para el resto del mundo, GeoIP utiliza los códigos FIPS 10-4 para representar las regiones. Se puede verificar el sitio <http://www.maxmind.com/app/fips10_4> para obtener una lista detallada de los códigos FIPS 10-4.

Esta función está siempre disponible si se utiliza la versión 1.4.1 o superior de la biblioteca GeoIP. Los datos se obtienen directamente de la biblioteca GeoIP y no de una tabla de referencia.

## Parámetros

`country_code`  
El código del país, en dos letras (véase `geoip_country_code_by_name`)

`region_code`  
El código de la región en dos letras (véase `geoip_region_by_name`)

## Valores devueltos

Devuelve el nombre de la región en caso de éxito, o `false` si el país, la región o la combinación de ambos no se encuentra.

## Ejemplos

Ejemplo con `geoip_region_name_by_code` para EE.UU. y Canadá

Este script mostrará el nombre de la región para la región QC en CA.

```
<?php
$region = geoip_region_name_by_code('CA', 'QC');
if ($region) {
    echo 'Nombre de la región CA/QC: ' . $region;
}
?>

    
```php

El ejemplo anterior mostrará:

    Nombre de la región CA/QC: Quebec

Ejemplo con `geoip_region_name_by_code` utilizando los códigos FIPS

Este script mostrará el nombre de la región para la región 01 en JP (Japón).

```
<?php
$region = geoip_region_name_by_code('JP', '01');
if ($region) {
    echo 'Nombre de la región JP/01: ' . $region;
}
?>

    
```php

El ejemplo anterior mostrará:

    Nombre de la región JP/01: Aichi
