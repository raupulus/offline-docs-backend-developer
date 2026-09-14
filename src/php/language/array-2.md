---
title: Arrays
source_url: https://www.php.net/manual/es/language.types.array.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/array.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 911fe79de
order: 4380
---

## Arrays

Para obtener una lista de todas las funciones de arrays, vea el capítulo [funciones de arrays](#ref.array) en la documentación.

Un `array` en PHP es en realidad un mapa ordenado. Un mapa es un tipo que asocia *valores* a *claves*. Este tipo está optimizado para varios usos diferentes; puede ser tratado como un array, lista (vector), tabla hash (una implementación de un mapa), diccionario, colección, pila, cola, y probablemente más. Como los valores `array` pueden ser otros `array`s, también son posibles árboles y `array`s multidimensionales.

La explicación de esas estructuras de datos está fuera del alcance de este manual, pero al menos se proporciona un ejemplo para cada una de ellas. Para más información, consulte la considerable literatura que existe sobre este amplio tema.

## Sintaxis

### Especificación con `array`

Un `array` puede ser creado usando la construcción del lenguaje `array`. Acepta cualquier número de pares `clave => valor` separados por comas como argumentos.

array(

clave

=\>

valor

,

clave2

=\>

valor2

,

clave3

=\>

valor3

, ... )

La coma después del último elemento del array es opcional y puede ser omitida. Esto se suele hacer para arrays de una sola línea, es decir, `array(1, 2)` es preferido sobre `array(1, 2, )`. Para arrays de múltiples líneas, por otro lado, la coma final es comúnmente usada, ya que permite una adición más fácil de nuevos elementos al final.

> [!NOTE]
> Existe una sintaxis corta para arrays que reemplaza `array()` con `[]`.

Un array simple

```php
<?php
$array1 = array(
    "foo" => "bar",
    "bar" => "foo",
);

// Usando la sintaxis corta de array
$array2 = [
    "foo" => "bar",
    "bar" => "foo",
];

var_dump($array1, $array2);
?>

    
```

La \<clave\> puede ser un `int` o un `string`. El \<valor\> puede ser de cualquier tipo.

Además, se producirán las siguientes conversiones de \<clave\>:

- `String`s que contienen `int`s decimales válidos, a menos que el número esté precedido por un signo `+`, serán convertidos al tipo `int`. Por ejemplo, la clave `"8"` se almacenará realmente bajo `8`. Por otro lado, `"08"` no será convertido, ya que no es un entero decimal válido.

- Los `float`s también se convierten a `int`s, lo que significa que la parte fraccionaria será truncada. Por ejemplo, la clave `8.7` se almacenará realmente bajo `8`.

- Los `bool`s se convierten a `int`s también, es decir, la clave `true` se almacenará realmente bajo `1` y la clave `false` bajo `0`.

- `Null` se convertirá en una cadena vacía, es decir, la clave `null` se almacenará realmente bajo `""`.

- Los `array`s y `object`s *no pueden* ser usados como claves. Hacerlo resultará en una advertencia: `Illegal offset type`.

Si múltiples elementos en la declaración del array usan la misma clave, solo el último será usado, ya que todos los demás son sobrescritos.

Ejemplo de conversión de tipos y sobrescritura

```php
<?php
$array = array(
    1    => "a",
    "1"  => "b",
    1.5  => "c",
    true => "d",
);
var_dump($array);
?>

    
```

El ejemplo anterior mostrará:

    array(1) {
      [1]=>
      string(1) "d"
    }

        

Como todas las claves en el ejemplo anterior se convierten a `1`, el valor será sobrescrito en cada nuevo elemento y el último valor asignado `"d"` es el único que queda.

Los arrays de PHP pueden contener claves `int` y `string` al mismo tiempo ya que PHP no distingue entre arrays indexados y asociativos.

Claves `int` y `string` mezcladas

```php
<?php
$array = array(
    "foo" => "bar",
    "bar" => "foo",
    100   => -100,
    -100  => 100,
);
var_dump($array);
?>

    
```

El ejemplo anterior mostrará:

    array(4) {
      ["foo"]=>
      string(3) "bar"
      ["bar"]=>
      string(3) "foo"
      [100]=>
      int(-100)
      [-100]=>
      int(100)
    }

La \<clave\> es opcional. Si no se especifica, PHP usará el incremento de la clave `int` más grande usada previamente.

Arrays indexados sin clave

```php
<?php
$array = array("foo", "bar", "hello", "world");
var_dump($array);
?>

    
```

El ejemplo anterior mostrará:

    array(4) {
      [0]=>
      string(3) "foo"
      [1]=>
      string(3) "bar"
      [2]=>
      string(5) "hello"
      [3]=>
      string(5) "world"
    }

Es posible especificar la clave solo para algunos elementos y omitirla para otros:

Claves no en todos los elementos

```php
<?php
$array = array(
         "a",
         "b",
    6 => "c",
         "d",
);
var_dump($array);
?>

    
```

El ejemplo anterior mostrará:

    array(4) {
      [0]=>
      string(1) "a"
      [1]=>
      string(1) "b"
      [6]=>
      string(1) "c"
      [7]=>
      string(1) "d"
    }

        

Como puede ver, el último valor `"d"` fue asignado a la clave `7`. Esto es porque la clave entera más grande antes de eso era `6`.

Ejemplo complejo de conversión de tipos y sobrescritura

Este ejemplo incluye todas las variaciones de conversión de tipos de claves y sobrescritura de elementos.

```php
<?php
$array = array(
    1    => 'a',
    '1'  => 'b', // el valor "a" será sobrescrito por "b"
    1.5  => 'c', // el valor "b" será sobrescrito por "c"
    -1 => 'd',
    '01'  => 'e', // como esto no es una cadena entera no sobrescribirá la clave para 1
    '1.5' => 'f', // como esto no es una cadena entera no sobrescribirá la clave para 1
    true => 'g', // el valor "c" será sobrescrito por "g"
    false => 'h',
    '' => 'i',
    null => 'j', // el valor "i" será sobrescrito por "j"
    'k', // el valor "k" se asigna a la clave 2. Esto es porque la clave entera más grande antes de eso era 1
    2 => 'l', // el valor "k" será sobrescrito por "l"
);

var_dump($array);
?>

    
```

El ejemplo anterior mostrará:

    array(7) {
      [1]=>
      string(1) "g"
      [-1]=>
      string(1) "d"
      ["01"]=>
      string(1) "e"
      ["1.5"]=>
      string(1) "f"
      [0]=>
      string(1) "h"
      [""]=>
      string(1) "j"
      [2]=>
      string(1) "l"
    }

Ejemplo de índice negativo

Al asignar una clave entera negativa `n`, PHP se asegurará de asignar la siguiente clave a `n+1`.

```php
     
<?php
$array = [];

$array[-5] = 1;
$array[] = 2;

var_dump($array);
?>

    
```

El ejemplo anterior mostrará:

         
    array(2) {
      [-5]=>
      int(1)
      [-4]=>
      int(2)
    }

        

> [!WARNING]
> Antes de PHP 8.3.0, asignar una clave entera negativa `n` asignaría la siguiente clave a `0`, el ejemplo anterior produciría por lo tanto:
>
> <div class="informalexample">
>
>     array(2) {
>       [-5]=>
>       int(1)
>       [0]=>
>       int(2)
>     }
>
>           
>
> </div>

### Acceso a elementos de array con sintaxis de corchetes

Los elementos de array pueden ser accedidos usando la sintaxis `array[clave]`.

Acceso a elementos de array

```php
<?php
$array = array(
    "foo" => "bar",
    42    => 24,
    "multi" => array(
         "dimensional" => array(
             "array" => "foo"
         )
    )
);

var_dump($array["foo"]);
var_dump($array[42]);
var_dump($array["multi"]["dimensional"]["array"]);
?>

    
```

El ejemplo anterior mostrará:

    string(3) "bar"
    int(24)
    string(3) "foo"

> [!NOTE]
> Antes de PHP 8.0.0, los corchetes y las llaves podían usarse indistintamente para acceder a elementos de array (por ejemplo, `$array[42]` y `$array{42}` harían lo mismo en el ejemplo anterior). La sintaxis de llaves fue deprecada a partir de PHP 7.4.0 y ya no es soportada a partir de PHP 8.0.0.

Desreferenciación de array

```php
<?php
function getArray() {
    return array(1, 2, 3);
}

$secondElement = getArray()[1];

var_dump($secondElement);
?>

    
```

> [!NOTE]
> Intentar acceder a una clave de array que no ha sido definida es lo mismo que acceder a cualquier otra variable no definida: se emitirá un mensaje de error de nivel `E_WARNING` (nivel `E_NOTICE` antes de PHP 8.0.0) y el resultado será `null`.

> [!NOTE]
> Desreferenciar un valor escalar que no es un `string` produce `null`. Antes de PHP 7.4.0, esto no emitía un mensaje de error. A partir de PHP 7.4.0, esto emite `E_NOTICE`; a partir de PHP 8.0.0, esto emite `E_WARNING`.

### Creación/modificación con sintaxis de corchetes

Un `array` existente puede ser modificado asignando valores explícitamente en él.

Esto se hace asignando valores al `array`, especificando la clave entre corchetes. La clave también puede ser omitida, resultando en un par de corchetes vacíos (`[]`).

\$arr\[

clave

\] =

valor

; \$arr\[\] =

valor

; //

clave

puede ser un

int

o

string

//

valor

puede ser cualquier valor de cualquier tipo

Si `$arr` no existe aún o está establecido a `null` o `false`, será creado, por lo que esto es también una forma alternativa de crear un `array`. Sin embargo, esta práctica está desaconsejada porque si `$arr` ya contiene algún valor (por ejemplo, `string` de una variable de petición) entonces este valor permanecerá en su lugar y `[]` podría en realidad representar el [operador de acceso a string](#language.types.string.substr). Siempre es mejor inicializar una variable mediante una asignación directa.

> [!NOTE]
> A partir de PHP 7.1.0, aplicar el operador de índice vacío en un string lanza un error fatal. Anteriormente, el string se convertía silenciosamente a un array.

> [!NOTE]
> A partir de PHP 8.1.0, crear un nuevo array a partir de un valor `false` está deprecado. Crear un nuevo array a partir de `null` y valores no definidos sigue estando permitido.

Para cambiar un cierto valor, asigne un nuevo valor a ese elemento usando su clave. Para eliminar un par clave/valor, llame a la función `unset` sobre él.

Uso de corchetes con arrays

```php
<?php
$arr = array(5 => 1, 12 => 2);

$arr[] = 56;    // Esto es lo mismo que $arr[13] = 56;
                // en este punto del script

$arr["x"] = 42; // Esto añade un nuevo elemento al
                // array con clave "x"

unset($arr[5]); // Esto elimina el elemento del array

var_dump($arr);

unset($arr);    // Esto elimina todo el array

var_dump($arr);
?>

    
```

> [!NOTE]
> Si no se especifica ninguna clave, la clave será el índice entero máximo existente + `1`. Si el array no tiene índices enteros positivos, la clave será `0`. A partir de PHP 8.3.0, también puede ser un entero negativo.
>
> Tenga en cuenta que el índice entero máximo usado para esto *no necesita existir actualmente en el `array`*. Solo necesita haber existido en el `array` en algún momento desde la última vez que el `array` fue reindexado. El siguiente ejemplo lo ilustra:
>
> <div class="informalexample">
>
> ```
> <?php
> // Crear un array simple.
> $array = array(1, 2, 3, 4, 5);
> print_r($array);
>
> // Ahora eliminar cada elemento, pero dejar el array en sí intacto:
> foreach ($array as $i => $value) {
>     unset($array[$i]);
> }
> print_r($array);
>
> // Añadir un elemento (note que la nueva clave es 5, en lugar de 0).
> $array[] = 6;
> print_r($array);
>
> // Reindexar:
> $array = array_values($array);
> $array[] = 7;
> print_r($array);
> ?>
>
>      
> ```
>
> El ejemplo anterior mostrará:
>
>     Array
>     (
>         [0] => 1
>         [1] => 2
>         [2] => 3
>         [3] => 4
>         [4] => 5
>     )
>     Array
>     (
>     )
>     Array
>     (
>         [5] => 6
>     )
>     Array
>     (
>         [0] => 6
>         [1] => 7
>     )
>
>          
>
> </div>

### Desestructuración de arrays

Los arrays pueden ser desestructurados usando la construcción de lenguaje `[]` (a partir de PHP 7.1.0) o `list`. Estas construcciones pueden ser usadas para desestructurar un array en variables distintas.

Desestructuración de array

```php
<?php
$source_array = ['foo', 'bar', 'baz'];

[$foo, $bar, $baz] = $source_array;

echo $foo, PHP_EOL;    // imprime "foo"
echo $bar, PHP_EOL;    // imprime "bar"
echo $baz, PHP_EOL;    // imprime "baz"
?>

    
```

La desestructuración de arrays puede ser usada en [`foreach`](#control-structures.foreach) para desestructurar un array multidimensional mientras se itera sobre él.

Desestructuración de array en foreach

```php
<?php
$source_array = [
    [1, 'John'],
    [2, 'Jane'],
];

foreach ($source_array as [$id, $name]) {
    echo "{$id}: '{$name}'\n";
}
?>

    
```

Los elementos del array serán ignorados si la variable no está proporcionada. La desestructuración de array siempre comienza en el índice `0`.

Ignorar elementos

```php
<?php
$source_array = ['foo', 'bar', 'baz'];

// Asignar el elemento en el índice 2 a la variable $baz
[, , $baz] = $source_array;

echo $baz;    // imprime "baz"
?>

    
```

A partir de PHP 7.1.0, los arrays asociativos también pueden ser desestructurados. Esto también permite una selección más fácil del elemento correcto en arrays indexados numéricamente, ya que el índice puede ser especificado explícitamente.

Desestructuración de arrays asociativos

```php
<?php
$source_array = ['foo' => 1, 'bar' => 2, 'baz' => 3];

// Asignar el elemento en el índice 'baz' a la variable $three
['baz' => $three] = $source_array;

echo $three, PHP_EOL;  // imprime 3

$source_array = ['foo', 'bar', 'baz'];

// Asignar el elemento en el índice 2 a la variable $baz
[2 => $baz] = $source_array;

echo $baz, PHP_EOL;    // imprime "baz"
?>

    
```

La desestructuración de arrays puede ser usada para intercambiar fácilmente dos variables.

Intercambio de dos variables

```php
<?php
$a = 1;
$b = 2;

[$b, $a] = [$a, $b];

echo $a, PHP_EOL;    // imprime 2
echo $b, PHP_EOL;    // imprime 1
?>

    
```

> [!NOTE]
> El operador de propagación (`...`) no está soportado en asignaciones.

> [!NOTE]
> Intentar acceder a una clave de array que no ha sido definida es lo mismo que acceder a cualquier otra variable no definida: se emitirá un mensaje de error de nivel `E_WARNING` (nivel `E_NOTICE` antes de PHP 8.0.0) y el resultado será `null`.

> [!NOTE]
> Desestructurar un valor escalar asigna `null` a todas las variables.

## Funciones útiles

Hay bastantes funciones útiles para trabajar con arrays. Vea la sección de [funciones de array](#ref.array).

> [!NOTE]
> La función `unset` permite eliminar claves de un `array`. Tenga en cuenta que el array *no* será reindexado. Si se desea un comportamiento de "eliminar y desplazar", el `array` puede ser reindexado usando la función `array_values`.
>
> <div class="example">
>
> <div class="title">
>
> Eliminación de elementos intermedios
>
> </div>
>
> ```
> <?php
> $a = array(1 => 'one', 2 => 'two', 3 => 'three');
>
> /* producirá un array que habría sido definido como
>    $a = array(1 => 'one', 3 => 'three');
>    y NO
>    $a = array(1 => 'one', 2 =>'three');
> */
> unset($a[2]);
> var_dump($a);
>
> $b = array_values($a);
> // Ahora $b es array(0 => 'one', 1 =>'three')
> var_dump($b);
> ?>
>
>     
> ```
>
> </div>

La estructura de control [`foreach`](#control-structures.foreach) existe específicamente para `array`s. Proporciona una forma fácil de recorrer un `array`.

## Lo que se debe y no se debe hacer con arrays

### ¿Por qué `$foo[bar]` está mal?

Siempre use comillas alrededor de un índice de array literal de cadena. Por ejemplo, `$foo['bar']` es correcto, mientras que `$foo[bar]` no lo es. Pero ¿por qué? Es común encontrar este tipo de sintaxis en scripts antiguos:

```php
<?php
$foo[bar] = 'enemy';
echo $foo[bar];
// etc
?>

    
```

Esto está mal, pero funciona. La razón es que este código tiene una constante no definida (`bar`) en lugar de un `string` (`'bar'` - note las comillas). Funciona porque PHP convierte automáticamente una *cadena desnuda* (una `string` sin comillas que no corresponde a ningún símbolo conocido) en un `string` que contiene la `string` desnuda. Por ejemplo, si no hay una constante definida llamada `bar`, entonces PHP sustituirá la `string` `'bar'` y la usará.

> [!WARNING]
> La retrocompatibilidad para tratar una constante no definida como cadena desnuda emite un error de nivel `E_NOTICE`. Esto ha sido deprecado a partir de PHP 7.2.0, y emite un error de nivel `E_WARNING`. A partir de PHP 8.0.0, ha sido eliminado y lanza una excepción `Error`.

Esto no significa que *siempre* deba poner comillas a la clave. No ponga comillas a claves que son [constantes](#language.constants) o [variables](#language.variables), ya que esto evitará que PHP las interprete.

Comillas en claves

```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', true);
ini_set('html_errors', false);

// Array simple:
$array = array(1, 2);
$count = count($array);

for ($i = 0; $i < $count; $i++) {
    echo "\nComprobando $i: \n";
    echo "Incorrecto: " . $array['$i'] . "\n";
    echo "Correcto: " . $array[$i] . "\n";
    echo "Incorrecto: {$array['$i']}\n";
    echo "Correcto: {$array[$i]}\n";
}
?>

     
```

El ejemplo anterior mostrará:

    Comprobando 0:
    Notice: Undefined index:  $i in /path/to/script.html on line 9
    Incorrecto:
    Correcto: 1
    Notice: Undefined index:  $i in /path/to/script.html on line 11
    Incorrecto:
    Correcto: 1

    Comprobando 1:
    Notice: Undefined index:  $i in /path/to/script.html on line 9
    Incorrecto:
    Correcto: 2
    Notice: Undefined index:  $i in /path/to/script.html on line 11
    Incorrecto:
    Correcto: 2

       

Más ejemplos para demostrar este comportamiento:

Más ejemplos

```php
<?php
// Mostrar todos los errores
error_reporting(E_ALL);

$arr = array('fruit' => 'apple', 'veggie' => 'carrot');

// Correcto
echo $arr['fruit'], PHP_EOL;  // apple
echo $arr['veggie'], PHP_EOL; // carrot

// Incorrecto. Esto no funciona y lanza un error de PHP debido a
// una constante no definida llamada fruit
//
// Error: Undefined constant "fruit"
try {
    echo $arr[fruit];
} catch (Error $e) {
    echo get_class($e), ': ', $e->getMessage(), PHP_EOL;
}

// Esto define una constante para demostrar lo que está pasando. El valor 'veggie'
// es asignado a una constante llamada fruit.
define('fruit', 'veggie');

// Note la diferencia ahora
echo $arr['fruit'], PHP_EOL;  // apple
echo $arr[fruit], PHP_EOL;    // carrot

// Lo siguiente está bien, ya que está dentro de una cadena. Las constantes no se buscan
// dentro de cadenas, por lo que no ocurre ningún error aquí
echo "Hello $arr[fruit]", PHP_EOL;      // Hello apple

// Con una excepción: las llaves que rodean arrays dentro de cadenas permiten que las constantes
// sean interpretadas
echo "Hello {$arr[fruit]}", PHP_EOL;    // Hello carrot
echo "Hello {$arr['fruit']}", PHP_EOL;  // Hello apple

// La concatenación es otra opción
echo "Hello " . $arr['fruit'], PHP_EOL; // Hello apple
?>

    
```

```php
<?php
// Esto no funcionará, y resultará en un error de análisis, como:
// Parse error: parse error, expecting T_STRING' or T_VARIABLE' or T_NUM_STRING'
// Esto, por supuesto, también se aplica al usar superglobals en cadenas
print "Hello $arr['fruit']";
print "Hello $_GET['foo']";
?>

    
```

Como se indica en la sección de [sintaxis](#language.types.array.syntax), lo que está dentro de los corchetes ('`[`' y '`]`') debe ser una expresión. Esto significa que el código como este funciona:

```php
<?php
echo $arr[somefunc($bar)];
?>

    
```

Este es un ejemplo de uso del valor de retorno de una función como índice del array. PHP también conoce las constantes:

```php
<?php
$error_descriptions[E_ERROR]   = "Ha ocurrido un error fatal";
$error_descriptions[E_WARNING] = "PHP emitió una advertencia";
$error_descriptions[E_NOTICE]  = "Esto es solo un aviso informal";
?>

    
```

Tenga en cuenta que `E_ERROR` también es un identificador válido, al igual que `bar` en el primer ejemplo. Pero el último ejemplo es en realidad lo mismo que escribir:

```php
<?php
$error_descriptions[1] = "Ha ocurrido un error fatal";
$error_descriptions[2] = "PHP emitió una advertencia";
$error_descriptions[8] = "Esto es solo un aviso informal";
?>

    
```

porque `E_ERROR` es igual a `1`, etc.

#### Entonces, ¿por qué está mal?

En algún momento en el futuro, el equipo de PHP podría querer añadir otra constante o palabra clave, o una constante en otro código podría interferir. Por ejemplo, ya está mal usar las palabras `empty` y `default` de esta manera, ya que son [palabras clave reservadas](#reserved).

> [!NOTE]
> Para reiterar, dentro de una `string` entre comillas dobles, es válido no rodear los índices de array con comillas, por lo que `"$foo[bar]"` es válido. Consulte los ejemplos anteriores para más detalles, así como la sección sobre [análisis de variables en cadenas](#language.types.string.parsing).

## Conversión a array

Para cualquiera de los tipos `int`, `float`, `string`, `bool` y `resource`, convertir un valor a un `array` resulta en un array con un solo elemento con índice cero y el valor del escalar que fue convertido. En otras palabras, `(array) $scalarValue` es exactamente lo mismo que `array($scalarValue)`.

Si un `object` es convertido a un `array`, el resultado es un `array` cuyos elementos son las propiedades del `object`. Las claves son los nombres de las variables miembro, con algunas excepciones notables: las propiedades enteras son inaccesibles; las variables privadas tienen el nombre de la clase antepuesto al nombre de la variable; las variables protegidas tienen un '\*' antepuesto al nombre de la variable. Estos valores antepuestos tienen bytes `NUL` a ambos lados. Las [propiedades tipadas](#language.oop5.properties.typed-properties) no inicializadas se descartan silenciosamente.

Conversión a un array

```php
    
<?php

class A {
    private $B;
    protected $C;
    public $D;
    function __construct()
    {
        $this->{1} = null;
    }
}

var_export((array) new A());
?>

   
```

El ejemplo anterior mostrará:

        
    array (
      '' . "\0" . 'A' . "\0" . 'B' => NULL,
      '' . "\0" . '*' . "\0" . 'C' => NULL,
      'D' => NULL,
      1 => NULL,
    )

Estos `NUL` pueden resultar en algún comportamiento inesperado:

Conversión de un objeto a un array

```php
<?php

class A {
    private $A; // Esto se convertirá en '\0A\0A'
}

class B extends A {
    private $A; // Esto se convertirá en '\0B\0A'
    public $AA; // Esto se convertirá en 'AA'
}

var_dump((array) new B());
?>

    
```

El ejemplo anterior mostrará:

    array(3) {
      ["BA"]=>
      NULL
      ["AA"]=>
      NULL
      ["AA"]=>
      NULL
    }

Lo anterior parecerá tener dos claves llamadas 'AA', aunque una de ellas en realidad se llama '\0A\0A'.

Convertir `null` a un `array` resulta en un `array` vacío.

## Comparación

Es posible comparar arrays con la función `array_diff` y con [operadores de array](#language.operators.array).

## Desempaquetado de arrays

Un array precedido por `...` será expandido en su lugar durante la definición del array. Solo arrays y objetos que implementan Traversable pueden ser expandidos. El desempaquetado de arrays con `...` está disponible a partir de PHP 7.4.0. Esto también se llama el operador de propagación.

Es posible expandir múltiples veces, y añadir elementos normales antes o después del operador `...`:

Desempaquetado de array simple

```php
<?php
// Usando sintaxis corta de array.
// También funciona con la sintaxis array().
$arr1 = [1, 2, 3];
$arr2 = [...$arr1]; // [1, 2, 3]
$arr3 = [0, ...$arr1]; // [0, 1, 2, 3]
$arr4 = [...$arr1, ...$arr2, 111]; // [1, 2, 3, 1, 2, 3, 111]
$arr5 = [...$arr1, ...$arr1]; // [1, 2, 3, 1, 2, 3]

function getArr() {
  return ['a', 'b'];
}
$arr6 = [...getArr(), 'c' => 'd']; // ['a', 'b', 'c' => 'd']

var_dump($arr1, $arr2, $arr3, $arr4, $arr5, $arr6);
?>

    
```

Desempaquetar un array con el operador `...` sigue la semántica de la función `array_merge`. Es decir, las claves de cadena posteriores sobrescriben las anteriores y las claves enteras se renumeran:

Desempaquetado de array con clave duplicada

```php
<?php
// clave de cadena
$arr1 = ["a" => 1];
$arr2 = ["a" => 2];
$arr3 = ["a" => 0, ...$arr1, ...$arr2];
var_dump($arr3); // ["a" => 2]

// clave entera
$arr4 = [1, 2, 3];
$arr5 = [4, 5, 6];
$arr6 = [...$arr4, ...$arr5];
var_dump($arr6); // [1, 2, 3, 4, 5, 6]
// Que es [0 => 1, 1 => 2, 2 => 3, 3 => 4, 4 => 5, 5 => 6]
// donde las claves enteras originales no se han conservado.
?>

    
```

> [!NOTE]
> Las claves que no son ni enteros ni cadenas lanzan un `TypeError`. Tales claves solo pueden ser generadas por un objeto Traversable.

> [!NOTE]
> Antes de PHP 8.1, el desempaquetado de un array que tiene una clave de cadena no está soportado:
>
> <div class="informalexample">
>
> ```
> <?php
>
> $arr1 = [1, 2, 3];
> $arr2 = ['a' => 4];
> $arr3 = [...$arr1, ...$arr2];
> // Fatal error: Uncaught Error: Cannot unpack array with string keys in example.php:5
>
> $arr4 = [1, 2, 3];
> $arr5 = [4, 5];
> $arr6 = [...$arr4, ...$arr5]; // funciona. [1, 2, 3, 4, 5]
> ?>
>
>     
> ```
>
> </div>

## Ejemplos

El tipo array en PHP es muy versátil. Aquí hay algunos ejemplos:

Versatilidad de los arrays

```php
<?php
// Esto:
$a = array( 'color' => 'red',
            'taste' => 'sweet',
            'shape' => 'round',
            'name'  => 'apple',
            4        // la clave será 0
          );

$b = array('a', 'b', 'c');

var_dump($a, $b);

// ...es completamente equivalente a esto:
$a = array();
$a['color'] = 'red';
$a['taste'] = 'sweet';
$a['shape'] = 'round';
$a['name']  = 'apple';
$a[]        = 4;        // la clave será 0

$b = array();
$b[] = 'a';
$b[] = 'b';
$b[] = 'c';

// Después de que el código anterior se ejecute, $a será el array
// array('color' => 'red', 'taste' => 'sweet', 'shape' => 'round',
// 'name' => 'apple', 0 => 4), y $b será el array
// array(0 => 'a', 1 => 'b', 2 => 'c'), o simplemente array('a', 'b', 'c').

var_dump($a, $b);
?>

   
```

Uso de array()

```php
<?php
// Array como (propiedad-)mapa
$map = array( 'version'    => 4,
              'OS'         => 'Linux',
              'lang'       => 'english',
              'short_tags' => true
            );
var_dump($map);

// claves estrictamente numéricas
// esto es lo mismo que array(0 => 7, 1 => 8, ...)
$array = array( 7,
                8,
                0,
                156,
                -10
              );
var_dump($array);

$switching = array(         10, // clave = 0
                    5    =>  6,
                    3    =>  7,
                    'a'  =>  4,
                            11, // clave = 6 (el máximo de los índices enteros era 5)
                    '8'  =>  2, // clave = 8 (¡entero!)
                    '02' => 77, // clave = '02'
                    0    => 12  // el valor 10 será sobrescrito por 12
                  );
var_dump($switching);

// array vacío
$empty = array();
var_dump($empty);
?>

   
```

Colección

```php
<?php
$colors = array('red', 'blue', 'green', 'yellow');

foreach ($colors as $color) {
    echo "¿Te gusta $color?\n";
}

?>

   
```

El ejemplo anterior mostrará:

    ¿Te gusta red?
    ¿Te gusta blue?
    ¿Te gusta green?
    ¿Te gusta yellow?

Cambiar los valores del `array` directamente es posible pasándolos por referencia.

Cambiar elemento en el bucle

```php
<?php
$colors = array('red', 'blue', 'green', 'yellow');

foreach ($colors as &$color) {
    $color = mb_strtoupper($color);
}
unset($color); /* asegúrese de que las escrituras siguientes a
$color no modificarán el último elemento del array */

print_r($colors);
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => RED
        [1] => BLUE
        [2] => GREEN
        [3] => YELLOW
    )

Este ejemplo crea un array basado en uno.

Índice basado en uno

```php
<?php
$firstquarter = array(1 => 'January', 'February', 'March');
print_r($firstquarter);
?>

    
```

El ejemplo anterior mostrará:

    Array
    (
        [1] => January
        [2] => February
        [3] => March
    )

Llenar un array

```php
<?php
// llenar un array con todos los elementos de un directorio
$handle = opendir('.');
while (false !== ($file = readdir($handle))) {
    $files[] = $file;
}
closedir($handle);

var_dump($files);
?>

    
```

Los `array`s están ordenados. El orden puede ser cambiado usando varias funciones de ordenación. Vea la sección de [funciones de array](#ref.array) para más información. La función `count` puede ser usada para contar el número de elementos en un `array`.

Ordenar un array

```php
<?php
sort($files);
print_r($files);
?>

    
```

Debido a que el valor de un `array` puede ser cualquier cosa, también puede ser otro `array`. Esto permite la creación de `array`s recursivos y multidimensionales.

Arrays recursivos y multidimensionales

```php
<?php
$fruits = array ( "fruits"  => array ( "a" => "orange",
                                       "b" => "banana",
                                       "c" => "apple"
                                     ),
                  "numbers" => array ( 1,
                                       2,
                                       3,
                                       4,
                                       5,
                                       6
                                     ),
                  "holes"   => array (      "first",
                                       5 => "second",
                                            "third"
                                     )
                );
var_dump($fruits);

// Algunos ejemplos para direccionar valores en el array anterior
echo $fruits["holes"][5];    // imprime "second"
echo $fruits["fruits"]["a"]; // imprime "orange"
unset($fruits["holes"][0]);  // elimina "first"

// Crear un nuevo array multidimensional
$juices["apple"]["green"] = "good";
var_dump($juices);
?>

    
```

La asignación de `array` siempre implica una copia de valores. Use el [operador de referencia](#language.operators) para copiar un `array` por referencia.

Copiado de arrays

```php
<?php
$arr1 = array(2, 3);
$arr2 = $arr1;
$arr2[] = 4; // $arr2 es cambiado,
             // $arr1 sigue siendo array(2, 3)

$arr3 = &$arr1;
$arr3[] = 4; // ahora $arr1 y $arr3 son iguales

var_dump($arr1, $arr2, $arr3);
?>

    
```
