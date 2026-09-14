---
title: Palabra clave "final"
source_url: https://www.php.net/manual/es/language.oop5.final.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/final.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 907f8ab64
order: 2460
---

## Palabra clave "final"

La palabra clave final impide que las clases hijas redefinan un método, una propiedad o constante prefijando la definición con `final`. Si la clase misma es definida como final, no podrá ser extendida.

Ejemplo de método final

```php
<?php
class BaseClass {
   public function test() {
       echo "BaseClass::test() llamada\n";
   }

   final public function moreTesting() {
       echo "BaseClass::moreTesting() llamada\n";
   }
}

class ChildClass extends BaseClass {
   public function moreTesting() {
       echo "ChildClass::moreTesting() llamada\n";
   }
}
// Resultado: Fatal error: Cannot override final method BaseClass::moreTesting()
?>

   
```

Ejemplo de clase final

```php
<?php
final class BaseClass {
   public function test() {
       echo "BaseClass::test() llamada\n";
   }

   // Como la clase ya es final, la palabra clave final es redundante
   final public function moreTesting() {
       echo "BaseClass::moreTesting() llamada\n";
   }
}

class ChildClass extends BaseClass {
}
// Resultado: Fatal error: Class ChildClass may not inherit from final class (BaseClass)
?>

   
```

Ejemplo de propiedad final a partir de PHP 8.4.0

```php
<?php
class BaseClass {
   final protected string $test;
}

class ChildClass extends BaseClass {
    public string $test;
}
// Resultado: Error fatal: Imposible redefinir la propiedad final BaseClass::$test
?>

  
```

Ejemplo de constantes finales a partir de PHP 8.1.0

```php
<?php
class Foo
{
    final public const X = "foo";
}

class Bar extends Foo
{
    public const X = "bar";
}

// Fatal error: Bar::X cannot override final constant Foo::X
?>

  
```

> [!NOTE]
> A partir de PHP 8.0.0, los métodos privados no pueden ser declarados finales, con la excepción del [constructor](#language.oop5.decon.constructor).

> [!NOTE]
> Una propiedad declarada [`private(set)`](#language.oop5.visibility-members-aviz) es implícitamente `final`.
