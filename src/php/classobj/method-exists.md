---
title: method_exists
description: Verifica si el método existe en una clase
source_url: https://www.php.net/manual/es/function.method-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/method-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_reviewed: false
translation_revision: 3d8c79ee5
order: 6900
---

method_exists

Verifica si el método existe en una clase

## Descripción

```php
method_exists(object $object_or_class, string $method): bool
```php

Verifica si el método existe en el objeto `object_or_class` proporcionado.

## Parámetros

`object_or_class`  
Una instancia de un objeto o el nombre de una clase

`method`  
El nombre del método

## Valores devueltos

Devuelve `true` si el método proporcionado por el argumento `method` ha sido definido en el objeto `object_or_class`, `false` en caso contrario.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Las verificaciones de clase contra métodos privados heredados devuelven ahora `false`. |

## Ejemplos

Ejemplo con `method_exists`

```
<?php
$directory = new Directory('.');
var_dump(method_exists($directory,'read'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

Ejemplo con `method_exists` en llamada estática

```
<?php
var_dump(method_exists('Directory','read'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

## Notas

> [!NOTE]
> El uso de esta función utilizará todos los [autoloaders](#language.oop5.autoload) registrados si la clase no es conocida aún.

> [!NOTE]
> La función `method_exists` no puede detectar los métodos que son mágicamente accesibles utilizando el método mágico [`__call`](#language.oop5.overloading.methods).

## Véase también

`function_exists`, `is_callable`, `class_exists`
