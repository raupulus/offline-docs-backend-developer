---
title: La clase Parle\Lexer
source_url: https://www.php.net/manual/es/class.parle-lexer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle.lexer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 60980
---

## Introducción

Clase de análisis léxico de estado único. Los lexemas pueden ser definidos sobre la marcha. Si la instancia particular del lexer está destinada a ser utilizada con `Parle\Parser`, los identificadores de tokens deben ser tomados de allí. De lo contrario, pueden proporcionarse identificadores de tokens arbitrarios. Este lexer puede ofrecer cierta ventaja de rendimiento en comparación con `Parle\RLexer`, si no se necesitan múltiples estados. Es importante señalar que `Parle\RParser` no es compatible con este lexer.

## Sinopsis de la clase

Parle\Lexer

Parle\Lexer

Constantes

const

int

Parle\Lexer::ICASE

1

const

int

Parle\Lexer::DOT_NOT_LF

2

const

int

Parle\Lexer::DOT_NOT_CRLF

4

const

int

Parle\Lexer::SKIP_WS

8

const

int

Parle\Lexer::MATCH_ZERO_LEN

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

`Parle\Lexer::ICASE`  

`Parle\Lexer::DOT_NOT_LF`  

`Parle\Lexer::DOT_NOT_CRLF`  

`Parle\Lexer::SKIP_WS`  

`Parle\Lexer::MATCH_ZERO_LEN`  

## Propiedades

`bol`  
Indicador de inicio de entrada.

`flags`  
Flags del lexer.

`state`  
Estado actual del lexer, solo lectura.

`marker`  
Posición de la última coincidencia de token, solo lectura.

`cursor`  
Desplazamiento de entrada actual, solo lectura.
