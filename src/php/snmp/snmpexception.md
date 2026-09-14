---
title: La clase SNMPException
source_url: https://www.php.net/manual/es/class.snmpexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/snmp/snmpexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: snmp
translation_status: ready
translation_revision: '409067254'
order: 75030
---

## Introducción

Representa un error lanzado por SNMP. No se debe lanzar una excepción `SNMPException` desde su código. Ver las [excepciones](#language.exceptions) para más información sobre las excepciones en PHP.

## Sinopsis de la clase

SNMPException

extends

RuntimeException

Propiedades heredadas

Métodos heredados

## Propiedades

`code`  
Código de error de la biblioteca `SNMP`. Utilizar la función `Exception::getCode` para acceder a él.
