---
title: Generator::getReturn
description: Obtener el valor devuelto de un generador
source_url: https://www.php.net/manual/es/generator.getreturn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/generator/getreturn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 8fee3ae97
order: 3560
---

Generator::getReturn

Obtener el valor devuelto de un generador

## Descripción

```php
public Generator::getReturn(): mixed
```php

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el valor devuelto del generador una vez ha finalizado su ejecución.

## Ejemplos

Ejemplo de Generator::getReturn

```
<?php

$gen = (function() {
    yield 1;
    yield 2;

    return 3;
})();

foreach ($gen as $val) {
    echo $val, PHP_EOL;
}

echo $gen->getReturn(), PHP_EOL;

    
```php

El ejemplo anterior mostrará:

    1
    2
    3
