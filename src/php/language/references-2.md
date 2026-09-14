---
title: Las referencias
source_url: https://www.php.net/manual/es/language.references.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/references.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 50e6f42c8
order: 4370
---

## Las referencias

## ¿Qué es una referencia?

En PHP, las referencias son una forma de acceder al contenido de una misma variable utilizando varios nombres. Las referencias no son como los punteros en C: no se pueden realizar operaciones aritméticas de punteros sobre ellas, no son direcciones de memoria, etc. Se puede consultar [Lo que las referencias no son](#language.references.arent) para más información. De hecho, las referencias son alias en la [tabla de símbolos](#features.gc.refcounting-basics). Tenga en cuenta que en PHP, el nombre de una variable y su contenido son dos nociones distintas, lo que hace que se puedan dar varios nombres al mismo contenido. Se puede hacer la analogía con los ficheros bajo Unix, y sus nombres: los nombres de las variables son las entradas en un directorio, mientras que el contenido de la variable es el fichero en sí mismo. Las referencias en PHP pueden entonces ser consideradas similares a los enlaces bajo Unix.

## ¿Qué hacen las referencias?

Existen tres principales usos de las referencias: la [asignación por referencia](#language.references.whatdo.assign), el [paso por referencia](#language.references.whatdo.pass) y el [retorno por referencia](#language.references.whatdo.return). Esta sección introducirá estas operaciones, con enlaces a más detalles.

### Asignación por referencia

En este primer caso, las referencias PHP permiten que dos variables referencien el mismo contenido. Por ejemplo:

```php
<?php
$a =& $b;

     
```

Esta escritura indica que `$a` y `$b` apuntan al mismo contenido.

> [!NOTE]
> `$a` y `$b` son completamente iguales aquí: no es `$a` quien apunta a `$b`, o viceversa. Son `$a` y `$b` quienes apuntan al mismo contenido.

> [!NOTE]
> Si se asigna, pasa o devuelve una variable indefinida por referencia, se creará automáticamente.
>
> <div class="example">
>
> <div class="title">
>
> Uso de referencias con variables indefinidas
>
> </div>
>
> ```
> <?php
>
> function foo(&$var) {}
>
> foo($a); // $a es "creada" y asignada a NULL
>
> $b = array();
> foo($b['b']);
> var_dump(array_key_exists('b', $b)); // bool(true)
>
> $c = new stdClass();
> foo($c->d);
> var_dump(property_exists($c, 'd')); // bool(true)
>
>       
> ```
>
> </div>

La misma sintaxis puede ser utilizada con las funciones que devuelven referencias:

```php
<?php
$foo =& find_var($bar);

     
```

Utilizar la misma sintaxis con una función que *no* devuelve por referencia generará un error, al igual que utilizarla con el resultado del operador [new](#language.oop5.basic.new). Aunque los objetos se pasan como punteros, esto no es idéntico a las referencias como se explica en la sección los [Objetos y referencias](#language.oop5.references).

> [!WARNING]
> Si se asigna una referencia a una variable declarada como `global` en una función, la referencia solo será visible dentro de la función. Se puede evitar esto utilizando el array `$GLOBALS`.
>
> <div class="example">
>
> <div class="title">
>
> Referenciar variables globales desde funciones
>
> </div>
>
> ```
> <?php
> $var1 = "Variable Ejemplo";
> $var2 = "";
>
> function global_references($use_globals)
> {
>     global $var1, $var2;
>
>     if (!$use_globals) {
>         $var2 =& $var1; // visible solo en la función
>     } else {
>         $GLOBALS["var2"] =& $var1; // visible también en el contexto global
>     }
> }
>
> global_references(false);
> echo "var2 está definido como '$var2'\n"; // var2 está definido como ''
>
> global_references(true);
> echo "var2 está definido como '$var2'\n"; // var2 está definido como 'Variable Ejemplo'
>
>       
> ```
>
> </div>
>
> Vea `global $var;` como un atajo para `$var =& $GLOBALS['var'];`. Por lo tanto, asignar otra referencia a `$var` solo modifica la referencia local de la variable.

> [!NOTE]
> Si se asigna un valor a una variable que tiene referencias en una estructura [`foreach`](#control-structures.foreach), las referencias también serán modificadas.
>
> <div class="example">
>
> <div class="title">
>
> Referencias y estructura foreach
>
> </div>
>
> ```
> <?php
> $ref = 0;
> $row =& $ref;
>
> foreach (array(1, 2, 3) as $row) {
>     // hacer algo
> }
>
> echo $ref; // 3 - el último elemento del array iterado
>
>       
> ```
>
> </div>

Aunque no es estrictamente una asignación por referencia, las expresiones creadas con la estructura de lenguaje [`array()`](#function.array) pueden también comportarse como tales, prefijando con `&` el elemento del array. Aquí hay un ejemplo:

```php
<?php
$a = 1;
$b = array(2, 3);
$arr = array(&$a, &$b[0], &$b[1]);
$arr[0]++;
$arr[1]++;
$arr[2]++;
/* $a == 2, $b == array(3, 4); */
var_dump($a);
var_dump($b);

     
```

Note que las referencias dentro de los arrays pueden resultar peligrosas. Utilizar una asignación normal (no por referencia) con una referencia a la derecha del operador no transforma la parte izquierda de la asignación en referencia, pero las referencias dentro de los arrays son preservadas. Esto se aplica también a las llamadas de funciones con un array pasado por valor. Ejemplo:

```php
<?php

/* Asignación de variables escalares */
$a = 1;
$b =& $a;
$c = $b;
$c = 7; // $c no es una referencia; no hay cambio en $a o $b
print "a = {$a}; b = {$b}; c = {$c}\n\n";

/* Asignación de variables de tipo array */
$arr = array(1);
$a =& $arr[0]; // $a y $arr[0] son referencias al mismo valor
$arr2 = $arr; // NO es una asignación por referencia!
$arr2[0]++;
/* $a == 2, $arr == array(2) */
/* ¡Los contenidos de $arr son cambiados aunque no fuera una referencia! */
print "a = {$a}\n";
var_dump($arr);
var_dump($arr2);

     
```

En otras palabras, desde el punto de vista de las referencias, el comportamiento de los arrays está definido elemento por elemento; el comportamiento de cada elemento es independiente del estado de referencia del array que los contiene.

### Paso por referencia

El segundo interés de las referencias es permitir pasar variables por referencia. Esto se realiza haciendo referenciar el mismo contenido por una variable local a una función y por una variable del contexto llamante. Por ejemplo:

```php
<?php
function foo(&$var)
{
    $var++;
}

$a = 5;
foo($a);
print $a;

     
```

Después de la ejecución de esta porción de código, `$a` vale 6. Esto se debe a que, en la función `foo`, la variable `$var` apunta al mismo contenido que `$a`. Para más información sobre este tema, se puede consultar la sección [paso por referencia](#language.references.pass).

### Retorno por referencia

El tercer interés de las referencias es permitir el [retorno de valores por referencia](#language.references.return).

## Lo que las referencias no son

Como se ha visto anteriormente, las referencias no son punteros. Esto significa que el script siguiente no hará lo que se espera:

```php
<?php
function foo(&$var)
{
    $var =& $GLOBALS["baz"];
}

foo($bar);

    
```

Aquí, la variable `$var` en la función `foo` estará ligada a `$bar` en el llamante, pero luego estará ligada a `$GLOBALS["baz"]`. No es posible ligar `$bar` a otra cosa utilizando el mecanismo de referencias, ya que `$bar` no es accesible en la función `foo` (aunque está representada por `$var`, `$var` solo hace referencia al valor, y no tiene una ligadura en la [tabla de símbolos](#features.gc.refcounting-basics) del llamante). Se puede utilizar el [retorno por referencia](#language.references.return) para referenciar variables seleccionadas por la función.

## Paso por referencia

Se puede pasar una variable por referencia a una función, de manera que esta pueda modificarla. La sintaxis es la siguiente:

```php
<?php
function foo(&$var)
{
    $var++;
}

$a = 5;
foo($a);
print $a; // $a vale 6 ahora

    
```

> [!NOTE]
> No hay signo de referencia en la llamada de la función, solo en su definición. La definición de la función en sí misma es suficiente para pasar correctamente argumentos por referencia.

Los siguientes datos pueden ser pasados por referencia:

- Una variable, como en `foo($a)`

- Una referencia devuelta por una función:

```php
  <?php
  function foo(&$var)
  {
      $var++;
      print $var;
  }

  function &bar()
  {
   $a = 5;
   return $a;
  }

  foo(bar());

         
  ```

  Para más información, ver los detalles en [retorno por referencia](#language.references.return).

Todas las otras expresiones no deben ser pasadas por referencia, ya que el resultado será indefinido. Por ejemplo, los siguientes pasos por referencia son inválidos:

```php
<?php

function foo(&$var)
{
    $var++;
}

function bar() // Note la ausencia de &
{
   $a = 5;
   return $a;
}

foo(bar());    // Produce una notificación

foo($a = 5);    // Expresión, no una variable
foo(5);         // Produce un error fatal

class Foobar{}

foo(new Foobar()) // Produce una notificación desde PHP 7.0.7
                  // Notificación: Solo las variables deben ser pasadas por referencia.

    
```

## Devolver referencias

Devolver referencias es útil cuando se quiere utilizar una función para determinar a qué variable debe estar ligada una referencia. No utilice *no* el retorno por referencia para mejorar el rendimiento, el motor es suficientemente robusto para optimizar esto internamente. Devuelva referencias solo cuando haya buenas razones técnicas para hacerlo. Para devolver referencias, utilice esta sintaxis:

```php
<?php
class Foo
{
    public $value = 42;

    public function &getValue()
    {
        return $this->value;
    }
}

$obj = new Foo();
$myValue = &$obj->getValue(); // $myValue es una referencia de $obj->value, que vale 42.
$obj->value = 2;
echo $myValue;                // muestra el nuevo valor de $obj->value, es decir, 2.

    
```

En este ejemplo, se asigna un valor a la propiedad del objeto devuelta por la función `getValue`, y no a su copia, como sería el caso si no se hubiera utilizado la sintaxis de referencia.

> [!NOTE]
> A diferencia del paso de parámetro, aquí, se debe utilizar `&` en ambos lugares, tanto para indicar que se devuelve por referencia (no por copia), como para indicar que también se asigna por referencia (no por copia tampoco) para la variable `$myValue`.

> [!NOTE]
> Si se intenta devolver una referencia desde una función con la sintaxis: `return ($this->value);`, esto no funcionará *no* como se espera, y devolverá el resultado de la *expresión*, y no de la variable, por referencia. Solo se pueden devolver variables por referencia desde una función, y nada más.

Para utilizar la referencia devuelta, se debe utilizar la asignación por referencia:

```php
<?php

function &collector()
{
    static $collection = array();
    return $collection;
}

$collection = &collector();
// Ahora, la variable $collection es una variable por referencia que referencia el array static dentro de la función

$collection[] = 'foo';

print_r(collector());

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => foo
    )

> [!NOTE]
> Si la asignación se realiza sin el símbolo `&`, por ejemplo `$collection = collector();`, la variable `$collection` recibirá una copia del valor, y no la referencia devuelta por la función.

Para pasar la referencia devuelta a otra función que espera una referencia, se puede utilizar la siguiente sintaxis:

```php
<?php

function &collector()
{
  static $collection = array();
  return $collection;
}

array_push(collector(), 'foo');

    
```

> [!NOTE]
> Note que `array_push(&collector(), 'foo');` *no funcionará*, y resultará en un error fatal.

## Destruir una referencia

Cuando se destruye una referencia, solo se rompe el enlace entre el nombre de la variable y su contenido. Esto no significa que el contenido de la variable sea destruido. Por ejemplo:

```php
<?php
$a = 1;
$b =& $a;
unset($a);
var_dump($a);
var_dump($b);

    
```

Este ejemplo no destruirá `$b`, solo `$a`.

Una vez más, se puede comparar esta acción con la llamada `unlink` de Unix.

## Identificar una referencia

Muchas sintaxis de PHP están implementadas a través del mecanismo de referencia, y todo lo que se ha visto en cuanto a las ligaduras entre variables se aplica a estas sintaxis. Algunas construcciones, como el paso de argumentos y el retorno por referencia, han sido mencionadas anteriormente. Otras construcciones que utilizan referencias son las siguientes:

### Referencias globales

Cuando se declara una variable como `global $var`, se crea en realidad una referencia a una variable global. En otras palabras, esto es lo mismo que:

```php
<?php
$var =& $GLOBALS["var"];

     
```

Esto también significa que destruir la variable `$var` no resultará en la destrucción de la variable global.
