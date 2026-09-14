---
title: Propiedades
source_url: https://www.php.net/manual/es/language.oop5.properties.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/properties.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 801e7a15e
order: 2560
---

## Propiedades

Las variables dentro de una clase se denominan *propiedades*. También pueden encontrarse bajo otros nombres como *campos*, pero para esta documentación se utilizará *propiedad*. Se definen utilizando al menos un modificador (como [???](#language.oop5.visibility), [???](#language.oop5.static), o, a partir de PHP 8.1.0, [readonly](#language.oop5.properties.readonly-properties)), seguido opcionalmente (excepto para las propiedades `readonly`), a partir de PHP 7.4, de una declaración de tipo, seguida de una declaración clásica de variable. Esta declaración puede incluir una inicialización, pero esta debe ser un valor [constante](#language.constants)

> [!NOTE]
> Una manera obsoleta de declarar una propiedad de clase es utilizar la palabra clave `var` en lugar de un modificador.

> [!NOTE]
> Una propiedad declarada sin modificador de [???](#language.oop5.visibility) será declarada como `public`.

Dentro de los métodos de clases, las propiedades no estáticas pueden ser llamadas utilizando la sintaxis `->` (operador de objeto) : `$this->property` (donde `property` es el nombre de la propiedad). Las propiedades estáticas pueden ser llamadas utilizando la sintaxis `::` (dos puntos) : `self::$property`. Consulte la documentación sobre [???](#language.oop5.static) para más información sobre la diferencia entre las propiedades estáticas y no estáticas.

La pseudo-variable `$this` está disponible dentro de cualquier método, cuando este método es llamado dentro de un objeto. `$this` es el valor del objeto que llama.

Declaraciones de propiedades

```php
<?php
class SimpleClass
{
   public $var1 = 'hello ' . 'world';
   public $var2 = <<<EOD
hello world
EOD;
   public $var3 = 1+2;
   // declaración de propiedad no válida :
   public $var4 = self::myStaticMethod();
   public $var5 = $myVar;

   // Declaraciones válidas de propiedades :
   public $var6 = myConstant;
   public $var7 = [true, false];
   public $var8 = <<<'EOD'
hello world
EOD;

   // Sin modificador de visibilidad :
   static $var9;
   readonly int $var10;
}
?>

   
```

> [!NOTE]
> Existen diversas funciones que permiten gestionar clases y objetos. Ver la referencia sobre las [Funciones Clases/Objetos](#ref.classobj).

## Declaraciones de tipos

A partir de PHP 7.4.0, las definiciones de propiedades pueden incluir una [???](#language.types.declarations), con la excepción del tipo `callable`.

Ejemplo de propiedades tipadas

```php
<?php

class User
{
    public int $id;
    public ?string $name;

    public function __construct(int $id, ?string $name)
    {
        $this->id = $id;
        $this->name = $name;
    }
}

$user = new User(1234, null);

var_dump($user->id);
var_dump($user->name);

?>

    
```

El ejemplo anterior mostrará:

    int(1234)
    NULL

Las propiedades tipadas deben ser inicializadas antes de acceder a ellas, de lo contrario, se emitirá un `Error`.

Acceso a propiedades

```php
<?php

class Shape
{
    public int $numberOfSides;
    public string $name;

    public function setNumberOfSides(int $numberOfSides): void
    {
        $this->numberOfSides = $numberOfSides;
    }

    public function setName(string $name): void
    {
        $this->name = $name;
    }

    public function getNumberOfSides(): int
    {
        return $this->numberOfSides;
    }

    public function getName(): string
    {
        return $this->name;
    }
}

$triangle = new Shape();
$triangle->setName("triangle");
$triangle->setNumberofSides(3);
var_dump($triangle->getName());
var_dump($triangle->getNumberOfSides());

$circle = new Shape();
$circle->setName("circle");
var_dump($circle->getName());
var_dump($circle->getNumberOfSides());
?>

     
```

El ejemplo anterior mostrará:

    string(8) "triangle"
    int(3)
    string(6) "circle"

    Fatal error: Uncaught Error: Typed property Shape::$numberOfSides must not be accessed before initialization

## Propiedades de solo lectura (readonly)

A partir de PHP 8.1.0, una propiedad puede ser declarada con el modificador `readonly`, lo que impide la modificación de la propiedad después de la inicialización. Antes de PHP 8.4.0 una propiedad `readonly` es implícitamente privada-modificable, y solo puede ser escrita desde la misma clase. A partir de PHP 8.4.0, las propiedades `readonly` son implícitamente [`protected(set)`](#language.oop5.visibility-members-aviz), por lo que pueden ser definidas desde clases hijas. Esto puede ser reemplazado explícitamente si se desea.

Ejemplo de propiedades de solo lectura

```php
<?php

class Test {
   public readonly string $prop;

   public function __construct(string $prop) {
       // Inicialización legal.
       $this->prop = $prop;
   }
}

$test = new Test("foobar");
// Lectura legal.
var_dump($test->prop); // string(6) "foobar"

// Reasignación ilegal. No importa que el valor asignado sea idéntico.
$test->prop = "foobar";
// Error: Cannot modify readonly property Test::$prop
?>

    
```

> [!NOTE]
> El modificador de solo lectura solo puede ser aplicado a [propiedades tipadas](#language.oop5.properties.typed-properties). Una propiedad de solo lectura sin restricción de tipo puede ser creada utilizando el tipo [???](#language.types.mixed).

> [!NOTE]
> Las propiedades estáticas de solo lectura no son soportadas.

Una propiedad de solo lectura solo puede ser inicializada una vez, y solo desde el ámbito en el que fue declarada. Cualquier otra asignación o modificación de la propiedad resultará en una excepción `Error`.

Inicialización ilegal de propiedades de solo lectura

```php
<?php
class Test1 {
    public readonly string $prop;
}

$test1 = new Test1;
// Inicialización ilegal fuera del ámbito privado.
$test1->prop = "foobar";
// Error: Cannot initialize readonly property Test1::$prop from global scope
?>

    
```

> [!NOTE]
> Especificar un valor por defecto explícito a una propiedad de solo lectura no está permitido, ya que una propiedad de solo lectura con un valor por defecto es esencialmente idéntica a una constante, y por lo tanto no particularmente útil.
>
> <div class="informalexample">
>
> ```
> <?php
>
> class Test {
>     // Fatal error: Readonly property Test::$prop cannot have default value
>     public readonly int $prop = 42;
> }
> ?>
>
>      
> ```
>
> </div>

> [!NOTE]
> Las propiedades de solo lectura no pueden ser `unset` una vez que han sido inicializadas. Sin embargo, es posible unset una propiedad de solo lectura antes de su inicialización, desde el ámbito donde la propiedad fue declarada.

Las modificaciones no son necesariamente asignaciones simples, todos los ejemplos siguientes resultarán en una excepción `Error` :

```php
<?php

class Test {
    public function __construct(
        public readonly int $i = 0,
        public readonly array $ary = [],
    ) {}
}

$test = new Test;
$test->i += 1;
$test->i++;
++$test->i;
$test->ary[] = 1;
$test->ary[0][] = 1;
unset($test->ary[0]);
$ref =& $test->i;
$test->i =& $ref;
byRef($test->i);
foreach ($test as &$prop);
?>

    
```

Sin embargo, las propiedades de solo lectura no excluyen la mutabilidad interna. Los objetos (o recursos) almacenados en las propiedades de solo lectura pueden ser modificados internamente :

```php
<?php

class Test {
    public function __construct(public readonly object $obj) {}
}

$test = new Test(new stdClass);
// Mutación interna legal.
$test->obj->foo = 1;
// Reasignación ilegal.
$test->obj = new stdClass;
?>

    
```

A partir de PHP 8.3.0, las propiedades de solo lectura pueden ser reinicializadas al clonar un objeto utilizando el método [\_\_clone()](#object.clone).

Propiedades de solo lectura y clonación

```php
<?php
class Test1 {
    public readonly ?string $prop;

    public function __clone() {
        $this->prop = null;
    }

    public function setProp(string $prop): void {
        $this->prop = $prop;
    }
}

$test1 = new Test1;
$test1->setProp('foobar');

$test2 = clone $test1;
var_dump($test2->prop); // NULL
?>

    
```

## Propiedades Dinámicas

Al intentar asignar a una propiedad no existente en un `object`, PHP creará automáticamente una propiedad correspondiente. Esta propiedad creada dinámicamente estará *únicamente* disponible en esta instancia de clase.

> [!WARNING]
> Las propiedades dinámicas están obsoletas a partir de PHP 8.2.0. Se recomienda declarar la propiedad en su lugar. Para manejar nombres de propiedades arbitrarios, la clase debería implementar los métodos mágicos [\_\_get()](#object.get) y [\_\_set()](#object.set). Como último recurso, la clase puede ser marcada con el atributo `#[\AllowDynamicProperties]`.
