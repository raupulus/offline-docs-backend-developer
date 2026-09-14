---
title: class_alias
description: Crea un alias de clase
source_url: https://www.php.net/manual/es/function.class-alias.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/class-alias.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: ff9181ea0
order: 6740
---

class_alias

Crea un alias de clase

## Descripción

```php
class_alias(string $class, string $alias, [bool $autoload]): bool
```php

Crea un alias llamado `alias` basado en una clase `class` definida por el usuario. El alias es en todos los puntos similar a la clase original.

El alias de clase no puede ser ninguna de las [palabras reservadas](#reserved.other-reserved-words) de PHP.

> [!NOTE]
> A partir de PHP 8.3.0, `class_alias` también soporta la creación de un alias de una clase interna de PHP.

## Parámetros

`class`  
La clase original.

`alias`  
El nombre del alias de la clase.

`autoload`  
Si debe [cargarse automáticamente](#language.oop5.autoload) si la clase original no es encontrada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | `class_alias` ahora soporta la creación de un alias de una clase interna. |

## Ejemplos

Ejemplo con `class_alias`

```
<?php

class Foo { }

class_alias('Foo', 'Bar');

$a = new Foo;
$b = new Bar;

// los objetos son los mismos
var_dump($a == $b, $a === $b);
var_dump($a instanceof $b);

// las clases son las mismas
var_dump($a instanceof Foo);
var_dump($a instanceof Bar);

var_dump($b instanceof Foo);
var_dump($b instanceof Bar);

?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    bool(true)
    bool(true)
    bool(true)
    bool(true)
    bool(true)

## Notas

> [!NOTE]
> Los nombres de clases no son sensibles a mayúsculas/minúsculas en PHP, y esto se refleja en esta función. Los alias creados por `class_alias` son declarados en minúsculas. Esto significa que para una clase `MyClass`, la llamada `class_alias('MyClass', 'MyClassAlias')` declarará un nuevo alias de clase llamado `myclassalias`.

## Véase también

`get_parent_class`, `is_subclass_of`
