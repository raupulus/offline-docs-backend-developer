---
title: strstr
description: Encuentra la primera ocurrencia en un string
source_url: https://www.php.net/manual/es/function.strstr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/strstr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 89460
---

strstr

Encuentra la primera ocurrencia en un string

## Descripción

```php
strstr(string $haystack, string $needle, [bool $before_needle]): string
```php

Devuelve una subcadena de `haystack`, desde la primera ocurrencia de `needle` (incluida) hasta el final del string.

> [!NOTE]
> `strstr` es sensible a mayúsculas y minúsculas. Para una funcionalidad idéntica, pero insensible a mayúsculas y minúsculas, consulte `stristr`.

> [!NOTE]
> Si el objetivo es únicamente determinar si un cierto valor de `needle` se encuentra en `haystack`, la función `str_contains` que es más rápida y menos exigente en memoria debería ser utilizada en su lugar.

## Parámetros

`haystack`  
El string de entrada.

`needle`  
El string a buscar.

Anterior a PHP 8.0.0, si `needle` no es una cadena de caracteres, se convierte en un entero y se aplica como valor ordinal de un carácter. Este comportamiento está obsoleto a partir de PHP 7.3.0, y confiar en él está fuertemente desaconsejado. Dependiendo del comportamiento esperado, `needle` debe ser explícitamente convertido a una cadena de caracteres, o debe realizarse una llamada explícita a `chr`.

`before_needle`  
Si es `true`, `strstr` devuelve la parte de `haystack` antes de la primera ocurrencia de `needle` (`needle` excluido).

## Valores devueltos

Devuelve la porción del string, o `false` si `needle` no es encontrado.

## Historial de cambios

| Versión | Descripción                                                     |
|---------|-----------------------------------------------------------------|
| 8.0.0   | `needle` acepta ahora una cadena vacía.                         |
| 8.0.0   | Pasar un `int` como `needle` ya no es soportado.                |
| 7.3.0   | Pasar un `int` como `before_needle` ha sido declarado obsoleto. |

## Ejemplos

Ejemplo con `strstr`

```
<?php
$email  = 'name@example.com';
$domain = strstr($email, '@');
echo $domain, PHP_EOL; // Muestra: @example.com

$user = strstr($email, '@', true);
echo $user, PHP_EOL; // Muestra: name
?>

    
```php

## Véase también

`stristr`, `strrchr`, `strpos`, `strpbrk`, `preg_match`
