---
title: ArrayAccess::offsetExists
description: Comprobar si existe un índice
source_url: https://www.php.net/manual/es/arrayaccess.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/arrayaccess/offsetexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 09003ff79
order: 2820
---

ArrayAccess::offsetExists

Comprobar si existe un índice

## Descripción

```php
public ArrayAccess::offsetExists(mixed $offset): bool
```php

Comprueba si existe o no un índice.

Este método se ejecuta cuando se utilizan las funciones `isset` o `empty` sobre los objetos que implementan `ArrayAccess`.

> [!NOTE]
> Cuando se utiliza `empty`, `ArrayAccess::offsetGet` será invocada para comprobar si está vacío solamente si `ArrayAccess::offsetExists` devuelve `true`.

## Parámetros

`offset`  
El índice a comprobar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!NOTE]
> El valor de retorno se debe convertir a `bool` si no devuelve un valor boleano.

## Ejemplos

Ejemplo de `ArrayAccess::offsetExists`

```
<?php
class obj implements ArrayAccess {
    public function offsetSet($offset, $value): void {
        var_dump(__METHOD__);
    }
    public function offsetExists($var): bool {
        var_dump(__METHOD__);
        if ($var == "foobar") {
            return true;
        }
        return false;
    }
    public function offsetUnset($var): void {
        var_dump(__METHOD__);
    }
    #[\ReturnTypeWillChange]
    public function offsetGet($var) {
        var_dump(__METHOD__);
        return "value";
    }
}

$obj = new obj;

echo "Runs obj::offsetExists()\n";
var_dump(isset($obj["foobar"]));

echo "\nRuns obj::offsetExists() and obj::offsetGet()\n";
var_dump(empty($obj["foobar"]));

echo "\nRuns obj::offsetExists(), *not* obj:offsetGet() as there is nothing to get\n";
var_dump(empty($obj["foobaz"]));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Runs obj::offsetExists()
    string(17) "obj::offsetExists"
    bool(true)

    Runs obj::offsetExists() and obj::offsetGet()
    string(17) "obj::offsetExists"
    string(14) "obj::offsetGet"
    bool(false)

    Runs obj::offsetExists(), *not* obj:offsetGet() as there is nothing to get
    string(17) "obj::offsetExists"
    bool(true)
