---
title: settype
description: Asigna un tipo a una variable
source_url: https://www.php.net/manual/es/function.settype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/settype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_reviewed: true
translation_revision: 8d49e302b
order: 100750
---

settype

Asigna un tipo a una variable

## Descripción

```php
settype(mixed $var, string $type): bool
```php

Fuerza el tipo de la variable `var` a `type`.

## Parámetros

`var`  
La variable a convertir.

`type`  
Los valores posibles para el argumento `type` son:

- "boolean" o "bool"

- "integer" o "int"

- "float" o "double"

- "string"

- "array"

- "object"

- "`null`"

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Lanza una excepción ValueError si el valor de `type` no es un tipo válido, a partir de PHP 8.0.0. Antes de PHP 8.0.0, se emitía un `E_WARNING` y se devolvía `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Ahora lanza una excepción ValueError cuando se pasa un tipo no válido a `type`. Anteriormente, se emitía un `E_WARNING` y la función devolvía `false`. |

## Ejemplos

Ejemplo con `settype`

```
<?php
$foo = "5bar"; // string
$bar = true;   // bool

settype($foo, "integer"); // $foo vale ahora 5   (integer)
settype($bar, "string");  // $bar vale ahora "1" (string)

var_dump($foo, $bar);
?>

    
```php

## Notas

> [!NOTE]
> El valor máximo de los enteros es el valor contenido en la variable `PHP_INT_MAX`.

## Véase también

`gettype`, [conversión de tipo](#language.types.typecasting), [manipulación de tipos](#language.types.type-juggling)
