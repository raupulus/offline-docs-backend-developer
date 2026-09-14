---
title: Abstracción de clases
source_url: https://www.php.net/manual/es/language.oop5.abstract.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/abstract.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: c1f37a6c2
order: 2380
---

## Abstracción de clases

PHP tiene clases, métodos y propiedades abstractas. Las clases definidas como abstractas no pueden ser instanciadas, y cualquier clase que contenga al menos un método abstracto debe ser también abstracta. Los métodos definidos como abstractos se contentan con declarar la firma del método y con indicar si es público o protegido; no pueden definir la implementación. Las propiedades definidas como abstractas pueden declarar un requisito para el comportamiento de `get` o de `set`, y pueden proporcionar una implementación para una de estas operaciones, pero no para ambas.

Al heredar de una clase abstracta, todos los métodos marcados como abstractos en la declaración de la clase padre deben ser definidos por la clase hija y seguir las reglas habituales de [herencia](#language.oop5.inheritance) y de [compatibilidad de firma](#language.oop.lsp).

A partir de PHP 8.4, una clase abstracta puede declarar una propiedad abstracta, pública o protegida. Una propiedad abstracta protegida puede ser satisfecha por una propiedad accesible en lectura/escritura desde un contexto protegido o público.

Una propiedad abstracta puede ser satisfecha ya sea por una propiedad estándar, ya sea por una propiedad con [hooks](#language.oop5.property-hooks) definidos, correspondiente a la operación requerida.

Ejemplo de método abstracto

```php
<?php

abstract class AbstractClass
{
    // Fuerza a las clases hijas a definir este método
    abstract protected function getValue();
    abstract protected function prefixValue($prefix);

    // método común
   public function printOut()
   {
        print $this->getValue() . "\n";
   }
}

class ConcreteClass1 extends AbstractClass
{
     protected function getValue()
     {
       return "ConcreteClass1";
     }

     public function prefixValue($prefix)
     {
       return "{$prefix}ConcreteClass1";
     }
}

class ConcreteClass2 extends AbstractClass
{
     public function getValue()
     {
       return "ConcreteClass2";
     }

     public function prefixValue($prefix)
     {
       return "{$prefix}ConcreteClass2";
     }
}

$class1 = new ConcreteClass1();
$class1->printOut();
echo $class1->prefixValue('FOO_'), "\n";

$class2 = new ConcreteClass2();
$class2->printOut();
echo $class2->prefixValue('FOO_'), "\n";

?>

  
```

El ejemplo anterior mostrará:

    ConcreteClass1
    FOO_ConcreteClass1
    ConcreteClass2
    FOO_ConcreteClass2

Ejemplo de método abstracto

```php
<?php

abstract class AbstractClass
{
    // Un método abstracto solo debe definir los argumentos requeridos
    abstract protected function prefixName($name);

}

class ConcreteClass extends AbstractClass
{

    // Una clase hija puede definir argumentos opcionales que no están presentes en la firma del padre
     public function prefixName($name, $separator = ".")
     {
        if ($name == "Pacman") {
            $prefix = "Mr";
        } elseif ($name == "Pacwoman") {
            $prefix = "Mrs";
        } else {
            $prefix = "";
        }

        return "{$prefix}{$separator} {$name}";
    }
}

$class = new ConcreteClass();
echo $class->prefixName("Pacman"), "\n";
echo $class->prefixName("Pacwoman"), "\n";

?>

   
```

El ejemplo anterior mostrará:

    Mr. Pacman
    Mrs. Pacwoman

Ejemplo de propiedad abstracta

```php
<?php

abstract class A
{
    // Las clases derivadas deben tener una propiedad públicamente accesible en lectura.
    abstract public string $readable {
        get;
    }

    // Las clases derivadas deben tener una propiedad modificable en escritura, protegida o pública.
     abstract protected string $writeable {
         set;
    }

    // Las clases derivadas deben tener una propiedad simétrica protegida o pública.
     abstract protected string $both {
         get;
         set;
     }
}

class C extends A
{
    // Esto satisface el requisito y también hace que la propiedad sea modificable, lo cual es válido.
    public string $readable;

    // Esto NO satisfaría el requisito, ya que la propiedad no es públicamente accesible en lectura.
    protected string $readable;

    // Esto satisface exactamente el requisito, por lo que es suficiente.
    // La propiedad solo puede ser modificada desde un contexto protegido.
    protected string $writeable {
        set => $value;
    }

    // Esto amplía la visibilidad de protegido a público, lo cual es aceptable.
    public string $both;
}
?>

   
```

Una propiedad abstracta en una clase abstracta puede proporcionar implementaciones para cualquier punto de anclaje, pero debe tener `get` o `set` declarados pero no definidos (como en el ejemplo anterior).

Ejemplo de propiedad abstracta con hooks

```php
<?php

abstract class A
{
    // Esto proporciona una implementación por defecto (pero sustituible) para set,
    // y exige que las clases derivadas proporcionen una implementación para get.
    abstract public string $foo {
        get;

        set {
            $this->foo = $value
        };
    }
}

?>

   
```
