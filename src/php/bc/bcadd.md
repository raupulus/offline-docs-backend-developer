---
title: bcadd
description: Suma dos números de precisión arbitrária
source_url: https://www.php.net/manual/es/function.bcadd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/functions/bcadd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: '329574156'
order: 6220
---

bcadd

Suma dos números de precisión arbitrária

## Descripción

```php
bcadd(string $num1, string $num2, [int $scale]): string
```php

Suma `num1` y `num2`.

## Parámetros

`num1`  
El operador izquierdo, como una cadena.

`num2`  
El operador derecho, como una cadena

`scale`  
Este parámetro se utiliza para establecer el número de dígitos después del punto decimal en el resultado. Si es `null`, se establecerá por defecto en la escala predeterminada establecida con `bcscale`, o se utilizará el valor de la directiva INI [`bcmath.scale`](#ini.bcmath.scale).

## Valores devueltos

La suma de dos operandos, como una cadena.

## Errores/Excepciones

Esta función lanza una excepción ValueError en los siguientes casos: `num1` o `num2` no es una cadena numérica bien formada de BCMath., `scale` está fuera del rango válido.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `scale` ahora es nullable. |

## Ejemplos

Ejemplo `bcadd`

```
<?php

$a = '1.234';
$b = '5';

echo bcadd($a, $b);     // 6
echo bcadd($a, $b, 4);  // 6.2340

?>

   
```php

## Véase también

`bcsub`, BcMath\Number::add
