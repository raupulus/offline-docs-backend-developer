---
title: wddx_serialize_value
description: Serializa un solo valor en un paquete WDDX
source_url: https://www.php.net/manual/es/function.wddx-serialize-value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/functions/wddx-serialize-value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: e41806c30
order: 101240
---

wddx_serialize_value

Serializa un solo valor en un paquete WDDX

> [!WARNING]
> Esta función ha sido *ELIMINADA* a partir de PHP 7.4.0.

## Descripción

```php
wddx_serialize_value(mixed $var, [string $comment]): string
```php

Crea un paquete WDDX a partir de un solo valor dado.

## Parámetros

`var`  
El valor a serializar.

`comment`  
Una `string` opcional que contiene un comentario que aparece en el encabezado del paquete.

## Valores devueltos

Devuelve el paquete WDDX, o `false` si ocurre un error.
