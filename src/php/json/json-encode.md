---
title: json_encode
description: Retorna la representación JSON de un valor
source_url: https://www.php.net/manual/es/function.json-encode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/json/functions/json-encode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: json
translation_status: ready
translation_reviewed: false
translation_revision: 9f2e30a00
order: 42840
---

json_encode

Retorna la representación JSON de un valor

## Descripción

```php
json_encode(mixed $value, [int $flags], [int $depth]): string
```php

Retorna una cadena de caracteres que contiene la representación JSON del valor `value`. Si el parámetro es un `array` o un `object`, será serializado de manera recursiva.

Si uno de los valores a serializar es un objeto, entonces por defecto solo las propiedades visibles públicamente serán incluidas. Una clase puede implementar JsonSerializable para controlar cómo sus valores son serializados en JSON.

La codificación es afectada por los `flags` proporcionados. Además, la codificación de valores flotantes depende del valor de [serialize_precision](#ini.serialize-precision).

## Parámetros

`value`  
El valor a codificar. Puede ser de cualquier tipo, excepto un `resource`.

Todas las cadenas deben estar codificadas en UTF-8.

> [!NOTE]
> PHP implementa un superconjunto de JSON tal como se especifica en el [RFC 7159](https://datatracker.ietf.org/doc/html/rfc7159) original.

`flags`  
Máscara de bits compuesta por `JSON_FORCE_OBJECT`, `JSON_HEX_QUOT`, `JSON_HEX_TAG`, `JSON_HEX_AMP`, `JSON_HEX_APOS`, `JSON_INVALID_UTF8_IGNORE`, `JSON_INVALID_UTF8_SUBSTITUTE`, `JSON_NUMERIC_CHECK`, `JSON_PARTIAL_OUTPUT_ON_ERROR`, `JSON_PRESERVE_ZERO_FRACTION`, `JSON_PRETTY_PRINT`, `JSON_UNESCAPED_LINE_TERMINATORS`, `JSON_UNESCAPED_SLASHES`, `JSON_UNESCAPED_UNICODE`, `JSON_THROW_ON_ERROR`. El comportamiento de estas constantes se describe en la página de las [constantes JSON](#json.constants).

`depth`  
Define la profundidad máxima. Debe ser superior a cero.

## Valores devueltos

Retorna un JSON codificado como `string` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.3.0 | El `flags` `JSON_THROW_ON_ERROR` fue añadido. |
| 7.2.0 | Los `flags` `JSON_INVALID_UTF8_IGNORE` y `JSON_INVALID_UTF8_SUBSTITUTE` fueron añadidos. |
| 7.1.0 | El `flags` `JSON_UNESCAPED_LINE_TERMINATORS` fue añadido. |
| 7.1.0 | [serialize_precision](#ini.serialize-precision) es utilizado en lugar de [precision](#ini.precision) al codificar valores `float`. |

## Ejemplos

Ejemplo con `json_encode`

```
<?php
$arr = array('a' => 1, 'b' => 2, 'c' => 3, 'd' => 4, 'e' => 5);

echo json_encode($arr);
?>

    
```php

El ejemplo anterior mostrará:

    {"a":1,"b":2,"c":3,"d":4,"e":5}

Ejemplo con `json_encode` mostrando algunos flags en acción

```
<?php
$a = array('<foo>',"'bar'",'"baz"','&blong&', "\xc3\xa9");

echo "Normal : ",  json_encode($a), "\n";
echo "Tags : ",    json_encode($a, JSON_HEX_TAG), "\n";
echo "Apos : ",    json_encode($a, JSON_HEX_APOS), "\n";
echo "Quot : ",    json_encode($a, JSON_HEX_QUOT), "\n";
echo "Amp : ",     json_encode($a, JSON_HEX_AMP), "\n";
echo "Unicode : ", json_encode($a, JSON_UNESCAPED_UNICODE), "\n";
echo "Todas : ",     json_encode($a, JSON_HEX_TAG | JSON_HEX_APOS | JSON_HEX_QUOT | JSON_HEX_AMP | JSON_UNESCAPED_UNICODE), "\n\n";

$b = array();

echo "Array vacío como array : ", json_encode($b), "\n";
echo "Array vacío como objeto : ", json_encode($b, JSON_FORCE_OBJECT), "\n\n";

$c = array(array(1,2,3));

echo "Array no asociativo como array : ", json_encode($c), "\n";
echo "Array no asociativo como objeto : ", json_encode($c, JSON_FORCE_OBJECT), "\n\n";

$d = array('foo' => 'bar', 'baz' => 'long');

echo "Array asociativo mostrado como objeto: ", json_encode($d), "\n";
echo "Array asociativo mostrado como objeto: ", json_encode($d, JSON_FORCE_OBJECT), "\n\n";
?>

    
```php

El ejemplo anterior mostrará:

    Normal : ["<foo>","'bar'","\"baz\"","&blong&","\u00e9"]
    Tags : ["\u003Cfoo\u003E","'bar'","\"baz\"","&blong&","\u00e9"]
    Apos : ["<foo>","\u0027bar\u0027","\"baz\"","&blong&","\u00e9"]
    Quot : ["<foo>","'bar'","\u0022baz\u0022","&blong&","\u00e9"]
    Amp : ["<foo>","'bar'","\"baz\"","\u0026blong\u0026","\u00e9"]
    Unicode : ["<foo>","'bar'","\"baz\"","&blong&","é"]
    Todas : ["\u003Cfoo\u003E","\u0027bar\u0027","\u0022baz\u0022","\u0026blong\u0026","é"]

    Array vacío como array : []
    Array vacío como objeto : {}

    Array no asociativo como array : [[1,2,3]]
    Array no asociativo como objeto : {"0":{"0":1,"1":2,"2":3}}

    Array asociativo mostrado como objeto: {"foo":"bar","baz":"long"}
    Array asociativo mostrado como objeto: {"foo":"bar","baz":"long"}

Ejemplo con la opción JSON_NUMERIC_CHECK

```
<?php
echo "Las cadenas que representan números son convertidas automáticamente a números".PHP_EOL;
$numbers = array('+123123', '-123123', '1.2e3', '0.00001');
var_dump(
 $numbers,
 json_encode($numbers, JSON_NUMERIC_CHECK)
);
echo "Cadenas que contienen números no formateados correctamente".PHP_EOL;
$strings = array('+a33123456789', 'a123');
var_dump(
 $strings,
 json_encode($strings, JSON_NUMERIC_CHECK)
);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Las cadenas que representan números son convertidas automáticamente a números
    array(4) {
      [0]=>
      string(7) "+123123"
      [1]=>
      string(7) "-123123"
      [2]=>
      string(5) "1.2e3"
      [3]=>
      string(7) "0.00001"
    }
    string(28) "[123123,-123123,1200,1.0e-5]"
    Cadenas que contienen números no formateados correctamente
    array(2) {
      [0]=>
      string(13) "+a33123456789"
      [1]=>
      string(4) "a123"
    }
    string(24) "["+a33123456789","a123"]"

Ejemplo con un array secuencial y un array no secuencial

```
<?php
echo "Array secuencial".PHP_EOL;
$sequential = array("foo", "bar", "baz", "blong");
var_dump(
 $sequential,
 json_encode($sequential)
);

echo PHP_EOL."Array no secuencial".PHP_EOL;
$nonsequential = array(1=>"foo", 2=>"bar", 3=>"baz", 4=>"blong");
var_dump(
 $nonsequential,
 json_encode($nonsequential)
);

echo PHP_EOL."Array secuencial con una clave eliminada".PHP_EOL;
unset($sequential[1]);
var_dump(
 $sequential,
 json_encode($sequential)
);
?>

    
```php

El ejemplo anterior mostrará:

    Array secuencial
    array(4) {
      [0]=>
      string(3) "foo"
      [1]=>
      string(3) "bar"
      [2]=>
      string(3) "baz"
      [3]=>
      string(5) "blong"
    }
    string(27) "["foo","bar","baz","blong"]"

    Array no secuencial
    array(4) {
      [1]=>
      string(3) "foo"
      [2]=>
      string(3) "bar"
      [3]=>
      string(3) "baz"
      [4]=>
      string(5) "blong"
    }
    string(43) "{"1":"foo","2":"bar","3":"baz","4":"blong"}"

    Array secuencial con una clave eliminada
    array(3) {
      [0]=>
      string(3) "foo"
      [2]=>
      string(3) "baz"
      [3]=>
      string(5) "blong"
    }
    string(33) "{"0":"foo","2":"baz","3":"blong"}"

Ejemplo con la opción `JSON_PRESERVE_ZERO_FRACTION`

```
<?php
var_dump(json_encode(12.0, JSON_PRESERVE_ZERO_FRACTION));
var_dump(json_encode(12.0));
?>

    
```php

El ejemplo anterior mostrará:

    string(4) "12.0"
    string(2) "12"

## Notas

> [!NOTE]
> Cuando ocurre un error durante la codificación, la función `json_last_error` puede ser utilizada para determinar la naturaleza exacta del error.

> [!NOTE]
> Al codificar un array, si las claves no están en forma de una secuencia numérica continua comenzando en 0, todas las claves serán codificadas como cadenas de caracteres, y especificadas explícitamente para cada par clave-valor.

> [!NOTE]
> Al igual que el codificador JSON de referencia, la función `json_encode` generará un JSON que es un valor simple (ni un objeto, ni un array) si una `string`, un `int`, un `float`, o un `bool` es proporcionado como entrada para el parámetro `value`. Aunque algunos decodificadores aceptan estos valores como JSON válido, otros no los aceptan, sabiendo que la especificación es ambigua sobre este punto.
>
> Para resumir, siempre se debe probar que su decodificador JSON puede manejar la salida que se genera desde la función `json_encode`.

## Véase también

JsonSerializable, `json_decode`, `json_last_error`, `json_last_error_msg`, `serialize`
