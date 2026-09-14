---
title: preg_replace
description: Buscar y reemplazar mediante expresión regular estándar
source_url: https://www.php.net/manual/es/function.preg-replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_revision: 79c53e3fa
order: 61660
---

preg_replace

Buscar y reemplazar mediante expresión regular estándar

## Descripción

```php
preg_replace(string $pattern, string $replacement, string $subject, [int $limit], [int $count]): string
```php

Analiza `subject` para encontrar la expresión regular `pattern` y reemplaza los resultados por `replacement`.

Para hacer coincidir una cadena exacta, en lugar de una expresión regular, se recomienda el uso de `str_replace` o `str_ireplace` en lugar de esta función.

## Parámetros

`pattern`  
El patrón a buscar. Puede ser una cadena o un array de cadenas.

También están disponibles varios [modificadores PCRE](#reference.pcre.pattern.modifiers).

`replacement`  
La cadena o un array de cadenas para el reemplazo. Si este parámetro es una cadena y el parámetro `pattern` es un array, todos los patrones serán reemplazados por esta cadena. Si los parámetros `pattern` y `replacement` son arrays, cada `pattern` será reemplazado por su `replacement` asociado. Si `replacement` tiene menos elementos que `pattern`, entonces una cadena vacía es utilizada para los `pattern` adicionales.

`replacement` puede contener referencias de la forma `\n` o `$n`. Esta última forma es recomendada. Estas referencias serán reemplazadas por el texto capturado por la \<n\>-ésima parentesis capturante del patrón. \<n\> puede tomar valores de 0 a 99, y `\0` o `$0`, corresponden al texto que satisface el patrón completo. Los paréntesis abiertos son contados de izquierda a derecha (empezando por 1) para determinar el número de paréntesis capturante. Es de notar que en los `string` literales los backslashs deben ser escapados.

Cuando se trabaja con un patrón de reemplazo donde una referencia hacia atrás es seguida directamente por un número (i.e.: colocar un número literal inmediatamente después de una referencia hacia atrás), no se puede usar la sintaxis clásica `\1` para la referencia hacia atrás. `\11`, por ejemplo, será confuso para la función `preg_replace` en el sentido de que no sabrá si se desea la referencia hacia atrás `\1` seguida del número `1` o si se desea la referencia hacia atrás `\11` seguida de "nada". En este caso, la solución es usar la sintaxis `${1}1`. Esto creará una referencia hacia atrás aislada `$1`, seguida del número literal `1`.

`subject`  
La cadena o el array que contiene las cadenas a buscar y reemplazar.

Si `subject` es un array, entonces la búsqueda y el reemplazo se realiza en cada entrada de `subject`, y el array será devuelto.

Si el array `subject` es asociativo, entonces las claves serán preservadas en el valor devuelto.

`limit`  
El número máximo de reemplazos para cada patrón en cada cadena `subject`. Por omisión, vale `-1` (sin límite).

`count`  
Si se proporciona, esta variable contendrá el número de reemplazos realizados.

## Valores devueltos

`preg_replace` devuelve un array si el parámetro `subject` es un array, o una cadena en caso contrario.

Si se encuentran coincidencias, el nuevo `subject` será devuelto, de lo contrario `subject` será devuelto sin cambios, o `null` si ocurre un error.

## Errores/Excepciones

Utilizar la opción "\e" es un error; se emite una `E_WARNING` en este caso.

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Ejemplos

Uso de referencias hacia atrás con literales numéricos

```
<?php
$string = 'April 15, 2003';
$pattern = '/(\w+) (\d+), (\d+)/i';
$replacement = '${1}1,$3';
echo preg_replace($pattern, $replacement, $string);
?>

    
```php

El ejemplo anterior mostrará:

    April1,2003

Uso de arrays indexados con `preg_replace`

```
<?php
$string = 'Le renard marron agile saute par dessus le chien paresseux.';
$patterns = array();
$patterns[0] = '/agile/';
$patterns[1] = '/marron/';
$patterns[2] = '/renard/';
$replacements = array();
$replacements[2] = 'grizzly';
$replacements[1] = 'brun';
$replacements[0] = 'lent';
echo preg_replace($patterns, $replacements, $string);
?>

    
```php

El ejemplo anterior mostrará:

    Le lent brun grizzly saute par dessus le chien paresseux.

        

Ordenando los patrones y los reemplazos, se debería obtener el resultado esperado.

```
<?php
$string = 'Le renard marron agile saute par dessus le chien paresseux.';
$patterns = array();
$patterns[0] = '/agile/';
$patterns[1] = '/marron/';
$patterns[2] = '/renard/';
$replacements = array();
$replacements[2] = 'grizzly';
$replacements[1] = 'brun';
$replacements[0] = 'lent';
ksort($patterns);
ksort($replacements);
echo preg_replace($patterns, $replacements, $string);
?>

    
```php

El ejemplo anterior mostrará:

    Le grizzly brun lent saute par dessus le chien paresseux.

Reemplazo de múltiples valores simultáneamente

```
<?php
$patterns = array ('/(19|20)(\d{2})-(\d{1,2})-(\d{1,2})/',
                   '/^\s*{(\w+)}\s*=/');
$replace = array ('\3/\4/\1\2', '$\1 =');
echo preg_replace($patterns, $replace, '{startDate} = 1999-5-27');
?>

    
```php

El ejemplo anterior mostrará:

    $startDate = 5/27/1999

Eliminación de espacios

Este ejemplo elimina los espacios en exceso en una cadena.

```
<?php
$str = 'foo   o';
$str = preg_replace('/\s\s+/', ' ', $str);
// Mostrará 'foo o'
echo $str;
?>

    
```php

Uso del parámetro `count`

```
<?php
$count = 0;

echo preg_replace(array('/\d/', '/\s/'), '*', 'xp 4 to', -1 , $count);
echo $count; //3
?>

    
```php

El ejemplo anterior mostrará:

    xp***to
    3

## Notas

> [!NOTE]
> Cuando se usan arrays con los parámetros `pattern` y `replacement`, las claves son tratadas en el orden en que aparecen en el array. Esto *no es necesariamente* lo mismo que el orden de los índices numéricos. Si se usan índices para identificar qué `pattern` debe ser reemplazado por qué `replacement`, se recomienda hacer un ordenamiento `ksort` en cada array antes de llamar a `preg_replace`.

> [!NOTE]
> Cuando `pattern` y `replacement` son arrays, las reglas de coincidencia funcionarán de manera secuencial. Es decir, la segunda pareja `pattern`/`replacement` operará sobre la cadena de caracteres que resulta de la primera pareja `pattern`/`replacement`, y no sobre la cadena original. Si se desea simular reemplazos funcionando en paralelo, como el intercambio de dos valores, reemplace un patrón por un sustituto intermedio, luego en una pareja posterior, reemplace este marcador intermedio por el reemplazo deseado.
>
> <div class="informalexample">
>
> ```
> <?php
> $p = array('/a/', '/b/', '/c/');
> $r = array('b', 'c', 'd');
> print_r(preg_replace($p, $r, 'a'));
> // imprime d
> ?>
>
>     
> ```
>
> </div>

## Véase también

[Patrones PCRE](#pcre.pattern), `preg_quote`, `preg_filter`, `preg_match`, `preg_replace_callback`, `preg_split`, `preg_last_error`, `str_replace`
