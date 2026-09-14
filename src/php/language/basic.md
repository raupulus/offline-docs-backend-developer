---
title: Sintaxis básica
source_url: https://www.php.net/manual/es/language.oop5.basic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/basic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: fc068b485
order: 2410
---

## Sintaxis básica

## class

Una definición de clase básica comienza con la palabra clave `class`, seguida del nombre de la clase. Sigue un par de llaves que contienen la definición de las propiedades y los métodos que pertenecen a la clase.

El nombre de la clase puede ser cualquiera siempre que no sea una [palabra reservada](#reserved) en PHP. A partir de PHP 8.4.0, el uso de un solo guion bajo `_` como nombre de clase es obsoleto. Un nombre de clase válido comienza con una letra o un guion bajo, seguido de cualquier número de letras, dígitos o guiones bajos. En términos de expresión regular, esto se expresaría así: `^[a-zA-Z_\x80-\xff][a-zA-Z0-9_\x80-\xff]*$`.

Una clase puede contener sus propias [constantes](#language.oop5.constants), [variables](#language.oop5.properties) (llamadas "propiedades"), y funciones (llamadas "métodos").

Definición típica de una clase

```php
<?php
class SimpleClass
{
    // declaración de una propiedad
    public $var = 'un valor por omisión';

    // declaración de los métodos
    public function displayVar() {
        echo $this->var;
    }
}
?>

    
```

La pseudo-variable `$this` está disponible cuando un método es llamado desde un contexto de objeto. `$this` es el valor del objeto que llama.

> [!WARNING]
> Llamar a un método no estático estáticamente lanza una `Error`. Antes de PHP 8.0.0, esto generaba una notificación de obsolescencia, y `$this` no estaba definido.
>
> <div id="language.oop5.basic.class.this" class="example">
>
> <div class="title">
>
> Algunos ejemplos de la pseudo-variable `$this`
>
> </div>
>
> ```
> <?php
> class A
> {
>     function foo()
>     {
>         if (isset($this)) {
>             echo '$this está definido (';
>             echo get_class($this);
>             echo ")\n";
>         } else {
>             echo "\$this no está definido.\n";
>         }
>     }
> }
>
> class B
> {
>     function bar()
>     {
>         A::foo();
>     }
> }
>
> $a = new A();
> $a->foo();
>
> A::foo();
>
> $b = new B();
> $b->bar();
>
> B::bar();
> ?>
>
>      
> ```
>
> Resultado del ejemplo anterior en PHP 7:
>
>     $this está definido (A)
>
>     Deprecated: Non-static method A::foo() should not be called statically in %s  on line 27
>     $this no está definido.
>
>     Deprecated: Non-static method A::foo() should not be called statically in %s  on line 20
>     $this no está definido.
>
>     Deprecated: Non-static method B::bar() should not be called statically in %s  on line 32
>
>     Deprecated: Non-static method A::foo() should not be called statically in %s  on line 20
>     $this no está definido.
>
>          
>
> Resultado del ejemplo anterior en PHP 8:
>
>     $this está definido (A)
>
>     Fatal error: Uncaught Error: Non-static method A::foo() cannot be called statically in %s :27
>     Stack trace:
>     #0 {main}
>       thrown in %s  on line 27
>
>          
>
> </div>

### Clases de solo lectura (readonly)

A partir de PHP 8.2.0, una clase puede ser marcada con el modificador readonly. Marcar una clase como readonly añadirá el [modificador readonly](#language.oop5.properties.readonly-properties) a cada propiedad declarada, y evitará la creación de [propiedades dinámicas](#language.oop5.properties.dynamic-properties). Además, no es posible añadir su soporte utilizando el atributo `AllowDynamicProperties`. Cualquier intento de hacerlo desencadenará un error de compilación.

```php
<?php
#[\AllowDynamicProperties]
readonly class Foo {
}

// Fatal error: Cannot apply #[AllowDynamicProperties] to readonly class Foo
?>

        
```

Como ni las propiedades no tipadas ni las propiedades estáticas pueden ser marcadas con el modificador `readonly`, las clases readonly no pueden declararlas:

```php
<?php
readonly class Foo
{
    public $bar;
}

// Fatal error: Readonly property Foo::$bar must have type
?>

        
```

```php
<?php
readonly class Foo
{
    public static int $bar;
}

// Fatal error: Readonly class Foo cannot declare static properties
?>

        
```

Una clase readonly puede ser [extendida](#language.oop5.basic.extends) si, y solo si, la clase hija es también una clase readonly.

## La palabra clave `new`

Para crear una instancia de una clase, la palabra clave `new` debe ser utilizada. Un objeto será entonces sistemáticamente creado, a menos que tenga un [constructor](#language.oop5.decon) definido que lance una [excepción](#language.exceptions) en caso de error. Las clases deben ser definidas antes de la instanciación (en algunos casos, esto es imprescindible).

Si una variable `string` que contiene un nombre de clase es utilizada con `new`, una nueva instancia de esa clase será creada. Si la clase está en un espacio de nombres, su nombre completamente calificado debe ser utilizado.

> [!NOTE]
> Si no hay argumentos para pasar al constructor de la clase, los paréntesis después del nombre de la clase pueden ser omitidos.

Creación de una instancia

```php
<?php

class SimpleClass {
}

$instance = new SimpleClass();
var_dump($instance);

// Esto también puede realizarse con una variable:
$className = 'SimpleClass';
$instance = new $className(); // new SimpleClass()
var_dump($instance);
?>

    
```

A partir de PHP 8.0.0, el uso de `new` con expresiones arbitrarias es soportado. Esto permite instanciaciones más complejas si la expresión produce un `string`. La expresión debe estar rodeada de paréntesis.

Crear una instancia utilizando una expresión arbitraria

En el ejemplo dado, se muestran varios ejemplos de expresiones arbitrarias válidas que producen un nombre de clase. Esto muestra una llamada de función, una concatenación de cadenas y la constante `::class`.

```php
<?php

class ClassA extends \stdClass {}
class ClassB extends \stdClass {}
class ClassC extends ClassB {}
class ClassD extends ClassA {}

function getSomeClass(): string
{
    return 'ClassA';
}

var_dump(new (getSomeClass()));
var_dump(new ('Class' . 'B'));
var_dump(new ('Class' . 'C'));
var_dump(new (ClassD::class));
?>

    
```

Resultado del ejemplo anterior en PHP 8:

    object(ClassA)#1 (0) {
    }
    object(ClassB)#1 (0) {
    }
    object(ClassC)#1 (0) {
    }
    object(ClassD)#1 (0) {
    }

En el contexto de la clase, es posible crear un nuevo objeto con `new self` y `new parent`.

Al asignar una instancia ya creada de una clase a una variable, la nueva variable accederá a la misma instancia que el objeto que fue asignado. Este comportamiento es el mismo al pasar una instancia a una función. Una copia de un objeto ya creado puede ser realizada por [clonación](#language.oop5.cloning).

Asignación de un objeto

```php
<?php
class SimpleClass {
    public string $var;
}

$instance = new SimpleClass();

$assigned   =  $instance;
$reference  =& $instance;

$instance->var = '$assigned tendrá este valor';

$instance = null; // $instance y $reference se vuelven null

var_dump($instance);
var_dump($reference);
var_dump($assigned);
?>

    
```

El ejemplo anterior mostrará:

    NULL
    NULL
    object(SimpleClass)#1 (1) {
       ["var"]=>
         string(30) "$assigned tendrá este valor"
    }

Es posible crear una instancia de un objeto de varias maneras diferentes:

Crear nuevos objetos

```php
<?php

class Test
{
    public static function getNew()
    {
        return new static();
    }
}

class Child extends Test {}

$obj1 = new Test(); // Por el nombre de la clase
$obj2 = new $obj1; // A través de la variable que contiene un objeto
var_dump($obj1 !== $obj2);

$obj3 = Test::getNew(); // Por el método de clase
var_dump($obj3 instanceof Test);

$obj4 = Child::getNew(); // A través de un método de clase hija
var_dump($obj4 instanceof Child);

?>

    
```

El ejemplo anterior mostrará:

    bool(true)
    bool(true)
    bool(true)

Es posible acceder a un miembro de un objeto recién creado en una sola expresión:

Acceder a un miembro de un objeto recién creado

```php
<?php
echo (new DateTime())->format('Y'), PHP_EOL;

// los paréntesis alrededor son opcionales desde PHP 8.4.0
echo new DateTime()->format('Y'), PHP_EOL;
?>

    
```

Resultado del ejemplo anterior es similar a:

    2025
    2025

> [!NOTE]
> Anterior a PHP 7.1, los argumentos no son evaluados si no hay función constructora definida.

## Propiedades y métodos

Las propiedades y métodos de clase viven en "espacios de nombres" separados, por lo que es posible tener una propiedad y un método con el mismo nombre. Hacer referencia tanto a una propiedad como a un método tienen la misma notación, y el hecho de que una propiedad será accedida o que un método será llamado, depende solo del contexto, es decir, si el uso es un acceso variable o una llamada de función.

Acceso a propiedad contra llamada de método

```php
<?php
class Foo
{
    public $bar = 'propiedad';

    public function bar() {
        return 'método';
    }
}

$obj = new Foo();
echo $obj->bar, PHP_EOL, $obj->bar(), PHP_EOL;

    
```

El ejemplo anterior mostrará:

    propiedad
    método

Esto significa que llamar a una [función anónima](#functions.anonymous) que ha sido asignada a una propiedad no es posible directamente. En su lugar, la propiedad debe ser primero asignada a una variable. Es posible llamar a este tipo de propiedad directamente poniéndola entre paréntesis.

Llamar a una función anónima almacenada en una propiedad

```php
<?php
class Foo
{
    public $bar;

    public function __construct() {
        $this->bar = function() {
            return 42;
        };
    }
}

$obj = new Foo();

echo ($obj->bar)(), PHP_EOL;

    
```

El ejemplo anterior mostrará:

    42

## La palabra clave `extends`

Una clase puede heredar las constantes, métodos y propiedades de otra clase utilizando la palabra clave `extends` en la declaración. No es posible extender múltiples clases: una clase puede heredar solo de una clase base.

Las constantes, métodos y propiedades heredadas pueden ser redefinidas redeclarándolas con el mismo nombre que en la clase padre. Sin embargo, si la clase padre ha definido un método o constante como [final](#language.oop5.final), entonces estos no pueden ser redefinidos. Es posible acceder a los métodos o propiedades estáticas redefinidas haciendo referencia a ellos con el operador [parent::](#language.oop5.paamayim-nekudotayim).

> [!NOTE]
> A partir de PHP 8.1.0, las constantes pueden ser declaradas como finales.

Herencia simple de una clase

```php
<?php
class SimpleClass
{
    function displayVar()
    {
        echo "Clase padre\n";
    }
}

class ExtendClass extends SimpleClass
{
  // Redefinición del método padre
  function displayVar()
  {
    echo "Clase extendida\n";
    parent::displayVar();
  }
}

$extended = new ExtendClass();
$extended->displayVar();
?>

    
```

El ejemplo anterior mostrará:

    Clase extendida
    Clase padre

### Reglas de compatibilidad de firma

Al sobrecargar un método, su firma debe ser compatible con el método padre. De lo contrario, se emite un error fatal, o, anterior a PHP 8.0.0, se genera un error de nivel `E_WARNING`. Una firma es compatible si respeta las reglas de [varianza](#language.oop5.variance), hace un parámetro obligatorio opcional, y solo si todos los nuevos parámetros son opcionales y suavizan las reglas de visibilidad. Esto es conocido como el Principio de Sustitución de Liskov (Liskov Substitution Principle), o simplemente LSP. El [constructor](#language.oop5.decon.constructor), y los métodos `private` están excluidos de estas reglas de compatibilidad de firmas, y por lo tanto no emitirán un error fatal en caso de firma incompatible.

Métodos hijos compatibles

```php
<?php
class Base
{
    public function foo(int $a) {
        echo "Válido\n";
    }
}
class Extend1 extends Base
{
    function foo(int $a = 5)
    {
        parent::foo($a);
    }
}
class Extend2 extends Base
{
    function foo(int $a, $b = 5)
    {
        parent::foo($a);
    }
}
$extended1 = new Extend1();
$extended1->foo();
$extended2 = new Extend2();
$extended2->foo(1);

     
```

El ejemplo anterior mostrará:

    Válido
    Válido

Los siguientes ejemplos demuestran que un método hijo que elimina un parámetro, o hace un parámetro opcional obligatorio, no es compatible con el método padre.

Error fatal cuando un método hijo elimina un parámetro

```php
<?php
class Base
{
    public function foo(int $a = 5) {
        echo "Válido\n";
    }
}
class Extend extends Base
{
    function foo()
    {
        parent::foo(1);
    }
}

     
```

Resultado del ejemplo anterior en PHP 8 es similar a:

    Fatal error: Declaration of Extend::foo() must be compatible with Base::foo(int $a = 5) in /in/evtlq on line 13

Error fatal cuando un método hijo hace un parámetro opcional obligatorio

```php
<?php
class Base
{
    public function foo(int $a = 5) {
        echo "Válido\n";
    }
}
class Extend extends Base
{
    function foo(int $a)
    {
        parent::foo($a);
    }
}

     
```

Resultado del ejemplo anterior en PHP 8 es similar a:

    Fatal error: Declaration of Extend::foo(int $a) must be compatible with Base::foo(int $a = 5) in /in/qJXVC on line 13

> [!WARNING]
> Renombrar un parámetro de un método en una clase hija no es una incompatibilidad de firma. Sin embargo, esto es desaconsejado ya que resultará en una `Error` en tiempo de ejecución si los [argumentos nombrados](#functions.named-arguments) son utilizados.
>
> <div class="example">
>
> <div class="title">
>
> Error al usar argumentos nombrados y cuando los parámetros han sido renombrados en una clase hija
>
> </div>
>
> ```
> <?php
> class A {
>     public function test($foo, $bar) {}
> }
> class B extends A {
>     public function test($a, $b) {}
> }
> $obj = new B;
> // Pasar parámetros según el contrato A::test()
> $obj->test(foo: "foo", bar: "bar"); // ERROR!
>
>       
> ```
>
> Resultado del ejemplo anterior es similar a:
>
>     Fatal error: Uncaught Error: Unknown named parameter $foo in /in/XaaeN:14
>     Stack trace:
>     #0 {main}
>       thrown in /in/XaaeN on line 14
>
>           
>
> </div>

## ::class

La palabra clave `class` también se utiliza para la resolución de nombres de clases. Es posible obtener el nombre completamente calificado de una clase `ClassName` utilizando `ClassName::class`. Esto es particularmente útil con las clases que utilizan [espacios de nombres](#language.namespaces).

Resolución de nombre de clase

```php
<?php
namespace NS {
    class ClassName {
    }

    echo ClassName::class;
}
?>

     
```

El ejemplo anterior mostrará:

    NS\ClassName

> [!NOTE]
> La resolución del nombre de clase utilizando `::class` es una transformación durante la compilación. Es decir, en el instante en que se crea la cadena del nombre de la clase, aún no se ha producido ninguna carga automática. Por lo tanto, los nombres de clases se extienden incluso si la clase no existe. No se emite ningún error en este caso.
>
> <div id="language.oop5.basic.class.class.fail" class="example">
>
> <div class="title">
>
> Resolución de nombre de clase faltante
>
> </div>
>
> ```
> <?php
> print Does\Not\Exist::class;
> ?>
>
>      
> ```
>
> El ejemplo anterior mostrará:
>
>     Does\Not\Exist
>
>          
>
> </div>

A partir de PHP 8.0.0, `::class` puede ser utilizado en los objetos. Esta resolución ocurre durante la ejecución, y no durante la compilación. Sus efectos son los mismos que llamar `get_class` en el objeto.

Resolución del nombre de un objeto

```php
<?php
namespace NS {
    class ClassName {
    }

    $c = new ClassName();
    print $c::class;
}
?>

    
```

El ejemplo anterior mostrará:

    NS\ClassName

## Métodos y propiedades nullsafe

A partir de PHP 8.0.0, los métodos y propiedades también pueden ser accedidos con el operador "nullsafe": `?->`. El operador nullsafe funciona de manera idéntica al acceso de propiedades o métodos como si fuera arriba, con la excepción de que si el objeto que se está desreferenciando es `null` entonces `null` será devuelto en lugar de lanzar una excepción. Si la desreferencia se hace por una cadena, el resto de la cadena es ignorado.

El efecto es similar a rodear cada acceso con una verificación con `is_null` primero, pero más compacto.

Operador nullsafe

```php
<?php

// A partir de PHP 8.0.0, esta línea:
$result = $repository?->getUser(5)?->name;

// Es equivalente al siguiente bloque de código:
if (is_null($repository)) {
    $result = null;
} else {
    $user = $repository->getUser(5);
    if (is_null($user)) {
        $result = null;
    } else {
        $result = $user->name;
    }
}
?>

    
```

> [!NOTE]
> El operador nullsafe es mejor utilizado cuando null es considerado un valor válido y potencialmente esperado para una propiedad o valor de retorno de un método. Para indicar un error, lanzar una excepción es preferible.
