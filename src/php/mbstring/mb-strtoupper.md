---
title: mb_strtoupper
description: Convierte todos los caracteres a mayúsculas
source_url: https://www.php.net/manual/es/function.mb-strtoupper.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strtoupper.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: b4afab59d
order: 45540
---

mb_strtoupper

Convierte todos los caracteres a mayúsculas

## Descripción

```php
mb_strtoupper(string $string, [string $encoding]): string
```php

Devuelve el string `string` después de convertir todos los caracteres alfabéticos a mayúsculas.

## Parámetros

`string`  
El string a convertir a mayúsculas.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

Devuelve el string `string` con todos los caracteres convertidos a mayúsculas.

## Ejemplos

Ejemplo con `mb_strtoupper`

```
<?php
$str = "Marie A Un Petit Agneau Et Elle L'Aime BEAUCOUP.";
$str = mb_strtoupper($str);
echo $str; // MARIE A UN PETIT AGNEAU ET ELLE L'AIME BEAUCOUP.
?>

    
```php

Ejemplo con `mb_strtoupper` y texto UTF-8 no latino

```
<?php
$str = "Τάχιστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός";
$str = mb_strtoupper($str, 'UTF-8');
echo $str; // Muestra ΤΆΧΙΣΤΗ ΑΛΏΠΗΞ ΒΑΦΉΣ ΨΗΜΈΝΗ ΓΗ, ΔΡΑΣΚΕΛΊΖΕΙ ΥΠΈΡ ΝΩΘΡΟΎ ΚΥΝΌΣ
?>

    
```php

## Notas

A diferencia de `strtoupper`, el concepto de carácter 'alfabético' se determina por las propiedades Unicode. Por lo tanto, el comportamiento de esta función no se modifica por las configuraciones locales, y puede convertir todos los caracteres considerados alfabéticos como la c cedilla (ç).

Para más información sobre las propiedades de Unicode, véase <http://www.unicode.org/reports/tr21/>.

## Véase también

`mb_strtolower`, `mb_convert_case`, `strtoupper`
