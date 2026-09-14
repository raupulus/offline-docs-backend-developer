---
title: bcsqrt
description: Obtiene la raiz cuadrada de un número de precisión arbitraria
source_url: https://www.php.net/manual/es/function.bcsqrt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcsqrt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: '329574156'
order: 6340
---

bcsqrt

Obtiene la raiz cuadrada de un número de precisión arbitraria

## Descripción

```php
bcsqrt(string $num, [int $scale]): string
```php

Devuelve la raiz cudrada de `num`.

## Parámetros

`num`  
El operando, como un string numérico con formato válido de BCMath.

## Valores devueltos

Devuelve la raiz cuadrada como un string numérico con formato válido de BCMath.

## Errores/Excepciones

Esta función lanza un `ValueError` en los siguientes casos: `num` no es un string numérico con formato válido de BCMath, `num` es menor que `0`, `scale` está fuera del rango válido

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si `num` no es un string numérico con formato válido de BCMath, o es menor que `0`, se lanza un `ValueError`. Anteriormente, se emitía `E_WARNING` en su lugar. |
| 8.0.0 | `scale` ahora necesita ser entre `0` y `2147483647`; anteriormente, las escalas negativas se trataban silenciosamente como `0`. |
| 8.0.0 | `scale` ahora es nullable. |

## Ejemplos

Ejemplo de `bcsqrt`

```
<?php

echo bcsqrt('2', 3); // 1.414

?>

   
```php

## Véase también

`bcpow`, BcMath\Number::sqrt
