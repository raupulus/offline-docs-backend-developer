---
title: bcdivmod
description: Devuelve el cociente y el resto de un número de precisión arbitraria
source_url: https://www.php.net/manual/es/function.bcdivmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcdivmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: 5783476ce
order: 6260
---

bcdivmod

Devuelve el cociente y el resto de un número de precisión arbitraria

## Descripción

```php
bcdivmod(string $num1, string $num2, [int $scale]): array
```php

Devuelve el cociente y el resto de la división de `num1` por `num2`.

## 

## Valores devueltos

Devuelve un `array` indexado donde el primer elemento es el cociente en forma de `string` y el segundo elemento es el resto en forma de `string`.

## Ejemplos

Ejemplo de `bcdivmod`

```
<?php
bcscale(0);

[$quot, $rem] = bcdivmod('5',  '3');
echo $quot; // 1
echo $rem;  // 2

[$quot, $rem] = bcdivmod('5',  '-3');
echo $quot; // -1
echo $rem;  // 2

[$quot, $rem] = bcdivmod('-5',  '3');
echo $quot; // -1
echo $rem;  // -2

[$quot, $rem] = bcdivmod('-5',  '-3');
echo $quot; // 1
echo $rem;  // -2
?>

   
```php

`bcdivmod` con decimales

```
<?php
[$quot, $rem] = bcdivmod('5.7', '1.3', 1);
echo $quot; // 4
echo $rem;  // 0.5
?>

   
```php

## Véase también

bcdiv

bcmod

BcMath\Number::divmod
