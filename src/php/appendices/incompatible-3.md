---
title: Cambios incompatibles con versiones anteriores
source_url: https://www.php.net/manual/es/migration71.incompatible.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration71/incompatible.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 19e812213
order: 470
---

## Cambios incompatibles con versiones anteriores

## Excepción al pasar muy pocos argumentos de función

Anteriormente, se emitía una advertencia al invocar funciones definidas por el usuario con muy pocos argumentos. Ahora, esta advertencia se ha promovido a una excepción de error. Esta modificación se aplica únicamente a las funciones definidas por el usuario, y no a las funciones internas. Por ejemplo:

```php
<?php
function test($param){}
test();

   
```

Resultado del ejemplo anterior es similar a:

    Fatal error: Uncaught ArgumentCountError: Too few arguments to function test(), 0 passed in %s on line %d and exactly 1 expected in %s:%d

## Prohibir las llamadas dinámicas a las funciones de introspección de ámbito

Se han prohibido las llamadas dinámicas para ciertas funciones (en forma de `$func()` o `array_map('extract', ...)`, etc.). Estas funciones inspeccionan o modifican otro ámbito, y presentan un comportamiento ambiguo y no fiable. Las funciones son las siguientes:

- `assert` - con una cadena como primer argumento

- `compact`

- `extract`

- `func_get_args`

- `func_get_arg`

- `func_num_args`

- `get_defined_vars`

- `mb_parse_str` - con un argumento

- `parse_str` - con un argumento

```php
<?php
(function () {
    $func = 'func_num_args';
    $func();
})();

   
```

El ejemplo anterior mostrará:

    Warning: Cannot call func_num_args() dynamically in %s on line %d

## Nombres de clases, interfaces y traits no válidos

Los siguientes nombres no se pueden utilizar para nombrar clases, interfaces o traits:

- `void`

- `iterable`

## Las conversiones de strings numéricos ahora respetan la notación científica

Las operaciones enteras y las conversiones sobre strings numéricos ahora respetan la notación científica. Esto incluye también la operación de cast `(int)` y las siguientes funciones: `intval` (donde la base es 10), `settype`, `decbin`, `decoct` y `dechex`.

## Correcciones al algoritmo `mt_rand`

`mt_rand` ahora utiliza por defecto la versión corregida del algoritmo Mersenne Twister. Si la salida determinista de `mt_rand` se ha invocado, entonces `MT_RAND_PHP` se puede utilizar como segundo parámetro opcional de `mt_srand` para preservar la antigua (e incorrecta) implementación.

## `rand` alias de `mt_rand` y `srand` alias de `mt_srand`

`rand` y `srand` son ahora alias de `mt_rand` y `mt_srand`, respectivamente. Esto significa que la salida para las siguientes funciones se ha modificado: `rand`, `shuffle`, `str_shuffle` y `array_rand`.

## Prohibir el carácter de control de eliminación ASCII en los identificadores

El carácter de control de eliminación ASCII (`0x7F`) no se puede utilizar en los identificadores que no están entre comillas.

## Cambios de `error_log` con el valor `syslog`

Si el parámetro INI `error_log` está definido en `syslog`, los niveles de error PHP se mapean a los niveles de error syslog. Esto aporta una diferenciación más fina en los registros de errores en comparación con el enfoque anterior donde todos los errores se registraban con el nivel de aviso únicamente.

## No llamar a los destructores en objetos incompletos

Los destructores ya no se llaman para los objetos que lanzan una excepción durante la ejecución de su constructor. En versiones anteriores, este comportamiento dependía de si el objeto era referenciado fuera del constructor (por ejemplo, por una traza de excepción).

## `call_user_func` manejo de argumentos de referencia

`call_user_func` ahora siempre generará una advertencia en las llamadas a funciones que esperan referencias como argumentos. Anteriormente, esto dependía de si la llamada estaba completamente calificada.

Además, `call_user_func` y `call_user_func_array` ya no abandonarán la llamada de función en este caso. La advertencia "referencia esperada" se emitirá, pero la llamada continuará como de costumbre.

## El operador de índice vacío ya no se admite para los strings

La aplicación del operador de índice vacío a un string (por ejemplo, `$str[] = $x`) lanza un error fatal en lugar de convertirlo silenciosamente en un array.

## Asignación mediante acceso por índice de string en un string vacío

