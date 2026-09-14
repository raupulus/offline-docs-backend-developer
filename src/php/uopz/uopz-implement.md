---
title: uopz_implement
description: Implementa una interfaz en tiempo de ejecución
source_url: https://www.php.net/manual/es/function.uopz-implement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uopz/functions/uopz-implement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uopz
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 99330
---

uopz_implement

Implementa una interfaz en tiempo de ejecución

## Descripción

```php
uopz_implement(string $class, string $interface): bool
```php

Implementa la `interface` en la `class`.

## Parámetros

`class`  
El nombre de la clase.

`interface`  
El nombre de la interfaz.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

A partir de PHP 7.4.0, `uopz_implement` emite una `RuntimeException`, si [OPcache](#book.opcache) está activado, y la entrada de clase de `class` es inmutable.

## Ejemplos

Ejemplo con `uopz_implement`

```
<?php
interface myInterface {}

class myClass {}

uopz_implement(myClass::class, myInterface::class);

var_dump(class_implements(myClass::class));
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      ["myInterface"]=>
      string(11) "myInterface"
    }
