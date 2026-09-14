---
title: geoip_isp_by_name
description: Recupera el nombre del proveedor de servicios de Internet
source_url: https://www.php.net/manual/es/function.geoip-isp-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-isp-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26210
---

geoip_isp_by_name

Recupera el nombre del proveedor de servicios de Internet

## Descripción

```php
geoip_isp_by_name(string $hostname): string
```php

La función `geoip_isp_by_name` devuelve el nombre del ISP al que está asignada la IP.

Esta función está actualmente disponible solo para los usuarios que han adquirido una edición comercial de GeoIP ISP. Se emitirá una advertencia si la base de datos no puede ser localizada.

## Parámetros

`hostname`  
El nombre del host o la dirección IP.

## Valores devueltos

Devuelve el nombre del ISP en caso de éxito, o `false` si la dirección no puede ser encontrada en la base de datos.

## Ejemplos

Ejemplo con `geoip_isp_by_name`

Esto mostrará el nombre del ISP para el host example.com.

```
<?php
$isp = geoip_isp_by_name('www.example.com');
if ($isp) {
    echo 'La IP del host proviene del ISP: ' . $isp;
}
?>

   
```php

El ejemplo anterior mostrará:

    La IP del host proviene del ISP: ICANN c/o Internet Assigned Numbers Authority