La modificación de un string carácter por carácter en un string vacío ahora funciona de la misma manera que para los strings no vacíos; es decir, escribiendo en un índice fuera de rango del string con espacios, donde los tipos que no sean integer se convierten a integer, y solo se utiliza el primer carácter del string asignado. Anteriormente, los strings vacíos se trataban silenciosamente como un array vacío.

```php
<?php
$a = '';
$a[10] = 'foo';
var_dump($a);
?>

    
```

Resultado del ejemplo anterior en PHP 7.0:

    array(1) {
      [10]=>
      string(3) "foo"
    }

        

Resultado del ejemplo anterior en PHP 7.1:

    string(11) "          f"

## Directivas INI eliminadas

Las siguientes directivas INI se han eliminado:

- `session.entropy_file`

- `session.entropy_length`

- `session.hash_function`

- `session.hash_bits_per_character`

## El orden de los elementos en un array ha cambiado cuando se crean automáticamente durante las asignaciones por referencia

El orden de los elementos en un array ha cambiado cuando estos elementos se crearon automáticamente al referenciarlos en una asignación por referencia. Por ejemplo:

```php
<?php
$array = [];
$array["a"] =& $array["b"];
$array["b"] = 1;
var_dump($array);
?>

   
```

Resultado del ejemplo anterior en PHP 7.0:

    array(2) {
      ["a"]=>
      &int(1)
      ["b"]=>
      &int(1)
    }

       

Resultado del ejemplo anterior en PHP 7.1:

    array(2) {
      ["b"]=>
      &int(1)
      ["a"]=>
      &int(1)
    }

## Orden de clasificación de elementos iguales

El algoritmo de ordenación interno se ha mejorado, lo que puede dar lugar a un orden de ordenación diferente de los elementos que se comparaban como iguales anteriormente.

> [!NOTE]
> No se debe confiar en el orden de los elementos que se comparan como iguales; podría cambiar en cualquier momento.

## Mensaje de error para los errores E_RECOVERABLE

El mensaje de error para los errores E_RECOVERABLE se ha cambiado de "Catchable fatal error" a "Recoverable fatal error".

## Parámetro \$options de unserialize()

El elemento `allowed_classes` del parámetro \$options de `unserialize` ahora es estrictamente tipado, es decir, si se da un valor distinto de un `array` o un `bool`, unserialize() devuelve false y emite un `E_WARNING`.

## El constructor de DateTime incorpora microsegundos

`DateTime` y `DateTimeImmutable` ahora incorporan correctamente los microsegundos cuando se construyen a partir de la hora actual, ya sea explícitamente o con una cadena relativa (por ejemplo, `"first day of next month"`). Esto significa que las comparaciones ingenuas de dos instancias recién creadas ahora serán más propensas a devolver false en lugar de true:

```php
<?php
new DateTime() == new DateTime();
?>

    
```

## Conversiones de errores fatales en excepciones `Error`

En la extensión date, los datos de serialización inválidos para las clases `DateTime` o `DatePeriod`, o el fallo de la inicialización de la zona horaria a partir de datos serializados, ahora lanzarán una excepción `Error` a partir del método \_\_wakeup o \_\_set_state, en lugar de traducirse en un error fatal.

En la extensión DBA, las funciones de modificación de datos (como `dba_insert`) ahora lanzarán una excepción `Error` en lugar de desencadenar un error fatal capturable si la clave no contiene exactamente dos elementos.

En la extensión DOM, los contextos de validación de esquema o RelaxNG no válidos ahora lanzarán una excepción `Error` en lugar de resultar en un error fatal. Asimismo, el intento de registrar una clase de nodo que no extiende la clase base apropiada, o intenta leer una propiedad no válida o escribir en una propiedad de solo lectura, también lanzará una excepción `Error`.

En la extensión IMAP, las direcciones de correo electrónico más largas que 16385 bytes lanzarán una excepción `Error` en lugar de traducirse en un error fatal.

En la extensión Intl, no llamar al constructor padre en una clase que extiende `Collator` antes de llamar a los métodos padres ahora lanzará una `Error` en lugar de resultar en un error fatal recuperable. Además, la clonación de un objeto `Transliterator` ahora lanza una excepción `Error` en caso de fallo de la clonación del Transliterator interno en lugar de un error fatal.

En la extensión LDAP, proporcionar un tipo de modificación desconocido a `ldap_batch_modify` ahora lanzará una excepción `Error` en lugar de un error fatal.

