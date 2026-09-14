---
title: ReflectionGenerator::getTrace
description: Obtiene la traza del generador en ejecución
source_url: https://www.php.net/manual/es/reflectiongenerator.gettrace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/gettrace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: ec2fe9a59
order: 70870
---

ReflectionGenerator::getTrace

Obtiene la traza del generador en ejecución

## Descripción

```php
public ReflectionGenerator::getTrace([int $options]): array
```php

Obtiene la traza del generador actualmente en ejecución.

## Parámetros

`options`  
El valor de `options` puede ser cualquiera de los flags siguientes.

| Opción | Descripción |
|----|----|
| `DEBUG_BACKTRACE_PROVIDE_OBJECT` | Por omisión. |
| `DEBUG_BACKTRACE_IGNORE_ARGS` | No incluye las informaciones de los argumentos para las funciones en la traza de llamadas. |

Opciones disponibles

## Valores devueltos

Devuelve la traza del generador actualmente en ejecución.

## Ejemplos

Ejemplo con ReflectionGenerator::getTrace

```
<?php
function foo() {
    yield 1;
}

function bar()
{
    yield from foo();
}

function baz()
{
    yield from bar();
}

$gen = baz();
$gen->valid(); // start the generator

var_dump((new ReflectionGenerator($gen))->getTrace());

    
```php

Resultado del ejemplo anterior es similar a:

    array(2) {
      [0]=>
      array(4) {
        ["file"]=>
        string(18) "example.php"
        ["line"]=>
        int(8)
        ["function"]=>
        string(3) "foo"
        ["args"]=>
        array(0) {
        }
      }
      [1]=>
      array(4) {
        ["file"]=>
        string(18) "example.php"
        ["line"]=>
        int(12)
        ["function"]=>
        string(3) "bar"
        ["args"]=>
        array(0) {
        }
      }
    }

## Véase también

ReflectionGenerator::getFunction, ReflectionGenerator::getThis
