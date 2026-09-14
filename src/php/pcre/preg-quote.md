---
title: preg_quote
description: Protección de caracteres especiales de expresiones regulares
source_url: https://www.php.net/manual/es/function.preg-quote.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pcre/functions/preg-quote.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pcre
translation_status: ready
translation_reviewed: true
translation_revision: 22e850b66
order: 61630
---

preg_quote

Protección de caracteres especiales de expresiones regulares

## Descripción

```php
preg_quote(string $str, [string $delimiter]): string
```php

`preg_quote` añade una barra invertida antes de cada carácter de la cadena `str` que forma parte de la sintaxis de expresiones regulares. Esto es muy útil si se tiene una cadena que va a servir como máscara, pero que es generada durante la ejecución.

Los caracteres especiales que serán protegidos son los siguientes: `. \ + * ? [ ^ ] $ ( ) { } = ! < > | : - #`

Tenga en cuenta que `/` no es un carácter especial de expresión regular.

> [!NOTE]
> Tenga en cuenta que `preg_quote` no está destinado a ser aplicado a las cadenas \$replacement de `preg_replace` etc.

## Parámetros

`str`  
La cadena de entrada.

`delimiter`  
Si el argumento opcional `delimiter` es proporcionado, también será escapado. Esto es práctico para escapar el delimitador requerido por las funciones PCRE. La barra `/` es el delimitador más común.

## Valores devueltos

Retorna la cadena protegida.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 7.3.0   | El carácter `#` ahora es protegido |
| 7.2.0   | `delimiter` ahora es nullable.     |

## Ejemplos

Ejemplo con `preg_quote`

```
<?php
$keywords = '$40 para un g3/400';
$keywords = preg_quote($keywords, '/');
echo $keywords; // retorna \$40 para un g3\/400
?>

    
```php

Poner en cursiva una palabra en un texto

```
<?php
// En este ejemplo, preg_quote($word) sirve para evitar que los asteriscos
// tengan un valor especial en la expresión regular.

$textbody = "Este libro es *muy* difícil de encontrar.";
$word = "*muy*";
$textbody = preg_replace ("/" . preg_quote($word, '/') . "/",
                          "<i>" . $word . "</i>",
                          $textbody);
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

[Máscaras PCRE](#pcre.pattern), `escapeshellcmd`
