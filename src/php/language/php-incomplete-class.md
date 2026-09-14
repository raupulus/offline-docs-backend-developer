---
title: La clase __PHP_Incomplete_Class
source_url: https://www.php.net/manual/es/class.php-incomplete-class.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/php-incomplete-class.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 77325b622
order: 3820
---

## Introducción

Creada por `unserialize` al intentar deserializar una clase no definida o una clase que no está incluida en el `allowed_classes` de `unserialize` en el array `options`.

Antes de PHP 7.2.0, usar `is_object` en la clase `__PHP_Incomplete_Class` devolvería `false`. A partir de PHP 7.2.0, se devolverá `true`.

## Sinopsis de la clase

\#\[\AllowDynamicProperties\]

final

\_\_PHP_Incomplete_Class

Esta clase no tiene propiedades o métodos predeterminados. Cuando es creada por `unserialize`, además de todas las propiedades y valores deserializados el objeto tendrá una propiedad `__PHP_Incomplete_Class_Name` que contendrá el nombre de la clase deserializada.

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | Esta clase ahora es `final`. |

## Ejemplos

Creada por `unserialize`

```php
<?php

class MyClass
{
    public string $property = "myValue";
}

$myObject = new MyClass;

$foo = serialize($myObject);

// deserializa todos los objetos en objetos __PHP_Incomplete_Class
$disallowed = unserialize($foo, ["allowed_classes" => false]);

var_dump($disallowed);

// deserializa todos los objetos en objetos __PHP_Incomplete_Class excepto aquellos de MyClass2 y MyClass3
$disallowed2 = unserialize($foo, ["allowed_classes" => ["MyClass2", "MyClass3"]]);

var_dump($disallowed2);

// deserializa una clase no definida en un objeto __PHP_Incomplete_Class
$undefinedClass = unserialize('O:16:"MyUndefinedClass":0:{}');

var_dump($undefinedClass);

    
```

El ejemplo anterior mostrará:

    object(__PHP_Incomplete_Class)#2 (2) {
      ["__PHP_Incomplete_Class_Name"]=>
      string(7) "MyClass"
      ["property"]=>
      string(7) "myValue"
    }
    object(__PHP_Incomplete_Class)#3 (2) {
      ["__PHP_Incomplete_Class_Name"]=>
      string(7) "MyClass"
      ["property"]=>
      string(7) "myValue"
    }
    object(__PHP_Incomplete_Class)#4 (1) {
      ["__PHP_Incomplete_Class_Name"]=>
      string(16) "MyUndefinedClass"
    }
