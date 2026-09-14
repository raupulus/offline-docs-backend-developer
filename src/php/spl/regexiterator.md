---
title: La clase RegexIterator
source_url: https://www.php.net/manual/es/class.regexiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/regexiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 83730
---

## Introducción

Este iterador puede ser usado para filtrar otro iterador basado en una expresión regular.

## Sinopsis de la clase

RegexIterator

extends

FilterIterator

Constantes

public

const

int

RegexIterator::USE_KEY

public

const

int

RegexIterator::INVERT_MATCH

public

const

int

RegexIterator::MATCH

public

const

int

RegexIterator::GET_MATCH

public

const

int

RegexIterator::ALL_MATCHES

public

const

int

RegexIterator::SPLIT

public

const

int

RegexIterator::REPLACE

Propiedades

public

string

null

replacement

null

Métodos

Métodos heredados

## Constantes predefinidas

## Modos de operación RegexIterator

`RegexIterator::ALL_MATCHES`  
Devuelve todas las coincidencias de la entrada actual. (véase `preg_match_all`).

`RegexIterator::GET_MATCH`  
Devuelve la primera coincidencia de la entrada actual. (véase `preg_match`).

`RegexIterator::MATCH`  
Sólo ejecuta la coincidencia (filtro) para la entrada actual (véase `preg_match`).

`RegexIterator::REPLACE`  
Reemplaza la entrada actual (véase `preg_replace`; No está completamente implementado)

`RegexIterator::SPLIT`  
Devuelve los valores divididos de la entrada actual (véase `preg_split`).

## Flags RegexIterator

`RegexIterator::USE_KEY`  
Flag especial: Coincidir con la clave de entrada en lugar del valor de la entrada.

`RegexIterator::INVERT_MATCH`  
Invierte el valor de retorno de RegexIterator::accept.

## Propiedades

`replacement`
