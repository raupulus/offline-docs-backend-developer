---
title: IntlCalendar::setLenient
description: Define si la interpretación de la fecha/hora es tolerante
source_url: https://www.php.net/manual/es/intlcalendar.setlenient.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/setlenient.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 2ca090342
order: 40600
---

IntlCalendar::setLenient

Define si la interpretación de la fecha/hora es tolerante

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::setLenient(bool $lenient): true
```php

Estilo procedimental

```php
intlcal_set_lenient(IntlCalendar $calendar, bool $lenient): true
```

Define si la interpretación de la fecha/hora es tolerante. En tal modo, ciertos valores fuera de límites para algunos campos son aceptados, el comportamiento siendo similar a aquel de `IntlCalendar::add` (es decir, el valor rebobina, reportándose en campos más significativos cada vez). Si el modo tolerante es desactivado, entonces tales valores generarán un error.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`lenient`  
Utilizar `true` para activar el modo tolerante; `false` en caso contrario.

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ver un ejemplo en `IntlCalendar::isLenient`.
