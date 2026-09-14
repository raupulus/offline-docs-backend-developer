---
title: Generator::key
description: Obtener la clave generada
source_url: https://www.php.net/manual/es/generator.key.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/generator/key.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 8fee3ae97
order: 3570
---

Generator::key

Obtener la clave generada

## Descripción

```php
public Generator::key(): mixed
```php

Obtiene la clave del valor generado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la clave generada.

## Ejemplos

Ejemplo de Generator::key

```
<?php

function Gen()
{
    yield 'key' => 'value';
}

$gen = Gen();

echo "{$gen->key()} => {$gen->current()}";

    
```php

El ejemplo anterior mostrará:

    key => value
