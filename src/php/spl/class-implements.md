---
title: class_implements
description: Devuelve las interfaces implementadas por una clase o interfaz dada
source_url: https://www.php.net/manual/es/function.class-implements.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/functions/class-implements.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 60af8c2b7
order: 82190
---

class_implements

Devuelve las interfaces implementadas por una clase o interfaz dada

## Descripción

```php
class_implements(object $object_or_class, [bool $autoload]): array
```php

Esta función devuelve un array con los nombres de las interfaces que la clase `object_or_class` así como sus padres implementan.

## Parámetros

`object_or_class`  
Un objeto (instancia) o una cadena de caracteres (nombre de la clase o de la interfaz).

`autoload`  
Define si debe [autocargarse](#language.oop5.autoload) si no está ya autocargado.

## Valores devueltos

Un array en caso de éxito, o `false` cuando la clase dada no existe.

## Ejemplos

Ejemplo con `class_implements`

```
<?php

interface foo { }
class bar implements foo {}

print_r(class_implements(new bar));

// También se puede especificar el argumento como una cadena de caracteres
print_r(class_implements('bar'));

spl_autoload_register();

// Uso del autoloading para cargar la clase 'not_loaded'
print_r(class_implements('not_loaded', true));

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
        [interface_de_non_chargée] => interface_de_non_chargée
    )

## Notas

> [!NOTE]
> Es preferible utilizar [`instanceof`](#language.operators.type) o la función `is_a` para verificar que un objeto implementa una interfaz.

## Véase también

`class_parents`, `get_declared_interfaces`, `is_a`, [`instanceof`](#language.operators.type)
