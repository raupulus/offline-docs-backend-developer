---
title: Ds\Stack::__construct
description: Crear una nueva instancia
source_url: https://www.php.net/manual/es/ds-stack.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/stack/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16090
---

Ds\Stack::\_\_construct

Crear una nueva instancia

## Descripción

```php
public Ds\Stack::__construct([mixed $values])
```php

Crear una nueva instancia, utilizando un objeto `traversable` o un `array` para los `values` iniciales.

## Parámetros

`values`  
Un objeto traversable o un `array` a utilizar para los valores iniciales.

## Ejemplos

Ejemplo de `Ds\Stack::__construct`

```
<?php
$stack = new \Ds\Stack();
print_r($stack);

$stack = new \Ds\Stack([1, 2, 3]);
print_r($stack);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Ds\Stack Object
    (
    )
    Ds\Stack Object
    (
        [0] => 3
        [1] => 2
        [2] => 1
    )
