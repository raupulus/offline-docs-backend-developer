---
title: Manipulación de tipos
source_url: https://www.php.net/manual/es/language.types.type-juggling.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/type-juggling.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 50f76f269
order: 4550
---

## Manipulación de tipos

PHP no requiere una definición explícita de tipo en la declaración de variables. En este caso, el tipo de una variable se determina por el valor que almacena. Es decir, si se asigna un `string` a la variable `$var`, entonces `$var` será de tipo `string`. Si posteriormente se asigna un valor de tipo `int` a `$var`, pasará a ser de tipo `int`.

PHP puede intentar convertir automáticamente el tipo de un valor a otro en ciertos contextos. Los diferentes contextos que existen son:

- Numérico

- Cadena

- Lógico

- Entero y cadena

- Comparativo

- Función

> [!NOTE]
> Cuando un valor necesita ser interpretado como un tipo diferente, el valor en sí *no* cambia de tipo.

Para forzar a que una variable sea evaluada como un tipo determinado, consulte la sección sobre [moldeado de tipos](#language.types.typecasting). Para cambiar el tipo de una variable, consulte la función `settype`.

## Contextos numéricos

Este es el contexto cuando se utiliza un [operador aritmético](#language.operators.arithmetic).

En este contexto, si alguno de los operandos es de tipo `float` (o no puede interpretarse como un `int`), ambos operandos se interpretarán como `float`s, y el resultado también será un `float`. De lo contrario, los operandos se interpretarán como `int`s, y el resultado también será un `int`. A partir de PHP 8.0.0, si uno de los operandos no puede interpretarse, se lanzará un `TypeError`.

## Contextos de cadena

Este es el contexto cuando se utiliza `echo`, `print`, [interpolación de cadena](#language.types.string.parsing), o el [operador de concatenación de cadena](#language.operators.string).

En este contexto, el valor se interpretará como `string`. Si el valor no puede interpretarse, se lanzará un `TypeError`. Antes de PHP 7.4.0, se generaba un `E_RECOVERABLE_ERROR`.

## Contextos lógicos

Este es el contexto cuando se utilizan sentencias condicionales, el [operador ternario](#language.operators.comparison.ternary), o un [operador lógico](#language.operators.logical).

En este contexto, el valor se interpretará como `bool`.

## Contextos entero y cadena

Este es el contexto cuando se utilizan [operadores a nivel de bits](#language.operators.bitwise).

En este contexto, si todos los operandos son de tipo `string`, el resultado también será un `string`. De lo contrario, los operandos se interpretarán como `int`s, y el resultado también será un `int`. A partir de PHP 8.0.0, si uno de los operandos no puede interpretarse, se lanzará un `TypeError`.

## Contextos comparativos

Este es el contexto cuando se utiliza un [operador de comparación](#language.operators.comparison).

Las conversiones de tipo que ocurren en este contexto se explican en la tabla de Comparación con diversos tipos [tabla](#language.operators.comparison.types).

## Contextos de función

Este es el contexto cuando un valor se pasa a un parámetro tipado, propiedad o se devuelve desde una función que declara un tipo de retorno.

En este contexto, el valor debe ser de ese tipo. Existen dos excepciones: la primera es: si el valor es de tipo `int` y el tipo declarado es `float`, entonces el entero se convierte en un número de punto flotante. La segunda es: si el tipo declarado es un tipo *escalar* , el valor es convertible a un tipo escalar y el modo de tipado coercitivo está activo (por omisión), el valor puede convertirse en un valor escalar aceptado. Consulte a continuación para obtener una descripción de este comportamiento.

> [!WARNING]
> Las [funciones internas](#functions.internal) convierten automáticamente `null` a tipos escalares; este comportamiento está *DEPRECADO* a partir de PHP 8.1.0.

### Tipado coercitivo con declaraciones de tipo simples

- Declaración de tipo `bool`: el valor se interpreta como `bool`.

- Declaración de tipo `int`: el valor se interpreta como `int` si la conversión está bien definida. Por ejemplo, la cadena es [numérica](#language.types.numeric-strings).

- Declaración de tipo `float`: el valor se interpreta como `float` si la conversión está bien definida. Por ejemplo, la cadena es [numérica](#language.types.numeric-strings).

- Declaración de tipo `string`: el valor se interpreta como `string`.

### Tipado coercitivo con tipos de unión

Cuando `strict_types` no está habilitado, las declaraciones de tipo escalar están sujetas a conversiones implícitas limitadas. Si el tipo exacto del valor no es parte de la unión, entonces el tipo objetivo se elige en el siguiente orden de preferencia:

1.  `int`

2.  `float`

3.  `string`

4.  `bool`

Si el tipo existe en la unión y el valor puede ser coercionado al tipo bajo la semántica de verificación de tipos existente de PHP, entonces se elige el tipo. De lo contrario, se prueba con el siguiente tipo.

> [!CAUTION]
> Como excepción, si el valor es una cadena y tanto int como float son parte de la unión, el tipo preferido se determina por la semántica de [cadena numérica](#language.types.numeric-strings) existente. Por ejemplo, para `"42"` se elige `int`, mientras que para `"42.0"` se elige `float`.

> [!NOTE]
> Los tipos que no forman parte de la lista de preferencias anterior no son objetivos elegibles para coerción implícita. En particular, no ocurren coerciones implícitas a los tipos `null`, `false` y `true`.

Ejemplo de tipos siendo coercionados a un tipo parte de la unión

```php
<?php
// int|string
42    --> 42          // tipo exacto
"42"  --> "42"        // tipo exacto
new ObjectWithToString --> "Resultado de __toString()"
                      // objeto nunca compatible con int, retrocede a string
42.0  --> 42          // float compatible con int
42.1  --> 42          // float compatible con int
1e100 --> "1.0E+100"  // float demasiado grande para int, retrocede a string
INF   --> "INF"       // float demasiado grande para int, retrocede a string
true  --> 1           // bool compatible con int
[]    --> TypeError   // array no compatible con int o string

// int|float|bool
"45"    --> 45        // cadena numérica int
"45.0"  --> 45.0      // cadena numérica float

"45X"   --> true      // no es cadena numérica, retrocede a bool
""      --> false     // no es cadena numérica, retrocede a bool
"X"     --> true      // no es cadena numérica, retrocede a bool
[]      --> TypeError // array no compatible con int, float o bool
?>

    
```

## Moldeado de tipos

El moldeado de tipos convierte el valor a un tipo elegido escribiendo el tipo entre paréntesis antes del valor a convertir.

Moldeado de tipos

```php
<?php
$foo = 10;          // $foo es un entero
$bar = (bool) $foo; // $bar es un booleano

var_dump($bar);
?>

   
```

Los moldeados permitidos son:

(int)

\- moldear a

int

(bool)

\- moldear a

bool

(float)

\- moldear a

float

(string)

\- moldear a

string

(array)

\- moldear a

array

(object)

\- moldear a

object

(unset)

\- moldear a

NULL

El moldeado [`(void)`](#language.types.void.casting) también está disponible a partir de PHP 8.5.0, pero no es una conversión de valor. Se utiliza como una sentencia para descartar explícitamente el resultado de una expresión.

> [!WARNING]
> `(integer)` es un alias del moldeado `(int)`. `(boolean)` es un alias del moldeado `(bool)`. `(binary)` es un alias del moldeado `(string)`. `(double)` y `(real)` son alias del moldeado `(float)`. Estos moldeados no utilizan el nombre canónico del tipo y están deprecados a partir de PHP 8.5.0.

> [!WARNING]
> El alias de moldeado `(real)` fue deprecado a partir de PHP 7.4.0 y eliminado a partir de PHP 8.0.0.

> [!WARNING]
> El moldeado `(unset)` fue deprecado a partir de PHP 7.2.0. Tenga en cuenta que el moldeado `(unset)` es igual a asignar el valor `NULL` a la variable o llamada. El moldeado `(unset)` fue eliminado a partir de PHP 8.0.0.

> [!CAUTION]
> El moldeado `(binary)` y el prefijo `b` existen para soporte futuro. Actualmente `(binary)` y `(string)` son idénticos, sin embargo esto puede cambiar y no debe ser utilizado como dependencia.

> [!NOTE]
> Los espacios en blanco se ignoran dentro de los paréntesis de un moldeado. Por lo tanto, los siguientes dos moldeados son equivalentes:
>
> <div class="informalexample">
>
> ```
> <?php
> $foo = (int) $bar;
> $foo = ( int ) $bar;
> ?>
>
>      
> ```
>
> </div>

Moldeando literales `string`s y variables a `string`s binarios:

```php
<?php
$binary = (binary) $string;
$binary = b"cadena binaria";
?>

   
```

En lugar de moldear una variable a un `string`, también es posible encerrar la variable entre comillas dobles.

Diferentes mecanismos de moldeado

```php
<?php
$foo = 10;            // $foo es un entero
$str = "$foo";        // $str es una cadena
$fst = (string) $foo; // $fst también es una cadena

// Esto imprime que "son iguales"
if ($fst === $str) {
    echo "son iguales", PHP_EOL;
}
?>

   
```

Puede que no sea obvio exactamente qué ocurrirá al moldear entre ciertos tipos. Para más información, consulte estas secciones: [Conversión a booleano](#language.types.boolean.casting), [Conversión a entero](#language.types.integer.casting), [Conversión a float](#language.types.float.casting), [Conversión a cadena](#language.types.string.casting), [Conversión a array](#language.types.array.casting), [Conversión a objeto](#language.types.object.casting), [Conversión a recurso](#language.types.resource.casting), [Conversión a NULL](#language.types.null.casting), [Descartar un valor con `(void)`](#language.types.void.casting), [Las tablas de comparación de tipos](#types.comparisons)

> [!NOTE]
> Dado que PHP soporta indexación en `string`s mediante offsets utilizando la misma sintaxis que el indexado en `array`, el siguiente ejemplo se cumple para todas las versiones de PHP:
>
> <div class="example">
>
> <div class="title">
>
> Usando offset de array con una cadena
>
> </div>
>
> ```
> <?php
> $a    = 'car'; // $a es una cadena
> $a[0] = 'b';   // $a sigue siendo una cadena
> echo $a;       // bar
> ?>
>
>     
> ```
>
> </div>
>
> Consulte la sección titulada [Acceso a cadena por carácter](#language.types.string.substr) para más información.
