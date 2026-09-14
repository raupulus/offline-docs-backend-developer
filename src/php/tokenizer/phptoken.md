---
title: La clase PhpToken
source_url: https://www.php.net/manual/es/class.phptoken.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tokenizer/phptoken.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tokenizer
translation_status: ready
translation_revision: 4d17b7b49
order: 94430
---

## Introducción

Esta clase proporciona una alternativa a `token_get_all`. Mientras que la función devuelve tokens ya sea como una única string, ya sea como un array con un ID de token, un texto de token y un número de línea, `PhpToken::tokenize` normaliza todos los tokens en objetos PhpToken, lo que hace que el código que opera sobre los tokens sea más eficiente en memoria y más legible.

## Sinopsis de la clase

PhpToken

implements

Stringable

Propiedades

public

int

id

public

string

text

public

int

line

public

int

pos

Métodos

## Propiedades

`id`  
Una de las constantes T\_\* o un código ASCII que representa un token de un solo carácter.

`text`  
El contenido textual del token.

`line`  
El número de línea (a partir de 1) del token.

`pos`  
La posición de inicio (a partir de 0) en la string tokenizada (el número de bytes).
