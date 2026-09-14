---
title: bcsub
description: Resta un número de precisión arbitraria de otro
source_url: https://www.php.net/manual/es/function.bcsub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcsub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6350
---

bcsub

Resta un número de precisión arbitraria de otro

## Descripción

```php
bcsub(string $num1, string $num2, [int $scale]): string
```php

Resta `num2` de `num1`.

## 

## Valores devueltos

El resultado de la resta, como un string.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `scale` ahora es nullable. |

## Ejemplos

Ejemplo de `bcsub`

```
<?php

$a = '1.234';
$b = '5';

echo bcsub($a, $b);     // -3
echo bcsub($a, $b, 4);  // -3.7660

?>

   
```php

## Véase también

`bcadd`, BcMath\Number::sub
