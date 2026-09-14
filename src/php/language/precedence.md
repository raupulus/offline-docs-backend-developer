---
title: La prioridad de los operadores
source_url: https://www.php.net/manual/es/language.operators.precedence.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/precedence.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 80dfa568e
order: 2750
---

## La prioridad de los operadores

La prioridad de los operadores especifica el orden en el que deben ser analizadas las valores. Por ejemplo, en la expresión `1 + 5 * 3`, el resultado es `16` y no `18`, ya que la multiplicación ("\*") tiene una prioridad superior a la suma ("+"). Las parentesis pueden ser utilizados para forzar la prioridad, si es necesario. Por ejemplo: `(1 + 5) * 3` dará `18`.

Cuando los operadores tienen una prioridad igual, su asociatividad decide la forma en que los operadores son agrupados. Por ejemplo, "-" es una asociatividad por la izquierda, así `1 - 2 - 3` es agrupado de esta manera `(1 - 2) - 3` y será evaluado a `-4`. Por otro lado, "=" es una asociatividad por la derecha, así, `$a = $b = $c` es agrupado de esta manera `$a = ($b = $c)`.

Los operadores, cuya prioridad es igual, que no son asociativos, no pueden ser utilizados entre ellos, por ejemplo, `1 < 2 > 1` está prohibido en PHP. La expresión `1 <= 1 == 1` por el contrario, está permitida, ya que el operador `==` tiene una precedencia inferior al operador `<=`.

La asociatividad tiene sentido únicamente para los operadores binarios (y ternarios). Los operadores unitarios son prefijos o sufijos, por lo que esta noción no es aplicable. Por ejemplo `!!$a` puede ser agrupado únicamente de la siguiente manera `!(!$a)`.

El uso de parentesis, incluso cuando no son necesarios, permite mejorar la legibilidad del código realizando agrupamientos explícitos en lugar de imaginar la prioridad de los operadores y sus asociatividades.

La tabla siguiente lista los operadores por orden de prioridad, con la prioridad más alta en la parte superior. Los operadores en la misma línea tienen una prioridad equivalente (por lo tanto, la asociatividad decide el agrupamiento).

