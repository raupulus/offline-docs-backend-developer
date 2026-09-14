---
title: preg_match_all
description: Expresión regular global
source_url: https://www.php.net/manual/es/function.preg-match-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-match-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: false
translation_revision: 4de6272a1
order: 61610
---

preg_match_all

Expresión regular global

## Descripción

```php
preg_match_all(string $pattern, string $subject, [array $matches], [int $flags], [int $offset]): int
```php

Analiza `subject` para encontrar la expresión `pattern` y almacena los resultados en `matches`, en el orden especificado por `flags`.

Tras encontrar un primer resultado, la búsqueda continúa hasta el final de la cadena.

## Parámetros

`pattern`  
La máscara a buscar, en forma de cadena.

`subject`  
La cadena de entrada.

`matches`  
Array que contiene todos los resultados, en un array multidimensional ordenado según el parámetro `flags`.

`flags`  
Si no se proporciona ningún flag de orden, se asume `PREG_PATTERN_ORDER`.

Puede ser una combinación de los siguientes valores (señalando que es incoherente usar `PREG_PATTERN_ORDER` con `PREG_SET_ORDER` ) :

`PREG_PATTERN_ORDER`  
El orden es tal que `$matches[0]` es un array que contiene los resultados que satisfacen la máscara completa, `$matches[1]` es un array que contiene los resultados que satisfacen la primera subexpresión capturante, etc.

```
<?php
preg_match_all("|<[^>]+>(.*)</[^>]+>|U",
    "<b>ejemplo : </b><div align=left>esto es una prueba</div>",
    $out, PREG_PATTERN_ORDER);
echo $out[0][0] . ", " . $out[0][1] . "\n";
echo $out[1][0] . ", " . $out[1][1] . "\n";
?>

            
```php

El ejemplo anterior mostrará:

```
<b>ejemplo : </b>, <div align=left>esto es una prueba</div>
ejemplo : , esto es una prueba

            
```php

Así, `$out[0]` es un array que contiene los resultados que satisfacen la máscara completa, y `$out[1]` es un array que contiene las etiquetas entre los caracteres de mayor y menor que.

Si la máscara contiene submáscaras nombradas, `$matches` contendrá además entradas que tendrán como claves los nombres de las submáscaras.

Si la máscara contiene submáscaras nombradas duplicadas, solo la submáscara más a la derecha será registrada en `$matches[NAME]`.

```
<?php
preg_match_all(
    '/(?J)(?<match>foo)|(?<match>bar)/',
    'foo bar',
    $matches,
    PREG_PATTERN_ORDER
);
print_r($matches['match']);
?>

            
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] =>
        [1] => bar
    )

`PREG_SET_ORDER`  
Los resultados se ordenan de tal forma que `$matches[0]` contiene la primera serie de resultados, `$matches[1]` contiene la segunda, etc.

```
<?php
preg_match_all("|<[^>]+>(.*)</[^>]+>|U",
    "<b>ejemplo : </b><div align=\"left\">esto es una prueba</div>",
    $out, PREG_SET_ORDER);
echo $out[0][0] . ", " . $out[0][1] . "\n";
echo $out[1][0] . ", " . $out[1][1] . "\n";
?>

            
```php

El ejemplo anterior mostrará:

```
<b>ejemplo : </b>, ejemplo :
<div align="left">esto es una prueba</div>, esto es una prueba

            
```php

`PREG_OFFSET_CAPTURE`  
Si este flag es pasado, todas las subcadenas que satisfacen la máscara también serán identificadas por su offset (en bytes). Tenga en cuenta que esto modifica el valor de `matches` en un array de arrays donde cada elemento es un array que contiene la subcadena satisfecha en el índice `0` y el índice de esta en la cadena `subject` en el índice `1`.

```
<?php
preg_match_all('/(foo)(bar)(baz)/', 'foobarbaz', $matches, PREG_OFFSET_CAPTURE);
print_r($matches);
?>

            
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [0] => Array
                    (
                        [0] => foobarbaz
                        [1] => 0
                    )

            )

        [1] => Array
            (
                [0] => Array
                    (
                        [0] => foo
                        [1] => 0
                    )

            )

        [2] => Array
            (
                [0] => Array
                    (
                        [0] => bar
                        [1] => 3
                    )

            )

        [3] => Array
            (
                [0] => Array
                    (
                        [0] => baz
                        [1] => 6
                    )

            )

    )

