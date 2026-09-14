---
title: radius_cvt_addr
description: Convierte datos brutos en dirección IP
source_url: https://www.php.net/manual/es/function.radius-cvt-addr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-cvt-addr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67600
---

radius_cvt_addr

Convierte datos brutos en dirección IP

## Descripción

```php
radius_cvt_addr(string $data): string
```php

Convierte datos brutos en dirección IP

## Parámetros

`data`  
Datos de entrada

## Valores devueltos

Devuelve la dirección IP.

## Ejemplos

Ejemplo con `radius_cvt_addr`

```
<?php
while ($resa = radius_get_attr($res)) {

    if (!is_array($resa)) {
        printf ("Error al recuperar los atributos: %s\n",  radius_strerror($res));
        exit;
    }

    $attr = $resa['attr'];
    $data = $resa['data'];

    switch ($attr) {

    case RADIUS_FRAMED_IP_ADDRESS:
        $ip = radius_cvt_addr($data);
        echo "IP: $ip<br>\n";
        break;

    case RADIUS_FRAMED_IP_NETMASK:
        $mask = radius_cvt_addr($data);
        echo "MÁSCARA: $mask<br>\n";
        break;
    }
}
?>

   
```php

## Véase también

radius_cvt_int

radius_cvt_string
