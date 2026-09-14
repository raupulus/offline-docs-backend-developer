---
title: Constantes de clase
source_url: https://www.php.net/manual/es/language.oop5.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 922b4b5ae
order: 2440
---

## Constantes de clase

Es posible definir [constantes](#language.constants) por clases que permanecen idénticas y no modificables. La visibilidad por omisión de las constantes de clase es `public`.

> [!NOTE]
> Las constantes de clases pueden ser redefinidas por una clase hija. A partir de PHP 8.1.0, las constantes de clases no pueden ser redefinidas por una clase hija si ha sido definida como [final](#language.oop5.final).

También es posible para las interfaces tener constantes. Ver la [documentación de las interfaces](#language.oop5.interfaces) para ejemplos.

Es posible referenciar la clase utilizando una variable. El valor de la variable no puede ser una palabra clave (por ejemplo, `self`, `parent` y `static`).

Tenga en cuenta que las constantes de clase son asignadas una vez por clase, y no para cada instancia de clase.

A partir de PHP 8.3.0, las constantes de clase pueden tener un tipo escalar como `bool`, `int`, `float`, `string`, o incluso `array`. Al utilizar `array`, su contenido solo puede contener otros tipos escalares.

Definición y uso de una constante de clase

```php
<?php
class MyClass
{
  const CONSTANT = 'valor constante';

  function showConstant() {
    echo  self::CONSTANT . "\n";
  }
}

echo MyClass::CONSTANT . "\n";

$classname = "MyClass";
echo $classname::CONSTANT . "\n";

$class = new MyClass();
$class->showConstant();

echo $class::CONSTANT."\n";
?>

  
```

La constante especial `::class` permite una resolución de nombre de clase completamente cualificado en el momento de la compilación, esto es útil para las clases en un espacio de nombres:

Ejemplo de uso de ::class

```php
<?php
namespace foo {
    class bar {
    }

    echo bar::class; // foo\bar
}
?>

  
```

Ejemplo de expresiones para una constante de clase

```php
<?php
const ONE = 1;
class foo {
    const TWO = ONE * 2;
    const THREE = ONE + self::TWO;
    const SENTENCE = 'El valor de THREE es '.self::THREE;
}
?>

  
```

Modificador de visibilidad de las constantes de clase, a partir de PHP 7.1

```php
<?php
class Foo {
    public const BAR = 'bar';
    private const BAZ = 'baz';
}
echo Foo::BAR, PHP_EOL;
echo Foo::BAZ, PHP_EOL;
?>

  
```

Resultado del ejemplo anterior en PHP 7.1:

    bar

    Fatal error: Uncaught Error: Cannot access private const Foo::BAZ in …

> [!NOTE]
> A partir de PHP 7.1.0, los modificadores de visibilidad son permitidos en las constantes de clase.

Verificación de varianza de visibilidad de las constantes de clase, a partir de PHP 8.3.0

```php
<?php

interface MyInterface
{
    public const VALUE = 42;
}

class MyClass implements MyInterface
{
    protected const VALUE = 42;
}
?>

  
```

Resultado del ejemplo anterior en PHP 8.3:

    Fatal error: Access level to MyClass::VALUE must be public (as in interface MyInterface) …

> [!NOTE]
> A partir de PHP 8.3.0, la varianza de visibilidad es verificada de manera más estricta. Antes de esta versión, la visibilidad de una constante de clase podía diferir de la de la constante en la interfaz implementada.

Sintaxis de acceso dinámico a las constantes de clase, a partir de PHP 8.3.0

```php
<?php
class Foo {
    public const BAR = 'bar';
    private const BAZ = 'baz';
}

$name = 'BAR';
echo Foo::{$name}, PHP_EOL; // bar
?>

  
```

> [!NOTE]
> A partir de PHP 8.3.0, las constantes de clase pueden ser recuperadas dinámicamente utilizando una variable.

Asignación de tipos a las constantes de clase, a partir de PHP 8.3.0

```php
<?php

class MyClass {
    public const bool MY_BOOL = true;
    public const int MY_INT = 1;
    public const float MY_FLOAT = 1.01;
    public const string MY_STRING = 'one';
    public const array MY_ARRAY = [self::MY_BOOL, self::MY_INT, self::MY_FLOAT, self::MY_STRING];
}

var_dump(MyClass::MY_BOOL);
var_dump(MyClass::MY_INT);
var_dump(MyClass::MY_FLOAT);
var_dump(MyClass::MY_STRING);
var_dump(MyClass::MY_ARRAY);
?>

    
```

Resultado del ejemplo anterior en PHP 8.3:

    bool(true)
    int(1)
    float(1.01)
    string(3) "one"
    array(4) {
      [0]=>
      bool(true)
      [1]=>
      int(1)
      [2]=>
      float(1.01)
      [3]=>
      string(3) "one"
    }
