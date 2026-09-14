---
title: bcdiv
description: Divide dos números de precisión arbitraria
source_url: https://www.php.net/manual/es/function.bcdiv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcdiv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: '329574156'
order: 6250
---

bcdiv

Divide dos números de precisión arbitraria

## Descripción

```php
bcdiv(string $num1, string $num2, [int $scale]): string
```php

Divide el `num1` entre el `num2`.

## Parámetros

`num1`  
El dividendo, como una cadena.

`num2`  
El divisor, como una cadena.

## Valores devueltos

Devuelve el resultado de la división como una cadena.

## 

Esta función lanza una excepción DivisionByZeroError si `num2` es `0`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `scale` ahora es nullable. |
| 8.0.0 | Dividir entre `0` ahora lanza una excepción DivisionByZeroError en vez de devolver `null`. |

## Ejemplos

Ejemplo de `bcdiv`

```
<?php

echo bcdiv('105', '6.55957', 3);  // 16.007

?>

   
```php

## Véase también

`bcdivmod`, `bcmod`, `bcmul`, BcMath\Number::div
