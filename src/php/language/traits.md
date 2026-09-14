---
title: Traits
source_url: https://www.php.net/manual/es/language.oop5.traits.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/traits.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: c1f37a6c2
order: 2610
---

## Traits

PHP implementa una manera de reutilizar código llamada Traits.

Los traits son un mecanismo de reutilización de código en un lenguaje de herencia simple como PHP. Un trait intenta reducir ciertas limitaciones de la herencia simple, permitiendo al desarrollador reutilizar un cierto número de métodos en clases independientes. La sémantica entre las clases y los traits reduce la complejidad y evita los problemas típicos de la herencia múltiple y los Mixins.

Un trait es similar a una clase, pero solo sirve para agrupar funcionalidades de una manera interesante. No es posible instanciar un Trait en sí mismo. Es un añadido a la herencia tradicional, que permite la composición horizontal de comportamientos, es decir, el uso de métodos de clase sin necesidad de herencia.

Ejemplo de uso de Trait

```php
<?php

trait TraitA {
    public function sayHello() {
        echo 'Hello';
    }
}

trait TraitB {
    public function sayWorld() {
        echo 'World';
    }
}

class MyHelloWorld
{
    use TraitA, TraitB; // Una clase puede usar múltiples traits

    public function sayHelloWorld() {
        $this->sayHello();
        echo ' ';
        $this->sayWorld();
        echo "!\n";
    }
}

$myHelloWorld = new MyHelloWorld();
$myHelloWorld->sayHelloWorld();

?>

  
```

El ejemplo anterior mostrará:

    Hello World!

## Precedencia

Un método heredado desde una clase madre es sobrescrito por un método proveniente de un Trait. El orden de precedencia hace que los métodos de la clase actual sobrescriban los métodos provenientes de un Trait, ellos mismos sobrecargando los métodos heredados.

Ejemplo con el orden de precedencia

Un método heredado desde la clase base es sobrescrito por el que proviene del Trait. No es el caso de los métodos reales, escritos en la clase base.

```php
<?php
class Base {
    public function sayHello() {
        echo 'Hello ';
    }
}

trait SayWorld {
    public function sayHello() {
        parent::sayHello();
        echo 'World!';
    }
}

class MyHelloWorld extends Base {
    use SayWorld;
}

$o = new MyHelloWorld();
$o->sayHello();
?>

   
```

El ejemplo anterior mostrará:

    Hello World!

Otro ejemplo de orden de precedencia

```php
<?php
trait HelloWorld {
    public function sayHello() {
        echo 'Hello World!';
    }
}

class TheWorldIsNotEnough {
    use HelloWorld;
    public function sayHello() {
        echo 'Hello Universe!';
    }
}

$o = new TheWorldIsNotEnough();
$o->sayHello();
?>

   
```

El ejemplo anterior mostrará:

    Hello Universe!

## Múltiples Traits

Una clase puede usar múltiples Traits declarándolos con la palabra clave `use`, separados por comas.

Uso de varios Traits

```php
<?php
trait Hello {
    public function sayHello() {
        echo 'Hello ';
    }
}

trait World {
    public function sayWorld() {
        echo 'World';
    }
}

class MyHelloWorld {
    use Hello, World;
    public function sayExclamationMark() {
        echo '!';
    }
}

$o = new MyHelloWorld();
$o->sayHello();
$o->sayWorld();
$o->sayExclamationMark();
?>

   
```

El ejemplo anterior mostrará:

    Hello World!

## Resolución de conflictos

Si dos Traits insertan un método con el mismo nombre, se produce un error fatal si el conflicto no es explícitamente resuelto.

Para resolver un conflicto de nombres entre Traits usados en la misma clase, se debe usar el operador `insteadof` para elegir uno de los métodos en conflicto.

Dado que este principio solo permite excluir métodos, el operador `as` puede ser usado para permitir la inclusión de uno de los métodos conflictivos bajo otro nombre. Se debe tener en cuenta que el operador `as` no renombra el método y no afecta a otros métodos tampoco.

