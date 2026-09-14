---
title: Interfaces
source_url: https://www.php.net/manual/es/language.oop5.interfaces.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/interfaces.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 565bd8b6c
order: 2480
---

## Interfaces

Las interfaces de objetos permiten crear código que especifica qué métodos y propiedades una clase debe implementar, sin tener que definir cómo se implementan estos métodos o propiedades. Las interfaces comparten un espacio de nombres con las clases, traits y enumeraciones, de modo que no pueden utilizar el mismo nombre.

Las interfaces se definen de la misma manera que una clase, pero utilizando la palabra clave `interface` en lugar de `class`, y sin que ninguno de los métodos tenga su contenido especificado.

Por la naturaleza misma de una interfaz, todos los métodos declarados en una interfaz deben ser públicos.

En la práctica, las interfaces sirven dos roles complementarios:

Permitir a los desarrolladores crear objetos de clases diferentes que pueden ser utilizados de manera intercambiable, ya que implementan la o las mismas interfaces. Un ejemplo común son varios servicios de acceso a bases de datos, varios gestores de pago o diferentes estrategias de caché. Diferentes implementaciones pueden ser intercambiadas sin necesitar cambios en el código que las utiliza.

Para permitir que una función o método acepte y opere sobre un argumento que se ajuste a una interfaz, sin preocuparse de qué más puede hacer el objeto o cómo está implementado. Estas interfaces suelen llamarse

Iterable

,

Cacheable

,

Renderable

, etc. para describir el significado de su comportamiento.

