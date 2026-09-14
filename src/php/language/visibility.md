---
title: Visibilidad
source_url: https://www.php.net/manual/es/language.oop5.visibility.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/visibility.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: b9af4bd4e
order: 2630
---

## Visibilidad

La visibilidad de una propiedad, un método o (a partir de PHP 7.1.0) una constante puede ser definida prefijando su declaración con una palabra clave: `public`, `protected`, o `private`. Los elementos declarados como públicos son accesibles en cualquier lugar. El acceso a los elementos protegidos está limitado a la clase misma, y mediante clases heredadas y a las clases padre. A los miembros declarados como privados solo puede acceder la clase que los ha definido.

## Visibilidad de las propiedades

Las propiedades de las clases pueden ser definidas como públicas, privadas o protegidas. Las propiedades declaradas sin utilizar explícitamente una palabra clave de visibilidad serán automáticamente definidas como públicas.

Declaración de propiedades

```php
<?php
/**
 * Definición de MyClass
 */
class MyClass
{
    public $public = 'Public';
    protected $protected = 'Protected';
    private $private = 'Private';

    function printHello()
    {
        echo $this->public;
        echo $this->protected;
        echo $this->private;
    }
}

$obj = new MyClass();
echo $obj->public; // Funciona
echo $obj->protected; // Error fatal
echo $obj->private; // Error fatal
$obj->printHello(); // Muestra Public, Protected y Private

/**
 * Definición de MyClass2
 */
class MyClass2 extends MyClass
{
    // Se pueden redeclarar las propiedades públicas o protegidas, pero no las privadas
    public $public = 'Public2';
    protected $protected = 'Protected2';

    function printHello()
    {
      echo $this->public;
      echo $this->protected;
      echo $this->private;
    }
}

$obj2 = new MyClass2();
echo $obj2->public; // Funciona
echo $obj2->protected; // Error fatal
echo $obj2->private; // Indefinido
$obj2->printHello(); // Muestra Public2, Protected2 y Undefined (Indefinido)

?>

      
```

### Visibilidad Asimétrica de las Propiedades

A partir de PHP 8.4, las propiedades de objeto pueden también tener su visibilidad definida de manera asimétrica, con un campo diferente para la lectura (`get`) y la escritura (`set`). Más precisamente, la visibilidad `set` puede ser especificada separadamente, siempre que no sea más permisiva que la visibilidad por defecto.

Visibilidad Asimétrica de las Propiedades

```php
<?php
class Book
{
    public function __construct(
        public private(set) string $title,
        public protected(set) string $author,
        protected private(set) int $pubYear,
    ) {}
}

class SpecialBook extends Book
{
    public function update(string $author, int $year): void
    {
        $this->author = $author; // OK
        $this->pubYear = $year; // Error Fatal
    }
}

$b = new Book('Cómo usar PHP', 'Peter H. Peterson', 2024);

echo $b->title; // Funciona
echo $b->author; // Funciona
echo $b->pubYear; // Error Fatal

$b->title = 'Cómo no usar PHP'; // Error Fatal
$b->author = 'Pedro H. Peterson'; // Error Fatal
$b->pubYear = 2023; // Error Fatal
?>

        
```

A partir de PHP 8.5, la visibilidad `set` también puede ser aplicada a las propiedades estáticas de las clases.

Visibilidad Asimétrica de Propiedades Estáticas

```php
<?php
class Manager
{
    public private(set) static int $calls = 0;

    public function doAThing(): string
    {
        self::$calls++;
        // Hacer otras cosas.
        return "alguna cadena";
    }
}

$m = new Manager();

$m->doAThing(); // Funciona
echo Manager::$calls; // Funciona
Manager::$calls = 5; // Error fatal
?>

        
```

El ejemplo anterior mostrará:

    1
    Fatal error: Uncaught Error: Cannot modify private(set) property Manager::$calls from global scope in /some/file.php

Hay algunas reservas concernientes a la visibilidad asimétrica:

- Solo las propiedades tipadas pueden tener una visibilidad `set` separada.

- La visibilidad `set` debe ser la misma que `get` o más restrictiva. Es decir, `public protected(set)` y `protected protected(set)` están permitidos, pero `protected public(set)` provocará un error de sintaxis.

- Si una propiedad es `public`, entonces la visibilidad principal puede ser omitida. Es decir, `public private(set)` y `private(set)` tendrán el mismo resultado.

- Una propiedad con una visibilidad `private(set)` es automáticamente `final`, y no puede ser redefinida en una clase hija.

- Obtener una referencia a una propiedad sigue la visibilidad `set`, no `get`. Esto se debe a que una referencia puede ser utilizada para modificar el valor de la propiedad.

- De igual manera, intentar escribir en una propiedad de array implica tanto una operación `get` como una operación `set` internamente, y seguirá por lo tanto la visibilidad `set`, ya que es siempre la más restrictiva.

> [!NOTE]
> Los espacios no están permitidos en la declaración de visibilidad para la modificación. `private(set)` es correcto. `private( set )` no es correcto y resultará en un error de análisis.

