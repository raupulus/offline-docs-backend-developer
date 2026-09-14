---
title: geoip_netspeedcell_by_name
description: Recupera la velocidad de la conexión a Internet
source_url: https://www.php.net/manual/es/function.geoip-netspeedcell-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-netspeedcell-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26220
---

geoip_netspeedcell_by_name

Recupera la velocidad de la conexión a Internet

## Descripción

```php
geoip_netspeedcell_by_name(string $hostname): string
```php

La función `geoip_netspeedcell_by_name` devolverá el tipo de conexión a Internet así como su velocidad, según un nombre de host o una dirección IP.

Esta función solo está disponible al utilizar la versión 1.4.8 de la biblioteca GeoIP, o superiores.

Esta función está actualmente disponible únicamente para los usuarios que han comprado una edición comercial de GeoIP NetSpeedCell. Se emitirá una alerta si no se puede encontrar la base de datos correcta.

El valor devuelto será un string cuyos valores comunes son:

- Cable/DSL

- Dialup

- Cellular

- Corporate

## Parámetros

`hostname`  
El nombre de host, o la dirección IP.

## Valores devueltos

Devuelve la velocidad de la conexión en caso de éxito, o `false` si la dirección no puede ser encontrada en la base de datos.

## Ejemplos

Ejemplo con `geoip_netspeedcell_by_name`

Este ejemplo mostrará la velocidad de la conexión del host example.com.

```
<?php
$netspeed = geoip_netspeedcell_by_name('www.example.com');

if ($netspeed) {
    echo 'El tipo de conexión es: '. $netspeed;
}
?>

   
```php

El ejemplo anterior mostrará:

    El tipo de conexión es: Corporate
