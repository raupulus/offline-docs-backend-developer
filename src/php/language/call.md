---
title: Closure::call
description: Vincula y llama al cierre
source_url: https://www.php.net/manual/es/closure.call.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/closure/call.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 9c74079f1
order: 3060
---

Closure::call

Vincula y llama al cierre

## Descripción

```php
public Closure::call(object $newThis, mixed ...$args): mixed
```php

Vincula temporalmente el cierre a `newThis`, y lo llama con cualquier parámetro dado.

## Parámetros

`newThis`  
El `object` a vincular al cierre mientras dure la llamada.

`args`  
Cero o más parámetros, que serán dados como parámetros al cierre.

## Valores devueltos

Devuelve el valor devuelto por el cierre.

## Ejemplos

Ejemplo de `Closure::call`

```
<?php
class Valor {
    protected $valor;

    public function __construct($valor) {
        $this->valor = $valor;
    }

    public function getValor() {
        return $this->valor;
    }
}

$tres = new Valor(3);
$cuatro = new Valor(4);

$cierre = function ($delta) { var_dump($this->getValor() + $delta); };
$cierre->call($tres, 4);
$cierre->call($cuatro, 4);
?>

   
```php

El ejemplo anterior mostrará:

    int(7)
    int(8)
