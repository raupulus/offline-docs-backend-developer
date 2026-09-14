---
title: Estático
source_url: https://www.php.net/manual/es/language.oop5.static.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/static.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 888507ca9
order: 2600
---

## Estático

> [!TIP]
> Esta página describe el uso de la palabra clave `static` que permite definir métodos y propiedades estáticas. `static` también puede ser utilizado para [definir variables estáticas](#language.variables.scope.static), [definir funciones anónimas estáticas](#functions.anonymous-functions.static) y para [Resoluciones estáticas a la volada](#language.oop5.late-static-bindings). Consulte estas páginas para obtener más información sobre el significado de `static`.

Declarar propiedades o métodos como estáticos permite acceder a ellos sin necesidad de instanciar la clase. Estos pueden ser accedidos estáticamente desde una instancia de objeto.

## Métodos estáticos

Dado que los métodos estáticos pueden ser llamados sin que una instancia de objeto haya sido creada, la pseudo-variable `$this` no está disponible en los métodos declarados como estáticos.

> [!WARNING]
> Llamar a un método no estático estáticamente lanzará una `Error`.
>
> Anterior a PHP 8.0.0, llamar a un método no estático estáticamente era obsoleto, y generaba un aviso `E_DEPRECATED`.

Ejemplo con un método estático

```php
<?php
class Foo
{
    public static function aStaticMethod() {
        // ...
    }
}

Foo::aStaticMethod();
$classname = 'Foo';
$classname::aStaticMethod();
?>

      
```

## Propiedades estáticas

Las propiedades estáticas son accedidas utilizando el [operador de resolución de ámbito](#language.oop5.paamayim-nekudotayim) (`::`) y no pueden ser accedidas a través del operador objeto (`->`).

Es posible referenciar la clase utilizando una variable. El valor de la variable no puede ser una palabra clave (por ejemplo `self`, `parent` y `static`).

Ejemplo con una propiedad estática

```php
<?php
class Foo
{
    public static $my_static = 'foo';

    public function staticValue() {
        return self::$my_static;
    }
}

class Bar extends Foo
{
    public function fooStatic() {
        return parent::$my_static;
    }
}

print Foo::$my_static . "\n";

$foo = new Foo();
print $foo->staticValue() . "\n";
print $foo->my_static . "\n";      // "Propiedad" my_static no definida

print $foo::$my_static . "\n";
$classname = 'Foo';
print $classname::$my_static . "\n";

print Bar::$my_static . "\n";
$bar = new Bar();
print $bar->fooStatic() . "\n";
?>

      
```

Resultado del ejemplo anterior en PHP 8 es similar a:

    foo
    foo
    Notice: Accessing static property Foo::$my_static as non static in /in/V0Rvv on line 23
    Warning: Undefined property: Foo::$my_static in /in/V0Rvv on line 23
    foo
    foo
    foo
    foo
