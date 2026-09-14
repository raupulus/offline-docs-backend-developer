---
title: Expresiones
source_url: https://www.php.net/manual/es/language.expressions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/expressions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 6e885e524
order: 2330
---

## Expresiones

La expresiones son los bloques de construcción más importantes de PHP. En PHP casi todo lo que se escribe es una expresión. La manera más simple y acertada de definir lo que es una expresión es «cualquier cosa que tiene un valor».

Las formas más básicas de expresiones son las constantes y las variables. Cuando se escribe `$a = 5`, se está asignando `5` a `$a`. `5`, obviamente, tiene el valor 5, o en otras palabras `5` es una expresión con el valor de 5 (en este caso, `5` es una constante entera).

Después de esta asignación, se espera que el valor de `$a` sea 5 también, por lo que si se escribe `$b = $a`, se espera que esto se comporte tal como si se escribiera `$b = 5`. En otras palabras, `$a` es también una expresión con el valor 5. Si todo funciona bien, esto es exactamente lo que sucederá.

Un ejemplo de expresiones algo más complejo son las funciones. Por ejemplo, considere la siguiente función:

```php
<?php

function foo ()
{
    return 5;
}

?>

     
```

Asumiendo que está familiarizado con el concepto de función (si no lo está, échele una ojeada al capítulo sobre [funciones](#language.functions)), asumirá que escribir `$c = foo()` es esencialmente igual que escribir `$c = 5`. Y está en lo cierto. Las funciones son expresiones con el valor de sus valores devueltos. Ya que `foo()` devuelve 5, el valor de la expresión '`foo()`' es 5. Normalmente las funciones no sólo devuelven un valor estático, sino que computan algo.

Por supuesto, los valores en PHP no tienen que ser enteros, y con frecuencia no lo son. PHP soporta cuatro tipos de valores escalares: valores enteros (`integer`), valores de coma (punto) flotante (`float`), valores de cadena (`string`) y valores booleanos (`boolean`) - (valores escalares son aquellos que no se pueden descomponer en piezas más pequeñas, a diferencia de las matrices, por ejemplo). PHP también soporta dos tipos compuestos (no escalares): matrices (arrays) y objetos. Cada uno de estos tipos de valores pueden ser asignados a variables o devueltos desde funciones.

PHP lleva las expresiones mucho más allá, de la misma manera que lo hacen otros lenguajes. PHP es un lenguaje orientado a expresiones, en el sentido de que casi todo es una expresión. Considere el ejemplo que ya hemos tratado, `$a = 5`. Es fácil de ver que aquí hay dos valores involucrados, el valor de la constante entera `5`, y el valor de `$a` que ha sido actualizado a 5 también. Aunque la verdad es que existe aquí un valor adicional involucrado, que es el valor de la asignación misma. La asignación evalúa al valor asignado, en este caso 5. En la práctica, esto significa que `$a = 5`, sin importar lo que haga, es una expresión con el valor 5. De este modo, escribir algo como `$b = ($a = 5)` es igual que escribir `$a = 5; $b = 5;` (el punto y coma marca el final de una sentencia). Ya que las asignaciones se analizan de derecha a izquierda, también se puede escribir `$b = $a = 5`.

Otro buen ejemplo de orientación a expresiones es el pre- y post-incremento y decremento. Los usuarios de PHP y de otros muchos lenguajes pueden estar familiarizados con la notación `variable++` y `variable--`. Éstos son los [ operadores de incremento y decremento](#language.operators.increment). En PHP, al igual que en C, hay dos tipos de incrementos - pre-incremento y post-incremento. Ambos esencialmente incrementan la variable, y el efecto sobre la variable es idéntico. La diferencia está con el valor de la expresión de incremento. Pre-incremento, que se escribre `++$variable`, evalúa al valor incrementado (PHP incrementa la variable antes de leer su valor, de ahí el nombre de 'pre-incremento'). Post-incremento, que se escribe `$variable++` evalúa el valor original de `$variable`, antes de que sea incrementado (PHP incrementa la variable después de leer su valor, de ahí el nombre de 'post-incremento').

Un tipo de expresiones muy comunes son las expresiones de [comparación](#language.operators.comparison). Estas expresiones evalúan si algo es `false` (falso) o `true` (verdadero). PHP soporta \> (mayor que), \>= (mayor o igual que), == (igual), != (distinto), \< (menor que) y \<= (menor o igual que). El lenguaje también soporta un conjunto de operadores de equivalencia estricta: === (igual y del mismo tipo) y !== (diferente o de distinto tipo). Estas expresiones se usan mayormente dentro de ejecuciones condicionales, tales como la sentencia `if`.

El último ejemplo de expresiones que trataremos aquí es una combinación de expresiones operador-asignación. Ya sabe que si quiere incrementar `$a` en 1, puede simplemente escribir `$a++` o `++$a`. Pero si lo que quiere es añadirle más de uno, por ejemplo 3, podría escribir `$a++` varias veces, pero esto, obviamente, no es una manera muy eficiente o cómoda. Una práctica mucho más común es escribir `$a = $a + 3`. `$a + 3` evalúa al valor de `$a` más 3, y se vuelve a asignar a `$a`, lo que resulta en incrementar `$a` en 3. En PHP, como en otros lenguajes como C, se puede escribir esto de una manera más abreviada, lo que con el tiempo se podría convertir en una forma más clara y rápida de entenderlo. Añadir 3 al valor actual de `$a` puede ser escrito `$a += 3`. Esto significa exactamente "toma el valor de `$a`, añádele 3 y asígnalo de nuevo a `$a`". Además de ser más corto y claro, también resulta en una ejecución más rápida. El valor de `$a += 3`, al igual que el valor de una asignación normal, es el valor asignado. Observe que NO es 3, sino el valor combinado de `$a` más 3 (éste es el valor que es asignado a `$a`). Se puede usar cualquier operador compuesto de dos partes en este modo de operador-asignación, por ejemplo `$a -= 5` (restar 5 del valor de `$a`), `$b *= 7` (multiplicar el valor de `$b` por 7), etc.

Existe una expresión más que le puede parecer rara si no la ha visto en otros lenguajes, el operador condicional ternario:

```php
<?php
$primero ? $segundo : $tercero
?>

     
```

Si el valor de la primera subexpresión es `true` (no es cero), se evalúa la segunda subexpresión, y ése será el resultado de la expresión condicional. Si no, se evalúa la tercera subexpresión, y ése será el valor.

El siguiente ejemplo debería ayudarle a comprender un poco mejor el pre- y post-incremento y las expresiones en general:

```php
<?php
function double($i)
{
    return $i * 2;
}

$b = $a = 5;        /* asignar el valor cinco a la variable $a y $b */
$c = $a++;          /* post-incremento, asignar el valor original de $a
                       (5) a $c */
print "a = {$a}; b = {$b}; c = {$c}" . PHP_EOL;

$e = $d = ++$b;     /* pre-incremento, asignar el valor incrementado de
                       $b (6) a $d y $e */
print "b = {$b}; d = {$d}; e = {$e}" . PHP_EOL;

/* en este punto, $d y $e son iguales a 6 */

$f = double($d++);  /* asignar el doble del valor de $d antes
                       del incremento, 2*6 = 12, a $f */
print "d = {$d}; f = {$f}" . PHP_EOL;

$g = double(++$e);  /* asignar el doble del valor de $e después
                       del incremento, 2*7 = 14, a $g */
print "e = {$e}; g = {$g}" . PHP_EOL;

$h = $g += 10;      /* primero, $g es incrementado en 10 y finaliza con el
                       valor 24. El valor de la asignación (24) es
                       asignado después a $h, y $h finaliza también con el
                       valor 24. */
print "g = {$g}; h = {$h}" . PHP_EOL;
?>

     
```

Algunas expresiones pueden considerarse como sentencias. En este caso, una sentencia tiene la forma '`expr ;`', es decir, una expresión seguida de un punto y coma. En `$b = $a = 5;`, `$a = 5` es una expresión válida, pero no es una sentencia en sí. Sin embargo, `$b = $a = 5;` es una sentencia válida.

Lo último que vale la pena mencionar es el valor verdadero de las expresiones. En muchos casos, principalmente en ejecuciones condicionales y bucles, no interesa saber el valor específico de la expresión, sino sólo si el valor significa `true` o `false`. Las constantes `true` y `false` (insensible a mayúsculas-minúsculas) son los dos valores booleanos posibles. Cuando es necesario, una expresión es convertida automáticamente al tipo boolean. Véase la [sección sobre conversión de tipos](#language.types.typecasting) para más detalles.

PHP proporciona una implementación completa y potente de expresiones, y documentarla por completo va más allá del ámbito de este manual. Los ejemplos de arriba deberían darle una buena idea de lo que son las expresiones y cómo construir expresiones útiles. Durante el resto de este manual se escribirá `expr` para indicar cualquier expresión de PHP válida.
