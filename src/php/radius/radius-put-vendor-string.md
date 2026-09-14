---
title: radius_put_vendor_string
description: Adjunta un atributo en forma de string a un vendedor específico
source_url: https://www.php.net/manual/es/function.radius-put-vendor-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-put-vendor-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67760
---

radius_put_vendor_string

Adjunta un atributo en forma de string a un vendedor específico

## Descripción

```php
radius_put_vendor_string(resource $radius_handle, int $vendor, int $type, string $value, [int $options], [int $tag]): bool
```php

Adjunta un atributo específico al vendedor a la petición actual RADIUS. En general, `radius_put_vendor_attr` es una función más práctica para adjuntar atributos, siendo segura a nivel de bits.

## Parámetros

`radius_handle`  
El recurso RADIUS.

`vendor`  
El identificador del proveedor.

`type`  
El tipo de atributo.

`value`  
El valor del atributo. Este valor es esperado por la biblioteca subyacente como terminado por `null` ; por lo tanto, este parámetro no es seguro a nivel de bits.

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

## Véase también

radius_put_vendor_int
