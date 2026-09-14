---
title: radius_put_vendor_attr
description: Adjunta un atributo binario a un proveedor específico
source_url: https://www.php.net/manual/es/function.radius-put-vendor-attr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-put-vendor-attr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67740
---

radius_put_vendor_attr

Adjunta un atributo binario a un proveedor específico

## Descripción

```php
radius_put_vendor_attr(resource $radius_handle, int $vendor, int $type, string $value, [int $options], [int $tag]): bool
```php

Adjunta un atributo binario específico al proveedor para la petición RADIUS actual.

> [!NOTE]
> Una petición debe ser creada mediante la función `radius_create_request` antes de que esta función pueda ser llamada.

## Parámetros

`radius_handle`  
El recurso RADIUS.

`vendor`  
El identificador del proveedor.

`type`  
El tipo de atributo.

`value`  
El valor del atributo, que será tratado como un string sin tratar.

`options`  
Una máscara de opciones de atributo. Las opciones disponibles incluyen [`RADIUS_OPTION_TAGGED`](#constant.radius-option-tagged) y [`RADIUS_OPTION_SALT`](#constant.radius-option-salt).

`tag`  
La etiqueta del atributo. Este parámetro es ignorado mientras que la opción [`RADIUS_OPTION_TAGGED`](#constant.radius-option-tagged) esté definida.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión           | Descripción                                       |
|-------------------|---------------------------------------------------|
| PECL radius 1.3.0 | Los parámetros `options` y `tag` fueron añadidos. |

## Ejemplos

Ejemplo con `radius_put_vendor_attr`

```
<?php
if (!radius_put_vendor_attr($res, RADIUS_VENDOR_MICROSOFT, RAD_MICROSOFT_MS_CHAP_CHALLENGE, $challenge)) {
    echo 'Error Radius :' . radius_strerror($res). "\n<br />";
    exit;
}
?>

     
```php

## Véase también

radius_get_vendor_attr