Resolución de conflictos

En este ejemplo, la clase Talker usa los traits A y B. Como A y B tienen métodos conflictivos, se indica que se desea usar la variante de smallTalk desde el trait B, y la variante de bigTalk desde el trait A.

La clase Aliased_Talker usa el operador `as` para poder usar la implementación bigTalk de B bajo un alias adicional `talk`.

```php
<?php
trait A {
    public function smallTalk() {
        echo 'a';
    }
    public function bigTalk() {
        echo 'A';
    }
}

trait B {
    public function smallTalk() {
        echo 'b';
    }
    public function bigTalk() {
        echo 'B';
    }
}

class Talker {
    use A, B {
        B::smallTalk insteadof A;
        A::bigTalk insteadof B;
    }
}

class Aliased_Talker {
    use A, B {
        B::smallTalk insteadof A;
        A::bigTalk insteadof B;
        B::bigTalk as talk;
    }
}
?>

   
```

## Cambiar la visibilidad de los métodos

Usando la sintaxis `as`, también se puede ajustar la visibilidad del método en la clase que lo usa.

Cambiar la visibilidad de los métodos

```php
<?php
trait HelloWorld {
    public function sayHello() {
        echo 'Hello World!';
    }
}

// Modificación de la visibilidad del método sayHello
class MyClass1 {
    use HelloWorld { sayHello as protected; }
}

// Uso de un alias al modificar la visibilidad
// La visibilidad del método sayHello no es modificada
class MyClass2 {
    use HelloWorld { sayHello as private myPrivateHello; }
}
?>

   
```

## Traits Compuestos desde otros Traits

Al igual que las clases pueden usar traits, otros traits también pueden hacerlo. Un trait puede, por lo tanto, usar otros traits y heredar todo o parte de ellos.

Traits Compuestos desde otros Traits

```php
<?php
trait Hello {
    public function sayHello() {
        echo 'Hello ';
    }
}

trait World {
    public function sayWorld() {
        echo 'World!';
    }
}

trait HelloWorld {
    use Hello, World;
}

class MyHelloWorld {
    use HelloWorld;
}

$o = new MyHelloWorld();
$o->sayHello();
$o->sayWorld();
?>

   
```

El ejemplo anterior mostrará:

    Hello World!

## Métodos abstractos en los Traits

Los traits soportan el uso de métodos abstractos para imponer restricciones a las clases subyacentes. Se soportan los métodos públicos, protegidos, y privados. Anterior a PHP 8.0.0, solo se soportaban los métodos públicos y protegidos abstractos.

