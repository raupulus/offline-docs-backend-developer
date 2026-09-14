---
title: La interfaz ArrayAccess
source_url: https://www.php.net/manual/es/class.arrayaccess.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/arrayaccess.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: true
translation_revision: 4b06b2d5c
order: 2860
---

## Introducción

Interfaz que permite acceder a los objetos de la misma manera que a los arrays.

## Sinopsis de la interfaz

ArrayAccess

Métodos

## Ejemplos

Ejemplo básico

```php
<?php
class Obj implements ArrayAccess {
    public $container = [
        "one"   => 1,
        "two"   => 2,
        "three" => 3,
    ];

    public function offsetSet($offset, $value): void {
        if (is_null($offset)) {
            $this->container[] = $value;
        } else {
            $this->container[$offset] = $value;
        }
    }

    public function offsetExists($offset): bool {
        return isset($this->container[$offset]);
    }

    public function offsetUnset($offset): void {
        unset($this->container[$offset]);
    }

    public function offsetGet($offset): mixed {
        return isset($this->container[$offset]) ? $this->container[$offset] : null;
    }
}

$obj = new Obj;

var_dump(isset($obj["dos"]));
var_dump($obj["dos"]);
unset($obj["dos"]);
var_dump(isset($obj["dos"]));
$obj["dos"] = "Un valor";
var_dump($obj["dos"]);
$obj[] = 'Añadido 1';
$obj[] = 'Añadido 2';
$obj[] = 'Añadido 3';
print_r($obj);

    
```

Resultado del ejemplo anterior es similar a:

    bool(true)
    int(2)
    bool(false)
    string(9) "Un valor"
    Obj Object
    (
        [container] => Array
            (
                [uno] => 1
                [tres] => 3
                [dos] => Un valor
                [0] => Añadido 1
                [1] => Añadido 2
                [2] => Añadido 3
            )

    )
