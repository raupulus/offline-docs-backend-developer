---
title: La clase IntlBreakIterator
source_url: https://www.php.net/manual/es/class.intlbreakiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlbreakiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1f68eecaa
order: 40180
---

## Introducción

Un "delimitador de ruptura" es un objeto ICU que expone métodos para localizar delimitaciones en texto (por ejemplo, delimitaciones de palabras o frases). La clase `IntlBreakIterator` de PHP sirve como clase base para todos los tipos de delimitadores de ruptura ICU. Cuando una funcionalidad adicional está disponible, la extensión intl puede exponer el delimitador de ruptura ICU con subclases apropiadas, tales como `IntlRuleBasedBreakIterator` o `IntlCodePointBreakIterator`.

Esta clase implementa IteratorAggregate. Recorrer un `IntlBreakIterator` produce valores enteros no negativos que representan las posiciones sucesivas de las delimitaciones de texto, expresadas como conteos de unidades de código UTF-8 (octetos), tomados desde el inicio del texto (que tiene la posición `0`). Las claves producidas por el iterador forman simplemente la secuencia de números naturales `{0, 1, 2, …}`.

## Sinopsis de la clase

IntlBreakIterator

implements

IteratorAggregate

Constantes

public

const

int

IntlBreakIterator::DONE

public

const

int

IntlBreakIterator::WORD_NONE

public

const

int

IntlBreakIterator::WORD_NONE_LIMIT

public

const

int

IntlBreakIterator::WORD_NUMBER

public

const

int

IntlBreakIterator::WORD_NUMBER_LIMIT

public

const

int

IntlBreakIterator::WORD_LETTER

public

const

int

IntlBreakIterator::WORD_LETTER_LIMIT

public

const

int

IntlBreakIterator::WORD_KANA

public

const

int

IntlBreakIterator::WORD_KANA_LIMIT

public

const

int

IntlBreakIterator::WORD_IDEO

public

const

int

IntlBreakIterator::WORD_IDEO_LIMIT

public

const

int

IntlBreakIterator::LINE_SOFT

public

const

int

IntlBreakIterator::LINE_SOFT_LIMIT

public

const

int

IntlBreakIterator::LINE_HARD

public

const

int

IntlBreakIterator::LINE_HARD_LIMIT

public

const

int

IntlBreakIterator::SENTENCE_TERM

public

const

int

IntlBreakIterator::SENTENCE_TERM_LIMIT

public

const

int

IntlBreakIterator::SENTENCE_SEP

public

const

int

IntlBreakIterator::SENTENCE_SEP_LIMIT

Métodos

## Constantes predefinidas

`IntlBreakIterator::DONE` `int`  

`IntlBreakIterator::WORD_NONE` `int`  

`IntlBreakIterator::WORD_NONE_LIMIT` `int`  

`IntlBreakIterator::WORD_NUMBER` `int`  

`IntlBreakIterator::WORD_NUMBER_LIMIT` `int`  

`IntlBreakIterator::WORD_LETTER` `int`  

`IntlBreakIterator::WORD_LETTER_LIMIT` `int`  

`IntlBreakIterator::WORD_KANA` `int`  

`IntlBreakIterator::WORD_KANA_LIMIT` `int`  

`IntlBreakIterator::WORD_IDEO` `int`  

`IntlBreakIterator::WORD_IDEO_LIMIT` `int`  

`IntlBreakIterator::LINE_SOFT` `int`  

`IntlBreakIterator::LINE_SOFT_LIMIT` `int`  

`IntlBreakIterator::LINE_HARD` `int`  

`IntlBreakIterator::LINE_HARD_LIMIT` `int`  

`IntlBreakIterator::SENTENCE_TERM` `int`  

`IntlBreakIterator::SENTENCE_TERM_LIMIT` `int`  

`IntlBreakIterator::SENTENCE_SEP` `int`  

`IntlBreakIterator::SENTENCE_SEP_LIMIT` `int`  

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Las constantes de clase ahora están tipadas. |
| 8.0.0 | `IntlBreakIterator` ahora implementa IteratorAggregate. Antes, Traversable era implementada en su lugar. |
