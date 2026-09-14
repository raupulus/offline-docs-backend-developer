---
title: geoip_db_filename
description: Devuelve el nombre del fichero que contiene la base de datos GeoIP especificada
source_url: https://www.php.net/manual/es/function.geoip-db-filename.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-db-filename.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26170
---

geoip_db_filename

Devuelve el nombre del fichero que contiene la base de datos GeoIP especificada

## Descripción

```php
geoip_db_filename(int $database): string
```php

La función `geoip_db_filename` devuelve el nombre del fichero que contiene la base de datos GeoIP especificada.

La función no indica si el fichero existe o no en el disco, sino únicamente el lugar en el que la biblioteca busca la base de datos.

## Parámetros

`database`  
El tipo de base de datos, en forma de un `int`. Se pueden utilizar diversas [constantes](#geoip.constants), definidas con esta extensión (ie: GEOIP\_\*\_EDITION).

## Valores devueltos

Devuelve el nombre del fichero de la base de datos correspondiente, o `null` si ocurre un error.

## Ejemplos

Ejemplo con `geoip_db_filename`

Esto mostrará el nombre del fichero correspondiente a la base de datos.

```
<?php

print geoip_db_filename(GEOIP_COUNTRY_EDITION);

?>

   
```php

El ejemplo anterior mostrará:

    /usr/share/GeoIP/GeoIP.dat
