---
title: radius_cvt_int
description: Convierte datos brutos en entero
source_url: https://www.php.net/manual/es/function.radius-cvt-int.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-cvt-int.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67610
---

radius_cvt_int

Convierte datos brutos en entero

## Descripción

```php
radius_cvt_int(string $data): int
```php

Convierte datos brutos en entero

## Parámetros

`data`  
Datos de entrada.

## Valores devueltos

Devuelve el entero, recuperado desde los datos.

## Ejemplos

Ejemplo con `radius_cvt_int`

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

    case RADIUS_FRAMED_MTU:
        $mtu = radius_cvt_int($data);
        echo "MTU: $mtu<br>\n";
        break;
    }
}
?>

   
```php

## Véase también

radius_cvt_addr

radius_cvt_string
