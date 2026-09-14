---
title: geoip_setup_custom_directory
description: Define un directorio personalizado para la base de datos GeoIP
source_url: https://www.php.net/manual/es/function.geoip-setup-custom-directory.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-setup-custom-directory.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26270
---

geoip_setup_custom_directory

Define un directorio personalizado para la base de datos GeoIP

## Descripción

```php
geoip_setup_custom_directory(string $path): void
```php

La función `geoip_setup_custom_directory` modificará el directorio por omisión de la base de datos GeoIP. Esto es equivalente a modificar la opción de configuración [geoip.custom_directory](#ini.geoip.custom-directory).

## Parámetros

`path`  
La ruta de acceso completa donde se encuentra la base de datos GeoIP en el disco.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo con `geoip_setup_custom_directory`

Este ejemplo modificará la ruta de acceso por omisión hacia la base de datos GeoIP.

```
<?php

geoip_setup_custom_directory('/un/otro/ruta');

print geoip_db_filename(GEOIP_COUNTRY_EDITION);

?>

   
```php

El ejemplo anterior mostrará:

    /un/otro/ruta/GeoIP.dat
