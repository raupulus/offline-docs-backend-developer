---
title: La clase DateError
source_url: https://www.php.net/manual/es/class.dateerror.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateerror.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 10200
---

## Introducción

Lanzada cuando la base de datos de los husos horarios no se encuentra, o contiene datos inválidos.

Este error no debería producirse nunca, y no depende del código. Hay dos excepciones hijas (DateObjectError y DateRangeError) que se lanzan en función de los errores del desarrollador o de los problemas de rango.

## Sinopsis de la clase

DateError

extends

Error

Propiedades heredadas

Métodos heredados

## Véase también

DateObjectError

DateRangeError
