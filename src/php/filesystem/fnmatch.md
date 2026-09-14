---
title: fnmatch
description: Prueba un nombre de fichero mediante un patrón de búsqueda
source_url: https://www.php.net/manual/es/function.fnmatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fnmatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: 39a98b1f1
order: 23600
---

fnmatch

Prueba un nombre de fichero mediante un patrón de búsqueda

## Descripción

```php
fnmatch(string $pattern, string $filename, [int $flags]): bool
```php

`fnmatch` verifica si la cadena `filename` cumple con el patrón de shell `pattern`.

## Parámetros

`pattern`  
El `pattern` a comparar. Habitualmente, el `pattern` contendrá caracteres genéricos como `'?'` y `'*'`.

| Carácter genérico | Descripción |
|----|----|
| `?` | El signo de interrogación coincidirá con cualquier carácter único. Por ejemplo, el patrón `"file?.txt"` coincidirá con `"file1.txt"` y `"fileA.txt"`, pero no coincidirá con `"file10.txt"`. |
| `*` | El asterisco coincidirá con cero o más caracteres. Por ejemplo, el patrón `"foo*.xml"` coincidirá con `"foo.xml"` y `"foobar.xml"`. |
| `[ ]` | Los corchetes se utilizan para crear rangos de puntos de código ASCII o conjuntos de caracteres. Por ejemplo, el patrón `"index.php[45]"` coincidirá con `"index.php4"` y `"index.php5"`, pero no coincidirá con `"index.phpt"`. Rangos conocidos son `[0-9]`, `[a-z]` y `[A-Z]`. Varios conjuntos y rangos pueden utilizarse simultáneamente, por ejemplo `[0-9a-zABC]`. |
| `!` | El signo de exclamación se utiliza para negar caracteres dentro de los corchetes. Por ejemplo, `"[!A-Z]*.html"` coincidirá con `"demo.html"`, pero no coincidirá con `"Demo.html"`. |
| `\` | La barra invertida se utiliza para escapar caracteres especiales. Por ejemplo, `"Name\?"` coincidirá con `"Name?"`, pero no coincidirá con `"Names"`. |

Caracteres genéricos a utilizar en el parámetro `pattern`

`filename`  
La cadena a probar. Esta función es particularmente útil para los nombres de fichero, pero también puede utilizarse con cadenas regulares.

El usuario medio de Shell puede estar familiarizado con los patrones de Shell, o al menos, sus expresiones más simples, como `'?'` y `'*'`. De esta manera, utilizar `fnmatch` en lugar de `preg_match` para búsquedas puede ser más práctico para los no iniciados.

`flags`  
El valor de `flags` puede ser una combinación de los siguientes flags, unidos con el [operador binario OR (\|)](#language.operators.bitwise).

| `Flag` | Descripción |
|----|----|
| `FNM_NOESCAPE` | Desactiva el escape de las barras invertidas. |
| `FNM_PATHNAME` | Una barra diagonal en una cadena coincide únicamente con una barra diagonal en el patrón proporcionado. |
| `FNM_PERIOD` | Un punto al inicio de la cadena debe coincidir exactamente con un punto en el patrón proporcionado. |
| `FNM_CASEFOLD` | Las coincidencias no distinguen mayúsculas y minúsculas. Forma parte de la extensión GNU. |

Lista de flags posibles para `fnmatch`

## Valores devueltos

Devuelve `true` si hay resultados, `false` en caso contrario.

## Ejemplos

Verificar el nombre de un color con un patrón de Shell

```
<?php
if (fnmatch("*gr[ae]y", $color)) {
  echo "formas de gris ...";
}
?>

    
```php

## Notas

> [!WARNING]
> Actualmente, esta función no está disponible para sistemas no-POSIX, a excepción de Windows.

## Véase también

`glob`, `preg_match`, `sscanf`, `printf`, `sprintf`
