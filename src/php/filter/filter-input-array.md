---
title: filter_input_array
description: Obtiene variables externas y opcionalmente las filtra
source_url: https://www.php.net/manual/es/function.filter-input-array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filter/functions/filter-input-array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filter
translation_status: ready
translation_reviewed: false
translation_revision: 53054bf8d
order: 24190
---

filter_input_array

Obtiene variables externas y opcionalmente las filtra

## Descripción

```php
filter_input_array(int $type, [array $options], [bool $add_empty]): array
```php

Esta función es útil para recuperar muchos valores sin necesidad de llamar repetidamente a `filter_input`.

## Parámetros

`type`  
Una de las constantes `INPUT_*`.

> [!WARNING]
> El contenido de la superglobal que se está filtrando es el original "sin procesar" proporcionado por SAPI, antes de cualquier modificación del usuario a la superglobal. Para filtrar una superglobal modificada, utilice `filter_var_array` en su lugar.

## Valores devueltos

En caso de éxito, un `array` que contiene los valores de las variables solicitadas.

En caso de fallo, se devuelve `false`. Excepto si el fallo es que el array de entrada designado por `type` no está poblado, donde se devuelve `null` si se usa el flag `FILTER_NULL_ON_FAILURE`.

Las entradas faltantes del array de entrada se rellenarán en el array devuelto si `add_empty` es `true`. En cuyo caso, las entradas faltantes se establecerán en `null`, a menos que se use el flag `FILTER_NULL_ON_FAILURE`, en cuyo caso será `false`.

Un valor del array devuelto será `false` si el filtro falla, a menos que se use el flag `FILTER_NULL_ON_FAILURE`, en cuyo caso será `null`.

## Notas

> [!NOTE]
> No hay una clave `REQUEST_TIME` en el array `INPUT_SERVER` porque este valor es insertado en `$_SERVER` posteriormente.

## Véase también

filter_input

filter_var

filter_var_array

Filtros de validación

FILTER_VALIDATE\_

\*

Filtros de saneación

FILTER_SANITIZE\_

\*
