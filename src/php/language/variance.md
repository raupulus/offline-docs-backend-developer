---
title: Covarianza y Contravarianza
source_url: https://www.php.net/manual/es/language.oop5.variance.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/variance.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 2e7c00fd3
order: 2620
---

## Covarianza y Contravarianza

A partir de PHP 7.2.0, se introdujo la contravarianza parcial eliminando las restricciones de tipo en los parámetros de un método hijo. A partir de PHP 7.4.0, se añadieron la covarianza y la contravarianza completas.

La covarianza permite a un método hijo devolver un tipo más específico que el tipo de retorno de su método padre. La contravarianza permite que un tipo de parámetro sea menos específico en un método hijo que en el de la clase padre.

Una declaración de tipo se considera más específica en el siguiente caso:

- Un tipo es retirado de un [tipo union](#language.types.type-system.composite.union)

- Un tipo es añadido a un [tipo de intersección](#language.types.type-system.composite.intersection)

- Un tipo de clase es transformado en un tipo de clase hijo

- `iterable` es reemplazado por `array` o `Traversable`

Un tipo de clase se considera menos específico si lo contrario es cierto.

## Covarianza

Para ilustrar el funcionamiento de la covarianza, se crea una simple clase padre abstracta, `Animal`. `Animal` será extendida por clases hijas, `Cat` y `Dog`.

```php
<?php

abstract class Animal
{
    protected string $name;

    public function __construct(string $name)
    {
        $this->name = $name;
    }

    abstract public function speak();
}

class Dog extends Animal
{
    public function speak()
    {
        echo $this->name . " barks";
    }
}

class Cat extends Animal
{
    public function speak()
    {
        echo $this->name . " meows";
    }
}

   
```

Téngase en cuenta que no hay métodos que devuelvan valores en este ejemplo. Se añadirán algunas fábricas y devolverán un nuevo objeto de clase de tipo `Animal`, `Cat`, o `Dog`.

```php
<?php

interface AnimalShelter
{
    public function adopt(string $name): Animal;
}

class CatShelter implements AnimalShelter
{
    public function adopt(string $name): Cat // en lugar de devolver el tipo de clase Animal, puede devolver el tipo de clase Cat
    {
        return new Cat($name);
    }
}

class DogShelter implements AnimalShelter
{
    public function adopt(string $name): Dog // en lugar de devolver el tipo de clase Animal, puede devolver el tipo de clase Dog
    {
        return new Dog($name);
    }
}

$kitty = (new CatShelter)->adopt("Ricky");
$kitty->speak();
echo "\n";

$doggy = (new DogShelter)->adopt("Mavrick");
$doggy->speak();

   
```

El ejemplo anterior mostrará:

    Ricky meows
    Mavrick barks

## Contravarianza

Retomando el ejemplo anterior con las clases `Animal`, `Cat` y `Dog`, se incluyen dos clases llamadas `Food` y `AnimalFood`, y se añade un método `eat(AnimalFood $food)` a la clase abstracta `Animal`.

```php
<?php

class Food {}

class AnimalFood extends Food {}

abstract class Animal
{
    protected string $name;

    public function __construct(string $name)
    {
        $this->name = $name;
    }

    public function eat(AnimalFood $food)
    {
        echo $this->name . " eats " . get_class($food);
    }
}

   
```

Para ver el comportamiento de la contravarianza, el método método `eat` es sobrecargado en la clase `Dog` para permitir cualquier objeto de tipo `Food`. La clase `Cat` permanece sin cambios.

```php
<?php

class Dog extends Animal
{
    public function eat(Food $food) {
        echo $this->name . " eats " . get_class($food);
    }
}

   
```

El siguiente ejemplo muestra el comportamiento de la contravarianza.

```php
<?php

$kitty = (new CatShelter)->adopt("Ricky");
$catFood = new AnimalFood();
$kitty->eat($catFood);
echo "\n";

$doggy = (new DogShelter)->adopt("Mavrick");
$banana = new Food();
$doggy->eat($banana);

   
```

El ejemplo anterior mostrará:

    Ricky eats AnimalFood
    Mavrick eats Food

       

Pero, ¿qué sucede si `$kitty` intenta comer (eat) la banana (`$banana`) ?

```php
$kitty->eat($banana);

   
```

El ejemplo anterior mostrará:

    Fatal error: Uncaught TypeError: Argument 1 passed to Animal::eat() must be an instance of AnimalFood, instance of Food given

## Variación de tipo de las propiedades

Por defecto, las propiedades no son ni covariantes ni contravariantes, por lo tanto, son invariantes. En otras palabras, su tipo no puede cambiar en absoluto en una clase hija. La razón es que las operaciones "get" deben ser covariantes, y las operaciones "set" deben ser contravariantes. La única manera para que una propiedad cumpla con estos dos requisitos es ser invariante.

A partir de PHP 8.4.0, con la adición de las propiedades abstractas (en una interfaz o una clase abstracta) y [propiedades virtuales](#language.oop5.property-hooks.virtual), es posible declarar una propiedad que solo tenga una operación "get" o "set". En consecuencia, las propiedades abstractas o las propiedades virtuales que solo requieren la operación "get" pueden ser covariantes. De manera similar, una propiedad abstracta o una propiedad virtual que solo requiere la operación "set" puede ser contravariante.

Sin embargo, una vez que una propiedad tiene tanto una operación "get" como "set", ya no es covariante ni contravariante para una extensión futura. En otras palabras, se vuelve invariante.

Variación del tipo de las propiedades

```php
<?php
class Animal {}
class Dog extends Animal {}
class Poodle extends Dog {}

interface PetOwner
{
    // Solo se requiere la operación "get", por lo tanto, puede ser covariante.
    public Animal $pet { get; }
}

class DogOwner implements PetOwner
{
    // Puede ser un tipo más restrictivo, ya que el lado "get"
    // siempre devuelve un Animal. Sin embargo, como propiedad nativa,
    // los hijos de esta clase ya no pueden cambiar el tipo.
    public Dog $pet;
}

class PoodleOwner extends DogOwner
{
    // ESTO NO ESTÁ PERMITIDO, ya que DogOwner::$pet tiene tanto
    // las operaciones "get" como "set" definidas y requeridas.
    public Poodle $pet;
}
?>

   
```
