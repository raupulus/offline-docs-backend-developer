---
title: radius_put_vendor_int
description: Adjunta un atributo entero a un proveedor específico
source_url: https://www.php.net/manual/es/function.radius-put-vendor-int.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-put-vendor-int.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67750
---

radius_put_vendor_int

Adjunta un atributo entero a un proveedor específico

## Descripción

```php
radius_put_vendor_int(resource $radius_handle, int $vendor, int $type, int $value, [int $options], [int $tag]): bool
```php

Adjunta un atributo específico al proveedor en la petición RADIUS actual.

## Parámetros

`radius_handle`  
El recurso RADIUS.

`vendor`  
El identificador del proveedor.

`type`  
El tipo de atributo.

`value`  
El valor del atributo.

`options`  
Una máscara de opciones de atributo. Las opciones disponibles incluyen [`RADIUS_OPTION_TAGGED`](#constant.radius-option-tagged) y [`RADIUS_OPTION_SALT`](#constant.radius-option-salt).

`tag`  
La etiqueta del atributo. Este parámetro es ignorado mientras que la opción [`RADIUS_OPTION_TAGGED`](#constant.radius-option-tagged) esté definida.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión           | Descripción                                      |
|-------------------|--------------------------------------------------|
| PECL radius 1.3.0 | Se han añadido los argumentos `options` y `tag`. |

## Véase también

radius_put_vendor_string