En la extensión mbstring, las funciones `mb_ereg` y `mb_eregi` ahora lanzarán una excepción `ParseError` si se proporciona una expresión PHP no válida y se utiliza la opción 'e'.

En la extensión mcrypt, `mcrypt_encrypt` y `mcrypt_decrypt` ahora lanzarán una excepción `Error` en lugar de un error fatal si mcrypt no puede ser inicializada.

En la extensión mysqli, el intento de leer una propiedad no válida o de escribir en una propiedad de solo lectura ahora lanza una excepción `Error` en lugar de traducirse en un error fatal.

En la extensión Reflection, no recuperar un objeto de reflexión o recuperar una propiedad de objeto ahora lanza una excepción `Error` en lugar de traducirse en un error fatal.

En la extensión de sesión, los gestores de sesión personalizados que no devuelvan cadenas para los ID de sesión ahora lanzarán una excepción `Error` en lugar de provocar un error fatal cuando se llama a una función para generar un ID de sesión.

En la extensión SimpleXML, la creación de un atributo sin nombre o duplicado ahora lanzará una excepción `Error` en lugar de generar un error fatal.

En la extensión SPL, un intento de clonar un objeto `SplDirectory` ahora lanzará una excepción `Error` en lugar de generar un error fatal. Asimismo, llamar a ArrayIterator::append durante la iteración sobre un objeto también lanzará una excepción `Error`.

En la extensión estándar, la función `assert`, cuando se proporciona con un argumento de cadena como primer parámetro, ahora lanzará una excepción `ParseError` en lugar de un error fatal capturable si el código PHP no es válido. Asimismo, la llamada a `forward_static_call` fuera de un ámbito de clase ahora lanza una excepción `Error`.

En la extensión Tidy, la creación manual de un `tidyNode` lanzará una excepción `Error` en lugar de un error fatal.

En la extensión WDDX, una referencia circular durante la serialización ahora lanzará una excepción `Error` en lugar de un error fatal.

En la extensión XML-RPC, una referencia circular durante la serialización ahora lanzará una instancia de excepción `Error` en lugar de traducirse en un error fatal.

En la extensión Zip, el método ZipArchive::addGlob ahora lanzará una excepción `Error` en lugar de traducirse en un error fatal si el soporte de glob no está disponible.

## Las variables ligadas léxicamente no pueden reutilizar los nombres

Las variables ligadas a una [función anónima](#functions.anonymous) vía la construcción `use` no pueden utilizar el mismo nombre que cualquier [superglobals](#language.variables.predefined), `$this` o cualquier parámetro. Por ejemplo, todas estas definiciones de función resultarán en un error fatal:

```php
<?php
$f = function () use ($_SERVER) {};
$f = function () use ($this) {};
$f = function ($param) use ($param) {};

    
```

## Cambio de tipo de parámetro de long2ip()

`long2ip` ahora espera un `int` en lugar de `string`.

## Codificación y decodificación JSON

El parámetro INI `serialize_precision` ahora controla la precisión de serialización al codificar los `float`s.

La decodificación de una clave vacía ahora resulta en un nombre de propiedad vacío, en lugar de `_empty_` como nombre de propiedad.

```php
<?php
var_dump(json_decode(json_encode(['' => 1])));

   
```

Resultado del ejemplo anterior es similar a:

    object(stdClass)#1 (1) {
      [""]=>
      int(1)
    }

Cuando se proporciona el indicador `JSON_UNESCAPED_UNICODE` a `json_encode`, las secuencias U+2028 y U+2029 ahora se escapan.

## Modificaciones de la semántica de los parámetros de `mb_ereg` y `mb_eregi`

El tercer parámetro de las funciones `mb_ereg` y `mb_eregi` (`regs`) ahora se establece en un array vacío si no se ha hecho ninguna coincidencia. Anteriormente, el parámetro no habría sido modificado.

## Deprecación de flujos sslv2

El flujo SSLv2 se ha deprecado en OpenSSL.

## Prohibido "return;" para los retornos tipados en tiempo de compilación

Una declaración de retorno sin argumentos en las funciones que declaran un tipo de retorno ahora emite `E_COMPILE_ERROR` (excepto si el tipo de retorno se declara como `void`), incluso si la declaración de retorno nunca se alcanzaría.
