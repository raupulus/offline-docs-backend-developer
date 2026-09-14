---
title: Random\Randomizer::__construct
description: Construye un nuevo Randomizer
source_url: https://www.php.net/manual/es/random-randomizer.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/random/random/randomizer/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: random
translation_status: ready
translation_reviewed: false
translation_revision: 1bcc40f81
order: 68140
---

Random\Randomizer::\_\_construct

Construye un nuevo Randomizer

## Descripción

```php
public Random\Randomizer::__construct([Random\Engine $engine])
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`engine`  
El `Random\Engine` a usar para generar aleatoriedad.

Si `engine` se omite o es `null`, se usará un nuevo objeto `Random\Engine\Secure`.

## Ejemplos

`Random\Randomizer::__construct` ejemplo

```
<?php
$r = new \Random\Randomizer();
$r = new \Random\Randomizer(new \Random\Engine\Mt19937());
?>

   
```php
