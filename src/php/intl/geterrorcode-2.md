---
title: IntlCalendar::getErrorCode
description: Devuelve el último código de error en el objeto
source_url: https://www.php.net/manual/es/intlcalendar.geterrorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/geterrorcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 40330
---

IntlCalendar::getErrorCode

intlcal_get_error_code

Devuelve el último código de error en el objeto

## Descripción

Estilo orientado a objetos (método):

```php
public IntlCalendar::getErrorCode(): int
```php

Estilo procedimental:

```php
intlcal_get_error_code(IntlCalendar $calendar): int
```

Devuelve el código de error numérico ICU para la última llamada en este objeto (incluyendo el clonado) o el objeto `IntlCalendar` dado para el argumento `calendar` (en la versión procedimental). Esto puede indicar solamente una advertencia (código de error negativo) o ninguna error en absoluto (`U_ZERO_ERROR`). La presencia real de un error puede ser probada con `intl_is_failure`.

Los argumentos inválidos detectados del lado PHP (antes de la invocación de las funciones de la biblioteca ICU) no son registrados para los propósitos de esta función.

El último código de error que ocurrió en cualquier llamada a una función de la extensión intl, incluyendo los errores de argumentos tempranos, puede ser obtenido con `intl_get_error_code`. Esta función reinicia el código de error global, pero no el código de error del objeto.

## Parámetros

`calendar`  
El objeto calendario, en la interfaz de estilo procedimental.

## Valores devueltos

Un código de error ICU indicando éxito, fallo o advertencia. Devuelve `false` en caso de fallo.

## Ejemplos

`IntlCalendar::getErrorCode` y `IntlCalendar::getErrorMessage`

```php
<?php
ini_set("intl.error_level", E_WARNING);
ini_set("intl.default_locale", "nl");

$intlcal = new IntlGregorianCalendar(2012, 1, 29);
var_dump(
    $intlcal->getErrorCode(),
    $intlcal->getErrorMessage()
);
$intlcal->fieldDifference(-1e100, IntlCalendar::FIELD_SECOND);

var_dump(
    $intlcal->getErrorCode(),
    $intlcal->getErrorMessage()
);

    
```

El ejemplo anterior mostrará:

    int(0)
    string(12) "U_ZERO_ERROR"

    Warning: IntlCalendar::fieldDifference(): intlcal_field_difference: Call to ICU method has failed in /home/glopes/php/ws/example.php on line 10
    int(1)
    string(81) "intlcal_field_difference: Call to ICU method has failed: U_ILLEGAL_ARGUMENT_ERROR"

## Véase también

IntlCalendar::getErrorMessage, intl_is_failure, intl_error_name, intl_get_error_code, intl_get_error_message
