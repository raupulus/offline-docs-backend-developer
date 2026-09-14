---
title: gethostbynamel
description: Devuelve la lista de direcciones IPv4 correspondientes a un host
source_url: https://www.php.net/manual/es/function.gethostbynamel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/gethostbynamel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56300
---

gethostbynamel

Devuelve la lista de direcciones IPv4 correspondientes a un host

## Descripción

```php
gethostbynamel(string $hostname): array
```php

Devuelve la lista de direcciones IPv4 correspondientes al host `hostname`.

## Parámetros

`hostname`  
El nombre del host.

## Valores devueltos

Devuelve un array de direcciones IPv4, o `false` si `hostname` no pudo ser resuelto.

## Ejemplos

Ejemplo con `gethostbynamel`

```
<?php
$hosts = gethostbynamel('www.example.com');
print_r($hosts);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => 192.0.34.166
    )

## Véase también

`gethostbyname`, `gethostbyaddr`, `checkdnsrr`, `getmxrr`, La página del manual `named(8)`
