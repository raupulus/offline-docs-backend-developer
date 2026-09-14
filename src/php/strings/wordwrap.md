---
title: wordwrap
description: Realiza el ajuste de línea de un string
source_url: https://www.php.net/manual/es/function.wordwrap.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/wordwrap.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: a6ee935b0
order: 89630
---

wordwrap

Realiza el ajuste de línea de un string

## Descripción

```php
wordwrap(string $string, [int $width], [string $break], [bool $cut_long_words]): string
```php

Realiza el ajuste de línea de un string. Los strings se cortan después de un carácter de espacio (U+0020) a menos que `cut_long_words` esté definido como `true`.

## Parámetros

`string`  
El string de entrada.

`width`  
El número de caracteres a partir del cual el string será cortado.

`break`  
La línea se rompe utilizando `break`, este parámetro opcional. No debe ser un string vacío.

`cut_long_words`  
Si el parámetro `cut_long_words` vale `true`, el ajuste de línea del string se realizará siempre al tamaño `width` o antes. Si se tiene una palabra que es más larga que el tamaño de ajuste, será cortada en trozos: ver el segundo ejemplo. Cuando vale `false`, la función no cortará la palabra, incluso si el parámetro `width` es más pequeño que el tamaño de la palabra.

## Valores devueltos

Devuelve el string proporcionado cortado a la longitud especificada.

## Errores/Excepciones

Si `break` es un string vacío, se lanza una `ValueError`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Si `break` es un string vacío, se lanza una `ValueError`; anteriormente, en este caso, se emitía un `E_WARNING` y se devolvía `false`. |

## Ejemplos

Ejemplo con `wordwrap`

```
<?php
$text = "Portez ce vieux whisky au juge blond qui fume.";
$newtext = wordwrap($text, 20, "<br />\n");

echo $newtext;
?>

    
```php

El ejemplo anterior mostrará:

    Portez ce vieux<br />
    whisky au juge<br />
    blond qui fume.

Ejemplo con `wordwrap`

```
<?php
$text = "Un mot très très loooooooooooooooooong.";
$newtext = wordwrap($text, 8, "\n", true);

echo "$newtext\n";
?>

    
```php

El ejemplo anterior mostrará:

    Un mot
    très
    très
    looooooo
    oooooooo
    ooong.

Ejemplo con `wordwrap`

```
<?php
$text = "A very long woooooooooooooooooord. and something";
$newtext = wordwrap($text, 8, "\n", false);

echo "$newtext\n";
?>

    
```php

El ejemplo anterior mostrará:

    A very
    long
    woooooooooooooooooord.
    and
    something

## Véase también

`nl2br`, `chunk_split`
