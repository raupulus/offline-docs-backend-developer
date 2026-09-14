---
title: geoip_country_code3_by_name
description: Recupera las tres letras del código del país
source_url: https://www.php.net/manual/es/function.geoip-country-code3-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-country-code3-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26130
---

geoip_country_code3_by_name

Recupera las tres letras del código del país

## Descripción

```php
geoip_country_code3_by_name(string $hostname): string
```php

La función `geoip_country_code3_by_name` devuelve las tres letras del código del país correspondiente al nombre del host o a la dirección IP.

## Parámetros

`hostname`  
El nombre del host o la dirección IP

## Valores devueltos

Devuelve las tres letras del código del país en caso de éxito, o `false` si la dirección no pudo ser encontrada en la base de datos.

## Ejemplos

Ejemplo con `geoip_country_code3_by_name`

Este ejemplo muestra dónde está localizado el host example.com.

```
<?php
$country = geoip_country_code3_by_name('www.example.com');
if ($country) {
    echo 'Localización de este host: ' . $country;
}
?>

   
```php

El ejemplo anterior mostrará:

    Localización de este host: USA

## Véase también

geoip_country_code_by_name

geoip_country_name_by_name
