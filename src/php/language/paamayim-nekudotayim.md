---
title: El operador de resolución de ámbito (::)
source_url: https://www.php.net/manual/es/language.oop5.paamayim-nekudotayim.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/paamayim-nekudotayim.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 2550
---

## El operador de resolución de ámbito (::)

El operador de resolución de ámbito (también llamado Paamayim Nekudotayim) o, en términos más simples, el símbolo "doble dos puntos" (::), proporciona un medio para acceder a los miembros una [constante](#language.oop5.constants), una propiedad [estática](#language.oop5.static), o un método [estático](#language.oop5.static) de una clase o de una de sus clases padre. Además, las propiedades o métodos estáticos pueden ser sobrecargados vía la [ligadura estática tardía](#language.oop5.late-static-bindings).

Cuando se hace referencia a estos elementos fuera de la definición de la clase, se utiliza el nombre de la clase.

Es posible referenciar una clase utilizando una variable. El valor de la variable no puede ser una palabra clave (e.g. `self`, `parent` y `static`).

Paamayim Nekudotayim podría parecer al principio una elección extraña para nombrar un doble dos puntos. Sin embargo, en el momento de la escritura del Zend Engine 0.5 (que hacía funcionar PHP 3), fue el nombre elegido por el equipo Zend. De hecho, esto significa un doble dos puntos... ¡en hebreo!

:: fuera de la definición de la clase

```php
<?php
class MyClass {
    const CONST_VALUE = 'Un valor constante';
}

$classname = 'MyClass';
echo $classname::CONST_VALUE;

echo MyClass::CONST_VALUE;
?>

  
```

Tres palabras clave especiales, `self`, `parent`, y `static` son utilizadas para acceder a las propiedades o a los métodos desde la definición de la clase.

:: desde la definición de la clase

```php
<?php
class MyClass {
    const CONST_VALUE = 'Un valor constante';
}

class OtherClass extends MyClass
{
    public static $my_static = 'variable estática';

    public static function doubleColon() {
        echo parent::CONST_VALUE . "\n";
        echo self::$my_static . "\n";
    }
}

$classname = 'OtherClass';
$classname::doubleColon();

OtherClass::doubleColon();
?>

  
```

Cuando una clase que hereda de otra redefine un método de su clase padre, PHP no llamará al método de la clase padre. Es responsabilidad del método derivado llamar al método original en caso de necesidad. Esto también es válido para las definiciones de los [constructores y destructores](#language.oop5.decon), la [sobrecarga](#language.oop5.overloading), y las definiciones de [métodos mágicos](#language.oop5.magic).

Llamada a un método padre

```php
<?php
class MyClass
{
    protected function myFunc() {
        echo "MyClass::myFunc()\n";
  }
}

class OtherClass extends MyClass
{
    // Sobrecarga de la definición padre
    public function myFunc() {

      // Pero llamada al método padre
      parent::myFunc();
      echo "OtherClass::myFunc()\n";
  }
}

$class = new OtherClass();
$class->myFunc();
?>

  
```

Ver también [algunos ejemplos de llamadas estáticas](#language.oop5.basic.class.this).
