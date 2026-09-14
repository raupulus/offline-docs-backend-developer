---
title: La clase PDO
source_url: https://www.php.net/manual/es/class.pdo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: a78c72907
order: 61980
---

## Introducción

Representa una conexión entre PHP y un servidor de base de datos.

## Sinopsis de la clase

PDO

Constantes

public

const

int

PDO::PARAM_NULL

public

const

int

PDO::PARAM_BOOL

5

public

const

int

PDO::PARAM_INT

1

public

const

int

PDO::PARAM_STR

2

public

const

int

PDO::PARAM_LOB

3

public

const

int

PDO::PARAM_STMT

4

public

const

int

PDO::PARAM_INPUT_OUTPUT

public

const

int

PDO::PARAM_STR_NATL

public

const

int

PDO::PARAM_STR_CHAR

public

const

int

PDO::PARAM_EVT_ALLOC

public

const

int

PDO::PARAM_EVT_FREE

public

const

int

PDO::PARAM_EVT_EXEC_PRE

public

const

int

PDO::PARAM_EVT_EXEC_POST

public

const

int

PDO::PARAM_EVT_FETCH_PRE

public

const

int

PDO::PARAM_EVT_FETCH_POST

public

const

int

PDO::PARAM_EVT_NORMALIZE

public

const

int

PDO::FETCH_DEFAULT

public

const

int

PDO::FETCH_LAZY

public

const

int

PDO::FETCH_ASSOC

public

const

int

PDO::FETCH_NUM

public

const

int

PDO::FETCH_BOTH

public

const

int

PDO::FETCH_OBJ

public

const

int

PDO::FETCH_BOUND

public

const

int

PDO::FETCH_COLUMN

public

const

int

PDO::FETCH_CLASS

public

const

int

PDO::FETCH_INTO

public

const

int

PDO::FETCH_FUNC

public

const

int

PDO::FETCH_GROUP

public

const

int

PDO::FETCH_UNIQUE

public

const

int

PDO::FETCH_KEY_PAIR

public

const

int

PDO::FETCH_CLASSTYPE

public

const

int

PDO::FETCH_SERIALIZE

public

const

int

PDO::FETCH_PROPS_LATE

public

const

int

PDO::FETCH_NAMED

public

const

int

PDO::ATTR_AUTOCOMMIT

public

const

int

PDO::ATTR_PREFETCH

public

const

int

PDO::ATTR_TIMEOUT

public

const

int

PDO::ATTR_ERRMODE

public

const

int

PDO::ATTR_SERVER_VERSION

public

const

int

PDO::ATTR_CLIENT_VERSION

public

const

int

PDO::ATTR_SERVER_INFO

public

const

int

PDO::ATTR_CONNECTION_STATUS

public

const

int

PDO::ATTR_CASE

public

const

int

PDO::ATTR_CURSOR_NAME

public

const

int

PDO::ATTR_CURSOR

public

const

int

PDO::ATTR_ORACLE_NULLS

public

const

int

PDO::ATTR_PERSISTENT

public

const

int

PDO::ATTR_STATEMENT_CLASS

public

const

int

PDO::ATTR_FETCH_TABLE_NAMES

public

const

int

PDO::ATTR_FETCH_CATALOG_NAMES

public

const

int

PDO::ATTR_DRIVER_NAME

public

const

int

PDO::ATTR_STRINGIFY_FETCHES

public

const

int

PDO::ATTR_MAX_COLUMN_LEN

public

const

int

PDO::ATTR_EMULATE_PREPARES

public

const

int

PDO::ATTR_DEFAULT_FETCH_MODE

public

const

int

PDO::ATTR_DEFAULT_STR_PARAM

public

const

int

PDO::ERRMODE_SILENT

public

const

int

PDO::ERRMODE_WARNING

public

const

int

PDO::ERRMODE_EXCEPTION

public

const

int

PDO::CASE_NATURAL

public

const

int

PDO::CASE_LOWER

public

const

int

PDO::CASE_UPPER

public

const

int

PDO::NULL_NATURAL

public

const

int

PDO::NULL_EMPTY_STRING

public

const

int

PDO::NULL_TO_STRING

public

const

string

PDO::ERR_NONE

public

const

int

PDO::FETCH_ORI_NEXT

public

const

int

PDO::FETCH_ORI_PRIOR

public

const

int

PDO::FETCH_ORI_FIRST

public

const

int

PDO::FETCH_ORI_LAST

public

const

int

PDO::FETCH_ORI_ABS

public

const

int

PDO::FETCH_ORI_REL

public

const

int

PDO::CURSOR_FWDONLY

public

const

int

PDO::CURSOR_SCROLL

Métodos

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