`PREG_UNMATCHED_AS_NULL`  
Si este flag es pasado, las subexpresiones no satisfechas son reportadas como `null`; de lo contrario, son reportadas como una `string` vacía.

`offset`  
Normalmente, la búsqueda comienza al inicio de la cadena subject. El parámetro opcional `offset` puede ser usado para especificar una posición para el inicio de la búsqueda (en bytes).

> [!NOTE]
> Usar el parámetro `offset` no equivale a pasar `substr($subject, $offset)` a `preg_match_all` en lugar de la cadena subject, ya que `pattern` puede contener aserciones como *^*, *\$* o *(?\<=x)*. Consulte la documentación sobre la función `preg_match` para ejemplos.

## Valores devueltos

Devuelve el número de resultados que satisfacen la máscara completa, o `false` si ocurre un error.

## Errores/Excepciones

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.2.0 | `PREG_UNMATCHED_AS_NULL` es ahora soportado para el parámetro `flags`. |

## Ejemplos

Extracción de todos los números de teléfono de un texto

```
<?php
preg_match_all("/\(?  (\d{3})?  \)?  (?(1)  [\-\s] ) \d{3}-\d{4}/x",
                "Llamar al 555-1212 o 1-800-555-1212", $phones);
?>

    
```php

Buscar pares de etiquetas HTML (voraz)

```
<?php
// Este ejemplo utiliza referencias hacia atrás (\\2).
// Indican al analizador que debe encontrar algo que ya ha identificado antes
// el número 2 indica que es el segundo juego de paréntesis
// capturante que debe ser usado (en este caso, ([\w]+)).
// La barra invertida es necesaria aquí, ya que la cadena está entre comillas dobles

$html = "<b>texto en negrita</b><a href=howdy.html>haz clic aquí</a>";

preg_match_all("/(<([\w]+)[^>]*>)(.*?)(<\/\\2>)/", $html, $matches, PREG_SET_ORDER);

foreach ($matches as $val) {
    echo "coincidencia: " . $val[0] . "\n";
    echo "parte 1: " . $val[1] . "\n";
    echo "parte 2: " . $val[2] . "\n";
    echo "parte 3: " . $val[3] . "\n";
    echo "parte 4: " . $val[4] . "\n\n";
}
?>

    
```php

El ejemplo anterior mostrará:

```
coincidencia: <b>texto en negrita</b>
parte 2: b
parte 3: texto en negrita
parte 4: </b>

coincidencia: <a href=howdy.html>haz clic aquí</a>
parte 1: <a href=howdy.html>
parte 2: a
parte 3: haz clic aquí
parte 4: </a>

    
```php

Uso de una subexpresión nombrada

```
<?php

$str = <<<FOO
a: 1
b: 2
c: 3
FOO;

preg_match_all('/(?P<name>\w+): (?P<digit>\d+)/', $str, $matches);

/* Alternativa */
// preg_match_all('/(?<name>\w+): (?<digit>\d+)/', $str, $matches);

print_r($matches);

?>

    
```php

El ejemplo anterior mostrará:

```
Array
(
    [0] => Array
        (
            [0] => a: 1
            [1] => b: 2
            [2] => c: 3
        )

    [name] => Array
        (
            [0] => a
            [1] => b
            [2] => c
        )

    [1] => Array
        (
            [0] => a
            [1] => b
            [2] => c
        )

    [digit] => Array
        (
            [0] => 1
            [1] => 2
            [2] => 3
        )

    [2] => Array
        (
            [0] => 1
            [1] => 2
            [2] => 3
        )

)

    
```php

## Véase también

[Máscaras PCRE](#pcre.pattern), `preg_quote`, `preg_match`, `preg_replace`, `preg_split`, `preg_last_error`
