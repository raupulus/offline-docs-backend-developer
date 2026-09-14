---
title: simdjson_is_valid
description: Verifica si un string JSON es válido
source_url: https://www.php.net/manual/es/function.simdjson-is-valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simdjson/functions/simdjson-is-valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simdjson
translation_status: ready
translation_reviewed: false
translation_revision: 78cc29837
order: 74300
---

simdjson_is_valid

Verifica si un string JSON es válido

## Descripción

```php
simdjson_is_valid(string $json, [int $depth]): bool
```php

Toma un string codificado en JSON y devuelve true si es válido.

## Parámetros

`json`  
El `string` `json` a validar.

Esta función solo funciona con strings codificados en UTF-8.

Esta función valida las entradas que `json_decode` puede decodificar, siempre que sean inferiores a 4 GB de longitud.

`depth`  
La profundidad máxima de la estructura a decodificar. El valor debe ser superior a `0`, e inferior o igual a `2147483647`. Quienes llamen a esta función deberían utilizar valores razonablemente pequeños, ya que profundidades mayores requieren más espacio de búfer y aumentarán la profundidad de recursión, a diferencia de la implementación actual de `json_decode`.

## Valores devueltos

Devuelve `true` si `json` es un string JSON válido, de lo contrario `false`.

## Errores/Excepciones

Si `json` es inválido, se lanza una `SimdJsonException` a partir de PECL simdjson 2.1.0, mientras que anteriormente se lanzaba una `RuntimeException`.

Si `depth` está fuera del rango permitido, se lanza una `SimdJsonValueError` a partir de PECL simdjson 3.0.0, mientras que anteriormente se lanzaba un error de nivel `E_WARNING`.

## Ejemplos

Ejemplos de `simdjson_decode`

```
<?php
$json = '{"a":1,"b":2,"c":3}';
$invalidJson = '{"a":1,"b":2,"c":';

var_dump(simdjson_is_valid($json));
var_dump(simdjson_is_valid($invalidJson));

?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

Errores de `depth`

```
<?php
// Codificar datos con una profundidad máxima de 4
// (array -> array -> array -> string)
$json = json_encode(
    [
        1 => [
            'English' => [
                'One',
                'January'
            ],
            'French' => [
                'Une',
                'Janvier'
            ]
        ]
    ]
);

// Mostrar errores para diferentes profundidades.
var_dump(simdjson_is_valid($json, 4));
var_dump(simdjson_is_valid($json, 3));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Notas

> [!NOTE]
> La especificación JSON no es JavaScript, sino un subconjunto de JavaScript.

> [!NOTE]
> En caso de que la decodificación falle, se lanza una `SimdJsonException` y SimdJsonException::getCode y SimdJsonException::getMessage pueden ser utilizados para determinar la naturaleza exacta del error.

## Véase también

json_encode

json_decode
