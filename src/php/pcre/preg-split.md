---
title: preg_split
description: Divide una cadena mediante expresión regular
source_url: https://www.php.net/manual/es/function.preg-split.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-split.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_revision: bb66ce4d4
order: 61670
---

preg_split

Divide una cadena mediante expresión regular

## Descripción

```php
preg_split(string $pattern, string $subject, [int $limit], [int $flags]): array
```php

Divide una cadena mediante expresión regular.

## Parámetros

`pattern`  
El patrón a buscar, en forma de cadena.

`subject`  
La cadena de entrada.

`limit`  
Si se especifica, entonces solo se devuelven las primeras sub-cadenas hasta `limit` con el resto de la cadena colocado en la última sub-cadena. Un `limit` de -1 o 0 significa "sin límite".

`flags`  
`flags` puede ser la combinación de las siguientes opciones (combinadas con el operador `|`):

`PREG_SPLIT_NO_EMPTY`  
Si esta opción está activada, solo se devuelven las sub-caenas no vacías por `preg_split`.

`PREG_SPLIT_DELIM_CAPTURE`  
Si esta opción está activada, las expresiones entre paréntesis entre los delimitadores de patrones también serán capturadas y devueltas.

`PREG_SPLIT_OFFSET_CAPTURE`  
Si esta opción está activada, para cada resultado, su posición será devuelta. Tenga en cuenta que esto cambia el valor devuelto a un array donde cada elemento es un array compuesto por la cadena encontrada en la posición `0` y la posición de la cadena en `subject` en la posición `1`.

## Valores devueltos

Devuelve un array que contiene las sub-caenas de `subject`, separadas por las cadenas que coinciden con `pattern`, o `false` si ocurre un error.

## Errores/Excepciones

Si el patrón regex pasado no se compila a una regex válida, se emite una `E_WARNING`.

## Ejemplos

Ejemplo con `preg_split`: División de una cadena de búsqueda

```
<?php
// divide la frase mediante comas y espacios
// lo que incluye los " ", \r, \t, \n y \f
$keywords = preg_split("/[\s,]+/", "lenguaje de marcado, programación");
print_r($keywords);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => lenguaje
        [1] => de
        [2] => marcado
        [3] => programación
    )

Dividir una cadena en caracteres

```
<?php
$str = 'string';
$chars = preg_split('//', $str, -1, PREG_SPLIT_NO_EMPTY);
print_r($chars);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => s
        [1] => t
        [2] => r
        [3] => i
        [4] => n
        [5] => g
    )

Dividir una cadena y capturar las posiciones

```
<?php
$str = 'lenguaje de marcado, programación';
$chars = preg_split('/ /', $str, -1, PREG_SPLIT_OFFSET_CAPTURE);
print_r($chars);
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [0] => lenguaje
                [1] => 0
            )

        [1] => Array
            (
                [0] => de
                [1] => 8
            )

        [2] => Array
            (
                [0] => marcado,
                [1] => 12
            )

        [3] => Array
            (
                [0] => programación
                [1] => 22
            )

    )

## Notas

> [!TIP]
> Si no se necesita el poder de las expresiones regulares, pueden elegirse alternativas más rápidas (aunque más simples) como `explode` o `str_split`.

> [!TIP]
> Si la búsqueda de una coincidencia falla, se devuelve un array que contiene un solo elemento que contiene la cadena de entrada.

## Véase también

[Patrones PCRE](#pcre.pattern), `preg_quote`, `explode`, `preg_match`, `preg_match_all`, `preg_replace`, `preg_last_error`
