---
title: bcmul
description: Multiplica dos números de precisión arbitraria
source_url: https://www.php.net/manual/es/function.bcmul.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcmul.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6290
---

bcmul

Multiplica dos números de precisión arbitraria

## Descripción

```php
bcmul(string $num1, string $num2, [int $scale]): string
```php

Multiplica `num1` por `num2`.

## 

## Valores devueltos

Devuelve el resultado como un string.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `scale` ahora es nullable. |
| 7.3.0 | `bcmul` ahora devuelve números con la escala solicitada. Anteriormente, los números devueltos podían omitir los ceros decimales finales. |

## Ejemplos

Ejemplo de `bcmul`

```
<?php
echo bcmul('1.34747474747', '35', 3); // 47.161
echo bcmul('2', '4'); // 8
?>

   
```php

## Notas

> [!NOTE]
> Antes de PHP 7.3.0, `bcmul` podría devolver un resultado con menos dígitos después del punto decimal que el parámetro `scale` indicaría. Esto solo ocurre cuando el resultado no requiere toda la precisión permitida por `scale`. Por ejemplo:
>
> <div class="example">
>
> <div class="title">
>
> Ejemplo de scale en `bcmul`
>
> </div>
>
> ```
> <?php
> echo bcmul('5', '2', 2);     // Imprime "10", no "10.00"
> ?>
>
>      
> ```
>
> </div>

## Véase también

`bcdiv`, BcMath\Number::mul
