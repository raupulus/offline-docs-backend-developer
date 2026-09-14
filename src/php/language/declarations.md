---
title: Declaraciones de tipo
source_url: https://www.php.net/manual/es/language.types.declarations.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/declarations.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 911fe79de
order: 4410
---

## Declaraciones de tipo

Las declaraciones de tipos pueden ser añadidas a los argumentos de las funciones, valores de retorno, a partir de PHP 7.4.0, las propiedades de clase, y a partir de PHP 8.3.0, las constantes de clase. Aseguran que el valor es del tipo especificado en el momento de la llamada, de lo contrario se lanza un `TypeError`.

Cada tipo soportado por PHP, con la excepción del tipo `resource`, puede ser utilizado en una declaración de tipo por el usuario. Esta página contiene un registro de cambios de la disponibilidad de los diferentes tipos y la documentación sobre su uso en las declaraciones de tipo.

> [!NOTE]
> Cuando una clase implementa un método de interfaz o reimplementa un método que ya ha sido definido por una clase padre, debe ser compatible con la definición mencionada. Un método es compatible si sigue las reglas de [variance](#language.oop5.variance).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Añadido soporte para las constantes tipadas de clase, interfaz, trait y enum. |
| 8.2.0 | Añadido soporte de tipo DNF (Forma Normal Disyuntiva). |
| 8.2.0 | Añadido soporte del tipo `true`. |
| 8.2.0 | Los tipos `null` y `false` pueden ahora ser utilizados de manera autónoma. |
| 8.1.0 | Se ha añadido soporte para los tipos de intersección. |
| 8.1.0 | El retorno por referencia desde una función `void` ahora está desaconsejado. |
| 8.1.0 | Se ha añadido soporte para el tipo de retorno únicamente `never`. |
| 8.0.0 | Añadido soporte de `mixed` |
| 8.0.0 | Se ha añadido soporte para el tipo de retorno únicamente `static`. |
| 8.0.0 | Se ha añadido soporte para los tipos de unión. |
| 7.4.0 | Añadido soporte para el tipado de propiedades de clase. |
| 7.2.0 | Añadido soporte para `object`. |
| 7.1.0 | Añadido soporte para `iterable`. |
| 7.1.0 | Añadido soporte para `void`. |
| 7.1.0 | Se ha añadido soporte para los tipos nullable. |

## Notas de uso de los tipos atómicos

Los tipos atómicos tienen un comportamiento directo con algunas advertencias menores que se describen en esta sección.

### Tipos escalares

> [!WARNING]
> Los alias para los tipos escalares (`bool`, `int`, `float`, `string`) no son soportados. En su lugar, son tratados como nombres de clase o interfaz. Por ejemplo, utilizar `boolean` como una declaración de tipo requiere que el valor sea una [`instanceof`](#language.operators.type) de la clase o interfaz `boolean`, en lugar de tipo `bool`:
>
> <div class="informalexample">
>
> ```
> <?php
>     function test(boolean $param) {}
>     test(true);
> ?>
>
>      
> ```
>
> Resultado del ejemplo anterior en PHP 8:
>
>     Warning: "boolean" will be interpreted as a class name. Did you mean "bool"? Write "\boolean" to suppress this warning in /in/9YrUX on line 2
>
>     Fatal error: Uncaught TypeError: test(): Argument #1 ($param) must be of type boolean, bool given, called in - on line 3 and defined in -:2
>     Stack trace:
>     #0 -(3): test(true)
>     #1 {main}
>       thrown in - on line 2
>
>          
>
> </div>

### void

> [!NOTE]
> El retorno por referencia desde una función `void` está obsoleto a partir de PHP 8.1.0, ya que tal función es contradictoria. Anteriormente, ya emitía los siguientes `E_NOTICE` cuando se llamaba: `Only variable references should be returned by reference`.
>
> <div class="informalexample">
>
> ```
> <?php
> function &test(): void {}
> ?>
>
>       
> ```
>
> </div>

### Tipos Callable

Este tipo no puede ser utilizado como declaración de tipo de propiedad de clase.

> [!NOTE]
> No es posible especificar la firma de la función.

### Declaraciones de tipo sobre los parámetros de referencia

Si un parámetro pasado por referencia a una declaración de tipo, el tipo de la variable *solo se verifica* a la entrada de la función, al inicio de la llamada, pero no cuando la función es llamada nuevamente. Esto significa que una función puede modificar el tipo de la variable pasada por referencia.

Parámetro tipado pasado por referencia

```php
<?php
function array_baz(array &$param)
{
    $param = 1;
}
$var = [];
array_baz($var);
var_dump($var);
array_baz($var);
?>

    
```

Resultado del ejemplo anterior es similar a:

    int(1)

    Fatal error: Uncaught TypeError: array_baz(): Argument #1 ($param) must be of type array, int given, called in - on line 9 and defined in -:2
    Stack trace:
    #0 -(9): array_baz(1)
    #1 {main}
      thrown in - on line 2

## Notas de uso de los tipos compuestos

Las declaraciones de tipo compuesto están sujetas a algunas restricciones y realizarán un control de redundancia en el momento de la compilación para evitar errores simples.

> [!CAUTION]
> Anterior a PHP 8.2.0 y la introducción de los tipos DNF, no era posible combinar las intersecciones de tipo con las uniones de tipo.

### Tipos de uniones

> [!WARNING]
> No es posible combinar los dos tipos de singleton `false` y `true` juntos en una unión de tipo. Utilice en su lugar `bool`.

> [!CAUTION]
> Anterior a PHP 8.2.0, como `false` y `null` no podían ser utilizados como tipos autónomos, una unión de tipo compuesta únicamente de estos tipos no estaba permitida. Esto incluye los tipos siguientes: `false`, `false|null` y `?false`.

#### Azúcar sintáctico de tipo nullable

Una declaración de tipo de base única puede ser marcada como valor NULL anteponiendo el tipo de un signo de interrogación (`?`). Así `?T` y `T|null` son idénticos.

> [!NOTE]
> Esta sintaxis es soportada a partir de PHP 7.1.0, y es anterior a la soporte generalizado de los tipos de unión.

> [!NOTE]
> También es posible obtener argumentos nullable haciendo de `null` el valor por defecto. Esto no es recomendado, ya que si el valor por defecto es modificado en una clase hija, se desencadenará una violación de compatibilidad de tipo ya que el tipo `null` deberá ser añadido a la declaración de tipo. Este comportamiento también está obsoleto a partir de PHP 8.4.
>
> <div class="example">
>
> <div class="title">
>
> Forma antigua de hacer los argumentos nullable
>
> </div>
>
> ```
> <?php
> class C {}
>
> function f(C $c = null) {
>     var_dump($c);
> }
>
> f(new C);
> f(null);
> ?>
>
>       
> ```
>
> El ejemplo anterior mostrará:
>
>     object(C)#1 (0) {
>     }
>     NULL
>
>           
>
> </div>

### Tipos duplicados y redundantes

Para detectar errores simples en las declaraciones de tipo compuesto, los tipos redundantes que pueden ser detectados sin realizar una carga de clase resultarán en un error de compilación. Esto incluye:

- Cada tipo resuelto por nombre solo puede ocurrir una vez. Los tipos como `int|string|INT` o `Countable&Traversable&COUNTABLE` generan un error.

- El uso de `mixed` o `never` resulta en un error.

- Para los tipos de uniones:

  - Si `bool` es utilizado, `false` o `true` no puede ser utilizado adicionalmente.

  - Si `object` es utilizado, los tipos de clase no pueden ser utilizados adicionalmente.

  - Si `iterable` es utilizado, `array` y `Traversable` no pueden ser utilizados adicionalmente.

- Para los tipos de intersecciones:

  - El uso de un tipo que no es un tipo de clase genera un error.

  - El uso de `self`, `parent` o `static` resulta en un error.

- Para los tipos DNF:

  - Si un tipo más genérico es utilizado, el más restrictivo es redundante.

  - Uso de dos tipos de intersección idénticos.

> [!NOTE]
> Esto no garantiza que el tipo sea « mínimo », ya que esto requeriría cargar todos los tipos de clase utilizados.

Por ejemplo, si `A` y `B` son alias de clase, entonces `A|B` sigue siendo una unión de tipo legal, aunque sea posible reducir a `A` o `B`. Asimismo, si la clase `B extends A {}`, entonces `A|B` también es una unión de tipo legal, aunque podría ser reducida al tipo `A` únicamente.

```php
<?php
function foo(): int|INT {} // No autorizado
function foo(): bool|false {} // No autorizado
function foo(): int&Traversable {} // No autorizado
function foo(): self&Traversable {} // No autorizado

use A as B;
function foo(): A|B {} // No autorizado ("use" forma parte de la resolución de nombres)
function foo(): A&B {} // No autorizado ("use" forma parte de la resolución de nombres)

class_alias('X', 'Y');
function foo(): X|Y {} // Autorizado (la redundancia solo se conoce en tiempo de ejecución)
function foo(): X&Y {} // Autorizado (la redundancia solo se conoce en tiempo de ejecución)
?>

     
```

## Ejemplos

Declaración de tipo de clase de base

```php
<?php
class C {}
class D extends C {}

// Esta no extiende C.
class E {}

function f(C $c) {
    echo get_class($c)."\n";
}

f(new C);
f(new D);
f(new E);
?>

   
```

Resultado del ejemplo anterior en PHP 8:

    C
    D

    Fatal error: Uncaught TypeError: f(): Argument #1 ($c) must be of type C, E given, called in /in/gLonb on line 14 and defined in /in/gLonb:8
    Stack trace:
    #0 -(14): f(Object(E))
    #1 {main}
      thrown in - on line 8

Declaración de tipo de interfaz de base

```php
<?php
interface I { public function f(); }
class C implements I { public function f() {} }

// Esta no implementa I.
class E {}

function f(I $i) {
    echo get_class($i)."\n";
}

f(new C);
f(new E);
?>

   
```

Resultado del ejemplo anterior en PHP 8:

    C

    Fatal error: Uncaught TypeError: f(): Argument #1 ($i) must be of type I, E given, called in - on line 13 and defined in -:8
    Stack trace:
    #0 -(13): f(Object(E))
    #1 {main}
      thrown in - on line 8

Declaración de tipo de retorno de base

```php
<?php
function sum($a, $b): float {
    return $a + $b;
}

// Note que un float será devuelto.
var_dump(sum(1, 2));
?>

   
```

El ejemplo anterior mostrará:

    float(3)

Retorno de un objeto

```php
<?php
class C {}

function getC(): C {
    return new C;
}

var_dump(getC());
?>

   
```

El ejemplo anterior mostrará:

    object(C)#1 (0) {
    }

