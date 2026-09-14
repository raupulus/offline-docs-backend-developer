---
title: uopz_compose
description: Componer una clase
source_url: https://www.php.net/manual/es/function.uopz-compose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-compose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_revision: c9490d424
order: 99200
---

uopz_compose

Componer una clase

> [!WARNING]
> Esta función ha sido *ELIMINADA* en PECL uopz 5.0.0.

## Descripción

```php
uopz_compose(string $name, array $classes, [array $methods], [array $properties], [int $flags]): void
```php

Crea una nueva clase con el nombre especificado, que implementa, extiende o utiliza todas las clases proporcionadas.

## Parámetros

`name`  
Un nombre de clase válido

`classes`  
Un array de clases, interfaces o nombres de trait

`methods`  
Un array asociativo de métodos; los valores son o bien closures, o bien \[modificadores =\> closure\]

`properties`  
Un array asociativo de propiedades, con las claves como nombres, y los valores como modificadores

`flags`  
Tipo de entrada; por omisión, ZEND_ACC_CLASS

## Valores devueltos

## Ejemplos

Ejemplo con `uopz_compose`

```
<?php
class myClass {}
trait myTrait {}
interface myInterface {}

uopz_compose(
    Composed::class, [
        myClass::class,
        myTrait::class,
        myInterface::class
    ], [
    "__construct" => function() {
        /* ... */
    }
]);

var_dump(
 class_uses(Composed::class),
 class_parents(Composed::class),
 class_implements(Composed::class));
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      ["myTrait"]=>
      string(7) "myTrait"
    }
    array(1) {
      ["myClass"]=>
      string(7) "myClass"
    }
    array(1) {
      ["myInterface"]=>
      string(11) "myInterface"
    }
