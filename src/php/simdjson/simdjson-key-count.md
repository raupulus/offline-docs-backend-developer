---
title: simdjson_key_count
description: Devuelve el valor a un puntero JSON.
source_url: https://www.php.net/manual/es/function.simdjson-key-count.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simdjson/functions/simdjson-key-count.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simdjson
translation_status: ready
translation_reviewed: false
translation_revision: 78cc29837
order: 74310
---

simdjson_key_count

Devuelve el valor a un puntero JSON.

## Descripción

```php
simdjson_key_count(string $json, string $key, [int $depth], [bool $throw_if_uncountable]): int
```php

Cuenta el número de elementos del objeto/array encontrado en el puntero JSON solicitado.

## Parámetros

`json`  
El `string` `json` a consultar.

`key`  
El `string` del puntero JSON.

`depth`  
La profundidad máxima de la estructura a decodificar. El valor debe ser superior a `0`, e inferior o igual a `2147483647`. Aquellos que llamen a esta función deberían utilizar valores razonablemente pequeños, ya que profundidades mayores requieren más espacio de búfer y aumentarán la profundidad de recursión, a diferencia de la implementación actual de `json_decode`.

`throw_if_uncountable`  
Cuando es verdadero, se lanzará una `SimdJsonException` en lugar de devolver 0 cuando el valor apuntado por el JSON no es ni un objeto ni un array.

## Valores devueltos

Devuelve un `int` con el número de elementos del valor en el puntero JSON dado.
