---
title: La clase Parle\RLexer
source_url: https://www.php.net/manual/es/class.parle-rlexer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle.rlexer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 61020
---

## Introducción

Clase de análisis léxico de múltiples estados. Los lexemas pueden ser definidos sobre la marcha. Si la instancia particular del lexer está destinada a ser utilizada con `Parle\RParser`, los identificadores de tokens deben ser tomados de allí. De lo contrario, se pueden proporcionar identificadores de tokens arbitrarios. Es importante señalar que `Parle\Parser` no es compatible con este lexer.

## Sinopsis de la clase

Parle\RLexer

Parle\RLexer

Constantes

const

int

Parle\RLexer::ICASE

1

const

int

Parle\RLexer::DOT_NOT_LF

2

const

int

Parle\RLexer::DOT_NOT_CRLF

4

const

int

Parle\RLexer::SKIP_WS

8

const

int

Parle\RLexer::MATCH_ZERO_LEN

16

Propiedades

public

bool

bol

false

public

int

flags

0

public

int

state

0

public

int

marker

0

public

int

cursor

0

Métodos

## Constantes predefinidas

`Parle\RLexer::ICASE`  

`Parle\RLexer::DOT_NOT_LF`  

`Parle\RLexer::DOT_NOT_CRLF`  

`Parle\RLexer::SKIP_WS`  

`Parle\RLexer::MATCH_ZERO_LEN`  

## Propiedades

`bol`  
Indicador de inicio de entrada.

`flags`  
Flags del lexer.

`state`  
Estado actual del lexer, de solo lectura.

`marker`  
Posición de la última coincidencia de token, de solo lectura.

`cursor`  
Desplazamiento de entrada actual, de solo lectura.
