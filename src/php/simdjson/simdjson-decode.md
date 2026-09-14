---
title: simdjson_decode
description: Decodifica una cadena JSON
source_url: https://www.php.net/manual/es/function.simdjson-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/simdjson/functions/simdjson-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: simdjson
translation_status: ready
translation_reviewed: false
translation_revision: 78cc29837
order: 74290
---

simdjson_decode

Decodifica una cadena JSON

## Descripción

```php
simdjson_decode(string $json, [bool $associative], [int $depth]): mixed
```php

Toma una cadena codificada en JSON y la convierte en un valor PHP. Esto utiliza una Instrucción Simultánea más Rápida, Datos Múltiples (Simultaneous Instruction, Multiple Data - SIMD) que `json_decode` cuando es soportada por la arquitectura del ordenador.

## Parámetros

`json`  
El `string` `json` a decodificar.

Esta función solo funciona con cadenas codificadas en UTF-8.

Esta función analiza las entradas válidas que `json_decode` puede decodificar, siempre que sean inferiores a 4 GB de longitud.

`associative`  
Cuando `true`, los objetos JSON serán devueltos como `array` asociativos; cuando sean `false`, los objetos JSON serán devueltos como `object`s.

`depth`  
La profundidad máxima de la estructura a decodificar. El valor debe ser superior a `0`, e inferior o igual a `2147483647`. Aquellos que llamen a esta función deberían utilizar valores razonablemente pequeños, ya que profundidades mayores requieren más espacio de búfer y aumentarán la profundidad de recursión, a diferencia de la implementación actual de `json_decode`.

## Valores devueltos

Devuelve el valor codificado en `json` en el tipo PHP apropiado. Los valores `true`, `false` y `null` son devueltos respectivamente como `true`, `false` y `null`.

## Errores/Excepciones

Si `json` es inválido, una `SimdJsonException` es lanzada a partir de PECL simdjson 2.1.0, mientras que anteriormente, una `RuntimeException` era lanzada.

Si `depth` está fuera del rango permitido, una `SimdJsonValueError` es lanzada a partir de PECL simdjson 3.0.0, mientras que anteriormente, un error de nivel `E_WARNING` era lanzado.

## Ejemplos

Ejemplos de `simdjson_decode`

```
<?php
$json = '{"a":1,"b":2,"c":3}';

var_dump(simdjson_decode($json));
var_dump(simdjson_decode($json, true));

?>

    
```php

El ejemplo anterior mostrará:

    object(stdClass)#1 (3) {
      ["a"]=>
      int(1)
      ["b"]=>
      int(2)
      ["c"]=>
      int(3)
    }
    array(3) {
      ["a"]=>
      int(1)
      ["b"]=>
      int(2)
      ["c"]=>
      int(3)
    }

Acceder a propiedades de objeto no válidas

Acceder a elementos en un objeto que contienen caracteres no permitidos por la convención de nomenclatura de PHP (por ejemplo, el guion) puede ser logrado encapsulando el nombre del elemento entre llaves y comillas.

```
<?php

$json = '{"foo-bar": 12345}';

$obj = simdjson_decode($json);
print $obj->{'foo-bar'}; // 12345

?>

    
```php

Errores comunes al usar `simdjson_decode`

```
<?php

// las siguientes cadenas son válidas en JavaScript pero no en JSON

// el nombre y el valor deben estar encerrados entre comillas dobles
// las comillas simples no son válidas
$bad_json = "{ 'bar': 'baz' }";
simdjson_decode($bad_json); // Lanza SimdJsonException

// el nombre debe estar encerrado entre comillas dobles
$bad_json = '{ bar: "baz" }';
simdjson_decode($bad_json); // Lanza SimdJsonException

// las comas finales no están permitidas
$bad_json = '{ bar: "baz", }';
simdjson_decode($bad_json); // Lanza SimdJsonException

?>

    
```php

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
var_dump(simdjson_decode($json, true, 4));
try {
    var_dump(simdjson_decode($json, true, 3));
} catch (SimdJsonException $e) {
     echo "Capturado: ", $e->getMessage(), "\n";
}
?>

    
```php

El ejemplo anterior mostrará:

    array(1) {
      [1]=>
      array(2) {
        ["English"]=>
        array(2) {
          [0]=>
          string(3) "One"
          [1]=>
          string(7) "January"
        }
        ["French"]=>
        array(2) {
          [0]=>
          string(3) "Une"
          [1]=>
          string(7) "Janvier"
        }
      }
    }
    Capturado: El documento JSON era demasiado profundo (demasiados objetos y arrays anidados)

`simdjson_decode` de grandes enteros

```
<?php
$json = '{"number": 12345678901234567890}';

var_dump(simdjson_decode($json));

?>

    
```php

El ejemplo anterior mostrará:

    object(stdClass)#1 (1) {
      ["number"]=>
      float(1.2345678901235E+19)
    }

## Notas

> [!NOTE]
> La especificación JSON no es JavaScript, sino un subconjunto de JavaScript.

> [!NOTE]
> En el caso de que la decodificación falle, una `SimdJsonException` es lanzada y SimdJsonException::getCode y SimdJsonException::getMessage pueden ser utilizados para determinar la naturaleza exacta del error.

## Véase también

json_encode

json_decode
