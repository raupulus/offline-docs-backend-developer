---
title: ucwords
description: Pone en mayúscula la primera letra de todas las palabras
source_url: https://www.php.net/manual/es/function.ucwords.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/ucwords.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: false
translation_revision: 45042fef6
order: 89570
---

ucwords

Pone en mayúscula la primera letra de todas las palabras

## Descripción

```php
ucwords(string $string, [string $separators]): string
```php

Devuelve la cadena `string` después de poner en mayúscula la primera letra de todas las palabras, si este carácter es un carácter ASCII entre `"a"` (0x61) y `"z"` (0x7a).

En el contexto de esta función, una palabra es cualquier secuencia de caracteres que no están listados en el parámetro `separators`. Por omisión, estos son: un espacio, un salto de línea, una nueva línea, un retorno de carro, un salto de página, una tabulación horizontal y una tabulación vertical.

Para realizar una conversión similar en cadenas multiocteto, utilice `mb_convert_case` con el modo `MB_CASE_TITLE`.

## Parámetros

`string`  
La cadena de entrada.

`separators`  
El parámetro opcional `separators` contiene el carácter de separación.

## Valores devueltos

Devuelve la cadena, después de la modificación.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | La conversión de la casilla ya no depende de la configuración local definida con `setlocale`. Solo se convertirán los caracteres ASCII. |

## Ejemplos

Ejemplo con `ucwords`

```
<?php
$foo = 'bonjour tout le monde!';
echo ucwords($foo), PHP_EOL;             // Bonjour Tout Le Monde!

$bar = 'BONJOUR TOUT LE MONDE!';
echo ucwords($bar), PHP_EOL;             // BONJOUR TOUT LE MONDE!
echo ucwords(strtolower($bar)), PHP_EOL; // Bonjour Tout Le Monde!
?>

    
```php

Ejemplo con `ucwords` y un separador personalizado

```
<?php
$foo = 'hello|world!';
echo ucwords($foo), PHP_EOL;             // Hello|world!

echo ucwords($foo, "|"), PHP_EOL;        // Hello|World!
?>

    
```php

Ejemplo de `ucwords` con separadores adicionales

```
     
<?php
$foo = "mike o'hara";
echo ucwords($foo), PHP_EOL;                 // Mike O'hara

echo ucwords($foo, " \t\r\n\f\v'"), PHP_EOL; // Mike O'Hara
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`strtoupper`, `strtolower`, `ucfirst`, `mb_convert_case`
