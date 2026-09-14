---
title: ucfirst
description: Pone en mayúscula el primer carácter
source_url: https://www.php.net/manual/es/function.ucfirst.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/ucfirst.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89560
---

ucfirst

Pone en mayúscula el primer carácter

## Descripción

```php
ucfirst(string $string): string
```php

Devuelve una cadena con el primer carácter de `string` en mayúscula, si este carácter es un carácter ASCII en el rango de `"a"` (0x61) a `"z"` (0x7a).

## Parámetros

`string`  
La cadena de entrada.

## Valores devueltos

Devuelve la cadena después de la modificación.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | La conversión de la casilla ya no depende de la configuración local definida con `setlocale`. Solo se convertirán los caracteres ASCII. |

## Ejemplos

Ejemplo con `ucfirst`

```
<?php
$foo = 'bonjour tout le monde!';
echo ucfirst($foo), PHP_EOL;             // Bonjour tout le monde!

$bar = 'BONJOUR TOUT LE MONDE!';
$bar = ucfirst($bar), PHP_EOL;             // BONJOUR TOUT LE MONDE!
$bar = ucfirst(strtolower($bar)), PHP_EOL; // Bonjour tout le monde!
?>

    
```php

## Véase también

`lcfirst`, `strtolower`, `strtoupper`, `ucwords`, `mb_convert_case`
