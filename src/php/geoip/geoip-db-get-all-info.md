---
title: geoip_db_get_all_info
description: Devuelve información detallada sobre todos los tipos de bases de datos
  GeoIP
source_url: https://www.php.net/manual/es/function.geoip-db-get-all-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-db-get-all-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26180
---

geoip_db_get_all_info

Devuelve información detallada sobre todos los tipos de bases de datos GeoIP

## Descripción

```php
geoip_db_get_all_info(): array
```php

La función `geoip_db_get_all_info` devuelve información detallada, en forma de un array multidimensional, sobre todos los tipos de bases de datos GeoIP.

Esta función está disponible incluso si no se ha instalado ninguna base de datos. Simplemente listará las bases de datos como no disponibles.

Los nombres de las diferentes claves del array asociativo devuelto son los siguientes:

- `"available"` : Booleano, indica si la base de datos está disponible (ver la función `geoip_db_avail`)

- `"description"` : La descripción de la base de datos

- `"filename"` : El nombre del fichero que contiene la base de datos en el disco (ver la función `geoip_db_filename`)

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array asociativo.

## Ejemplos

Ejemplo con `geoip_db_get_all_info`

Esto mostrará un array que contiene toda la información.

```
<?php
$infos = geoip_db_get_all_info();
if (is_array($infos)) {
    var_dump($infos);
}
?>

   
```php

El ejemplo anterior mostrará:

    array(11) {
      [1]=>
      array(3) {
        ["available"]=>
        bool(true)
        ["description"]=>
        string(21) "GeoIP Country Edition"
        ["filename"]=>
        string(32) "/usr/share/GeoIP/GeoIP.dat"
      }

    [ ... ]

      [11]=>
      array(3) {
        ["available"]=>
        bool(false)
        ["description"]=>
        string(25) "GeoIP Domain Name Edition"
        ["filename"]=>
        string(38) "/usr/share/GeoIP/GeoIPDomain.dat"
      }
    }

Ejemplo con `geoip_db_get_all_info`

Se pueden utilizar diversas constantes como claves para recuperar solo partes de la información.

```
<?php
$infos = geoip_db_get_all_info();
if ($infos[GEOIP_COUNTRY_EDITION]['available']) {
    echo $infos[GEOIP_COUNTRY_EDITION]['description'];
}
?>

   
```php

El ejemplo anterior mostrará:

    GeoIP Country Edition
