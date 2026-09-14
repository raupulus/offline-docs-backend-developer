---
title: mb_convert_case
description: Realiza una conversión a mayúsculas/minúsculas de un string
source_url: https://www.php.net/manual/es/function.mb-convert-case.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-convert-case.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: d6f54016d
order: 44980
---

mb_convert_case

Realiza una conversión a mayúsculas/minúsculas de un string

## Descripción

```php
mb_convert_case(string $string, int $mode, [string $encoding]): string
```php

Realiza una conversión a mayúsculas/minúsculas de un `string`, de acuerdo al valor especificado en `mode`.

## Parámetros

`string`  
El `string` que se va a convertir.

`mode`  
El modo de conversión. Puede ser uno de `MB_CASE_UPPER`, `MB_CASE_LOWER`, `MB_CASE_TITLE`, `MB_CASE_FOLD`, `MB_CASE_UPPER_SIMPLE`, `MB_CASE_LOWER_SIMPLE`, `MB_CASE_TITLE_SIMPLE`, `MB_CASE_FOLD_SIMPLE`.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

La versión convertida del `string` en función del valor especificado en `mode`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Se implementaron reglas de mayúsculas y minúsculas condicionales para la letra griega sigma que solo se aplican a los modos `MB_CASE_LOWER` y `MB_CASE_TITLE`, no a `MB_CASE_LOWER_SIMPLE` y `MB_CASE_TITLE_SIMPLE`. |
| 7.3.0 | Añadido soporte para `MB_CASE_FOLD`, `MB_CASE_UPPER_SIMPLE`, `MB_CASE_LOWER_SIMPLE`, `MB_CASE_TITLE_SIMPLE`, y `MB_CASE_FOLD_SIMPLE` como `mode`. |

## Ejemplos

Ejemplo de `mb_convert_case`

```
<?php
$str = "mary had a Little lamb and she loved it so";
$str = mb_convert_case($str, MB_CASE_UPPER, "UTF-8");
echo $str, PHP_EOL;
$str = mb_convert_case($str, MB_CASE_TITLE, "UTF-8");
echo $str, PHP_EOL;
?>

    
```php

Ejemplo de `mb_convert_case` con alfabeto no latino en UTF-8

```
<?php
$str = "Τάχιστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός";
$str = mb_convert_case($str, MB_CASE_UPPER, "UTF-8");
echo $str, PHP_EOL;
$str = mb_convert_case($str, MB_CASE_TITLE, "UTF-8");
echo $str, PHP_EOL;
?>

    
```php

## Notas

A diferencia de las funciones estándar de mayúsculas/minúsculas, como `strtolower` y `strtoupper`, la conversión se lleva a cabo según los fundamentos de las propiedades de los caracteres Unicode. Por lo tanto, el comportamiento de esta función no se ve afectado por la configuración regional y puede convertir cualquier carácter que tenga propiedad 'alfabética', como la a con diéresis (ä).

Para más información sobre las propiedades Unicode, por favor, revise <http://www.unicode.org/reports/tr21/>.

## Véase también

`mb_strtolower`, `mb_strtoupper`, `strtolower`, `strtoupper`, `ucfirst`, `ucwords`
