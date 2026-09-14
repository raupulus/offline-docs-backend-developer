---
title: La clase Pdo\Odbc
source_url: https://www.php.net/manual/es/class.pdo-odbc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_odbc/pdo-odbc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_odbc
translation_status: ready
translation_reviewed: true
translation_revision: 3f82c5450
order: 62460
---

## Introducción

Una subclase de `PDO` que representa una conexión utilizando el controlador PDO ODBC.

## Sinopsis de la clase

Pdo

Odbc

extends

PDO

Constantes heredadas

Constantes

public

const

int

Pdo\Odbc::ATTR_USE_CURSOR_LIBRARY

public

const

int

Pdo\Odbc::ATTR_ASSUME_UTF8

public

const

int

Pdo\Odbc::SQL_USE_IF_NEEDED

public

const

int

Pdo\Odbc::SQL_USE_DRIVER

public

const

int

Pdo\Odbc::SQL_USE_ODBC

Métodos heredados

## Constantes predefinidas

`Pdo\Odbc::ATTR_USE_CURSOR_LIBRARY`  
Esta opción controla el uso de la biblioteca de cursoes ODBC. La biblioteca de cursoes ODBC admite ciertas funcionalidades avanzadas de ODBC (por ejemplo, cursoes desplazables por bloques), que pueden no estar implementadas por el controlador. Se admiten los siguientes valores:

`Pdo\Odbc::SQL_USE_IF_NEEDED`  
Utiliza la biblioteca de cursoes ODBC si es necesario. Este es el valor por omisión.

`Pdo\Odbc::SQL_USE_DRIVER`  
No utilizar nunca la biblioteca de cursoes ODBC.

`Pdo\Odbc::SQL_USE_ODBC`  
Utilizar siempre la biblioteca de cursoes ODBC.

`Pdo\Odbc::ATTR_ASSUME_UTF8`  
Solo para Windows. Si `true`, los datos de caracteres codificados en UTF-16 (`CHAR`, `VARCHAR` y `LONGVARCHAR`) se convierten a UTF-8 al leer o escribir datos en la base de datos. Si `false` (el valor por omisión), la conversión de la codificación de caracteres puede ser realizada por el controlador.
