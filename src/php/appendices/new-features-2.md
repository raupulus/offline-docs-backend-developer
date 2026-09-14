---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration70.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 1422d543b
order: 380
---

## Nuevas características

## Declaraciones de tipo escalar

Las [declaraciones de tipo](#language.types.declarations) escalar vienen en dos modos: coercitivo (por defecto) o estricto. Los tipos de parámetros siguientes pueden ser forzados (ya sea coercitivo o estricto): los strings (`string`), los enteros (`int`), los decimales (`float`) y los valores booleanos (`bool`). Complementan los otros tipos introducidos en PHP 5: los nombres de clases, las interfaces, los arrays (`array`) y las funciones invocables (`callable`).

```php
<?php
// Modo coercitivo
function sumaEnteros(int ...$enteros)
{
    return array_sum($enteros);
}

var_dump(sumaEnteros(2, '3', 4.1));

   
```

El ejemplo anterior mostrará:

    int(9)

Para activar el modo estricto, se debe colocar una sola directiva [`declare`](#control-structures.declare) en la parte superior del fichero. Esto significa que el modo estricto de declaración de tipo escalar se configura por fichero. La directiva no solo afecta a la declaración de parámetros, sino también al tipo de retorno de la función (ver [las declaraciones de tipo de retorno](#language.types.declarations) en las funciones de PHP y las que provienen de extensiones).

En la referencia se pueden encontrar una documentación completa y ejemplos de declaraciones de tipo escalar: [Declaraciones de tipo](#language.types.declarations).

## Declaraciones de tipo de retorno

PHP 7 añade soporte para [declaraciones de tipo de retorno](#language.types.declarations). similar a las [declaraciones de tipo de argumento](#language.types.declarations), las declaraciones de tipo de retorno especifican el tipo del valor que devuelve la función. Los mismos [tipos](#language.types.declarations) que están disponibles para las declaraciones de tipo de retorno están disponibles para las declaraciones de tipo de argumento.

```php
<?php

function sumaArrays(array ...$arrays): array
{
    return array_map(function(array $array): int {
        return array_sum($array);
    }, $arrays);
}

print_r(sumaArrays([1,2,3], [4,5,6], [7,8,9]));

   
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => 6
        [1] => 15
        [2] => 24
    )

Una documentación completa y ejemplos de declaraciones de tipo de retorno pueden encontrarse en la referencia: [Declaraciones de tipo de retorno](#language.types.declarations).

## El operador de fusión nula

El operador de fusión nula (`??`) se ha añadido como un azúcar sintáctico para los casos de uso más comunes de necesitar una tercera conjunción con la función `isset`. Devuelve el primer operando si existe y no tiene un valor `null`; y devuelve el segundo operando en caso contrario.

```php
<?php
// Recupera el valor de $_GET['usuario'] y devuelve 'ninguno'
// si no existe.
$identificador = $_GET['usuario'] ?? 'ninguno';
// Esto es equivalente a:
$identificador = isset($_GET['usuario']) ? $_GET['usuario'] : 'ninguno';

// El operador permite encadenar: esto devolverá el primer
// valor definido respectivamente en $_GET['usuario'], $_POST['usuario']
// y 'ninguno'.
$identificador = $_GET['usuario'] ?? $_POST['usuario'] ?? 'ninguno';
?>

   
```

## El operador nave espacial

El operador nave espacial se utiliza para comparar dos expresiones. Devuelve -1, 0 o 1 cuando `$a` es respectivamente menor, igual o mayor que `$b`. Las comparaciones se realizan según [las reglas de comparación de tipos](#types.comparisons) habituales de PHP.

```php
<?php
// Enteros
echo 1 <=> 1; // 0
echo 1 <=> 2; // -1
echo 2 <=> 1; // 1

// Números de coma flotante
echo 1.5 <=> 1.5; // 0
echo 1.5 <=> 2.5; // -1
echo 2.5 <=> 1.5; // 1

// Strings
echo "a" <=> "a"; // 0
echo "a" <=> "b"; // -1
echo "b" <=> "a"; // 1
?>

   
```

## Arrays constantes con `define`

Los arrays (`Array`) constantes ahora pueden ser definidos con la función `define`. En PHP 5.6, solo podían ser definidos con [`const`](#language.constants.syntax).

```php
<?php
define('ANIMALES', [
    'perro',
    'gato',
    'pájaro'
]);

echo ANIMALES[1]; // muestra "gato"
?>

   
```

## Clases anónimas

Se ha añadido soporte para clases anónimas a través de la instanciación `new class`. Esto puede ser utilizado en lugar de definir toda una clase para objetos desechables:

```php
<?php
interface Logger {
    public function log(string $msg);
}

class Application {
    private $logger;

    public function getLogger(): Logger {
         return $this->logger;
    }

    public function setLogger(Logger $logger) {
         $this->logger = $logger;
    }
}

$app = new Application;
$app->setLogger(new class implements Logger {
    public function log(string $msg) {
        echo $msg;
    }
});

var_dump($app->getLogger());
?>

   
```

El ejemplo anterior mostrará:

    object(class@anonymous)#2 (0) {
    }

La documentación completa puede encontrarse en [la referencia de clases anónimas](#language.oop5.anonymous).

## Sintaxis de escape de punto de código Unicode

Toma un punto de código Unicode en forma hexadecimal, en una cadena entre comillas dobles o una sintaxis heredoc, para convertirlo en UTF-8. Cualquier punto de código válido es aceptado, siendo opcionales los ceros iniciales.

```php
<?php

echo "\u{aa}", PHP_EOL;
echo "\u{0000aa}", PHP_EOL;

echo "\u{9999}", PHP_EOL;

echo <<<EOT
\u{01f418}
EOT;

?>

   
```

El ejemplo anterior mostrará:

    ª
    ª (misma visualización que la línea anterior pero con ceros iniciales)
    香

## Closure::call

El método Closure::call se ha vuelto más eficiente. Una forma más corta de enlazar temporalmente una clausura al ámbito de un objeto e invocarla.

```php
<?php
class A {private $x = 1;}

// Código antes de PHP 7
$getX = function() {return $this->x;};
$getXCB = $getX->bindTo(new A, 'A'); // clausura intermedia
echo $getXCB();

// Código PHP 7+
$getX = function() {return $this->x;};
echo $getX->call(new A);

   
```

El ejemplo anterior mostrará:

    1
    1

## `unserialize` filtrado

Esta funcionalidad tiene como objetivo garantizar una mayor seguridad cuando se realiza la deserialización de objetos con datos no confiables. Evita posibles inyecciones de código permitiendo al desarrollador crear una lista blanca de las clases que pueden ser deserializadas.

```php
<?php

// Convierte todos los objetos en un objeto __PHP_Incomplete_Class
$data = unserialize($foo, ["allowed_classes" => false]);

// Convierte todos los objetos en un objeto __PHP_Incomplete_Class excepto aquellos de MyClass y MyClass2
$data = unserialize($foo, ["allowed_classes" => ["MyClass", "MyClass2"]]);

// Comportamiento por defecto (el mismo que cuando se omite el segundo argumento) que acepta todas las clases
$data = unserialize($foo, ["allowed_classes" => true]);

   
```

## `IntlChar`

La nueva clase `IntlChar` expone la funcionalidad ICU adicional. La clase en sí define un número de métodos estáticos y constantes que pueden ser utilizados para manipular los caracteres Unicode.

```php
<?php

printf('%x', IntlChar::CODEPOINT_MAX);
echo IntlChar::charName('@');
var_dump(IntlChar::ispunct('!'));

   
```

El ejemplo anterior mostrará:

    10ffff
    COMMERCIAL AT
    bool(true)

Para usar esta clase, debe instalar la extensión [Intl](#book.intl).

## Expectativas

Las expectativas son una mejora retrocompatible a la antigua función `assert`. Ofrecen aserciones de muy bajo costo en el código de producción y permiten lanzar excepciones personalizadas cuando la aserción falla.

Aunque la antigua API sigue siendo mantenida por razones de compatibilidad, la función `assert` ahora es una construcción del lenguaje, permitiendo que el primer parámetro sea una expresión en lugar de un `string` a evaluar o un `bool` a probar.

```php
<?php
ini_set('assert.exception', 1);

class CustomError extends AssertionError {}

assert(false, new CustomError('Un mensaje de error'));
?>

   
```

El ejemplo anterior mostrará:

    Fatal error: Uncaught CustomError: Un mensaje de error

Se pueden encontrar más detalles sobre esta funcionalidad, incluyendo cómo configurarla en entornos de desarrollo y producción, en la sección de expectativas en la referencia de la función `assert`.

## Agrupar las declaraciones `use`

Las clases, funciones y constantes importadas desde el mismo [`namespace`](#language.namespaces.definition) ahora pueden ser agrupadas en una sola instrucción [`use`](#language.namespaces.importing).

```php
<?php
// Código antes de PHP 7
use some\namespace\ClassA;
use some\namespace\ClassB;
use some\namespace\ClassC as C;

use function some\namespace\fn_a;
use function some\namespace\fn_b;
use function some\namespace\fn_c;

use const some\namespace\ConstA;
use const some\namespace\ConstB;
use const some\namespace\ConstC;

// Código PHP 7+
use some\namespace\{ClassA, ClassB, ClassC as C};
use function some\namespace\{fn_a, fn_b, fn_c};
use const some\namespace\{ConstA, ConstB, ConstC};
?>

   
```

## Expresiones de retorno de generador

Esta funcionalidad se basa en la funcionalidad de generador introducida en PHP 5.5. Permite usar una instrucción `return` en un generador para devolver una expresión final (el retorno por referencia no está permitido). Este valor puede ser extraído usando el nuevo método `Generator::getReturn()`, que solo puede ser usado cuando el generador ha terminado de producir valores.

```php
<?php

$gen = (function() {
    yield 1;
    yield 2;

    return 3;
})();

foreach ($gen as $val) {
    echo $val, PHP_EOL;
}

echo $gen->getReturn(), PHP_EOL;

   
```

El ejemplo anterior mostrará:

    1
    2
    3

Es muy práctico poder devolver explícitamente un valor final de un generador. Esto permite que un valor final, susceptible de ser manejado especialmente por el código cliente que ejecuta el generador, sea devuelto por el generador (posiblemente a partir de alguna forma de cálculo de corrutina). Esto es mucho más simple que forzar al código cliente a verificar primero si el valor final ha sido producido, y luego manejar específicamente el valor cuando sea el caso.

## Delegación de generador

Los generadores ahora pueden ser delegados automáticamente a otro generador, un objeto `Traversable` o un `array`, usando [`yield from`](#control-structures.yield.from), sin necesidad de recurrir a un código repetitivo.

```php
<?php
function gen()
{
    yield 1;
    yield 2;
    yield from gen2();
}

function gen2()
{
    yield 3;
    yield 4;
}

foreach (gen() as $val)
{
    echo $val, PHP_EOL;
}
?>

   
```

El ejemplo anterior mostrará:

    1
    2
    3
    4

## División de enteros con `intdiv`

La nueva función `intdiv` devuelve el resultado de la división de enteros realizada sobre sus operandos.

```php
<?php
var_dump(intdiv(10, 3));
?>

   
```

El ejemplo anterior mostrará:

    int(3)

## Opciones de sesión

La función `session_start` ahora acepta un `array` de opciones que anulan [las directivas de configuración de sesión](#session.configuration) configuradas manualmente en el fichero php.ini.

Estas opciones también han extendido el soporte para la opción [session.lazy_write](#ini.session.lazy-write), que está habilitada por defecto y hace que PHP sobrescriba los ficheros de sesión solo si los datos de sesión se han actualizado, y la opción `read_and_close`, que solo se puede pasar a la función `session_start` para indicar si los datos de sesión se deben leer antes de que la sesión se cierre sin cambios.

Por ejemplo, para establecer [session.cache_limiter](#ini.session.cache-limiter) a `private` y cerrar inmediatamente la sesión después de leerla:

```php
<?php
session_start([
    'cache_limiter' => 'private',
    'read_and_close' => true,
]);
?>

   
```

## `preg_replace_callback_array`

La nueva función `preg_replace_callback_array` permite que el código se escriba de manera más limpia usando la función `preg_replace_callback`. Antes de PHP 7, se debía ejecutar una función de retrollamada por cada expresión regular, lo que requería que dicha función de retrollamada estuviera repleta de bifurcaciones (branching).

Ahora, las funciones de retrollamada se pueden registrar para cada expresión regular usando un array asociativo, donde la clave es una expresión regular que tiene la función de retrollamada como valor.

## Funciones CSPRNG

Se han añadido dos nuevas funciones para generar criptográficamente integers y strings seguros de manera multiplataforma: `random_bytes` y `random_int`.

## La función `list` ahora puede desempaquetar objetos que implementan `ArrayAccess`

Anteriormente, la función `list` no podía operar al 100% sobre objetos que implementaban `ArrayAccess`. Ahora esto ha sido corregido.

## Otras funcionalidades

- Se ha añadido acceso a los miembros de la clase (atributos y métodos) durante la clonación. Ejemplo, `(clone $foo)->bar()`.
