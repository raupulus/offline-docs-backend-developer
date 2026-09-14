---
title: radius_get_tagged_attr_data
description: Extrae los datos de un atributo
source_url: https://www.php.net/manual/es/function.radius-get-tagged-attr-data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-get-tagged-attr-data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67660
---

radius_get_tagged_attr_data

Extrae los datos de un atributo

## Descripción

```php
radius_get_tagged_attr_data(string $data): string
```php

Si un atributo que contiene un tag ha sido devuelto por la función `radius_get_attr`, `radius_get_tagged_attr_data` devuelve los datos desde este atributo.

## Parámetros

`data`  
El atributo que contiene un tag a decodificar.

## Valores devueltos

Devuelve los datos del atributo o `false` si ocurre un error.

## Ejemplos

Ejemplo con `radius_get_tagged_attr_data`

```
<?php
while ($resa = radius_get_attr($res)) {
    if (!is_array($resa)) {
        printf ("Error al recuperar el atributo: %s\n",  radius_strerror($res));
        exit;
    }

    $attr = $resa['attr'];
    $data = $resa['data'];

    $tag = radius_get_tagged_attr_tag($data);
    $value = radius_get_tagged_attr_data($data);

    printf("Recuperación del atributo que contiene el tag %d y el valor %s\n", $tag, $value);
}
?>

   
```php

## Véase también

radius_get_attr

radius_get_tagged_attr_tag
