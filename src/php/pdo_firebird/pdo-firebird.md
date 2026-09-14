---
title: La clase Pdo\Firebird
source_url: https://www.php.net/manual/es/class.pdo-firebird.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_firebird/pdo-firebird.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_firebird
translation_status: ready
translation_reviewed: true
translation_revision: 3f82c5450
order: 62320
---

## Introducción

Una subclase de `PDO` que representa una conexión utilizando el controlador PDO de Firebird.

## Sinopsis de la clase

Pdo

Firebird

extends

PDO

Constantes heredadas

Constantes

public

const

int

Pdo\Firebird::ATTR_DATE_FORMAT

public

const

int

Pdo\Firebird::ATTR_TIME_FORMAT

public

const

int

Pdo\Firebird::ATTR_TIMESTAMP_FORMAT

public

const

int

Pdo\Firebird::TRANSACTION_ISOLATION_LEVEL

public

const

int

Pdo\Firebird::READ_COMMITTED

public

const

int

Pdo\Firebird::REPEATABLE_READ

public

const

int

Pdo\Firebird::SERIALIZABLE

public

const

int

Pdo\Firebird::WRITABLE_TRANSACTION

Métodos

Métodos heredados

## Constantes predefinidas

`Pdo\Firebird::ATTR_DATE_FORMAT`  
Define el formato de fecha.

`Pdo\Firebird::ATTR_TIME_FORMAT`  
Define el formato de hora.

`Pdo\Firebird::ATTR_TIMESTAMP_FORMAT`  
Define el formato de la marca de tiempo.

`Pdo\Firebird::TRANSACTION_ISOLATION_LEVEL`  
Los atributos de transacción definen el nivel de aislamiento de la transacción. Puede ser uno de los siguientes: `Pdo\Firebird::READ_COMMITTED`, `Pdo\Firebird::REPEATABLE_READ`, o `Pdo\Firebird::SERIALIZABLE`.

`Pdo\Firebird::READ_COMMITTED`  
Bandera que indica que el nivel de aislamiento de la transacción ANSI es read committed. Este es el comportamiento por omisión.

`Pdo\Firebird::REPEATABLE_READ`  
Bandera que indica que el nivel de aislamiento de la transacción ANSI es repeatable read. Esto corresponde al nivel de aislamiento "snapshot" de Firebird.

`Pdo\Firebird::SERIALIZABLE`  
Bandera que indica que el nivel de aislamiento de la transacción ANSI es serializable. Esto corresponde al nivel de aislamiento "snapshot table stability" de Firebird.

`Pdo\Firebird::WRITABLE_TRANSACTION`  
El atributo booleano utilizado para cambiar el modo de acceso a la transacción entre `READ ONLY` y `READ WRITE`. Por omisión, es `true` indicando `READ WRITE`.
