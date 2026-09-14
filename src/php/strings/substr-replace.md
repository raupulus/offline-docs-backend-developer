---
title: substr_replace
description: Reemplaza un segmento en un string
source_url: https://www.php.net/manual/es/function.substr-replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/substr-replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: e095023e4
order: 89530
---

substr_replace

Reemplaza un segmento en un string

## Descripción

```php
substr_replace(array $string, array $replace, array $offset, [array $length]): string
```php

`substr_replace` reemplaza un segmento del string `string` por el string `replace`. El segmento está delimitado por `offset` y eventualmente por `length`.

## Parámetros

`string`  
El string de entrada.

Puede proporcionarse un array de strings, y en este caso, los reemplazos se realizarán en cada uno de los strings. En esta situación, los parámetros `replace`, `offset` y `length` deben proporcionarse ya sea como valores escalares a aplicar a cada string, o como arrays donde el elemento correspondiente del array será utilizado para cada string de entrada.

`replace`  
El string de reemplazo.

`offset`  
Si `offset` no es negativo, el reemplazo se realizará a partir del carácter número `offset` en `string`.

Si `offset` es negativo, el reemplazo se realizará a partir del `offset`-ésimo carácter contando desde el final del string `string`.

`length`  
Si `length` es proporcionado y positivo, representará la longitud del segmento de código reemplazado en el string `string`. Si es negativo, representará el número de caracteres desde el final del string `string` donde detener el reemplazo. Si es omitido, tomará el valor por omisión del tamaño del string, y reemplazará todo hasta el final del string `string`. Por supuesto, si `length` vale 0, entonces, esta función tendrá como efecto insertar `replace` en `string` en la posición `offset` dada.

## Valores devueltos

El string resultante es retornado. Si el parámetro `string` es un array, entonces un array será retornado.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `length` ahora es nullable. |

## Ejemplos

Ejemplo con `substr_replace`

```
<?php
$var = 'ABCDEFGH:/MNRPQR/';
echo "Original : $var<hr />\n";

// Reemplaza todo el string $var por 'bob'.
echo substr_replace($var, 'bob', 0) . "<br />\n";
echo substr_replace($var, 'bob', 0, strlen($var)) . "<br />\n";

// Inserta 'bob' al inicio del string
echo substr_replace($var, 'bob', 0, 0) . "<br />\n";

// Reemplaza la secuencia 'MNRPQR' por 'bob'.
echo substr_replace($var, 'bob', 10, -1) . "<br />\n";
echo substr_replace($var, 'bob', -7, -1) . "<br />\n";

// Borra la secuencia 'MNRPQR' de $var.
echo substr_replace($var, '', 10, -1) . "<br />\n";
?>

    
```php

Uso de `substr_replace` para reemplazar múltiples strings de una sola vez

```
<?php
$input = array('A: XXX', 'B: XXX', 'C: XXX');

// Un caso simple: reemplazar XXX en cada string por YYY.
echo implode('; ', substr_replace($input, 'YYY', 3, 3))."\n";

// Un caso más complejo donde cada reemplazo es diferente.
$replace = array('AAA', 'BBB', 'CCC');
echo implode('; ', substr_replace($input, $replace, 3, 3))."\n";

// Reemplaza un número diferente de caracteres cada vez.
$length = array(1, 2, 3);
echo implode('; ', substr_replace($input, $replace, 3, $length))."\n";
?>

    
```php

El ejemplo anterior mostrará:

    A: YYY; B: YYY; C: YYY
    A: AAA; B: BBB; C: CCC
    A: AAAXX; B: BBBX; C: CCC

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`str_replace`, `substr`, [Acceso y modificación de un string, por carácter](#language.types.string.substr)
