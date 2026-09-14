---
title: geoip_asnum_by_name
description: Recupera el ASN (Autonomous System Numbers)
source_url: https://www.php.net/manual/es/function.geoip-asnum-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-asnum-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26100
---

geoip_asnum_by_name

Recupera el ASN (Autonomous System Numbers)

## Descripción

```php
geoip_asnum_by_name(string $hostname): string
```php

La función `geoip_asnum_by_name` recupera el ASN (Autonomous System Numbers) asociado con la dirección IP.

## Parámetros

`hostname`  
El nombre de host o la dirección IP.

## Valores devueltos

Devuelve el ASN en caso de éxito, o `false` si la dirección no puede ser encontrada en la base de datos.

## Ejemplos

Ejemplo con `geoip_asnum_by_name`

Este ejemplo mostrará el ASN para el host www.example.com.

```
<?php
$asn = geoip_asnum_by_name('www.example.com');

if ($asn) {
    echo 'El ASN es: ' . $asn;
}
?>

   
```php

El ejemplo anterior mostrará:

    El ASN es: AS15133 EdgeCast Networks, Inc
