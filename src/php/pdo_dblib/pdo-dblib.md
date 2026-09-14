---
title: La clase Pdo\Dblib
source_url: https://www.php.net/manual/es/class.pdo-dblib.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_dblib/pdo-dblib.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_dblib
translation_status: ready
translation_reviewed: true
translation_revision: 5d8e96f9b
order: 62280
---

## Introducción

Una subclase de `PDO` que representa una conexión utilizando el controlador PDO DBLib.

## Sinopsis de la clase

Pdo

Dblib

extends

PDO

Constantes heredadas

Constantes

public

const

int

Pdo\Dblib::ATTR_CONNECTION_TIMEOUT

public

const

int

Pdo\Dblib::ATTR_QUERY_TIMEOUT

public

const

bool

Pdo\Dblib::ATTR_STRINGIFY_UNIQUEIDENTIFIER

public

const

int

Pdo\Dblib::ATTR_VERSION

public

const

int

Pdo\Dblib::ATTR_TDS_VERSION

public

const

int

Pdo\Dblib::ATTR_SKIP_EMPTY_ROWSETS

public

const

bool

Pdo\Dblib::ATTR_DATETIME_CONVERT

Métodos heredados

## Constantes predefinidas

`Pdo\Dblib::ATTR_CONNECTION_TIMEOUT`  

`Pdo\Dblib::ATTR_QUERY_TIMEOUT`  

`Pdo\Dblib::ATTR_STRINGIFY_UNIQUEIDENTIFIER`  
A partir de PHP 8.4.0 esta constante es de tipo `bool`; anteriormente, era de tipo `int`.

`Pdo\Dblib::ATTR_VERSION`  

`Pdo\Dblib::ATTR_TDS_VERSION`  

`Pdo\Dblib::ATTR_SKIP_EMPTY_ROWSETS`  

`Pdo\Dblib::ATTR_DATETIME_CONVERT`  
Este atributo de conexión controla el formato de las cadenas para los tipos datetime. Cuando es `false`, PDO_DBLIB devolverá un tipo datetime como una cadena en el formato que SQL Server lo devuelve (es decir, `"2017-10-27 10:22:44"`). Cuando es `true`, PDO_DBLIB convertirá el tipo datetime en una cadena utilizando un formato definido por el usuario o por la configuración regional, según se especifica en el archivo `locales.conf` de FreeTDS. Por defecto, este atributo es `false`.

A partir de PHP 8.4.0 esta constante es de tipo `bool`; anteriormente, era de tipo `int`.
