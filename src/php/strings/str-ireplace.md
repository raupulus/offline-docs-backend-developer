---
title: str_ireplace
description: Versión insensible a mayúsculas y minúsculas de str_replace
source_url: https://www.php.net/manual/es/function.str-ireplace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/str-ireplace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 464fbf0d1
order: 89150
---

str_ireplace

Versión insensible a mayúsculas y minúsculas de

str_replace

## Descripción

```php
str_ireplace(array $search, array $replace, string $subject, [int $count]): string
```php

`str_ireplace` devuelve una cadena de caracteres o un array en el que todas las ocurrencias de `search` en `subject` (ignorando mayúsculas y minúsculas), han sido reemplazadas por el valor de `replace`.

Para reemplazar un texto según un patrón en lugar de una cadena fija, utilice `preg_replace` con el modificador de patrón `i` [.](#reference.pcre.pattern.modifiers).

## Parámetros

Si los parámetros `search` y `replace` son arrays, entonces la función `str_ireplace` tomará un valor de cada array y los utilizará para la búsqueda y el reemplazo en `subject`. Si el parámetro `replace` tiene menos valores que el parámetro `search`, entonces una `string` vacía será utilizada como valor para el resto de los valores de reemplazo. Si el parámetro `search` es un array y el parámetro `replace` es una `string`, entonces esta `string` de reemplazo será utilizada para cada valor de `search`. Lo contrario no tiene sentido.

Si el parámetro `search` o el parámetro `replace` son arrays, sus elementos son tratados del primero al último.

`search`  
El valor a buscar, conocido también como *needle*. Un array puede ser utilizado para designar múltiples needles.

`replace`  
El valor de reemplazo utilizado para cada valor encontrado en `search`. Un array puede ser utilizado para designar múltiples reemplazos.

`subject`  
Una `string` o un `array` en el que se realiza la búsqueda, también conocido como *haystack*.

Si `subject` es un array, el reemplazo se realiza en cada uno de los elementos del sujeto `subject`, y el valor devuelto es también un array.

`count`  
Si se proporciona, esta variable contendrá el número de reemplazos realizados.

## Valores devueltos

Devuelve una cadena o un array de reemplazo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.2.0 | El case folding ya no depende de la configuración local definida con `setlocale`. Solo se realizará el case folding ASCII. Los octetos no-ASCII serán comparados por su valor de octeto. |

## Ejemplos

Ejemplo con `str_ireplace`

```
<?php
$bodytag = str_ireplace("%body%", "black", "<body text=%BODY%>");
echo $bodytag; // <body text=black>
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

> [!CAUTION]
> Dado que la función `str_ireplace` realiza los reemplazos de izquierda a derecha, puede reemplazar un valor previamente insertado durante un reemplazo múltiple. El ejemplo \#2 de la documentación de la función `str_replace` sobre cómo tratar esta problemática.

## Véase también

`str_replace`, `preg_replace`, `strtr`
