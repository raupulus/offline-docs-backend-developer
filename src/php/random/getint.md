---
title: Random\Randomizer::getInt
description: Obtener un entero seleccionado uniformemente
source_url: https://www.php.net/manual/es/random-randomizer.getint.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/getint.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 1bcc40f81
order: 68180
---

Random\Randomizer::getInt

Obtener un entero seleccionado uniformemente

## Descripción

```php
public Random\Randomizer::getInt(int $min, int $max): int
```php

## Parámetros

`min`  
El valor más bajo que se devolverá.

`max`  
El valor más alto que se devolverá.

## Valores devueltos

Un entero seleccionado uniformemente del intervalo cerrado \[`min`, `max`\]. Tanto `min` como `max` son valores de retorno posibles.

## Errores/Excepciones

- Si `max` es menor que `min`, se lanzará un `ValueError`.

- Cualquier `Throwable` lanzado por el método Random\Engine::generate del [`Random\Randomizer::$engine`](#random-randomizer.props.engine) subyacente.

## Ejemplos

`Random\Randomizer::getInt` ejemplo

```
<?php
$r = new \Random\Randomizer();

// Entero aleatorio en el rango:
echo $r->getInt(1, 100), "\n";
?>

   
```php

Resultado del ejemplo anterior es similar a:

    42

## Véase también

random_int

Random\Randomizer::getFloat
