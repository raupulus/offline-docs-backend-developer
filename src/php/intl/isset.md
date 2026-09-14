---
title: IntlCalendar::isSet
description: Indica si un campo está definido
source_url: https://www.php.net/manual/es/intlcalendar.isset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/isset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40530
---

IntlCalendar::isSet

Indica si un campo está definido

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::isSet(int $field): bool
```php

Estilo procedimental

```php
intlcal_is_set(IntlCalendar $calendar, int $field): bool
```

Indica si un campo está definido (en oposición a [borrado](#intlcalendar.clear)). Los campos definidos tienen prioridad sobre los campos no definidos y sus valores por defecto durante el cálculo de la fecha/hora. Los campos definidos más tarde tienen prioridad sobre los campos definidos antes.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Suponiendo que no hay errores de argumentos, devuelve `true` si el campo está definido.

## Ejemplos

Ver un ejemplo en `IntlCalendar::clear`.

## Véase también

IntlCalendar::clear, IntlCalendar::set
