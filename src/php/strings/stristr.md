---
title: stristr
description: Versión insensible a mayúsculas y minúsculas de strstr
source_url: https://www.php.net/manual/es/function.stristr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/stristr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89330
---

stristr

Versión insensible a mayúsculas y minúsculas de

strstr

## Descripción

```php
stristr(string $haystack, string $needle, [bool $before_needle]): string
```php

Devuelve una subcadena de `haystack`, desde la primera ocurrencia de `needle` (incluida) hasta el final de la cadena.

## Parámetros

`haystack`  
La cadena en la que se debe buscar.

`needle`  
La cadena a buscar.

Anterior a PHP 8.0.0, si `needle` no es una cadena de caracteres, se convierte en un entero y se aplica como valor ordinal de un carácter. Este comportamiento está obsoleto a partir de PHP 7.3.0, y confiar en él está fuertemente desaconsejado. Dependiendo del comportamiento esperado, `needle` debe ser explícitamente convertido a una cadena de caracteres, o debe realizarse una llamada explícita a `chr`.

`before_needle`  
Si es `true`, `stristr` devuelve la parte de `haystack` antes de la primera ocurrencia de `needle` (`needle` excluida).

`needle` y `haystack` se tratan sin tener en cuenta mayúsculas y minúsculas.

## Valores devueltos

Devuelve la parte correspondiente de la cadena. Si `needle` no se encuentra, la función devuelve `false`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El case folding ya no depende de la configuración local definida con `setlocale`. Solo se realizará el case folding ASCII. Los octetos no-ASCII serán comparados por su valor de octeto. |
| 8.0.0 | `needle` acepta ahora una cadena vacía. |
| 8.0.0 | Pasar un `int` como `needle` ya no está soportado. |
| 7.3.0 | Pasar un `int` como `before_needle` se ha marcado como obsoleto. |

## Ejemplos

Ejemplo con `stristr`

```
<?php
  $email = 'USER@EXAMPLE.com';
  echo stristr($email, 'e'), PHP_EOL; // muestra ER@EXAMPLE.com
  echo stristr($email, 'e', true), PHP_EOL; // muestra US
?>

    
```php

Comprueba si una cadena es encontrada o no

```
<?php
  $string = 'Hello World!';
  if (stristr($string, 'earth') === FALSE) {
   echo '"terre" no encontrado en la cadena';
  }
// muestra: "terre" no encontrado en la cadena
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`strstr`, `strrchr`, `stripos`, `strpbrk`, `preg_match`
