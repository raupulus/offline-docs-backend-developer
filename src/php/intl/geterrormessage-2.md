---
title: IntlCalendar::getErrorMessage
description: Devuelve el último mensaje de error en el objeto
source_url: https://www.php.net/manual/es/intlcalendar.geterrormessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/geterrormessage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40340
---

IntlCalendar::getErrorMessage

intlcal_get_error_message

Devuelve el último mensaje de error en el objeto

## Descripción

Estilo orientado a objetos (método):

```php
public IntlCalendar::getErrorMessage(): string
```php

Estilo procedimental:

```php
intlcal_get_error_message(IntlCalendar $calendar): string
```

Devuelve (si existe) el mensaje de error asociado al error reportado por `IntlCalendar::getErrorCode` o `intlcal_get_error_code`. Si no existe un mensaje de error asociado, solo se devuelve la representación de string del nombre de la constante de error. De lo contrario, el mensaje incluye también un mensaje definido del lado de la ligadura PHP.

## Parámetros

`calendar`  
El objeto calendario, en la interfaz de estilo procedimental.

## Valores devueltos

El mensaje de error asociado al último error ocurrido en una llamada de función sobre este objeto, o un string indicando la inexistencia de un error. Devuelve `false` en caso de fallo.

## Ejemplos

`IntlCalendar::getErrorMessage`

```php
<?php
$cal = IntlCalendar::createInstance('UTC', 'en_US');
var_dump($cal->getErrorMessage());

$cal->getWeekendTransition(IntlCalendar::DOW_WEDNESDAY);
var_dump($cal->getErrorMessage());

    
```

El ejemplo anterior mostrará:

    string(12) "U_ZERO_ERROR"
    string(82) "intlcal_get_weekend_transition: Error calling ICU method: U_ILLEGAL_ARGUMENT_ERROR"
