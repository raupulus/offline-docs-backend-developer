---
title: La clase DateInvalidOperationException
source_url: https://www.php.net/manual/es/class.dateinvalidoperationexception.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/dateinvalidoperationexception.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 10260
---

## Introducción

Lanzada por DateTimeImmutable::sub y DateTime::sub cuando se intenta una operación no soportada.

Un ejemplo de operación no soportada es el uso de un objeto `DateInterval` que representa especificaciones de tiempo como `next weekday`, ya que no se puede construir ninguna declaración lógica inversa.

## Sinopsis de la clase

DateInvalidOperationException

extends

DateException

Propiedades heredadas

Métodos heredados
