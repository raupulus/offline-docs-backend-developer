---
title: La clase Dom\TokenList
source_url: https://www.php.net/manual/es/class.dom-tokenlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-tokenlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ae7db14ea
order: 12500
---

## Introducción

Representa un conjunto de tokens en un atributo (por ejemplo, nombres de clases).

## Sinopsis de la clase

final

Dom\TokenList

implements

IteratorAggregate

Countable

Propiedades

public

readonly

int

length

public

string

value

Métodos

## Propiedades

`length`  
El número de tokens.

`value`  
El valor del atributo vinculado a este objeto.

## Notas

> [!NOTE]
> La extensión DOM utiliza el codificado UTF-8 al utilizar los métodos o las propiedades. Los métodos del analizador detectan automáticamente el codificado o permiten al llamante especificar un codificado.

> [!NOTE]
> Los tokens de la lista pueden ser accedidos mediante una sintaxis de tipo array.