Declaración de tipo de argumento nullable

```php
    
<?php
class C {}

function f(?C $c) {
    var_dump($c);
}

f(new C);
f(null);
?>

   
```

El ejemplo anterior mostrará:

        
    object(C)#1 (0) {
    }
    NULL

Declaración de tipo de retorno nullable

```php
    
<?php
function get_item(): ?string {
    if (isset($_GET['item'])) {
        return $_GET['item'];
    } else {
        return null;
    }
}
?>

   
```

Declaración de tipo para las propiedades de clase

```php
<?php
class User {
    public static string $foo = 'foo';

    public int $id;
    public string $username;

    public function __construct(int $id, string $username) {
        $this->id = $id;
        $this->username = $username;
    }
}
?>

   
```

## Tipado estricto

Por defecto, PHP convertirá los valores de un tipo incorrecto al tipo escalar esperado siempre que sea posible. Por ejemplo, una función, que espera como parámetro una `string`, a la que se pasa un `int` recibirá una variable de tipo `string`.

Es posible activar el modo de tipado estricto archivo por archivo. En el modo estricto, solo una variable que coincida exactamente con el tipo esperado en la declaración será aceptada, de lo contrario se lanzará un `TypeError`. La única excepción a esta regla es que un valor de tipo `int` puede pasar una declaración de tipo `float`.

