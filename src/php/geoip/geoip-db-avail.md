---
title: geoip_db_avail
description: Verifica si la base de datos GeoIP está disponible
source_url: https://www.php.net/manual/es/function.geoip-db-avail.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-db-avail.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26160
---

geoip_db_avail

Verifica si la base de datos GeoIP está disponible

## Descripción

```php
geoip_db_avail(int $database): bool
```php

La función `geoip_db_avail` verifica si la base de datos correspondiente está disponible y puede ser abierta en el disco.

La función no indica si el fichero es una base de datos válida, sino únicamente si es legible.

## Parámetros

`database`  
El tipo de base de datos, en forma de un `int`. Se pueden utilizar diversas [constantes](#geoip.constants), definidas con esta extensión (ie: GEOIP\_\*\_EDITION).

## Valores devueltos

Devuelve `true` si la base de datos existe, `false` si no se encuentra, o `null` si ocurre un error.

## Ejemplos

Ejemplo con `geoip_db_avail`

Esto mostrará la versión de la base de datos actual.

```
<?php

if (geoip_db_avail(GEOIP_COUNTRY_EDITION))
    print geoip_database_info(GEOIP_COUNTRY_EDITION);
?>

   
```php

El ejemplo anterior mostrará:

    GEO-106FREE 20080801 Build 1 Copyright (c) 2006 MaxMind LLC All Rights Reserved
