---
title: La clase Parle\RParser
source_url: https://www.php.net/manual/es/class.parle-rparser.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/parle/parle.rparser.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: parle
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 61030
---

## Introducción

Clase de análisis sintáctico. Las reglas pueden ser definidas sobre la marcha. Una vez finalizada, se requiere una instancia de `Parle\RLexer` para proporcionar el flujo de tokens.

## Sinopsis de la clase

Parle\RParser

Parle\RParser

Constantes

const

int

Parle\RParser::ACTION_ERROR

0

const

int

Parle\RParser::ACTION_SHIFT

1

const

int

Parle\RParser::ACTION_REDUCE

2

const

int

Parle\RParser::ACTION_GOTO

3

const

int

Parle\RParser::ACTION_ACCEPT

4

const

int

Parle\RParser::ERROR_SYNTAX

0

const

int

Parle\RParser::ERROR_NON_ASSOCIATIVE

1

const

int

Parle\RParser::ERROR_UNKNOWN_TOKEN

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

`Parle\RParser::ACTION_ERROR`  

`Parle\RParser::ACTION_SHIFT`  

`Parle\RParser::ACTION_REDUCE`  

`Parle\RParser::ACTION_GOTO`  

`Parle\RParser::ACTION_ACCEPT`  

`Parle\RParser::ERROR_SYNTAX`  

`Parle\RParser::ERROR_NON_ASSOCIATIVE`  

`Parle\RParser::ERROR_UNKNOWN_TOKEN`  

## Propiedades

`action`  
Las acciones del parser actual que corresponden a una de las constantes de clase de acción, en modo de solo lectura.

`reduceId`  
Las reglas de gramática id justo tratadas en la acción de reducción. El valor corresponde a un token o a un identificador de producción. En modo de solo lectura.
