---
title: geoip_id_by_name
description: Recupera el tipo de conexión a Internet
source_url: https://www.php.net/manual/es/function.geoip-id-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-id-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26200
---

geoip_id_by_name

Recupera el tipo de conexión a Internet

## Descripción

```php
geoip_id_by_name(string $hostname): int
```php

La función `geoip_id_by_name` devuelve el tipo de conexión a Internet correspondiente al nombre del host o a la dirección IP.

El valor devuelto es de tipo numérico y puede ser comparado con las siguientes constantes:

- GEOIP_UNKNOWN_SPEED

- GEOIP_DIALUP_SPEED

- GEOIP_CABLEDSL_SPEED

- GEOIP_CORPORATE_SPEED

## Parámetros

`hostname`  
El nombre del host o la dirección IP cuyo tipo de conexión debe ser examinado.

## Valores devueltos

Devuelve el tipo de conexión.

## Ejemplos

Ejemplo con `geoip_id_by_name`

Este ejemplo muestra el tipo de conexión del host example.com.

```
<?php
$netspeed = geoip_id_by_name('www.example.com');

echo 'La conexión es del tipo ';

switch ($netspeed) {
    case GEOIP_DIALUP_SPEED:
        echo 'dial-up';
        break;
    case GEOIP_CABLEDSL_SPEED:
        echo 'cable o DSL';
        break;
    case GEOIP_CORPORATE_SPEED:
        echo 'corporate';
        break;
    case GEOIP_UNKNOWN_SPEED:
    default:
        echo 'desconocido';
}
?>

   
```php

El ejemplo anterior mostrará:

    La conexión es del tipo corporate
