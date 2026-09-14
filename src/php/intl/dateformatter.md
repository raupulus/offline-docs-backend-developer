---
title: La clase IntlDateFormatter
source_url: https://www.php.net/manual/es/class.intldateformatter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1786db6ef
order: 39760
---

## Introducción

La clase `DateFormatter` es una clase concreta, que activa el análisis y el formato de fechas, basado en cadenas modelo, o reglas.

Esta clase representa las funcionalidades de formato de fechas ICU. Permite a los usuarios mostrar fechas en un formato localizado, o analizar cadenas PHP para extraer fechas.

## Sinopsis de la clase

IntlDateFormatter

Constantes

public

const

int

IntlDateFormatter::FULL

public

const

int

IntlDateFormatter::LONG

public

const

int

IntlDateFormatter::MEDIUM

public

const

int

IntlDateFormatter::SHORT

public

const

int

IntlDateFormatter::NONE

public

const

int

IntlDateFormatter::RELATIVE_FULL

public

const

int

IntlDateFormatter::RELATIVE_LONG

public

const

int

IntlDateFormatter::RELATIVE_MEDIUM

public

const

int

IntlDateFormatter::RELATIVE_SHORT

public

const

int

IntlDateFormatter::PATTERN

public

const

int

IntlDateFormatter::GREGORIAN

public

const

int

IntlDateFormatter::TRADITIONAL

Métodos

## Historial de cambios

| Versión | Descripción                             |
|---------|-----------------------------------------|
| 8.4.0   | Se añadió `IntlDateFormatter::PATTERN`. |

## Véase también

[Formateador de fechas ICU](https://unicode-org.github.io/icu-docs/apidoc/dev/icu4c/udat_8h.html) [Formatos de fechas ICU](https://unicode-org.github.io/icu/userguide/format_parse/datetime/#datetime-format-syntax)

## Historial de cambios

| Versión | Descripción                                  |
|---------|----------------------------------------------|
| 8.4.0   | Las constantes de clase ahora están tipadas. |
