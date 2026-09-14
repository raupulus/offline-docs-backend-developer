---
title: abs
description: Valor absoluto
source_url: https://www.php.net/manual/es/function.abs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/abs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 19e812213
order: 44470
---

abs

Valor absoluto

## Descripción

```php
abs(int $num): int
```php

Devuelve el valor absoluto del número `num`.

## Parámetros

`num`  
El valor numérico a tratar

## Valores devueltos

El valor absoluto del número `num`. Si el número es un `float`, entonces el tipo de retorno es también `float`, de lo contrario es `int` (ya que `float` generalmente tiene un intervalo de valores más amplio que `int`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `num` ya no acepta objetos internos que soportan conversiones numéricas. |

## Ejemplos

Ejemplo con `abs`

```
<?php
var_dump(abs(-4.2));
var_dump(abs(5));
var_dump(abs(-5));
?>

    
```php

El ejemplo anterior mostrará:

    float(4.2)
    int(5)
    int(5)

## Véase también

`gmp_abs`, `gmp_sign`
