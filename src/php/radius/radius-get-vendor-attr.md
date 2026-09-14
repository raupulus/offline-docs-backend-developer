---
title: radius_get_vendor_attr
description: Extrae un atributo específico del proveedor
source_url: https://www.php.net/manual/es/function.radius-get-vendor-attr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-get-vendor-attr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 4047ef2a8
order: 67680
---

radius_get_vendor_attr

Extrae un atributo específico del proveedor

## Descripción

```php
radius_get_vendor_attr(string $data): array
```php

Si `radius_get_attr` devuelve `RADIUS_VENDOR_SPECIFIC`, `radius_get_vendor_attr` puede ser llamado para determinar el proveedor.

## Parámetros

`data`  
Datos de entrada.

## Valores devueltos

Devuelve un array asociativo que contiene el tipo de atributo, el proveedor así como los datos, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `radius_get_vendor_attr`

```
<?php
while ($resa = radius_get_attr($res)) {

    if (!is_array($resa)) {
        printf ("Error al recuperar el atributo: %s\n",  radius_strerror($res));
        exit;
    }

    $attr = $resa['attr'];
    $data = $resa['data'];
    printf("Atributo recuperado :%d %d octetos %s\n", $attr, strlen($data), bin2hex($data));
    if ($attr == RADIUS_VENDOR_SPECIFIC) {

        $resv = radius_get_vendor_attr($data);
        if (is_array($resv)) {
            $vendor = $resv['vendor'];
            $attrv = $resv['attr'];
            $datav = $resv['data'];
            printf("Recuperación del proveedor del atributo :%d %d octetos %s\n", $attrv, strlen($datav), bin2hex($datav));
        }

    }
}
?>

   
```php

## Véase también

radius_get_attr

radius_put_vendor_attr
