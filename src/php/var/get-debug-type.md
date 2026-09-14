---
title: get_debug_type
description: Devuelve el nombre del tipo de la variable de una manera adecuada para
  el depurado
source_url: https://www.php.net/manual/es/function.get-debug-type.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/var/functions/get-debug-type.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: var
translation_status: ready
translation_revision: d816a0fad
order: 100490
---

get_debug_type

Devuelve el nombre del tipo de la variable de una manera adecuada para el depurado

## Descripción

```php
get_debug_type(mixed $value): string
```php

Devuelve el nombre resuelto de la variable PHP `value`. Esta función resolverá los objetos a su nombre de clase, los recursos a su nombre de tipo de recurso, y los valores escalares a su nombre común tal como se utilizaría en las declaraciones de tipo.

Esta función difiere de `gettype` en que devuelve nombres de tipo que son más coherentes con el uso real, en lugar de aquellos presentes por razones históricas.

## Parámetros

`value`  
La variable cuyo tipo debe ser verificado.

## Valores devueltos

Los tipos posibles de retorno `string` son :

| Tipo + Estado | Valor de retorno | Notas |
|----|----|----|
| null | `"null"` | \- |
| Booleans (`true` or `false`) | `"bool"` | \- |
| Números enteros | `"int"` | \- |
| Números de coma flotante | `"float"` | \- |
| String | `"string"` | \- |
| Arrays | `"array"` | \- |
| Recursos | `"resource (resourcename)"` | \- |
| Recursos (Cerrados) | `"resource (closed)"` | Ejemplo: Un flujo de archivo después de ser cerrado con `fclose`. |
| Objetos desde Clases Nombradas | El nombre completo de la clase incluyendo el namespace por ejemplo `Foo\Bar` | \- |
| Objetos desde Clases Anónimas | `"class@anonymous"` o el nombre de la clase padre/el nombre de la interfaz si la clase extiende otra clase o implementa una interfaz, por ejemplo `"Foo\Bar@anonymous"` | Las clases anónimas se crean mediante la sintaxis `\$x = new class { ... }` |

## Ejemplos

Ejemplo de `get_debug_type`

```
<?php

namespace Foo;

echo get_debug_type(null), PHP_EOL;
echo get_debug_type(true), PHP_EOL;
echo get_debug_type(1), PHP_EOL;
echo get_debug_type(0.1), PHP_EOL;
echo get_debug_type("foo"), PHP_EOL;
echo get_debug_type([]), PHP_EOL;

$fp = fopen('/examples/book.xml', 'rb');
echo get_debug_type(\$fp), PHP_EOL;

fclose(\$fp);
echo get_debug_type(\$fp), PHP_EOL;

echo get_debug_type(new stdClass), PHP_EOL;
echo get_debug_type(new class {}), PHP_EOL;

interface A {}
interface B {}
class C {}

echo get_debug_type(new class implements A {}), PHP_EOL;
echo get_debug_type(new class implements A,B {}), PHP_EOL;
echo get_debug_type(new class extends C {}), PHP_EOL;
echo get_debug_type(new class extends C implements A {}), PHP_EOL;

?>

    
```php

Resultado del ejemplo anterior es similar a:

    null
    bool
    int
    float
    string
    array
    resource (stream)
    resource (closed)
    stdClass
    class@anonymous
    Foo\A@anonymous
    Foo\A@anonymous
    Foo\C@anonymous
    Foo\C@anonymous

## Véase también

`gettype`, `get_class`
