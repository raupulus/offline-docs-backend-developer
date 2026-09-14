---
title: Ds\Vector::__construct
description: Crea una nueva instancia
source_url: https://www.php.net/manual/es/ds-vector.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ds/ds/vector/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ds
translation_status: ready
translation_reviewed: false
translation_revision: dd07341fa
order: 16220
---

Ds\Vector::\_\_construct

Crea una nueva instancia

## Descripción

```php
public Ds\Vector::__construct([mixed $values])
```php

Crea una nueva instancia, utilizando un objeto `traversable` o un `array` para los `valores` iniciales.

## Parámetros

`values`  
Un objeto traversable o un `array` a utilizar para los valores iniciales.

## Ejemplos

Ejemplo de `Ds\Vector::__construct`

```
<?php
$vector = new \Ds\Vector();
var_dump($vector);

$vector = new \Ds\Vector([1, 2, 3]);
var_dump($vector);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    object(Ds\Vector)#2 (0) {
    }
    object(Ds\Vector)#2 (3) {
      [0]=>
      int(1)
      [1]=>
      int(2)
      [2]=>
      int(3)
    }
