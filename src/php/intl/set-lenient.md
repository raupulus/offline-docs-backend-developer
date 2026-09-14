---
title: IntlDateFormatter::setLenient
description: Configura la flexibilidad del analizador
source_url: https://www.php.net/manual/es/intldateformatter.setlenient.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/set-lenient.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 39720
---

IntlDateFormatter::setLenient

datefmt_set_lenient

Configura la flexibilidad del analizador

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::setLenient(bool $lenient): void
```php

Estilo procedimental

```php
datefmt_set_lenient(IntlDateFormatter $formatter, bool $lenient): void
```

Define si el analizador es estricto o flexible al interpretar strings que no coinciden exactamente con el patrón buscado. Activar la flexibilidad del analizador permite aceptar valores que podrían ser considerados erróneos por el analizador estricto. Los espacios, los caracteres desconocidos o las fechas inválidas no son aceptados.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

`lenient`  
Si el analizador es flexible o no, por defecto, vale `true` (flexible).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `datefmt_set_lenient`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'dd/MM/yyyy'
);
echo 'El formateador es flexible : ';
if ($fmt->isLenient()) {
    echo 'Sí';
} else {
    echo 'No';
}
datefmt_parse($fmt, '35/13/1971');
echo "\nIntento de análisis de la fecha '35/13/1971'.\nEl resultado es : " . datefmt_parse($fmt, '35/13/1971');
if (intl_get_error_code() != 0) {
    echo "\nError_msg es : " . intl_get_error_message();
    echo "\nError_code es : " . intl_get_error_code();
}
datefmt_set_lenient($fmt, false);
echo "\nAhora, el formateador es estricto : ";
if ($fmt->isLenient()) {
    echo 'Sí';
} else {
    echo 'No';
}
datefmt_parse($fmt, '35/13/1971');
echo "\nIntento de análisis de la fecha '35/13/1971'.\nEl resultado es : " . datefmt_parse($fmt, '35/13/1971');
if (intl_get_error_code() != 0) {
    echo "\nError_msg es : ".intl_get_error_message();
    echo "\nError_code es : ".intl_get_error_code();
}

?>

   
```

Ejemplo orientado a objetos

```php
<?php
$fmt = new IntlDateFormatter(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'dd/MM/yyyy'
);
echo 'El formateador es flexible : ';
if ($fmt->isLenient()) {
    echo 'Sí';
} else {
    echo 'No';
}
$fmt->parse('35/13/1971');
echo "\n Intento de análisis de la fecha '35/13/1971'.\nEl resultado es : " . $fmt->parse('35/13/1971');
if (intl_get_error_code() != 0) {
    echo "\nError_msg es : " . intl_get_error_message();
    echo "\nError_code es : " . intl_get_error_code();
}

$fmt->setLenient(FALSE);
echo "\nAhora, el formateador es estricto : ";
if ($fmt->isLenient()) {
    echo 'Sí';
} else {
    echo 'No';
}
$fmt->parse('35/13/1971');
echo "\n Intento de análisis de la fecha '35/13/1971'.\nEl resultado es : " . $fmt->parse('35/13/1971');
if (intl_get_error_code() != 0) {
    echo "\nError_msg es : " . intl_get_error_message();
    echo "\nError_code es : " . intl_get_error_code();
}

?>

   
```

El ejemplo anterior mostrará:

    El formateador es flexible : No
    Intento de análisis de la fecha '35/13/1971'.
    El resultado es : 66038400
    Ahora, el formateador es estricto : Sí
    Intento de análisis de la fecha '35/13/1971'.
    El resultado es : Error_msg es : Date parsing failed: U_PARSE_ERROR Error_code es : 9

      

## Véase también

`datefmt_is_lenient`, `datefmt_create`
