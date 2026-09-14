---
title: La clase Parle\Parser
source_url: https://www.php.net/manual/es/class.parle-parser.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle.parser.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 61000
---

## Introducción

Clase de análisis sintáctico. Las reglas pueden ser definidas sobre la marcha. Una vez finalizada, se requiere una instancia de `Parle\Lexer` para proporcionar el flujo de tokens.

## Sinopsis de la clase

Parle\Parser

Parle\Parser

Constantes

const

int

Parle\Parser::ACTION_ERROR

0

const

int

Parle\Parser::ACTION_SHIFT

1

const

int

Parle\Parser::ACTION_REDUCE

2

const

int

Parle\Parser::ACTION_GOTO

3

const

int

Parle\Parser::ACTION_ACCEPT

4

const

int

Parle\Parser::ERROR_SYNTAX

0

const

int

Parle\Parser::ERROR_NON_ASSOCIATIVE

1

const

int

Parle\Parser::ERROR_UNKNOWN_TOKEN

2

Propiedades

public

int

action

0

public

int

reduceId

0

Métodos

## Constantes predefinidas

`Parle\Parser::ACTION_ERROR`  

`Parle\Parser::ACTION_SHIFT`  

`Parle\Parser::ACTION_REDUCE`  

`Parle\Parser::ACTION_GOTO`  

`Parle\Parser::ACTION_ACCEPT`  

`Parle\Parser::ERROR_SYNTAX`  

`Parle\Parser::ERROR_NON_ASSOCIATIVE`  

`Parle\Parser::ERROR_UNKNOWN_TOKEN`  

## Propiedades

`action`  
Las acciones del analizador actual que corresponden a una de las constantes de clase de acción, en modo de solo lectura.

`reduceId`  
Las reglas de gramática id justo tratadas en la acción de reducción. El valor corresponde a un token o a un identificador de producción. En modo de solo lectura.
