---
title: mb_decode_numericentity
description: Decodificar referencia numérica de cadena HTML a carácter
source_url: https://www.php.net/manual/es/function.mb-decode-numericentity.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-decode-numericentity.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: 4e69a9f2b
order: 45030
---

mb_decode_numericentity

Decodificar referencia numérica de cadena HTML a carácter

## Descripción

```php
mb_decode_numericentity(string $string, array $map, [string $encoding]): string
```php

Convierte la referencia numérica de cadena de `string` `string` en un bloque especificado a carácter.

## Parámetros

`string`  
La `string` que se está decodificando.

`map`  
`map` es un `array` que especifica el área de código a convertir.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

La `string` convertida.

## Errores/Excepciones

Genera una excepción ValueError si `map` no es una lista de `int`s.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | `mb_decode_numericentity` ahora genera una ValueError si `map` no es una lista de `int`s. |
| 8.0.0 | `encoding` ahora acepta `null`. |

## Ejemplos

Ejemplo de `map`

```
<?php
$convmap = array (
   int start_code1, int end_code1, int offset1, int mask1,
   int start_code2, int end_code2, int offset2, int mask2,
   // ........
   int start_codeN, int end_codeN, int offsetN, int maskN );
// Especificar valor Unicode para start_codeN y end_codeN
// Añadir offsetN al valor y realizar 'AND' a nivel de bits con maskN,
// luego convertir el valor a referencia numérica de cadena.
?>

    
```php

Ejemplo de `map` para escapar cadena JavaScript

```
<?php
function escape_javascript_string($str) {
  $map = [
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,0,0, // 49
          0,0,0,0,0,0,0,0,1,1,
          1,1,1,1,1,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,
          0,1,1,1,1,1,1,0,0,0, // 99
          0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,
          0,0,0,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1, // 149
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1, // 199
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1, // 249
          1,1,1,1,1,1,1, // 255
          ];
  // Codificación de caracteres es UTF-8
  $mblen = mb_strlen($str, 'UTF-8');
  $utf32 = bin2hex(mb_convert_encoding($str, 'UTF-32', 'UTF-8'));
  for ($i=0, $encoded=''; $i < $mblen; $i++) {
      $u = substr($utf32, $i*8, 8);
      $v = base_convert($u, 16, 10);
      if ($v < 256 && $map[$v]) {
        $encoded .= '\\x'.substr($u, 6,2);
      } else if ($v == 2028) {
        $encoded .= '\\u2028';
      } else if ($v == 2029) {
        $encoded .= '\\u2029';
      } else {
        $encoded .= mb_convert_encoding(hex2bin($u), 'UTF-8', 'UTF-32');
      }
   }
   return $encoded;
}

  // Datos de prueba
$convmap = [ 0x0, 0xffff, 0, 0xffff ];
$msg = '';
for ($i=0; $i < 1000; $i++) {
  // chr() no puede generar datos UTF-8 correctos mayores que 128, usar mb_decode_numericentity().
  $msg .= mb_decode_numericentity('&#'.$i.';', $convmap, 'UTF-8');
}

// var_dump($msg);
var_dump(escape_javascript_string($msg));

    
```php

## Véase también

`mb_encode_numericentity`