> [!WARNING]
> Las llamadas a funciones desde funciones internas no serán afectadas por la declaración `strict_types`.

Para activar el modo estricto, se utiliza la expresión [`declare`](#control-structures.declare) con la declaración `strict_types`:

> [!NOTE]
> El tipado estricto se aplica a las llamadas de función realizadas desde *dentro* de un archivo cuyo tipado estricto está activo, y no a las funciones declaradas en ese archivo. Si un archivo cuyo tipado estricto no está activado realiza una llamada a una función que ha sido definida en un archivo cuyo tipo estricto está activo, la preferencia del llamante (modo coercitivo) será respetada y el valor será forzado.

> [!NOTE]
> El tipado estricto solo está definido para las declaraciones de tipo escalar.

Tipado estricto para los valores de argumentos

```php
<?php
declare(strict_types=1);

function sum(int $a, int $b) {
    return $a + $b;
}

var_dump(sum(1, 2));
var_dump(sum(1.5, 2.5));
?>

   
```

Resultado del ejemplo anterior en PHP 8:

    int(3)

    Fatal error: Uncaught TypeError: sum(): Argument #1 ($a) must be of type int, float given, called in - on line 9 and defined in -:4
    Stack trace:
    #0 -(9): sum(1.5, 2.5)
    #1 {main}
      thrown in - on line 4

Tipado coercitivo para los valores de argumentos

```php
<?php
function sum(int $a, int $b) {
    return $a + $b;
}

var_dump(sum(1, 2));

// Estos serán forzados a enteros: ¡note la salida a continuación!
var_dump(sum(1.5, 2.5));
?>

   
```

El ejemplo anterior mostrará:

    int(3)
    int(3)

Tipado estricto para los valores de retorno

```php
<?php
declare(strict_types=1);

function sum($a, $b): int {
    return $a + $b;
}

var_dump(sum(1, 2));
var_dump(sum(1, 2.5));
?>

   
```

El ejemplo anterior mostrará:

    int(3)

    Fatal error: Uncaught TypeError: sum(): Return value must be of type int, float returned in -:5
    Stack trace:
    #0 -(9): sum(1, 2.5)
    #1 {main}
      thrown in - on line 5
