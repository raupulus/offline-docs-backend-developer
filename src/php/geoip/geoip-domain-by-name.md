---
title: geoip_domain_by_name
description: Recupera el segundo nivel del nombre de dominio
source_url: https://www.php.net/manual/es/function.geoip-domain-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-domain-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26190
---

geoip_domain_by_name

Recupera el segundo nivel del nombre de dominio

## Descripción

```php
geoip_domain_by_name(string $hostname): string
```php

La función `geoip_domain_by_name` devuelve el segundo nivel del dominio asociado con un nombre de host o la dirección IP.

Esta función está actualmente disponible solo para los usuarios que han comprado una edición comercial de GeoIP Domain. Se emitirá una alerta si no se puede encontrar la base de datos correcta.

## Parámetros

`hostname`  
El nombre de host o la dirección IP.

## Valores devueltos

Devuelve el nombre de dominio en caso de éxito, o `false` si la dirección no puede ser encontrada en la base de datos.

## Ejemplos

Ejemplo con `geoip_domain_by_name`

Este ejemplo mostrará el dominio asociado con la IP 61.106.139.1.

```
<?php
$domain = geoip_domain_by_name('61.106.139.1');

if ($domain) {
    echo 'El dominio es: '. $domain;
}

?>

   
```php

El ejemplo anterior mostrará:

    El dominio es: von.co.kr
