---
title: lcfirst
description: Pone el primer carácter en minúscula
source_url: https://www.php.net/manual/es/function.lcfirst.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/lcfirst.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 88840
---

lcfirst

Pone el primer carácter en minúscula

## Descripción

```php
lcfirst(string $string): string
```php

Devuelve una cadena cuyo primer carácter de `string` ha sido puesto en minúscula, si este carácter es un carácter ASCII en el rango que va de `"A"` (0x41) a `"Z"` (0x5a).

## Parámetros

`string`  
La cadena de entrada.

## Valores devueltos

Devuelve la cadena resultante.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | La conversión de la casilla ya no depende de la configuración local definida con `setlocale`. Solo se convertirán los caracteres ASCII. |

## Ejemplos

Ejemplo con `lcfirst`

```
<?php
$foo = 'HelloWorld';
echo lcfirst($foo), PHP_EOL;             // helloWorld

$bar = 'HELLO WORLD!';
echo lcfirst($bar), PHP_EOL;             // hELLO WORLD!
echo lcfirst(strtoupper($bar)), PHP_EOL; // hELLO WORLD!
?>

    
```php

## Véase también

`ucfirst`, `strtolower`, `strtoupper`, `ucwords`
