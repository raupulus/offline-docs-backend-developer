---
title: La clase PDOException
source_url: https://www.php.net/manual/es/class.pdoexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdoexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: 3c4752c0a
order: 61990
---

## Introducción

Representa un error emitido por PDO. No debe lanzarse una excepción `PDOException` desde el propio código. Ver el capítulo sobre las [excepciones](#language.exceptions) para obtener más información sobre las excepciones en PHP.

## Sinopsis de la clase

PDOException

extends

RuntimeException

Propiedades

protected

int

string

code

public

array

null

errorInfo

null

Propiedades heredadas

Métodos heredados

## Propiedades

`errorInfo`  
Corresponde a PDO::errorInfo o PDOStatement::errorInfo

`code`  
Código de error `SQLSTATE`. Utilice el método Exception::getCode para acceder a él.
