---
title: radius_cvt_string
description: Convierte datos brutos en string
source_url: https://www.php.net/manual/es/function.radius-cvt-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-cvt-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67620
---

radius_cvt_string

Convierte datos brutos en string

## Descripción

```php
radius_cvt_string(string $data): string
```php

Convierte datos brutos en string

## Parámetros

`data`  
Datos de entrada

## Valores devueltos

Devuelve el string, recuperado desde los datos.

## Ejemplos

Ejemplo con `radius_cvt_string`

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

    case RADIUS_FILTER_ID:
        $id = radius_cvt_string($data);
        echo "Filtre ID : $id<br>\n";
        break;
    }
}
?>

   
```php

## Véase también

radius_cvt_addr

radius_cvt_int
