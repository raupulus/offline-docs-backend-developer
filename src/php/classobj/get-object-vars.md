---
title: get_object_vars
description: Devuelve las propiedades de un objeto
source_url: https://www.php.net/manual/es/function.get-object-vars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-object-vars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: c9bc21cb7
order: 6850
---

get_object_vars

Devuelve las propiedades de un objeto

## Descripción

```php
get_object_vars(object $object): array
```php

Recupera las propiedades no estáticas del objeto `object`, accesibles desde el contexto.

## Parámetros

`object`  
Una instancia de un objeto.

## Valores devueltos

Devuelve un `array` asociativo que contiene las propiedades no estáticas, accesibles desde el contexto actual, del objeto `object`.

## Ejemplos

Ejemplo con `get_object_vars`

```
<?php

class foo {
    private $a;
    public $b = 1;
    public $c;
    private $d;
    static $e;

    public function test() {
        var_dump(get_object_vars($this));
    }
}

$test = new foo;
var_dump(get_object_vars($test));

$test->test();

?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      ["b"]=>
      int(1)
      ["c"]=>
      NULL
    }
    array(4) {
      ["a"]=>
      NULL
      ["b"]=>
      int(1)
      ["c"]=>
      NULL
      ["d"]=>
      NULL
    }

> [!NOTE]
> Las propiedades no inicializadas son consideradas inaccesibles, y por lo tanto no serán incluidas en el array.

## Véase también

`get_class_methods`, `get_class_vars`
