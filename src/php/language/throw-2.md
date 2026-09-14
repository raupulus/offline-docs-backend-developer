---
title: Generator::throw
description: Lanzar una excepción dentro generador
source_url: https://www.php.net/manual/es/generator.throw.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/generator/throw.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 8fee3ae97
order: 3610
---

Generator::throw

Lanzar una excepción dentro generador

## Descripción

```php
public Generator::throw(Throwable $exception): mixed
```php

Lanza una excepción dentro del generador y reanuda su ejecución. El comportamiento será el mismo que si la expresión [`yield`](#control-structures.yield) actual fuera reemplazada con una sentencia `throw $exception`.

Si el generador ya está cerrado al invocar a este método, la excepción será lanzada en su lugar en el contexto del invocador.

## Parámetros

`exception`  
La excepción a lanzar dentro del generador.

## Valores devueltos

Devuelve el valor generado.

## Ejemplos

Lanzar una ecepión dentro de un generador

```
<?php
function gen() {
    echo "Foo\n";
    try {
        yield;
    } catch (Exception $e) {
        echo "Excepción: {$e->getMessage()}\n";
    }
    echo "Bar\n";
}

$gen = gen();
$gen->rewind();
$gen->throw(new Exception('Prueba'));
?>

    
```php

El ejemplo anterior mostrará:

    Foo
    Excepción: Prueba
    Bar
