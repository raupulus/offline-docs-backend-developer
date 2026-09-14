---
title: class_uses
description: Devuelve los traits utilizados por una clase dada.
source_url: https://www.php.net/manual/es/function.class-uses.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/class-uses.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 42bd1bfed
order: 82210
---

class_uses

Devuelve los traits utilizados por una clase dada.

## Descripción

```php
class_uses(object $object_or_class, [bool $autoload]): array
```php

Esta función devuelve un array representando los nombres de los traits que la clase dada utiliza. Los traits de las clases padres no son representados.

## Parámetros

`object_or_class`  
Un objeto o un nombre de clase en forma de string.

`autoload`  
Define si debe [autocargarse](#language.oop5.autoload) si no está ya autocargado.

## Valores devueltos

Un array en caso de éxito, o `false` cuando la clase dada no existe.

## Ejemplos

Ejemplos para `class_uses`

```
<?php

trait foo { }
class bar {
  use foo;
}

print_r(class_uses(new bar));

print_r(class_uses('bar'));

spl_autoload_register();

// Utilización del autoloading para cargar la clase 'not_loaded'
print_r(class_uses('not_loaded', true));

?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [foo] => foo
    )
    Array
    (
        [foo] => foo
    )
    Array
    (
        [trait_of_not_loaded] => trait_of_not_loaded
    )

## Véase también

`class_parents`, `get_declared_traits`
