---
title: Las excepciones
source_url: https://www.php.net/manual/es/language.exceptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/exceptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 2320
---

## Las excepciones

> [!NOTE]
> Vea también la clase Exception

PHP tiene un manejo de excepciones similar al que ofrecen otros lenguajes de programación. Una excepción puede ser lanzada ("[`throw`](#language.exceptions)") y capturada ("[`catch`](#language.exceptions.catch)") en PHP. El código deberá estar rodeado de un bloque [`try`](#language.exceptions) para facilitar la captura de una excepción potencial. Cada [`try`](#language.exceptions) debe tener al menos un bloque [`catch`](#language.exceptions.catch) o [`finally`](#language.exceptions.finally) correspondiente.

Si una excepción es lanzada y el ámbito actual de la función no tiene un bloque [`catch`](#language.exceptions.catch), la excepción "subirá" la pila de llamadas de la función llamadora hasta encontrar un bloque [`catch`](#language.exceptions.catch) correspondiente. Todos los bloques [`finally`](#language.exceptions.finally) encontrados serán ejecutados. Si la pila de llamadas se desenrolla hasta el ámbito global sin encontrar un bloque [`catch`](#language.exceptions.catch) correspondiente, el programa será terminado con un error fatal a menos que se haya definido un manejador global de excepciones.

El objeto lanzado debe ser una [`instanceof`](#language.operators.type) Throwable. Intentar lanzar un objeto que no lo es resultará en un error fatal emitido por PHP.

A partir de PHP 8.0.0, la palabra clave [`throw`](#language.exceptions) es una expresión y puede ser utilizada en cualquier contexto de expresiones. En versiones anteriores era una declaración que debía estar en su propia línea.

## `catch`

Un bloque [`catch`](#language.exceptions.catch) define cómo reaccionar ante una excepción que ha sido lanzada. Un bloque [`catch`](#language.exceptions.catch) define uno o más tipos de excepciones o errores que puede manejar, y opcionalmente una variable en la que asignar la excepción. (Esta variable era requerida en versiones anteriores a PHP 8.0.0) El primer bloque [`catch`](#language.exceptions.catch) que una excepción o error lanzado encuentre y que corresponda al tipo del objeto lanzado manejará el objeto.

Varios bloques [`catch`](#language.exceptions.catch) pueden ser utilizados para atrapar diferentes clases de excepciones. La ejecución normal (cuando ninguna excepción es lanzada en el bloque [`try`](#language.exceptions)) continúa después del último bloque [`catch`](#language.exceptions.catch) definido en la secuencia. Las excepciones pueden ser lanzadas ([`throw`](#language.exceptions)) o relanzadas en un bloque [`catch`](#language.exceptions.catch). De lo contrario, la ejecución continuará después del bloque [`catch`](#language.exceptions.catch) que haya sido activado.

Cuando una excepción es lanzada, el código siguiente al tratamiento no será ejecutado y PHP intentará encontrar el primer bloque [`catch`](#language.exceptions.catch) correspondiente. Si una excepción no es capturada, un error fatal de PHP será enviado con un mensaje "`Uncaught Exception ...`" indicando que la excepción no pudo ser capturada a menos que un manejador de excepciones sea definido con la función `set_exception_handler`.

A partir de PHP 7.1, un bloque [`catch`](#language.exceptions.catch) puede especificar múltiples excepciones a través del carácter pipe (`|`). Esto es útil cuando diferentes excepciones de diferentes jerarquías de clases son tratadas de la misma manera.

A partir de PHP 8.0.0, el nombre de variable para la excepción capturada es opcional. Si no se especifica, el bloque [`catch`](#language.exceptions.catch) será siempre ejecutado pero no tendrá acceso al objeto lanzado.

## `finally`

Un bloque [`finally`](#language.exceptions.finally) también puede ser especificado después de bloques [`catch`](#language.exceptions.catch). El código dentro del bloque [`finally`](#language.exceptions.finally) será siempre ejecutado después de los bloques [`try`](#language.exceptions) y [`catch`](#language.exceptions.catch), independientemente de si una excepción ha sido lanzada, antes de continuar con la ejecución normal.

Una interacción notable es entre un bloque [`finally`](#language.exceptions.finally) y una declaración [`return`](#function.return). Si una declaración [`return`](#function.return) es encontrada dentro de los bloques [`try`](#language.exceptions) o [`catch`](#language.exceptions.catch), el bloque [`finally`](#language.exceptions.finally) será igualmente ejecutado. Además, la declaración [`return`](#function.return) es evaluada cuando es encontrada, pero el resultado será retornado después de que el bloque [`finally`](#language.exceptions.finally) sea ejecutado. Adicionalmente, si el bloque [`finally`](#language.exceptions.finally) contiene también una declaración [`return`](#function.return) el valor del bloque [`finally`](#language.exceptions.finally) es retornado.

Otra interacción notable es entre una excepción lanzada en un bloque [`try`](#language.exceptions), y una excepción lanzada en un bloque [`finally`](#language.exceptions.finally). Si una excepción es lanzada en ambos bloques, entonces, la excepción lanzada en el bloque [`finally`](#language.exceptions.finally) será la que se propagará, y la excepción lanzada en el bloque [`try`](#language.exceptions) será utilizada como excepción previa.

## Manejador global de excepciones

Si una excepción es permitida para subir hasta el ámbito global, puede ser capturada por un manejador de excepciones global si ha sido definido. La función `set_exception_handler` puede definir una función que será llamada en lugar de un bloque [`catch`](#language.exceptions.catch) si ningún otro bloque es invocado. El efecto es esencialmente idéntico a envolver el programa entero en un bloque [`try`](#language.exceptions)-[`catch`](#language.exceptions.catch) con esta función como [`catch`](#language.exceptions.catch).

## Notas

> [!NOTE]
> Las funciones internas de PHP utilizan principalmente el [Error reporting](#ini.error-reporting), solo las extensiones [orientadas a objetos](#language.oop5) utilizan excepciones. Sin embargo, los errores pueden ser fácilmente convertidos en excepciones con [ErrorException](#class.errorexception). Sin embargo, esta técnica solo funciona para errores no fatales.
>
> <div class="example">
>
> <div class="title">
>
> Convertir el error reporting en excepciones
>
> </div>
>
> ```
> <?php
> function exceptions_error_handler($severity, $message, $filename, $lineno) {
>     throw new ErrorException($message, 0, $severity, $filename, $lineno);
> }
>
> set_error_handler('exceptions_error_handler');
>
>      
> ```
>
> </div>

> [!TIP]
> La [biblioteca estándar PHP (SPL)](#intro.spl) proporciona un buen número [de excepciones adicionales](#spl.exceptions).

## Ejemplos

Lanzar una excepción

```php
<?php
function inverse($x) {
    if (!$x) {
        throw new Exception('División por cero.');
    }
    return 1/$x;
}

try {
    echo inverse(5) . "\n";
    echo inverse(0) . "\n";
} catch (Exception $e) {
    echo 'Excepción recibida: ',  $e->getMessage(), "\n";
}

// Continuar la ejecución
echo "¡Hola mundo!\n";

    
```

El ejemplo anterior mostrará:

    0.2
    Excepción recibida: División por cero.
    ¡Hola mundo!

Manejo de la excepción con un bloque [`finally`](#language.exceptions.finally)

```php
<?php
function inverse($x) {
    if (!$x) {
        throw new Exception('División por cero.');
    }
    return 1/$x;
}

try {
    echo inverse(5) . "\n";
} catch (Exception $e) {
    echo 'Excepción recibida: ',  $e->getMessage(), "\n";
} finally {
    echo "Primer fin.\n";
}

try {
    echo inverse(0) . "\n";
} catch (Exception $e) {
    echo 'Excepción recibida: ',  $e->getMessage(), "\n";
} finally {
    echo "Segundo fin.\n";
}

// Continuar la ejecución
echo "¡Hola mundo!\n";

    
```

El ejemplo anterior mostrará:

    0.2
    Primer fin.
    Excepción recibida: División por cero.
    Segundo fin.
    ¡Hola mundo!

Interacción entre el bloque [`finally`](#language.exceptions.finally) y [`return`](#function.return)

```php
<?php

function test() {
    try {
        throw new Exception('foo');
    } catch (Exception $e) {
        return 'catch';
    } finally {
        return 'finally';
    }
}

echo test();

    
```

El ejemplo anterior mostrará:

    finally

Herencia de una excepción

```php
<?php

class MyException extends Exception { }

class Test {
    public function testing() {
        try {
            try {
                throw new MyException('foo!');
            } catch (MyException $e) {
                // se relanza
                throw $e;
            }
        } catch (Exception $e) {
            var_dump($e->getMessage());
        }
    }
}

$foo = new Test;
$foo->testing();

    
```

El ejemplo anterior mostrará:

    string(4) "foo!"

Manejo de excepciones de captura múltiple

```php
<?php

class MyException extends Exception { }

class MyOtherException extends Exception { }

class Test {
    public function testing() {
        try {
            throw new MyException();
        } catch (MyException | MyOtherException $e) {
            var_dump(get_class($e));
        }
    }
}

$foo = new Test;
$foo->testing();

    
```

El ejemplo anterior mostrará:

    string(11) "MyException"

Omitir la variable capturada

Solo permitido en PHP 8.0.0 y versiones posteriores.

```php
<?php

function test() {
    throw new SpecificException('Oopsie');
}

try {
    test();
} catch (SpecificException) {
    print "Se lanzó una SpecificException, pero no nos importa con los detalles.";
}

    
```

El ejemplo anterior mostrará:

    Se lanzó una SpecificException, pero no nos importa con los detalles.

Throw como expresión

Solo permitido en PHP 8.0.0 y versiones posteriores.

```php
<?php

class SpecificException extends Exception {}

function test() {
    do_something_risky() or throw new Exception('No funcionó');
}

function do_something_risky() {
    return false; // Simular un fallo
}

try {
    test();
} catch (Exception $e) {
    print $e->getMessage();
}

    
```

El ejemplo anterior mostrará:

    No funcionó

Excepción en try y en finally

```php
<?php

try {
    try {
        throw new Exception(message: 'Third', previous: new Exception('Fourth'));
    } finally {
        throw new Exception(message: 'First', previous: new Exception('Second'));
    }
} catch (Exception $e) {
    var_dump(
        $e->getMessage(),
        $e->getPrevious()->getMessage(),
        $e->getPrevious()->getPrevious()->getMessage(),
        $e->getPrevious()->getPrevious()->getPrevious()->getMessage(),
    );
}

    
```

El ejemplo anterior mostrará:

    string(5) "First"
    string(6) "Second"
    string(5) "Third"
    string(6) "Fourth"

## Extender las Excepciones

Una clase de excepción definida por el usuario puede ser definida extendiendo la clase Exception integrada. Los miembros y las propiedades a continuación muestran lo que está accesible en la clase hija que deriva de la clase Exception integrada.

La clase de excepción integrada

```php
<?php
class Exception implements Throwable
{
    protected $message = 'Unknown exception';   // Mensaje de excepción
    private   $string;                          // caché de __toString
    protected $code = 0;                        // código de excepción definido por el usuario
    protected $file;                            // nombre de archivo fuente de la excepción
    protected $line;                            // línea fuente de la excepción
    private   $trace;                           // rastro de la pila de ejecución
    private   $previous;                        // excepción previa si excepción anidada

    public function __construct($message = '', $code = 0, ?Throwable $previous = null);

    final private function __clone();           // Inhibe la duplicación de excepciones.

    final public  function getMessage();        // mensaje de la excepción
    final public  function getCode();           // código de la excepción
    final public  function getFile();           // nombre del archivo fuente
    final public  function getLine();           // línea fuente
    final public  function getTrace();          // array de la pila de ejecución
    final public  function getPrevious();       // la excepción previa
    final public  function getTraceAsString();  // rastro en forma de string

    // Puede ser redefinido
    public function __toString();               // string formateado para la visualización
}

   
```

Si una clase extiende la clase Exception integrada y redefine el [constructor](#language.oop5.decon), se recomienda fuertemente que también llame a [parent::\_\_construct()](#language.oop5.paamayim-nekudotayim) para asegurarse de que todos los datos disponibles han sido correctamente asignados. El método [\_\_toString()](#language.oop5.magic) puede ser redefinido para proporcionar una salida personalizada cuando el objeto es presentado en forma de string.

> [!NOTE]
> Las excepciones no pueden ser clonadas. Intentar [clonar](#language.oop5.cloning) una Exception resultará en un error fatal `E_ERROR`.

Extender la clase Exception

```php
<?php
/**
 * Define una clase de excepción personalizada.
 */
class MyException extends Exception
{
    // Redefinir la excepción para que el mensaje no sea opcional.
    public function __construct($message, $code = 0, ?Throwable $previous = null) {
        // código

        // asegurarse de que todo está correctamente asignado
        parent::__construct($message, $code, $previous);
    }

    // Representación personalizada del objeto en forma de string.
    public function __toString() {
        return __CLASS__ . ": [{$this->code}]: {$this->message}\n";
    }

    public function customFunction() {
        echo "Una función personalizada para este tipo de excepción\n";
    }
}

/**
 * Crear una clase para probar la excepción
 */
class TestException
{
    public $var;

    const THROW_NONE    = 0;
    const THROW_CUSTOM  = 1;
    const THROW_DEFAULT = 2;

    function __construct($avalue = self::THROW_NONE) {

        switch ($avalue) {
            case self::THROW_CUSTOM:
                // Lanzar una excepción personalizada
                throw new MyException('1 no es un parámetro válido', 5);
                break;

            case self::THROW_DEFAULT:
                // Lanzar la por defecto.
                throw new Exception('2 no está permitido como parámetro', 6);
                break;

            default:
                // Ninguna excepción, el objeto será creado.
                $this->var = $avalue;
                break;
        }
    }
}

echo "# Ejemplo 1\n";
try {
    $o = new TestException(TestException::THROW_CUSTOM);
} catch (MyException $e) {      // Será capturada
    echo "MyException capturada\n", $e;
    $e->customFunction();
} catch (Exception $e) {        // Ignorado
    echo "Exception por defecto capturada\n", $e;
}

// Continuar la ejecución
var_dump($o); // Null

echo "\n\n# Ejemplo 2\n";
try {
    $o = new TestException(TestException::THROW_DEFAULT);
} catch (MyException $e) {      // No coincide con este tipo
    echo "MyException capturada\n", $e;
    $e->customFunction();
} catch (Exception $e) {        // Será capturada
    echo "Exception por defecto capturada\n", $e;
}

// Continuar la ejecución
var_dump($o); // Null

echo "\n\n# Ejemplo 3\n";
try {
    $o = new TestException(TestException::THROW_CUSTOM);
} catch (Exception $e) {        // Será capturada
    echo "Exception por defecto capturada\n", $e;
}

// Continuar la ejecución
var_dump($o); // Null

echo "\n\n# Ejemplo 4\n";
try {
    $o = new TestException();
} catch (Exception $e) {        // Saltado, ninguna excepción
    echo "Exception por defecto capturada\n", $e;
}

// Continuar la ejecución
var_dump($o); // TestException

   
```