| Asociatividad | Operadores | Información adicional |
|----|----|----|
| (n/a) | `clone` `new` | [clone](#language.oop5.cloning) y [new](#language.oop5.basic.new) |
| derecha | `**` | [aritmética](#language.operators.arithmetic) |
| (n/a) | `+` `-` `++` `--` `~` `(int)` `(float)` `(string)` `(array)` `(object)` `(bool)` `@` | [aritmética](#language.operators.arithmetic) (unario `+` y `-`), [incremento/decremento](#language.operators.increment) [a nivel de bits](#language.operators.bitwise), [conversión de tipo](#language.types.typecasting) y [control de errores](#language.operators.errorcontrol) |
| izquierda | `instanceof` | [tipo](#language.operators.type) |
| (n/a) | `!` | [lógico](#language.operators.logical) |
| izquierda | `*` `/` `%` | [aritmética](#language.operators.arithmetic) |
| izquierda | `+` `-` `.` | [aritmética](#language.operators.arithmetic) (binario `+` y `-`), [array](#language.operators.array) y [string](#language.operators.string) (`.` anterior a PHP 8.0.0) |
| izquierda | `<<` `>>` | [bitwise](#language.operators.bitwise) |
| izquierda | `.` | [string](#language.operators.string) (a partir de PHP 8.0.0) |
| izquierda | `|>` | [pipe](#language.operators.functional) |
| no asociativo | `<` `<=` `>` `>=` | [comparación](#language.operators.comparison) |
| no asociativo | `==` `!=` `===` `!==` `<>` `<=>` | [comparación](#language.operators.comparison) |
| izquierda | `&` | [bitwise](#language.operators.bitwise) y [referencias](#language.references) |
| izquierda | `^` | [bitwise](#language.operators.bitwise) |
| izquierda | `|` | [bitwise](#language.operators.bitwise) |
| izquierda | `&&` | [lógico](#language.operators.logical) |
| izquierda | `||` | [lógico](#language.operators.logical) |
| derecha | `??` | [coalescencia nula](#language.operators.comparison.coalesce) |
| no asociativo | `? :` | [ternario](#language.operators.comparison.ternary) (izquierda--asociativo anterior a PHP 8.0.0) |
| derecha | `=` `+=` `-=` `*=` `**=` `/=` `.=` `%=` `&=` `|=` `^=` `<<=` `>>=` `??=` | [asignación](#language.operators.assignment) |
| (n/a) | `yield from` | [yield from](#control-structures.yield.from) |
| (n/a) | `yield` | [yield](#control-structures.yield) |
| (n/a) | `print` | `print` |
| izquierda | `and` | [lógico](#language.operators.logical) |
| izquierda | `xor` | [lógico](#language.operators.logical) |
| izquierda | `or` | [lógico](#language.operators.logical) |
| (n/a) | `throw` | [throw](#language.exceptions) |

Prioridad de los operadores

> [!NOTE]
> Los operadores unarios que comparten la fila con los operadores de conversión (`~`, `@`, y `+`/`-` unarios) tienen mayor prioridad que `instanceof`, mientras que `!` tiene menor prioridad. En consecuencia, `(int) $x instanceof Foo` se agrupa como `((int) $x) instanceof Foo`, mientras que `!$x instanceof Foo` se agrupa como `!($x instanceof Foo)`.

Asociatividad

```php
    
<?php
$a = 3 * 3 % 5; // (3 * 3) % 5 = 4
// La asociatividad de los operadores ternarios difiere de C/C++
var_dump($a);

$a = 1;
$b = 2;
$a = $b += 3; // $a = ($b += 3) -> $a = 5, $b = 5
var_dump($a, $b);
?>

   
```

El operador ternario requiere específicamente el uso de parentesis para levantar la ambigüedad de la prioridad.

Precedencia explícita

```php
<?php
$a = true ? 0 : (true ? 1 : 2);
var_dump($a);

// Esto ya no está permitido a partir de PHP 8
// $a = true ? 0 : true ? 1 : 2;
?>

   
```

La prioridad y la asociatividad del operador determinan únicamente la forma en que las expresiones son agrupadas; no especifican el orden de la evaluación. PHP no especifica (de manera general) el orden en que una expresión es evaluada y el código que asume un orden específico de evaluación no debería existir, ya que el comportamiento puede cambiar entre las diferentes versiones de PHP o según el código circundante.

Orden de evaluación indefinido

```php
    
<?php
$a = 1;
echo $a + $a++; // puede mostrar 2 o 3

$i = 1;
$array[$i] = $i++; // puede definir el índice 1 o 2
?>

   
```

Precedencia de `+`, `-` y `.`

```php
<?php
$x = 4;

// Esta línea puede causar una salida inesperada :
echo "x menos uno es igual a" . $x-1 . ", en todo caso espero\n";

// la precedencia deseada puede ser reforzada utilizando parentesis. :
echo "x menos uno es igual a" . ($x-1) . ", en todo caso espero\n";

// Esto no está permitido, y levanta una TypeError :
echo ("x menos uno es igual a" . $x) - 1 . ", en todo caso espero\n";
?>

  
```

El ejemplo anterior mostrará:

    -1, en todo caso espero
    -1, en todo caso espero
    Fatal error: Uncaught TypeError: Unsupported operand types: string - int

Antes de PHP 8, `+`, `-` y `.` tenían la misma precedencia

```php
<?php
$x = 4;
// Esta línea puede causar una salida inesperada :
echo "x menos uno es igual a" . $x-1 . ", en todo caso espero\n";

// porque es evaluada como la línea siguiente (anterior a PHP 8.0.0) :
echo (("x menos uno es igual a" . $x) - 1) . ", en todo caso espero\n";

// la precedencia deseada puede ser reforzada utilizando parentesis. :
echo "x menos uno es igual a" . ($x-1) . ", en todo caso espero\n";

?>

   
```

El ejemplo anterior mostrará:

        
    -1, en todo caso espero
    -1, en todo caso espero
    x menos uno es igual 3, en todo caso espero

> [!NOTE]
> Aunque `=` tiene prioridad sobre la mayoría de los operadores, PHP ejecutará expresiones como: `if (!$a = foo())`. En esta situación, el resultado de `foo()` será colocado en la variable `$a`.
>
> Esto es posible porque el lado izquierdo de una asignación debe ser una variable, por lo que la asignación se agrupa con esa variable en lugar de con el operador prefijo circundante de mayor prioridad. Lo mismo se aplica a los demás operadores prefijos que toman una expresión como operando, como `clone`, los operadores de conversión, `@` y `~`: por ejemplo, `clone $a = $b` se agrupa como `clone ($a = $b)`, no como `(clone $a) = $b`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | La concatenación de strings (`.`) ahora tiene una precedencia más baja que la suma/resta aritmética (`+` y `-`) y los desplazamientos bit a bit izquierda/derecha (`<<` y `>>`); anteriormente, esto tenía la misma precedencia que `+` y `-`, y una precedencia más alta que `<<` y `>>`. |
| 8.0.0 | El operador ternario (`? :`) ahora es no asociativo; anteriormente, era asociativo por la izquierda. |
| 7.4.0 | Dependencia de la precedencia de la concatenación de strings (`.`) relativo a la suma/resta aritmética (`+` o `-`) o los desplazamientos bit a bit izquierda/derecha (`<<` o `>>`), es decir, su uso conjunto en una expresión sin parentesis, está obsoleto. |
| 7.4.0 | Dependencia de la asociatividad por la izquierda del operador ternario (`? :`), es decir, la imbricación de múltiples operadores ternarios que no están entre parentesis, está obsoleta. |
