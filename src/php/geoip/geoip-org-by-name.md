---
title: geoip_org_by_name
description: Recupera el nombre de la organización
source_url: https://www.php.net/manual/es/function.geoip-org-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-org-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26230
---

geoip_org_by_name

Recupera el nombre de la organización

## Descripción

```php
geoip_org_by_name(string $hostname): string
```php

La función `geoip_org_by_name` devuelve el nombre de la organización a la que se asigna la dirección IP.

Esta función está actualmente disponible únicamente para los usuarios que han adquirido una licencia comercial `GeoIP Organization`, `ISP` o `AS Edition`. Se emitirá una alerta si la base de datos no puede ser encontrada.

## Parámetros

`hostname`  
El nombre del host o la dirección IP

## Valores devueltos

Devuelve el nombre de la organización en caso de éxito, o `false` si la dirección no pudo ser encontrada en la base de datos.

## Ejemplos

Ejemplo con `geoip_org_by_name`

Este ejemplo muestra el nombre de la organización para el host example.com.

```
<?php
$org = geoip_org_by_name('www.example.com');
if ($org) {
    echo 'Nombre de la organización : ' . $org;
}
?>

   
```php

El ejemplo anterior mostrará:

    Nombre de la organización : ICANN c/o Internet Assigned Numbers Authority