Las interfaces pueden definir [métodos mágicos](#language.oop5.magic) para obligar a las clases que las implementan a implementar estos métodos.

> [!NOTE]
> Aunque esto es soportado, incluir los [constructores](#language.oop5.decon.constructor) en las interfaces está fuertemente desaconsejado. Hacerlo reduce radicalmente la flexibilidad de los objetos que implementan la interfaz. Además, los constructores no están sujetos a las reglas de herencia, lo que puede causar incoherencias y comportamientos inesperados.

## `implements`

Para implementar una interfaz, se utiliza el operador `implements`. Todos los métodos de la interfaz deben ser implementados en una clase; si no es así, se emitirá un error fatal. Las clases pueden implementar más de una interfaz, separando cada interfaz por una coma.

> [!WARNING]
> Una clase que implementa una interfaz puede utilizar nombres diferentes para sus argumentos que la interfaz. Sin embargo, a partir de PHP 8.0, el lenguaje soporta los [argumentos nombrados](#functions.named-arguments), lo que significa que el llamador puede depender del nombre del argumento en la interfaz. Por esta razón, se recomienda encarecidamente que los desarrolladores utilicen el mismo nombre de argumento que en la interfaz que se implementa.

> [!NOTE]
> Las interfaces pueden ser extendidas como clases, utilizando el operador [extends](#language.oop5.inheritance)

> [!NOTE]
> La clase que implementa la interfaz debe declarar todos los métodos en la interfaz con una [firma compatible](#language.oop.lsp). Una clase puede implementar dos interfaces que definan un método con el mismo nombre. En este caso, la implementación debe seguir las [reglas de compatibilidad de firmas](#language.oop.lsp) para todas las interfaces. Así, [la covarianza y la contravarianza](#language.oop5.variance) pueden ser aplicadas.

## Las constantes

Las interfaces pueden contener constantes. Las constantes de interfaces funcionan exactamente como las [constantes de clase](#language.oop5.constants). Anterior a PHP 8.1.0, no pueden ser redefinidas por una clase/interfaz que las hereda.

## Propiedades

A partir de PHP 8.4.0, las interfaces también pueden declarar propiedades. Si lo hacen, la declaración debe especificar si la propiedad es legible, modificable, o ambas. La declaración de la interfaz se aplica únicamente al acceso en lectura y escritura públicos.

Una clase puede satisfacer una propiedad de interfaz de varias maneras. Puede definir una propiedad pública. Puede definir una propiedad pública [virtual](#language.oop5.property-hooks.virtual) que implemente únicamente el crochet correspondiente. O una propiedad de lectura puede ser satisfecha por una propiedad `readonly`. Sin embargo, una propiedad de interfaz que es modificable no puede ser `readonly`.

Ejemplo de propiedades de interfaz

```php
<?php
interface I
{
    // Una clase que implementa esta interfaz DEBE tener una propiedad públicamente legible,
    // pero que esta sea o no modificable públicamente no está restringido.
    public string $readable { get; }

    // Una clase que implementa esta interfaz DEBE tener una propiedad públicamente modificable,
    // pero que esta sea o no legible públicamente no está restringido.
    public string $writeable { set; }

    // Una clase que implementa esta interfaz DEBE tener una propiedad que sea a la vez públicamente
    // legible y públicamente modificable.
    public string $both { get; set; }
}

// Esta clase implementa las tres propiedades como propiedades tradicionales, sin crochets.
// Esto es completamente válido.
class C1 implements I
{
    public string $readable;

    public string $writeable;

    public string $both;
}

// Esta clase implementa las tres propiedades utilizando únicamente los crochets
// solicitados. Esto también es completamente válido.
class C2 implements I
{
    private string $written = '';
    private string $all = '';

    // Utiliza únicamente un crochet get para crear una propiedad virtual.
    // Esto satisface el requisito "get public".
    // No es modificable, pero esto no es requerido por la interfaz.
    public string $readable { get => strtoupper($this->writeable); }

    // La interfaz requiere únicamente que la propiedad sea modificable,
    // pero incluir operaciones get también es completamente válido.
    // Este ejemplo crea una propiedad virtual, lo cual es aceptable.
    public string $writeable {
        get => $this->written;
        set {
            $this->written = $value;
        }
    }

    // Esta propiedad requiere que la lectura y la escritura sean posibles,
    // por lo que debemos implementar ambas o permitir el comportamiento por defecto.
    public string $both {
        get => $this->all;
        set {
            $this->all = strtoupper($value);
        }
    }
}
?>

    
```

## Ejemplos

Ejemplo de interfaz

```php
<?php

// Declaración de la interfaz 'Template'
interface Template
{
    public function setVariable($name, $var);
    public function getHtml($template);
}

// Implementación de la interfaz
// Esto funcionará
class WorkingTemplate implements Template
{
    private $vars = [];

    public function setVariable($name, $var)
    {
        $this->vars[$name] = $var;
    }

    public function getHtml($template)
    {
        foreach($this->vars as $name => $value) {
            $template = str_replace('{' . $name . '}', $value, $template);
        }

        return $template;
    }
}

// Esto no funcionará
// Fatal error: Class BadTemplate contains 1 abstract methods
// and must therefore be declared abstract (Template::getHtml)
class BadTemplate implements Template
{
    private $vars = [];

    public function setVariable($name, $var)
    {
        $this->vars[$name] = $var;
    }
}
?>

   
```

Las interfaces extensibles

```php
<?php
interface A
{
    public function foo();
}

interface B extends A
{
    public function baz(Baz $baz);
}

// Esto funcionará
class C implements B
{
    public function foo()
    {
    }

    public function baz(Baz $baz)
    {
    }
}

// Esto no funcionará y resultará en un error fatal
class D implements B
{
    public function foo()
    {
    }

    public function baz(Foo $foo)
    {
    }
}
?>

     
```

Compatibilidad de la varianza con múltiples interfaces

```php
<?php
class Foo {}
class Bar extends Foo {}

interface A {
    public function myfunc(Foo $arg): Foo;
}

interface B {
    public function myfunc(Bar $arg): Bar;
}

class MyClass implements A, B
{
    public function myfunc(Foo $arg): Bar
    {
        return new Bar();
    }
}
?>

     
```

Herencia de múltiples interfaces

```php
<?php
interface A
{
    public function foo();
}

interface B
{
    public function bar();
}

interface C extends A, B
{
    public function baz();
}

class D implements C
{
    public function foo()
    {
    }

    public function bar()
    {
    }

    public function baz()
    {
    }
}
?>

     
```

Interfaces con constantes

```php
<?php
interface A
{
    const B = 'Constante de la interfaz';
}

// Muestra: Constante de la interfaz
echo A::B;

// Sin embargo, esto no funcionará, ya que no está permitido
// sobrescribir constantes.
class B implements A
{
    const B = 'Constante de clase';
}

// Muestra: Constante de clase
// Anterior a PHP 8.1.0, esto no funcionaría, ya que no estaba permitido
// redefinir constantes.
echo B::B;
?>

     
```

Las interfaces con las clases abstractas

```php
<?php
interface A
{
    public function foo(string $s): string;

    public function bar(int $i): int;
}

// Una clase abstracta puede implementar solo una parte de una interfaz.
// Las clases que extienden la clase abstracta deben implementar el resto.
abstract class B implements A
{
    public function foo(string $s): string
    {
        return $s . PHP_EOL;
    }
}

class C extends B
{
    public function bar(int $i): int
    {
        return $i * 2;
    }
}
?>

    
```

Extendiendo e implementando simultáneamente

```php
<?php

class One
{
    /* ... */
}

interface Usable
{
    /* ... */
}

interface Updatable
{
    /* ... */
}

// El orden de las palabras clave aquí es importante. 'extends' debe ir primero.
class Two extends One implements Usable, Updatable
{
    /* ... */
}
?>

    
```

Una interfaz, con las declaraciones de tipos, proporciona una buena manera de asegurarse de que un objeto particular contiene métodos particulares. Ver el operador [instanceof](#language.operators.type) y las [declaraciones de tipo](#language.types.declarations).
