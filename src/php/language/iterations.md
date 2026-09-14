---
title: Recorrido de objetos
source_url: https://www.php.net/manual/es/language.oop5.iterations.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/oop5/iterations.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 1fb0ef23d
order: 2490
---

## Recorrido de objetos

PHP proporciona una manera de definir los objetos de manera que se pueda recorrer una lista de miembros, por ejemplo con una estructura [`foreach`](#control-structures.foreach). Por omisión, todas las propiedades [visibles](#language.oop5.visibility) serán utilizadas para el recorrido.

Recorrido de objeto simple

```php
<?php
class MyClass
{
  public $var1 = 'valor 1';
  public $var2 = 'valor 2';
  public $var3 = 'valor 3';

  protected $protected = 'variable protegida';
  private   $private   = 'variable privada';

  function iterateVisible() {
     echo "MyClass::iterateVisible:\n";
     foreach ($this as $key => $value) {
         print "$key => $value\n";
     }
  }
}

$class = new MyClass();

foreach($class as $key => $value) {
    print "$key => $value\n";
}
echo "\n";

$class->iterateVisible();

    
```

El ejemplo anterior mostrará:

```php
var1 => valor 1
var2 => valor 2
var3 => valor 3

MyClass::iterateVisible:
var1 => valor 1
var2 => valor 2
var3 => valor 3
protected => variable protegida
private => variable privada

    
```

Como muestra la salida, la iteración [`foreach`](#control-structures.foreach) recorrió todas las propiedades [visibles](#language.oop5.visibility) que pudieron ser accedidas.

## Véase también

[Generators](#language.generators), Iterator, IteratorAggregate, [SPL Iterators](#spl.iterators)
