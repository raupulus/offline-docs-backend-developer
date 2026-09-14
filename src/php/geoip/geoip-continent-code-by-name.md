---
title: geoip_continent_code_by_name
description: Lee el código de continente de una IP
source_url: https://www.php.net/manual/es/function.geoip-continent-code-by-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/geoip/functions/geoip-continent-code-by-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: geoip
translation_status: ready
translation_reviewed: false
translation_revision: 9d2fd3237
order: 26110
---

geoip_continent_code_by_name

Lee el código de continente de una IP

## Descripción

```php
geoip_continent_code_by_name(string $hostname): string
```php

`geoip_continent_code_by_name` devuelve el código de dos letras del continente correspondiente a un nombre de host o una dirección IP.

## Parámetros

`hostname`  
El nombre de host o la dirección IP que se está estudiando.

## Valores devueltos

Devuelve el código de dos letras del nombre del continente, en caso de éxito, y `false` si la dirección no ha podido ser encontrada en la base.

| Código | Nombre del continente |
|--------|-----------------------|
| `AF`   | África                |
| `AN`   | Antártida             |
| `AS`   | Asia                  |
| `EU`   | Europa                |
| `NA`   | América del Norte     |
| `OC`   | Oceanía               |
| `SA`   | América del Sur       |

Códigos de continente

## Ejemplos

Ejemplo con `geoip_continent_code_by_name`

Este script mostrará el continente del host example.com.

```
<?php
$continent = geoip_continent_code_by_name('www.example.com');
if ($continent) {
    echo 'Este host está situado en: ' . $continent;
}
?>

   
```php

El ejemplo anterior mostrará:

    Este host está situado en: NA

## Véase también

geoip_country_code_by_name
