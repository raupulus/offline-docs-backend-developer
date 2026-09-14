---
title: IntlDateFormatter::isLenient
description: Devuelve la severidad utilizada para IntlDateFormatter
source_url: https://www.php.net/manual/es/intldateformatter.islenient.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/is-lenient.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 39670
---

IntlDateFormatter::isLenient

datefmt_is_lenient

Devuelve la severidad utilizada para IntlDateFormatter

## Descripción

Estilo orientado a objetos

```php
public IntlDateFormatter::isLenient(): bool
```php

Estilo procedimental

```php
datefmt_is_lenient(IntlDateFormatter $formatter): bool
```

Verifica si el analizador es estricto o flexible al interpretar strings que no coinciden exactamente con el patrón buscado.

## Parámetros

`formatter`  
El recurso de formateador `IntlDateFormatter`.

## Valores devueltos

`true` si el analizador es flexible, `false` si el analizador es estricto. Por omisión, el analizador es flexible.

## Ejemplos

Ejemplo con `datefmt_is_lenient`

```php
<?php
$fmt = datefmt_create(
    'en_US',
    IntlDateFormatter::FULL,
    IntlDateFormatter::FULL,
    'America/Los_Angeles',
    IntlDateFormatter::GREGORIAN,
    'dd/mm/yyyy'
);
echo 'El formateador es estricto : ';
if ($fmt->isLenient()) {
    echo 'Sí';
} else {
    echo 'No';
}
datefmt_parse($fmt, '35/13/1971');
echo "\n Intento de análisis de la fecha '35/13/1971'.\nEl resultado es : " . datefmt_parse($fmt, '35/13/1971');
if (intl_get_error_code() != 0) {
    echo "\nError_msg es : " . intl_get_error_message();
    echo "\nError_code es : " . intl_get_error_code();
}
datefmt_set_lenient($fmt,false);
echo 'Ahora, el formateador es estricto : ';
if ($fmt->isLenient()) {
    echo 'Sí';
} else {
    echo 'No';
}
datefmt_parse($fmt, '35/13/1971');
echo "\n Intento de análisis de la fecha '35/13/1971'.\nEl resultado es : " . datefmt_parse($fmt, '35/13/1971');
if (intl_get_error_code() != 0) {
    echo "\nError_msg es : " . intl_get_error_message();
    echo "\nError_code es : " . intl_get_error_code();
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
    "dd/mm/yyyy"
);
echo "El formateador es estricto : ";
if ($fmt->isLenient()) {
    echo 'Sí';
} else {
    echo 'No';
}
$fmt->parse('35/13/1971');
echo "\n Intento de análisis de la fecha '35/13/1971'.\nEl resultado es : " . $fmt->parse('35/13/1971');
if (intl_get_error_code() != 0){
    echo "\nError_msg es : " . intl_get_error_message();
    echo "\nError_code es : " . intl_get_error_code();
}

$fmt->setLenient(FALSE);
echo 'Ahora el formateador es estricto : ';
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

    El formateador es estricto : Sí
    Intento de análisis de la fecha '35/13/1971'.
    El resultado es : 34503180
    Ahora, el formateador es estricto : No
    Intento de análisis de la fecha '35/13/1971'.
    El resultado es :
    Error_msg es : Date parsing failed: U_PARSE_ERROR
    Error_code es : 9
     
      

## Véase también

`datefmt_set_lenient`, `datefmt_create`
