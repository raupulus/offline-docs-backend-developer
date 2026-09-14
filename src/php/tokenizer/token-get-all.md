---
title: token_get_all
description: Divide la fuente dada en tokens PHP
source_url: https://www.php.net/manual/es/function.token-get-all.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/functions/token-get-all.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 82c84a325
order: 94350
---

token_get_all

Divide la fuente dada en tokens PHP

## Descripción

```php
token_get_all(string $code, [int $flags]): array
```php

`token_get_all` parsea el string de la `source` dada en tokens PHP usando el escaneador de léxico de Zend Engine.

Para ver la lista de los tokens analizados, vea [???](#tokens), o use `token_name` para traducir un valor token en su representación en string.

## Parámetros

`source`  
La fuente PHP a analizar.

`flags`  
Banderas válidas:

- `TOKEN_PARSE` - Reconoce la capacidad de usar palabras reservadas en contextos específicos.

## Valores devueltos

Un array de tokens identificadores. Cada token identificador individual es al mismo tiempo un carácter único (por ejemplo: `;`, `.`, `>`, `!`, etc...), un array de tres elementos conteniendo el índice de token en el elemento 0, el contenido del string del token original en el elemento 1 y el número de línea en el elemento 2.

## Ejemplos

`token_get_all` ejemplos

```
<?php
$tokens = token_get_all('<?php echo; ?>');

foreach ($tokens as $token) {
    if (is_array($token)) {
        echo "Line {$token[2]}: ", token_name($token[0]), " ('{$token[1]}')", PHP_EOL;
    }
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Line 1: T_OPEN_TAG ('<?php ')
    Line 1: T_ECHO ('echo')
    Line 1: T_WHITESPACE (' ')
    Line 1: T_CLOSE_TAG ('?>')

`token_get_all` ejemplo de uso incorrecto

```
<?php
$tokens = token_get_all('/* comment */');

foreach ($tokens as $token) {
    if (is_array($token)) {
        echo "Line {$token[2]}: ", token_name($token[0]), " ('{$token[1]}')", PHP_EOL;
    }
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Line 1: T_INLINE_HTML ('/* comment */')

Ten en cuenta en el ejemplo anterior que la cadena se analiza como `T_INLINE_HTML` en lugar del esperado `T_COMMENT`. Esto se debe a que no se utilizó ninguna etiqueta de apertura en el código proporcionado. Esto sería equivalente a colocar un comentario fuera de las etiquetas PHP en un archivo normal.

`token_get_all` en un ejemplo de clase que usa una palabra reservada

```
<?php

$source = <<<'code'
<?php

class A
{
    const PUBLIC = 1;
}
code;

$tokens = token_get_all($source, TOKEN_PARSE);

foreach ($tokens as $token) {
    if (is_array($token)) {
        echo token_name($token[0]) , PHP_EOL;
    }
}

?>

    
```php

Resultado del ejemplo anterior es similar a:

    T_OPEN_TAG
    T_WHITESPACE
    T_CLASS
    T_WHITESPACE
    T_STRING
    T_CONST
    T_WHITESPACE
    T_STRING
    T_LNUMBER

Sin la bandera `TOKEN_PARSE`, el penúltimo token (`T_STRING`) habría sido `T_PUBLIC`.

## Véase también

`PhpToken::tokenize`, `token_name`
