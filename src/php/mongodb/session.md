---
title: La clase MongoDB\Driver\Session
source_url: https://www.php.net/manual/es/class.mongodb-driver-session.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mongodb/mongodb/driver/session.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mongodb
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 51400
---

## Introducción

La clase `MongoDB\Driver\Session` representa una sesión de cliente y es devuelta por MongoDB\Driver\Manager::startSession. Los comandos, consultas y operaciones de escritura pueden entonces asociarse a la sesión.

## Sinopsis de la clase

MongoDB\Driver\Session

final

MongoDB\Driver\Session

Constantes

const

string

MongoDB\Driver\Session::TRANSACTION_NONE

none

const

string

MongoDB\Driver\Session::TRANSACTION_STARTING

starting

const

string

MongoDB\Driver\Session::TRANSACTION_IN_PROGRESS

in_progress

const

string

MongoDB\Driver\Session::TRANSACTION_COMMITTED

committed

const

string

MongoDB\Driver\Session::TRANSACTION_ABORTED

aborted

Métodos

## Constantes predefinidas

`MongoDB\Driver\Session::TRANSACTION_NONE`  
No hay ninguna transacción en curso.

`MongoDB\Driver\Session::TRANSACTION_STARTING`  
Se ha iniciado una transacción, pero no se ha enviado ninguna operación al servidor.

`MongoDB\Driver\Session::TRANSACTION_IN_PROGRESS`  
Hay una transacción en curso.

`MongoDB\Driver\Session::TRANSACTION_COMMITTED`  
La transacción se ha confirmado.

`MongoDB\Driver\Session::TRANSACTION_ABORTED`  
La transacción se ha abortado.
