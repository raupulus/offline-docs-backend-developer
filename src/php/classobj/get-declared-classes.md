---
title: get_declared_classes
description: Lista todas las clases definidas en PHP
source_url: https://www.php.net/manual/es/function.get-declared-classes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/classobj/functions/get-declared-classes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: classobj
translation_status: ready
translation_revision: 6846ebb4e
order: 6810
---

get_declared_classes

Lista todas las clases definidas en PHP

## Descripción

```php
get_declared_classes(): array
```php

Lista todas las clases definidas.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene la lista de nombres de las clases declaradas en el script actual.

> [!NOTE]
> Se debe tener en cuenta que, dependiendo de las extensiones que estén compiladas o cargadas en PHP, pueden estar presentes otras clases. Esto significa que no se podrán utilizar estos nombres de clases para definir sus propias clases. A continuación se muestra una lista de las [clases predefinidas](#reserved.classes).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | Anteriormente `get_declared_classes` siempre retornaba las clases padres antes que las clases hijas. Esto ya no es así. No se garantiza ningún orden particular para el valor de retorno de `get_declared_classes`. |

## Ejemplos

Ejemplo con `get_declared_classes`

```
<?php
print_r(get_declared_classes());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => stdClass
        [1] => __PHP_Incomplete_Class
        [2] => Directory
    )

## Véase también

`class_exists`, `get_declared_interfaces`, `get_defined_functions`
