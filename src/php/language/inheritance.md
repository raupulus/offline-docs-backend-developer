---
title: Herencia
source_url: https://www.php.net/manual/es/language.oop5.inheritance.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/inheritance.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 2470
---

## Herencia

La herencia es uno de los grandes principios de la programación orientada a objetos (POO), y PHP la implementa en su modelo de objetos. Este principio afectará la manera en que muchas clases están relacionadas entre sí.

Por ejemplo, cuando una clase es extendida, la clase hija hereda todas las métodos públicos y protegidos, propiedades y constantes de la clase padre. Mientras una clase no sobrescriba estos métodos, conservan su funcionalidad original.

La herencia es muy útil para definir y abstraer ciertas funcionalidades comunes a varias clases, permitiendo al mismo tiempo la implementación de funcionalidades adicionales en las clases hijas, sin tener que reimplementar en su interior todas las funcionalidades comunes.

Los métodos privados de una clase padre no son accesibles para la clase hija. Por consiguiente, las clases hijas pueden reimplementar un método privado por sí mismas sin preocuparse por las reglas normales de herencia. Anterior a PHP 8.0.0, sin embargo, las restricciones `final` y `static` se aplicaban a los métodos privados. A partir de PHP 8.0.0, la única restricción de método privado que se impone es `private final` en los constructores, ya que es una manera común para "desactivar" el constructor cuando se utilizan métodos de fábrica estáticos en su lugar.

La [visibilidad](#language.oop5.visibility) de los métodos, propiedades y constantes puede ser relajada, es decir, un método `protected` puede ser marcado como `public`, pero no pueden ser restringidos, por ejemplo, marcar una propiedad `public` como `private`. Una excepción son los constructores, para los cuales la visibilidad puede ser restringida, por ejemplo, un constructor `public` puede ser anotado como `private` en la clase hija.

> [!NOTE]
> A menos que se utilice la autocarga, las clases deben ser conocidas antes de ser utilizadas. Las clases padres deben ser definidas antes de escribir una herencia. Esta regla general se aplica también en el caso de herencia o implementación de interfaces.

> [!NOTE]
> No está permitido redefinir una propiedad de lectura-escritura con una [propiedad de solo lectura](#language.oop5.properties.readonly-properties) o viceversa.
>
> <div class="informalexample">
>
> ```
> <?php
>
> class A {
>     public int $prop;
> }
> class B extends A {
>     // Ilegal: lectura-escritura -> readonly
>     public readonly int $prop;
> }
> ?>
>
>     
> ```
>
> </div>

Ejemplo de herencia

```php
<?php

class Foo
{
    public function printItem($string)
    {
        echo 'Foo: ' . $string . PHP_EOL;
    }

    public function printPHP()
    {
        echo 'PHP es genial.' . PHP_EOL;
    }
}

class Bar extends Foo
{
    public function printItem($string)
    {
        echo 'Bar: ' . $string . PHP_EOL;
    }
}

$foo = new Foo();
$bar = new Bar();
$foo->printItem('baz'); // Muestra: 'Foo: baz'
$foo->printPHP();       // Muestra: 'PHP es genial.'
$bar->printItem('baz'); // Muestra: 'Bar: baz'
$bar->printPHP();       // Muestra: 'PHP es genial.'

?>

  
```

## Compatibilidad de los tipos de retorno con las clases internas

Anterior a PHP 8.1, la mayoría de las clases o métodos internos no declaraban su tipo de retorno, y cualquier tipo de retorno estaba permitido al heredarlos.

A partir de PHP 8.1.0, la mayoría de los métodos internos comenzaron a declarar "provisionalmente" su tipo de retorno, en este caso, el tipo de retorno de los métodos debe ser compatible con la clase padre; en caso contrario, se emite una notificación de deprecación. Tenga en cuenta que la ausencia de una declaración de retorno explícita también se considera un error de firma, y por lo tanto provoca el aviso de deprecación.

Si el tipo de retorno no puede ser declarado para un método de sobrecarga debido a problemas de compatibilidad entre versiones de PHP, un atributo `ReturnTypeWillChange` puede ser añadido para silenciar el aviso de deprecación.

El método sobrecargado no declara tipo de retorno.

```php
<?php

class MyDateTime extends DateTime
{
    public function modify(string $modifier) { return false; }
}

// "Deprecated: Return type of MyDateTime::modify(string $modifier) should either be compatible with DateTime::modify(string $modifier): DateTime|false, or the #[\ReturnTypeWillChange] attribute should be used to temporarily suppress the notice" A partir de PHP 8.1.0

   
```

El método sobrecargado declara un tipo de retorno incorrecto.

```php
<?php

class MyDateTime extends DateTime
{
    public function modify(string $modifier): ?DateTime { return null; }
}

// "Deprecated: Return type of MyDateTime::modify(string $modifier): ?DateTime should either be compatible with DateTime::modify(string $modifier): DateTime|false, or the #[\ReturnTypeWillChange] attribute should be used to temporarily suppress the notice" A partir de PHP 8.1.0

   
```

El método sobrecargado declara un tipo de retorno incorrecto sin aviso de deprecación.

```php
<?php

class MyDateTime extends DateTime
{
    /**
     * @return DateTime|false
     */
    #[\ReturnTypeWillChange]
    public function modify(string $modifier) { return false; }
}

// No se emite ningún aviso

   
```
