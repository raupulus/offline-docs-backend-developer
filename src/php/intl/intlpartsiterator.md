---
title: La clase IntlPartsIterator
source_url: https://www.php.net/manual/es/class.intlpartsiterator.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlpartsiterator.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1f68eecaa
order: 41480
---

## Introducción

Los objetos de esta clase pueden ser obtenidos a partir de objetos `IntlBreakIterator`. Mientras que los iteradores de ruptura proporcionan una secuencia de posiciones de límites cuando son iterados, los objetos `IntlPartsIterator` proporcionan, por conveniencia, los fragmentos de texto comprendidos entre dos límites sucesivos.

Las claves pueden representar el desplazamiento del límite izquierdo, del límite derecho, o pueden ser simplemente la secuencia de enteros no negativos. Ver `IntlBreakIterator::getPartsIterator`.

## Sinopsis de la clase

IntlPartsIterator

extends

IntlIterator

Constantes

public

const

int

IntlPartsIterator::KEY_SEQUENTIAL

public

const

int

IntlPartsIterator::KEY_LEFT

public

const

int

IntlPartsIterator::KEY_RIGHT

Métodos

Métodos heredados

## Constantes predefinidas

`IntlPartsIterator::KEY_SEQUENTIAL` `int`  

`IntlPartsIterator::KEY_LEFT` `int`  

`IntlPartsIterator::KEY_RIGHT` `int`  

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
