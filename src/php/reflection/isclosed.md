---
title: ReflectionGenerator::isClosed
description: Verifica si la ejecución ha finalizado
source_url: https://www.php.net/manual/es/reflectiongenerator.isclosed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectiongenerator/isclosed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: true
translation_revision: 84883b603
order: 70880
---

ReflectionGenerator::isClosed

Verifica si la ejecución ha finalizado

## Descripción

```php
public ReflectionGenerator::isClosed(): bool
```php

Indica si la ejecución ha alcanzado el final de la función, una instrucción de retorno o si se ha lanzado una excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Indica si el generador ha terminado su ejecución.

## Ejemplos

Ejemplo de ReflectionGenerator::isClosed

```
<?php

function gen()
{
    yield 'a';
    yield 'a';
}

$gen = gen();
$reflectionGen = new ReflectionGenerator($gen);

foreach ($gen as $value) {
    echo $value, PHP_EOL;
    var_dump($reflectionGen->isClosed());
}

var_dump($reflectionGen->isClosed());

?>

   
```php

El ejemplo anterior mostrará:

    a
    bool(false)
    a
    bool(false)
    bool(true)
