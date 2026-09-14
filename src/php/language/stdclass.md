---
title: La clase stdClass
source_url: https://www.php.net/manual/es/class.stdclass.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/stdclass.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 77325b622
order: 3930
---

## Introducción

Una clase genérica vacía con propiedades dinámicas.

Los objetos de esta clase pueden ser instanciados con [new](#language.oop5.basic.new) operador o creados por [conversión a objeto](#language.types.object.casting). Varias funciones de PHP también crean instancias de esta clase, por ejemplo `json_decode`, `mysqli_fetch_object` o PDOStatement::fetchObject.

A pesar de no implementar [\_\_get()](#object.get)/[\_\_set()](#object.set) métodos mágicos, esta clase permite propiedades dinámicas y no requiere el `#[\AllowDynamicProperties]` atributo.

Esto no es una clase base ya que PHP no tiene el concepto de una clase base universal. Sin embargo, es posible crear una clase personalizada que extienda de `stdClass` y como resultado herede la funcionalidad de propiedades dinámicas.

## Sinopsis de la clase

\#\[\AllowDynamicProperties\]

stdClass

Esta clase no tiene métodos ni propiedades predeterminadas.

## Ejemplos

Creado como resultado de la conversión a objeto

```php
<?php
$obj = (object) array('foo' => 'bar');
var_dump($obj);

    
```

El ejemplo anterior mostrará:

    object(stdClass)#1 (1) {
      ["foo"]=>
      string(3) "bar"
    }

Creado como resultado de `json_decode`

```php
<?php
$json = '{"foo":"bar"}';
var_dump(json_decode($json));

    
```

El ejemplo anterior mostrará:

    object(stdClass)#1 (1) {
      ["foo"]=>
      string(3) "bar"
    }

Declaración de propiedades dinámicas

```php
<?php
$obj = new stdClass();
$obj->foo = 42;
$obj->{1} = 42;
var_dump($obj);

    
```

El ejemplo anterior mostrará:

    object(stdClass)#1 (2) {
      ["foo"]=>
      int(42)
      ["1"]=>
      int(42)
    }
