---
title: La clase Pdo\Sqlite
source_url: https://www.php.net/manual/es/class.pdo-sqlite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_sqlite/pdo-sqlite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_sqlite
translation_status: ready
translation_reviewed: true
translation_revision: ae7db14ea
order: 62760
---

## Introducción

Una subclase de `PDO` que representa una conexión utilizando el controlador PDO SQLite.

Este controlador admite un analizador de consultas SQL dedicado para el dialecto SQLite. Puede gestionar los siguientes elementos:

- Los literales de string simples, dobles y en dólares, con el doblado como mecanismo de escape.

- Las comillas entre corchetes para los identificadores.

- Dos guiones y los comentarios de estilo C (no anidados).

## Sinopsis de la clase

Pdo\Sqlite

extends

PDO

Constantes heredadas

Constantes

public

const

int

Pdo\Sqlite::DETERMINISTIC

public

const

int

Pdo\Sqlite::OPEN_READONLY

public

const

int

Pdo\Sqlite::OPEN_READWRITE

public

const

int

Pdo\Sqlite::OPEN_CREATE

public

const

int

Pdo\Sqlite::ATTR_OPEN_FLAGS

public

const

int

Pdo\Sqlite::ATTR_READONLY_STATEMENT

public

const

int

Pdo\Sqlite::ATTR_EXTENDED_RESULT_CODES

Métodos

Métodos heredados

## Constantes predefinidas

`Pdo\Sqlite::DETERMINISTIC`  

`Pdo\Sqlite::OPEN_READONLY`  

`Pdo\Sqlite::OPEN_READWRITE`  

`Pdo\Sqlite::OPEN_CREATE`  

`Pdo\Sqlite::ATTR_OPEN_FLAGS`  

`Pdo\Sqlite::ATTR_READONLY_STATEMENT`  

`Pdo\Sqlite::ATTR_EXTENDED_RESULT_CODES`
