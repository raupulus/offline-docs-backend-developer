---
title: Tipos de clases relativas
source_url: https://www.php.net/manual/es/language.types.relative-class-types.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/types/relative-class-types.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 161dde4fe
order: 4510
---

## Tipos de clases relativas

Estas declaraciones de tipos solo pueden ser utilizadas dentro de las clases.

## `self`

El valor debe ser un [`instanceof`](#language.operators.type) de la misma clase en la que se utiliza la declaración de tipo.

## `parent`

El valor debe ser un [`instanceof`](#language.operators.type) de un padre de la clase en la que se utiliza la declaración de tipo.

## static

`static` es un tipo de retorno únicamente que exige que el valor devuelto sea un [`instanceof`](#language.operators.type) de la misma clase en la que se llama el método.
