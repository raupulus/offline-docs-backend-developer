---
title: sin
description: Seno
source_url: https://www.php.net/manual/es/function.sin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/sin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 761d72245
order: 44860
---

sin

Seno

## Descripción

```php
sin(float $num): float
```php

`sin` devuelve el seno de `num` (`num` en radianes).

## Parámetros

`num`  
Un valor, en radianes

## Valores devueltos

El seno de `num`.

## Ejemplos

Ejemplo con `sin`

```
<?php
// La precisión depende de la directiva precision
echo sin(deg2rad(60)), PHP_EOL;  //  0.866025403 ...
echo sin(60), PHP_EOL;           // -0.304810621 ...
?>

    
```php

## Véase también

`asin`, `sinh`, `cos`, `tan`, `deg2rad`
