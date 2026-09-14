---
title: geoip_database_info
description: Recupera la información de la base de datos GeoIP
source_url: https://www.php.net/manual/es/function.geoip-database-info.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-database-info.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26150
---

geoip_database_info

Recupera la información de la base de datos GeoIP

## Descripción

```php
geoip_database_info([int $database]): string
```php

La función `geoip_database_info` devuelve la versión de la base de datos GeoIP tal como se define en el fichero binario.

Si esta función se llama sin argumento, devuelve la versión de la `GeoIP Free Country Edition`.

## Parámetros

`database`  
El tipo de base de datos, como entero. Se pueden utilizar [diversas constantes](#geoip.constants) definidas con esta extensión (ie: GEOIP\_\*\_EDITION).

## Valores devueltos

Devuelve la versión correspondiente de la base de datos, o `null` si ocurre un error.

## Ejemplos

Ejemplo con `geoip_database_info`

Este ejemplo muestra la información contenida en la base de datos.

```
<?php
print geoip_database_info(GEOIP_COUNTRY_EDITION);
?>

   
```php

El ejemplo anterior mostrará:

    GEO-106FREE 20060801 Build 1 Copyright (c) 2006 MaxMind LLC All Rights Reserved
