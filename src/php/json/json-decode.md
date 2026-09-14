---
title: json_decode
description: Decodifica una cadena JSON
source_url: https://www.php.net/manual/es/function.json-decode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/json/functions/json-decode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: json
translation_status: ready
translation_reviewed: true
translation_revision: 9f2e30a00
order: 42830
---

json_decode

Decodifica una cadena JSON

## Descripción

```php
json_decode(string $json, [bool $associative], [int $depth], [int $flags]): mixed
```php

Recupera una cadena codificada en JSON y la convierte en un valor de PHP.

## Parámetros

`json`  
La `string` `json` a decodificar.

Esta función solo funciona con cadenas codificadas en UTF-8.

> [!NOTE]
> PHP implementa un superconjunto de JSON tal como se especifica en el [RFC 7159](https://datatracker.ietf.org/doc/html/rfc7159) original.

`associative`  
Cuando este parámetro vale `true`, los objetos JSON serán devueltos como arrays asociativos; cuando este parámetro vale `false`, los objetos JSON serán devueltos como objetos. Cuando este parámetro vale `null`, los objetos JSON serán devueltos como arrays asociativos o como objetos, según si la constante `JSON_OBJECT_AS_ARRAY` ha sido definida en el parámetro `flags`.

`depth`  
Profundidad máxima de anidamiento de la estructura en proceso de decodificación. El valor debe ser superior a `0`, e inferior o igual a `2147483647`.

`flags`  
Máscara de bits compuesta por `JSON_BIGINT_AS_STRING`, `JSON_INVALID_UTF8_IGNORE`, `JSON_INVALID_UTF8_SUBSTITUTE`, `JSON_OBJECT_AS_ARRAY`, `JSON_THROW_ON_ERROR`. El comportamiento de estas constantes se describe en la página de las [constantes JSON](#json.constants).

## Valores devueltos

Devuelve el valor codificado en el parámetro `json` en el tipo PHP apropiado. Los valores sin comillas `true`, `false` y `null` son devueltos respectivamente como `true`, `false` y `null`. `null` es devuelto si el parámetro `json` no ha podido ser decodificado o si los datos codificados son más profundos que el límite de anidamiento proporcionado.

## Errores/Excepciones

Si `depth` está fuera del rango permitido, una `ValueError` es lanzada a partir de PHP 8.0.0, mientras que anteriormente se generaba un error de nivel `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | El `flags` `JSON_THROW_ON_ERROR` ha sido añadido. |
| 7.2.0 | El parámetro `associative` ahora es nullable. |
| 7.2.0 | Los `flags` `JSON_INVALID_UTF8_IGNORE`, y `JSON_INVALID_UTF8_SUBSTITUTE` han sido añadidos. |
| 7.1.0 | Una clave JSON vacía ("") puede ser codificada en la propiedad de objeto vacía en lugar de usar una clave con el valor `_empty_`. |

## Ejemplos

Ejemplo con `json_decode`

```
<?php
$json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

var_dump(json_decode($json));
var_dump(json_decode($json, true));

?>

    
```php

El ejemplo anterior mostrará:

    object(stdClass)#1 (5) {
        ["a"] => int(1)
        ["b"] => int(2)
        ["c"] => int(3)
        ["d"] => int(4)
        ["e"] => int(5)
    }

    array(5) {
        ["a"] => int(1)
        ["b"] => int(2)
        ["c"] => int(3)
        ["d"] => int(4)
        ["e"] => int(5)
    }

Acceso a propiedades de objeto inválidas

Acceder a elementos de un objeto que contienen caracteres no permitidos por la convención de nombres de PHP (es decir, el guión) puede realizarse encapsulando el nombre del elemento con corchetes y comillas.

```
<?php

$json = '{"foo-bar": 12345}';

$obj = json_decode($json);
print $obj->{'foo-bar'}; // 12345

?>

    
```php

Errores comunes al usar la función `json_decode`

```
<?php

// Las siguientes cadenas son válidas en JavaScript pero no en JSON

// El nombre y el valor deben estar rodeados de comillas dobles.
// Las comillas simples no son válidas.
$bad_json = "{ 'bar': 'baz' }";
json_decode($bad_json); // null

// El nombre debe estar rodeado de comillas dobles.
$bad_json = '{ bar: "baz" }';
json_decode($bad_json); // null

// La coma final no está permitida.
$bad_json = '{ bar: "baz", }';
json_decode($bad_json); // null

?>

    
```php

Errores con el parámetro `depth`

```
<?php
// Codificación de datos con un nivel máximo de anidamiento de 4 (array -> array -> array -> string)
$json = json_encode(
    array(
        1 => array(
            'English' => array(
                'One',
                'January'
            ),
            'French' => array(
                'Une',
                'Janvier'
            )
        )
    )
);

// Definición de errores
$constants = get_defined_constants(true);
$json_errors = array();
foreach ($constants["json"] as $name => $value) {
 if (!strncmp($name, "JSON_ERROR_", 11)) {
  $json_errors[$value] = $name;
 }
}

$json = json_encode(
    array(
        1 => array(
            'English' => array(
                'One',
                'January'
            ),
            'French' => array(
                'Une',
                'Janvier'
            )
        )
    )
);

// Mostrar errores para diferentes niveles de anidamiento.
var_dump(json_decode($json, true, 4));
echo 'Last error: ', json_last_error_msg(), PHP_EOL, PHP_EOL;

var_dump(json_decode($json, true, 3));
echo 'Last error: ', json_last_error_msg(), PHP_EOL, PHP_EOL;
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
    Last error: No error

    NULL
    Last error: Maximum stack depth exceeded

Ejemplo con `json_decode` y grandes enteros

```
<?php
$json = '{"number": 12345678901234567890}';

var_dump(json_decode($json));
var_dump(json_decode($json, false, 512, JSON_BIGINT_AS_STRING));

?>

    
```php

El ejemplo anterior mostrará:

    object(stdClass)#1 (1) {
      ["number"]=>
      float(1.2345678901235E+19)
    }
    object(stdClass)#1 (1) {
      ["number"]=>
      string(20) "12345678901234567890"
    }

## Notas

> [!NOTE]
> La especificación JSON no forma parte de Javascript sino de un subproyecto de Javascript.

> [!NOTE]
> Si ocurre un error durante la decodificación, la función `json_last_error` (o `json_last_error_msg` con PHP5.5+) podrá ser utilizada para determinar la naturaleza exacta del error.

## Véase también

`json_encode`, `json_last_error`, `json_last_error_msg`
