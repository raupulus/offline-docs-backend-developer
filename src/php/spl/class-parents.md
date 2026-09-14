---
title: class_parents
description: Devuelve las clases padres de una clase
source_url: https://www.php.net/manual/es/function.class-parents.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/class-parents.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 60af8c2b7
order: 82200
---

class_parents

Devuelve las clases padres de una clase

## Descripción

```php
class_parents(object $object_or_class, [bool $autoload]): array
```php

`class_parents` devuelve un array con el nombre de las clases padres de la clase `object_or_class`.

## Parámetros

`object_or_class`  
Un objeto (instancia) o un string (nombre de la clase).

`autoload`  
Define si debe [autocargarse](#language.oop5.autoload) si no está ya autocargado.

## Valores devueltos

Un array en caso de éxito, o `false` cuando la clase dada no existe.

## Ejemplos

Ejemplo con `class_parents`

```
<?php

class foo { }
class bar extends foo {}

print_r(class_parents(new bar));

// También puede especificarse el argumento como un string
print_r(class_parents('bar'));

spl_autoload_register();

// Uso del autoloading para cargar la clase 'not_loaded'
print_r(class_parents('not_loaded', true));

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
       [parent_of_not_loaded] => parent_of_not_loaded
    )

## Notas

> [!NOTE]
> Es preferible utilizar [`instanceof`](#language.operators.type) o la función `is_a` para verificar que un objeto implementa una interfaz.

## Véase también

`class_implements`, `is_a`, [`instanceof`](#language.operators.type)
