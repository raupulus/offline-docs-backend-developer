---
title: radius_put_addr
description: Adjunta una dirección IP como atributo
source_url: https://www.php.net/manual/es/function.radius-put-addr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/functions/radius-put-addr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67690
---

radius_put_addr

Adjunta una dirección IP como atributo

## Descripción

```php
radius_put_addr(resource $radius_handle, int $type, string $addr, [int $options], [int $tag]): bool
```php

Adjunta una dirección IP a la solicitud RADIUS actual.

> [!NOTE]
> Una petición debe ser creada mediante la función `radius_create_request` antes de que esta función pueda ser llamada.

## Parámetros

`radius_handle`  
El recurso RADIUS.

`type`  
El tipo de atributo.

`addr`  
Una dirección IPv4; por ejemplo `10.0.0.1`.

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