Cuando una clase extiende a otra, la clase hija puede redefinir cualquier propiedad que no sea `final`. Al hacerlo, puede ampliar tanto la visibilidad principal como la visibilidad `set`, siempre que la nueva visibilidad sea la misma o más amplia que la de la clase padre. Sin embargo, tenga en cuenta que si una propiedad `private` es reemplazada, esto no cambia realmente la propiedad de la clase padre, sino que crea una nueva propiedad con un nombre interno diferente.

Herencia de Propiedades Asimétricas

```php
<?php
class Book
{
    protected string $title;
    public protected(set) string $author;
    protected private(set) int $pubYear;
}

class SpecialBook extends Book
{
    public protected(set) string $title; // OK, ya que la lectura es más amplia y la escritura es la misma.
    public string $author; // OK, ya que la lectura es la misma y la escritura es más amplia.
    public protected(set) int $pubYear; // Error Fatal. Las propiedades private(set) son finales.
}
?>

        
```

## Visibilidad de los métodos

Los métodos de las clases pueden ser definidos como públicos, privados o protegidos. Los métodos declarados sin utilizar explícitamente una palabra clave de visibilidad serán automáticamente definidos como públicos.

Declaración de métodos

```php
<?php
/**
 * Definición de MyClass
 */
class MyClass
{
    // Declara un constructor público
    public function __construct() { }

    // Declara un método público
    public function MyPublic() { }

    // Declara un método protegido
    protected function MyProtected() { }

    // Declara un método privado
    private function MyPrivate() { }

    // Este será público
    function Foo()
    {
        $this->MyPublic();
        $this->MyProtected();
        $this->MyPrivate();
    }
}

$myclass = new MyClass;
$myclass->MyPublic(); // Funciona
$myclass->MyProtected(); // Error fatal
$myclass->MyPrivate(); // Error fatal
$myclass->Foo(); // Public, Protected y Private funcionan

/**
 * Definición de MyClass2
 */
class MyClass2 extends MyClass
{
    // Este será público
    function Foo2()
    {
        $this->MyPublic();
        $this->MyProtected();
        $this->MyPrivate(); // Error fatal
    }
}

$myclass2 = new MyClass2;
$myclass2->MyPublic(); // Funciona
$myclass2->Foo2(); // Public y Protected funcionan, no Private

class Bar
{
    public function test() {
        $this->testPrivate();
        $this->testPublic();
    }

    public function testPublic() {
        echo "Bar::testPublic\n";
    }

    private function testPrivate() {
        echo "Bar::testPrivate\n";
    }
}

class Foo extends Bar
{
    public function testPublic() {
        echo "Foo::testPublic\n";
    }

    private function testPrivate() {
        echo "Foo::testPrivate\n";
    }
}

$myFoo = new Foo();
$myFoo->test(); // Bar::testPrivate
                // Foo::testPublic
?>

        
```

## Visibilidad de las constantes

A partir de PHP 7.1.0, las constantes de clases pueden ser definidas como públicas, privadas o protegidas. Las constantes declaradas sin una palabra clave de visibilidad explícita son definidas como públicas.

Declaración de constantes a partir de PHP 7.1.0

```php
<?php
/**
 * Declaremos MyClass
 */
class MyClass
{
    // Declaremos una constante pública
    public const MY_PUBLIC = 'public';

    // Declaremos una constante protegida
    protected const MY_PROTECTED = 'protected';

    // Declaremos una constante privada
    private const MY_PRIVATE = 'private';

    public function foo()
    {
        echo self::MY_PUBLIC;
        echo self::MY_PROTECTED;
        echo self::MY_PRIVATE;
    }
}

$myclass = new MyClass();
MyClass::MY_PUBLIC; // Funciona
MyClass::MY_PROTECTED; // Error fatal
MyClass::MY_PRIVATE; // Error fatal
$myclass->foo(); // Public, Protegida y Privada funcionan

/**
 * Definir MyClass2
 */
class MyClass2 extends MyClass
{
    // Esto es público
    function foo2()
    {
        echo self::MY_PUBLIC;
        echo self::MY_PROTECTED;
        echo self::MY_PRIVATE; // Error fatal
    }
}

$myclass2 = new MyClass2;
echo MyClass2::MY_PUBLIC; // Funciona
$myclass2->foo2(); // Public y Protegida funcionan, pero no Privada
?>

      
```

## Visibilidad desde otros objetos

Los objetos de mismos tipos tienen acceso a los miembros privados y protegidos de los otros, incluso si no son la misma instancia. Esto se debe a que los detalles específicos de la implementación ya son conocidos internamente por estos objetos.

Acceso a los miembros privados de un objeto del mismo tipo

```php
<?php
class Test
{
    private $foo;

    public function __construct($foo)
    {
        $this->foo = $foo;
    }

    private function bar()
    {
        echo 'Acceso al método privado.';
    }

    public function baz(Test $other)
    {
        // Podemos modificar la propiedad privada:
        $other->foo = 'Hola';
        var_dump($other->foo);

        // También podemos llamar al método privado:
        $other->bar();
    }
}

$test = new Test('test');

$test->baz(new Test('other'));
?>

      
```

El ejemplo anterior mostrará:

    string(5) "Hola"
    Acceso al método privado.
