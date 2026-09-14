---
title: Operadores de comparación
source_url: https://www.php.net/manual/es/language.operators.comparison.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/operators/comparison.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 16934048f
order: 2690
---

## Operadores de comparación

Los operadores de comparación, como su nombre indica, permiten comparar dos valores. También se debe estar interesado por las [tablas de comparaciones de tipos](#types.comparisons), ya que muestran ejemplos de muchos tipos de comparaciones.

| Ejemplo | Nombre | Resultado |
|----|----|----|
| \$a == \$b | Igual | `true` si `$a` es igual a `$b` después del transtipado. |
| \$a === \$b | Idéntico | `true` si `$a` es igual a `$b` y son del mismo tipo. |
| \$a != \$b | Diferente | `true` si `$a` es diferente de `$b` después del transtipado. |
| \$a \<\> \$b | Diferente | `true` si `$a` es diferente de `$b` después del transtipado. |
| \$a !== \$b | Diferente | `true` si `$a` es diferente de `$b` o bien si no son del mismo tipo. |
| \$a \< \$b | Menor que | `true` si `$a` es estrictamente menor que `$b`. |
| \$a \> \$b | Mayor | `true` si `$a` es estrictamente mayor que `$b`. |
| \$a \<= \$b | Menor o igual | `true` si `$a` es menor o igual a `$b`. |
| \$a \>= \$b | Mayor o igual | `true` si `$a` es mayor o igual a `$b`. |
| \$a \<=\> \$b | Combinado | Un `int` menor, igual o mayor a cero cuando `$a` es menor, igual, o mayor a `$b` respectivamente. |

Operadores de comparación

Si los dos operandos son [strings numéricos](#language.types.numeric-strings), o si un operando es un número y el otro es un [string numérico](#language.types.numeric-strings), entonces la comparación se efectuará numéricamente. Estas reglas también se aplican a la instrucción [switch](#control-structures.switch). La conversión de tipo no interviene cuando la comparación es `===` o `!==` ya que esto implica tanto una comparación de tipo como de valor.

> [!WARNING]
> Antes de PHP 8.0.0, si un `string` es comparado a un número o a un string numérico, entonces el `string` será convertido en un número antes de efectuar la comparación. Esto puede llevar a resultados sorprendentes como se puede ver en el siguiente ejemplo:
>
> <div class="informalexample">
>
> ```
> <?php
> var_dump(0 == "a");
> var_dump("1" == "01");
> var_dump("10" == "1e1");
> var_dump(100 == "1e2");
>
> switch ("a") {
> case 0:
>     echo "0";
>     break;
> case "a":
>     echo "a";
>     break;
> }
> ?>
>
>     
> ```
>
> Resultado del ejemplo anterior en PHP 7:
>
>     bool(true)
>     bool(true)
>     bool(true)
>     bool(true)
>     0
>
>         
>
> Resultado del ejemplo anterior en PHP 8:
>
>     bool(false)
>     bool(true)
>     bool(true)
>     bool(true)
>     a
>
>         
>
> </div>

Operadores de comparación

```php
<?php
// Enteros
echo 1 <=> 1, ' '; // 0
echo 1 <=> 2, ' '; // -1
echo 2 <=> 1, ' '; // 1

// Números flotantes
echo 1.5 <=> 1.5, ' '; // 0
echo 1.5 <=> 2.5, ' '; // -1
echo 2.5 <=> 1.5, ' '; // 1

// Strings
echo "a" <=> "a", ' '; // 0
echo "a" <=> "b", ' '; // -1
echo "b" <=> "a", ' '; // 1

echo "a" <=> "aa", ' '; // -1
echo "zz" <=> "aa", ' '; // 1

// Arrays
echo [] <=> [], ' '; // 0
echo [1, 2, 3] <=> [1, 2, 3], ' '; // 0
echo [1, 2, 3] <=> [], ' '; // 1
echo [1, 2, 3] <=> [1, 2, 1], ' '; // 1
echo [1, 2, 3] <=> [1, 2, 4], ' '; // -1

// Objetos
$a = (object) ["a" => "b"];
$b = (object) ["a" => "b"];
echo $a <=> $b, ' '; // 0

$a = (object) ["a" => "b"];
$b = (object) ["a" => "c"];
echo $a <=> $b, ' '; // -1

$a = (object) ["a" => "c"];
$b = (object) ["a" => "b"];
echo $a <=> $b, ' '; // 1

// No solo las valores son comparados; las claves deben coincidir
$a = (object) ["a" => "b"];
$b = (object) ["b" => "b"];
echo $a <=> $b, ' '; // 1

?>

   
```

Para los diferentes tipos, la comparación se realiza siguiendo la tabla siguiente (en orden).

| Tipo del operando 1 | Tipo del operando 2 | Resultado |
|----|----|----|
| `null` o `string` | `string` | Convierte `null` en "", comparación numérica o léxica |
| `bool` o `null` | Cualquier cosa | Convierte en `bool`, `false` \< `true` |
| `object` | `object` | Las clases internas pueden definir su propio método de comparación; diferentes clases son incomparables; entre objetos de la misma clase ver [Comparación de objetos](#language.oop5.object-comparison) |
| `string`, `resource`, `int` o `float` | `string`, `resource`, `int` o `float` | Transforma los strings y los recursos en números |
| `array` | `array` | El array con menos miembros es menor, si la clave del operando 1 no es encontrada en el operando 2, entonces los arrays son incomparables, de lo contrario la comparación se realiza valor por valor (ver el siguiente ejemplo) |
| `object` | Cualquier cosa | El `object` es siempre mayor |
| `array` | Cualquier cosa | El `array` es siempre mayor |

Comparación con múltiples tipos {#language.operators.comparison.types}

Comparación Booléen/null

```php
<?php
// Booléen y null siempre son comparados como booléans
var_dump(1 == TRUE);  // TRUE - idéntico a (bool) 1 == TRUE
var_dump(0 == FALSE); // TRUE - idéntico a (bool) 0 == FALSE
var_dump(100 < TRUE); // FALSE - idéntico a (bool) 100 < TRUE
var_dump(-10 < FALSE);// FALSE - idéntico a (bool) -10 < FALSE
var_dump(min(-100, -10, NULL, 10, 100)); // NULL - (bool) NULL < (bool) -100 es idéntico a FALSE < TRUE
?>

   
```

Transcripción de las comparaciones estándar de arrays

```php
<?php
// Los arrays son comparados de esta manera con los operadores estándar de comparación y el operador combinado
function standard_array_compare($op1, $op2)
{
   if (count($op1) < count($op2)) {
      return -1; // $op1 < $op2
   } elseif (count($op1) > count($op2)) {
      return 1; // $op1 > $op2
   }
   foreach ($op1 as $key => $val) {
      if (!array_key_exists($key, $op2)) {
         return 1;
      } elseif ($val < $op2[$key]) {
         return -1;
      } elseif ($val > $op2[$key]) {
         return 1;
      }
   }
   return 0; // $op1 == $op2
}
?>
  
   
```

> [!WARNING]
> Debido a la forma en que los `float`s son representados internamente, no se debe probar la igualdad entre dos números de tipo `float`.
>
> Ver la documentación de `float` para más información.

> [!NOTE]
> Tenga en cuenta que la manipulación de tipos no siempre es evidente al comparar valores de diferentes tipos, en particular al comparar `int`s con `bool`s o `int`s con `string`s. Por lo tanto, generalmente se recomienda utilizar los operadores de comparación `===` y `!==` en lugar de `==` y `!=` en la mayoría de los casos.

## Valores incomparables

Mientras que las comparaciones de identidad (`===` y `!==`) pueden ser aplicadas a valores arbitrarios, los otros operadores de comparación solo deben ser aplicados a valores comparables. El resultado de la comparación de valores incomparables es indefinido, y no debe ser utilizado.

## Véase también

`strcasecmp`, `strcmp`, [operador de arrays](#language.operators.array), [Tipos](#language.types)

## El operador ternario

Otro operador condicional es el operador ternario ("?:").

Asignación de un valor por defecto

```php
<?php
// Ejemplo de uso para el operador ternario
$action = (empty($_POST['action'])) ? 'default' : $_POST['action'];

// La línea anterior es idéntica a la siguiente condición:
if (empty($_POST['action'])) {
   $action = 'default';
} else {
   $action = $_POST['action'];
}
?>

    
```

La expresión `(expr1) ? (expr2) : (expr3)` se evalúa a \<expr2\> si \<expr1\> se evalúa a `true`, y \<expr3\> si \<expr1\> se evalúa a `false`.

Es posible omitir la parte central del operador ternario. La expresión `expr1 ?: expr3` evalúa el resultado de \<expr1\> si \<expr1\> vale `true`, y \<expr3\> en caso contrario. \<expr1\> solo se evalúa una vez en este caso.

> [!NOTE]
> Tenga en cuenta que el operador ternario es una expresión, y no se evalúa como una variable, sino como el resultado de la expresión. Es importante saberlo si se desea devolver una variable por referencia. La instrucción `return $var == 42 ? $a : $b;` en una función devuelta por referencia no funcionará y se emitirá una alerta.

> [!NOTE]
> Se recomienda no "apilar" las expresiones ternarias. El comportamiento de PHP al utilizar varios operadores ternarios que no están entre paréntesis en una única expresión es no evidente en comparación con otros lenguajes. Anteriormente a PHP 8.0.0, el operador ternario se evaluaba de izquierda a derecha, en lugar de derecha a izquierda como la mayoría de los otros lenguajes de programación. Dependiendo de la asociatividad a la izquierda es obsoleto a partir de PHP 7.4.0. A partir de PHP 8.0.0, el operador ternario no es asociativo.
>
> <div class="example">
>
> <div class="title">
>
> Comportamiento de PHP
>
> </div>
>
> ```
> <?php
> // A primera vista, lo siguiente debería devolver 'true'
> echo (true ? 'true' : false ? 't' : 'f');
>
> // sin embargo, la expresión anterior devolverá 't' antes de PHP 8.0.0
> // porque el operador ternario es de izquierda a derecha
>
> // la siguiente expresión es una versión más evidente del mismo código
> echo ((true ? 'true' : false) ? 't' : 'f');
>
> // aquí, se puede observar que la primera expresión se evalúa a 'true',
> // lo que hace que se evalúe a (bool)true, lo que devuelve la rama
> // 'verdadera' de la segunda expresión ternaria.
> ?>
>
>      
> ```
>
> </div>

> [!NOTE]
> La combinación de ternario corto (`?:`), sin embargo, es estable y se comporta de manera razonable. Esto evaluará el primer argumento que evalúa a un valor no-falsy. Tenga en cuenta que los valores indefinidos siempre emitirán un aviso.
>
> <div class="example">
>
> <div class="title">
>
> Combinación de ternario corto
>
> </div>
>
> ```
> <?php
> echo 0 ?: 1 ?: 2 ?: 3, PHP_EOL; //1
> echo 0 ?: 0 ?: 2 ?: 3, PHP_EOL; //2
> echo 0 ?: 0 ?: 0 ?: 3, PHP_EOL; //3
> ?>
>
>      
> ```
>
> </div>

## Operador de fusión Null

Otro operador corto útil es el operador "??" (o fusión null).

Asignar un valor por defecto

```php
<?php
// Ejemplo de uso para: Operador de fusión Null
$action = $_POST['action'] ?? 'default';

// el código anterior es equivalente a la siguiente estructura if/else
if (isset($_POST['action'])) {
    $action = $_POST['action'];
} else {
    $action = 'default';
}
?>

    
```

La expresión `(expr1) ?? (expr2)` devuelve \<expr2\> si \<expr1\> es `null`, y \<expr1\> en los otros casos.

En particular, este operador no emite una notificación o advertencia si la parte izquierda no existe, exactamente como `isset`. Esto es especialmente útil para las claves de los arrays.

> [!NOTE]
> Tenga en cuenta que el operador de fusión null es una expresión, y que no se evalúa como una variable, sino como el resultado de una expresión. Es importante saberlo si se desea devolver una variable por referencia. La expresión `return $foo ?? $bar;` es un retorno por referencia que no funciona y emite una advertencia.

> [!NOTE]
> El operador de fusión null tiene una precedencia baja. Esto significa que al mezclarlo con otros operadores (como la concatenación de strings o los operadores aritméticos) se requerirán paréntesis.
>
> ```
> <?php
> // Emite una advertencia de que $name es indefinida.
> print 'Mr. ' . $name ?? 'Anonymous';
>
> // Imprime "Mr. Anonymous"
> print 'Mr. ' . ($name ?? 'Anonymous');
> ?>
>
>    
> ```

> [!NOTE]
> Tenga en cuenta que el operador de fusión null permite una imbricación simple:
>
> <div class="example">
>
> <div class="title">
>
> Imbricación de la operación de fusión null
>
> </div>
>
> ```
> <?php
>
> $foo = null;
> $bar = null;
> $baz = 1;
> $qux = 2;
>
> echo $foo ?? $bar ?? $baz ?? $qux; // salida 1
>
> ?>
>
>      
> ```
>
> </div>
