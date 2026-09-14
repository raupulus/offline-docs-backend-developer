---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/intl.intldateformatter-constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter-constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 5e36b489f
order: 39750
---

## Constantes predefinidas

Estas constantes se utilizan para especificar diferentes formatos en el constructor de las clases `DateType` y `TimeType`.

`IntlDateFormatter::NONE` `int`  
No incluye este elemento

`IntlDateFormatter::FULL` `int`  
Estilo completamente especificado (`Tuesday, April 12, 1952 AD or 3:30:42pm PST`)

`IntlDateFormatter::LONG` `int`  
Estilo largo (`January 12, 1952 or 3:30:32pm`)

`IntlDateFormatter::MEDIUM` `int`  
Estilo intermedio (`Jan 12, 1952`)

`IntlDateFormatter::SHORT` `int`  
Estilo abreviado, solo la información esencial (`12/13/52` o `3:30pm`)

`IntlDateFormatter::RELATIVE_FULL` `int`  
Idéntico a `IntlDateFormatter::FULL`, pero ayer, hoy, y mañana se muestran como `yesterday`, `today`, y `tomorrow`, respectivamente. Disponible a partir de PHP 8.0.0, para `dateType` únicamente.

`IntlDateFormatter::RELATIVE_LONG` `int`  
Idéntico a `IntlDateFormatter::LONG`, pero ayer, hoy, y mañana se muestran como `yesterday`, `today`, y `tomorrow`, respectivamente. Disponible a partir de PHP 8.0.0, para `dateType` únicamente.

`IntlDateFormatter::RELATIVE_MEDIUM` `int`  
Idéntico a `IntlDateFormatter::MEDIUM`, pero ayer, hoy, y mañana se muestran como `yesterday`, `today`, y `tomorrow`, respectivamente. Disponible a partir de PHP 8.0.0, para `dateType` únicamente.

`IntlDateFormatter::RELATIVE_SHORT` `int`  
Idéntico a `IntlDateFormatter::SHORT`, pero ayer, hoy, y mañana se muestran como `yesterday`, `today`, y `tomorrow`, respectivamente. Disponible a partir de PHP 8.0.0, para `dateType` únicamente.

`IntlDateFormatter::PATTERN` `int`  
Utiliza el patrón dado en `pattern`. Disponible a partir de PHP 8.4.0.

Las constantes enteras siguientes se utilizan para especificar calendarios. Estos calendarios se basan directamente en el calendario gregoriano. Los calendarios no gregorianos deben especificarse en una configuración local. Los ejemplos pueden incluir `locale="hi@calendar=BUDDHIST"`.

`IntlDateFormatter::TRADITIONAL` `int`  
Calendario no gregoriano

`IntlDateFormatter::GREGORIAN` `int`  
Calendario gregoriano
