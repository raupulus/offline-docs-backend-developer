---
title: radius_get_tagged_attr_tag
description: Extrae la etiqueta desde un atributo
source_url: https://www.php.net/manual/es/function.radius-get-tagged-attr-tag.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-get-tagged-attr-tag.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67670
---

radius_get_tagged_attr_tag

Extrae la etiqueta desde un atributo

## Descripción

```php
radius_get_tagged_attr_tag(string $data): int
```php

Si un atributo que contiene una etiqueta ha sido devuelto por la función `radius_get_attr`, `radius_get_tagged_attr_data` va devolver la etiqueta desde el atributo.

## Parámetros

`data`  
El atributo a decodificar.

## Valores devueltos

Devuelve la etiqueta desde el atributo o `false` si ocurre un error.

## Ejemplos

Ejemplo con `radius_get_tagged_attr_tag`

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

    printf("Recuperación del atributo conteniendo la etiqueta %d y el valor %s\n", $tag, $value);
}
?>

   
```php

## Véase también

radius_get_attr

radius_get_tagged_attr_data
