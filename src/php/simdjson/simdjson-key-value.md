---
title: simdjson_key_value
description: Decodifica el valor de una cadena JSON situada en el indicador JSON solicitado.
source_url: https://www.php.net/manual/es/function.simdjson-key-value.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simdjson/functions/simdjson-key-value.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simdjson
translation_status: ready
translation_reviewed: false
translation_revision: 78cc29837
order: 74330
---

simdjson_key_value

Decodifica el valor de una cadena JSON situada en el indicador JSON solicitado.

## Descripción

```php
simdjson_key_value(string $json, string $key, [bool $associative], [int $depth]): mixed
```php

Decodifica y devuelve el valor encontrado en el indicador JSON solicitado.

## Parámetros

`json`  
El `json` `string` a interrogar y decodificar.

Esta función solo funciona con cadenas codificadas en UTF-8.

Esta función analiza las entradas válidas que `json_decode` puede decodificar, siempre que sean inferiores a 4 GB de longitud.

`key`  
El `string` del puntero JSON.

`associative`  
Cuando `true` los objetos JSON serán devueltos en forma de `array` asociativos; cuando son `false`, los objetos JSON serán devueltos en forma de `object`s.

`depth`  
La profundidad máxima de la estructura a decodificar. El valor debe ser superior a `0`, e inferior o igual a `2147483647`. Quienes llamen a esta función deberían utilizar valores razonablemente pequeños, ya que profundidades mayores requieren más espacio de búfer y aumentarán la profundidad de recursión, a diferencia de la implementación actual de `json_decode`.

## Valores devueltos

Devuelve la parte del valor codificado en `json` que `key` referencia en el tipo PHP apropiado. Los valores `true`, `false` y `null` son devueltos respectivamente como `true`, `false` y `null`.

## Errores/Excepciones

Si `json` es inválido, una `SimdJsonException` es lanzada a partir de PECL simdjson 2.1.0, mientras que anteriormente, una `RuntimeException` era lanzada.

Si `depth` está fuera del rango permitido, una `SimdJsonValueError` es lanzada a partir de PECL simdjson 3.0.0, mientras que anteriormente, un error de nivel `E_WARNING` era lanzado.

## Véase también

json_encode

simdjson_decode
