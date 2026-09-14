---
title: Clases anónimas
source_url: https://www.php.net/manual/es/language.oop5.anonymous.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/anonymous.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: d6f54016d
order: 2390
---

## Clases anónimas

Las clases anónimas son útiles cuando se necesita crear objetos únicos simples.

```php
<?php

// Utilizando una clase explícita
class Logger
{
    public function log($msg)
    {
        echo $msg;
    }
}

$util->setLogger(new Logger());

// Utilizando una clase anónima
$util->setLogger(new class {
    public function log($msg)
    {
        echo $msg;
    }
});

  
```

Se les pueden pasar argumentos a través del constructor, pueden extender otras clases, implementar interfaces o utilizar traits como con una clase normal.

```php
<?php

class SomeClass {}
interface SomeInterface {}
trait SomeTrait {}

var_dump(new class(10) extends SomeClass implements SomeInterface {
    private $num;

    public function __construct($num)
    {
        $this->num = $num;
    }

    use SomeTrait;
});

  
```

El ejemplo anterior mostrará:

    object(class@anonymous)#1 (1) {
      ["Command line code0x104c5b612":"class@anonymous":private]=>
      int(10)
    }

Anidar una clase anónima dentro de otra clase no da acceso a los métodos o propiedades privadas o protegidas de la clase contenedora. Para utilizar métodos o propiedades protegidas de la clase contenedora, la clase anónima debe extenderla. Para utilizar las propiedades privadas de la clase contenedora en la clase anónima, estas deben ser pasadas a través del constructor.

```php
<?php

class Outer
{
    private $prop = 1;
    protected $prop2 = 2;

    protected function func1()
    {
        return 3;
    }

    public function func2()
    {
        return new class($this->prop) extends Outer {
            private $prop3;

            public function __construct($prop)
            {
                $this->prop3 = $prop;
            }

            public function func3()
            {
                return $this->prop2 + $this->prop3 + $this->func1();
            }
        };
    }
}

echo (new Outer)->func2()->func3();

  
```

El ejemplo anterior mostrará:

    6

Todos los objetos creados por la misma declaración de clase anónima son instancias de la misma clase.

```php
<?php
function anonymous_class()
{
    return new class {};
}

if (get_class(anonymous_class()) === get_class(anonymous_class())) {
    echo 'same class';
} else {
    echo 'different class';
}
 
```

El ejemplo anterior mostrará:

    same class

> [!NOTE]
> Tenga en cuenta que las clases anónimas son asignadas un nombre por el motor, como se ilustra en el siguiente ejemplo. Este nombre debe considerarse como un detalle de implementación, que no debe ser invocado.
>
> <div class="informalexample">
>
> ```
> <?php
> echo get_class(new class {});
>
>   
> ```
>
> Resultado del ejemplo anterior es similar a:
>
>     class@anonymous/in/oNi1A0x7f8636ad2021
>
>        
>
> </div>

## Clases anónimas de solo lectura

A partir de PHP 8.3.0, el modificador `readonly` puede ser aplicado a las clases anónimas.

Definir una clase anónima de solo lectura

```php
    
<?php
// Utilización de una clase anónima
var_dump(new readonly class('[DEBUG]') {
    public function __construct(private string $prefix)
    {
    }

    public function log($msg)
    {
        echo $this->prefix . ' ' . $msg;
    }
});

   
```
