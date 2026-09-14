---
title: mb_strtolower
description: Convierte todos los caracteres a minúsculas
source_url: https://www.php.net/manual/es/function.mb-strtolower.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strtolower.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 6c550e6d0
order: 45530
---

mb_strtolower

Convierte todos los caracteres a minúsculas

## Descripción

```php
mb_strtolower(string $string, [string $encoding]): string
```php

Devuelve la cadena `string` después de convertir todos los caracteres alfabéticos a minúsculas.

## Parámetros

`string`  
La cadena a convertir a minúsculas.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve la cadena `string` con todos los caracteres alfabéticos convertidos a minúsculas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Implementación de reglas de conversión condicional a minúsculas para la letra griega sigma. |

## Ejemplos

Ejemplo con `mb_strtolower`

```
<?php
$str = "Marie A Un Petit Agneau Et Elle L'Aime BEAUCOUP.";
$str = mb_strtolower($str);
echo $str; // marie a un petit agneau et elle l'aime beaucoup
?>

    
```php

Ejemplo con `mb_strtolower` con texto UTF-8 no latino

```
<?php
$str = "Τάχιστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός";
$str = mb_strtolower($str, 'UTF-8');
echo $str; // Muestra τάχιστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός
?>

    
```php

## Notas

A diferencia de `strtolower`, el concepto de carácter 'alfabético' se determina mediante las propiedades Unicode. Por lo tanto, el comportamiento de esta función no se modifica por las configuraciones locales, y puede convertir todos los caracteres considerados alfabéticos como la c cédilla (ç).

Para más información sobre las propiedades de Unicode, véase <http://www.unicode.org/reports/tr21/>.

## Véase también

`mb_strtoupper`, `mb_convert_case`, `strtolower`