> [!CAUTION]
> A partir de PHP 8.0.0, la firma de un método concreto debe seguir las [reglas de compatibilidad de firmas](#language.oop.lsp). Anteriormente, su firma podía ser diferente.

Obligaciones requeridas por los métodos abstractos

```php
<?php
trait Hello {
    public function sayHelloWorld() {
        echo 'Hello'.$this->getWorld();
    }
    abstract public function getWorld();
}

class MyHelloWorld {
    private $world;
    use Hello;
    public function getWorld() {
        return $this->world;
    }
    public function setWorld($val) {
        $this->world = $val;
    }
}
?>

   
```

## Atributos estáticos en los Traits

Los traits pueden definir variables estáticas, métodos estáticos y propiedades estáticas.

> [!NOTE]
> A partir de PHP 8.1.0, llamar a un método estático o acceder a una propiedad estática directamente en un trait es obsoleto. Los métodos y propiedades estáticas deberían ser accedidos solo en una clase que use el trait.

Variables estáticas

```php
<?php

trait Counter
{
    public function inc()
    {
        static $c = 0;
        $c = $c + 1;
        echo "$c\n";
    }
}

class C1
{
    use Counter;
}

class C2
{
    use Counter;
}

$o = new C1();
$o->inc();
$p = new C2();
$p->inc();

?>

   
```

El ejemplo anterior mostrará:

    1
    1

Métodos estáticos

```php
<?php

trait StaticExample
{
    public static function doSomething()
    {
        return 'Doing something';
    }
}

class Example
{
    use StaticExample;
}

echo Example::doSomething();

?>

   
```

El ejemplo anterior mostrará:

    Doing something

Propiedades estáticas

> [!CAUTION]
> Antes de PHP 8.3.0, las propiedades estáticas definidas en un trait eran compartidas entre todas las clases de la misma jerarquía de herencia que usaban ese trait. A partir de PHP 8.3.0, si una clase hija usa un trait con una propiedad estática, esta será considerada como distinta de la definida en la clase padre.

```php
<?php

trait StaticExample
{
    public static $counter = 1;
}

class A
{
    use T;

    public static function incrementCounter()
    {
        static::$counter++;
    }
}

class B extends A
{
    use T;
}

A::incrementCounter();

echo A::$counter, "\n";
echo B::$counter, "\n";

?>

   
```

Resultado del ejemplo anterior en PHP 8.3:

    2
    1

## Propiedades

Los traits también pueden definir propiedades.

Definir propiedades

```php
<?php

trait PropertiesTrait
{
    public $x = 1;
}

class PropertiesExample
{
    use PropertiesTrait;
}

$example = new PropertiesExample();
$example->x;

?>

    
```

Si un trait define una propiedad, entonces la clase no puede definir una propiedad con el mismo nombre a menos que sea compatible (misma visibilidad, tipo, modificador readonly, valor inicial), de lo contrario se produce un error fatal.

Resolución de conflictos

```php
<?php
trait PropertiesTrait {
    public $same = true;
    public $different1 = false;
    public bool $different2;
    public bool $different3;
}

class PropertiesExample {
    use PropertiesTrait;
    public $same = true;
    public $different1 = true; // Fatal error
    public string $different2; // Fatal error
    readonly protected bool $different3; // Fatal error
}
?>

    
```

## Constantes

Los traits pueden, a partir de PHP 8.2.0, también definir constantes.

Trait definiendo una constante

```php
<?php
trait ConstantsTrait {
    public const FLAG_MUTABLE = 1;
    final public const FLAG_IMMUTABLE = 5;
}

class ConstantsExample {
    use ConstantsTrait;
}

$example = new ConstantsExample;
echo $example::FLAG_MUTABLE;
?>

   
```

El ejemplo anterior mostrará:

    1

Si un trait define una constante, entonces una clase no puede definir una constante con el mismo nombre, a menos que sea compatible (misma visibilidad, mismo valor, etc.), de lo contrario se produce un error fatal.

Resolución de conflicto

```php
<?php
trait ConstantsTrait {
    public const FLAG_MUTABLE = 1;
    final public const FLAG_IMMUTABLE = 5;
}

class ConstantsExample {
    use ConstantsTrait;
    public const FLAG_IMMUTABLE = 5; // Fatal error
}
?>

    
```

## Métodos finales

A partir de PHP 8.3.0, el modificador [final](#language.oop5.final) puede ser aplicado usando el operador `as` a los métodos importados desde los traits. Esto puede ser usado para impedir que las clases hijas sobrecarguen el método. Sin embargo, la clase que usa el trait puede seguir sobrecargando el método.

Definir un método proveniente de un trait como `final`

```php
    
<?php

trait CommonTrait
{
    public function method()
    {
        echo 'Hello';
    }
}

class FinalExampleA
{
    use CommonTrait {
        CommonTrait::method as final; // El 'final' impide que las clases hijas sobrecarguen el método
    }
}

class FinalExampleB extends FinalExampleA
{
    public function method() {}
}

?>

    
```

Resultado del ejemplo anterior es similar a:

    Fatal error: Cannot override final method FinalExampleA::method() in ...
