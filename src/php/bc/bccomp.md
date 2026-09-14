---
title: bccomp
description: Comparar dos números de gran tamaño
source_url: https://www.php.net/manual/es/function.bccomp.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bccomp.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6240
---

bccomp

Comparar dos números de gran tamaño

## Descripción

```php
bccomp(string $num1, string $num2, [int $scale]): int
```php

Compara el operando `num1` con `num2` y devuelve el resultado en forma de un `int`.

## 

## Valores devueltos

Devuelve `0` si los dos operandos son iguales, `1` si `num1` es superior a `num2`, o `-1` en caso contrario.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `scale` ahora es nullable. |

## Ejemplos

Ejemplo con `bccomp`

```
<?php

echo bccomp('1', '2') . "\n";   // -1
echo bccomp('1.00001', '1', 3); // 0
echo bccomp('1.00001', '1', 5); // 1

?>

   
```php

## Véase también

BcMath\Number::compare
