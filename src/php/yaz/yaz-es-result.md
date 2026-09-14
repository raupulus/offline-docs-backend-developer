---
title: yaz_es_result
description: Resulados de Servicios Extendidos de Inspección
source_url: https://www.php.net/manual/es/function.yaz-es-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-es-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 14af302c9
order: 107830
---

yaz_es_result

Resulados de Servicios Extendidos de Inspección

## Descripción

```php
yaz_es_result(resource $id): array
```php

Esta función inspecciona el último resultado de servicio extendido retornado de un servidor. Un servicio extendido es iniciado por cualquier `yaz_item_order` o `yaz_es`.

## Parámetros

`id`  
El resultado de conexión retornado por `yaz_connect`.

## Valores devueltos

Devuelve un arreglo con `targetReference` elemento para la referencia en la operación del servicio extendido (generado y retornado del servidor).

## Véase también

`yaz_es`
