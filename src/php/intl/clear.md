---
title: IntlCalendar::clear
description: Vacía un campo o todos los campos
source_url: https://www.php.net/manual/es/intlcalendar.clear.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/clear.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 2ca090342
order: 40220
---

IntlCalendar::clear

Vacía un campo o todos los campos

## Descripción

Estilo orientado a objetos

```php
public IntlCalendar::clear([int $field]): true
```php

Estilo procedimental

```php
intlcal_clear(IntlCalendar $calendar, [int $field]): true
```

Vacía un campo específico o todos los campos. Un campo vacío se marca como no utilizado, lo que le otorga la menor prioridad en comparación con los campos sobrescritos o incluso los valores por defecto durante el cálculo del tiempo. Además, este valor se establece a `0`, lo que otorga al campo una prioridad baja; este valor pudo haber sido establecido a otro valor por la duración que el campo tardó en completar su solicitud.

## Parámetros

`calendar`  
Una instancia de `IntlCalendar`.

`field`  

## Valores devueltos

Retorna siempre `true`.

## Historial de cambios

| Versión | Descripción                                                   |
|---------|---------------------------------------------------------------|
| 8.2.0   | El tipo de retorno es ahora `true`, anteriormente era `bool`. |

## Ejemplos

Ejemplo con `IntlCalendar::clear`

```php
<?php
ini_set('intl.default_locale', 'es_ES');
ini_set('date.timezone', 'UTC');

$fields = array(
    'FIELD_ERA'                  => 0,
    'FIELD_YEAR'                 => 1,
    'FIELD_MONTH'                => 2,
    'FIELD_WEEK_OF_YEAR'         => 3,
    'FIELD_WEEK_OF_MONTH'        => 4,
    'FIELD_DATE'                 => 5,
    'FIELD_DAY_OF_YEAR'          => 6,
    'FIELD_DAY_OF_WEEK'          => 7,
    'FIELD_DAY_OF_WEEK_IN_MONTH' => 8,
    'FIELD_AM_PM'                => 9,
    'FIELD_HOUR'                 => 10,
    'FIELD_HOUR_OF_DAY'          => 11,
    'FIELD_MINUTE'               => 12,
    'FIELD_SECOND'               => 13,
    'FIELD_MILLISECOND'          => 14,
    'FIELD_ZONE_OFFSET'          => 15,
    'FIELD_DST_OFFSET'           => 16,
    'FIELD_YEAR_WOY'             => 17,
    'FIELD_DOW_LOCAL'            => 18,
    'FIELD_EXTENDED_YEAR'        => 19,
    'FIELD_JULIAN_DAY'           => 20,
    'FIELD_MILLISECONDS_IN_DAY'  => 21,
    'FIELD_IS_LEAP_MONTH'        => 22,
    'FIELD_FIELD_COUNT'          => 23,
);
function getSetFields(IntlCalendar $cal) {
    global $fields;
    $ret = array();
    foreach ($fields as $name => $value) {
        if ($cal->isSet($value)) {
            $ret[] = $name;
        }
    }
    return $ret;
}

$cal = new IntlGregorianCalendar(2013, 2 /* Marzo */, 15);
echo "Después de crear un GregorianCalendar\n";
print_r(getSetFields($cal));
echo "\n";

echo IntlDateFormatter::formatObject($cal), "\n";
echo "Después de que el formateador solicite el año extendido\n";
print_r(getSetFields($cal));
echo "\n";

$cal->clear(IntlCalendar::FIELD_YEAR);
echo "Después de vaciar el año, la fecha permanece igual\n";
echo IntlDateFormatter::formatObject($cal), "\n";
echo "ya que FIELD_EXTENDED_YEAR sigue definido\n";
print_r(getSetFields($cal));
echo "\n";

var_dump($cal->clear(IntlCalendar::FIELD_EXTENDED_YEAR));
echo "Después de vaciar el año extendido\n";
print_r(getSetFields($cal));
echo IntlDateFormatter::formatObject($cal), "\n";
echo "\n";

echo "Después de recalcular los campos,\n"
        . " el año extendido está definido de nuevo (a 1970)\n";
print_r(getSetFields($cal));
echo "\n";

$cal->clear();
echo "Después de llamar a la variante sin argumentos\n";
print_r(getSetFields($cal));
echo IntlDateFormatter::formatObject($cal), "\n";

    
```

El ejemplo anterior mostrará:

    Después de crear un GregorianCalendar
    Array
    (
        [0] => FIELD_ERA
        [1] => FIELD_YEAR
        [2] => FIELD_MONTH
        [3] => FIELD_DATE
    )

    15/03/2013 00:00:00
    Después de que el formateador solicite el año extendido
    Array
    (
        [0] => FIELD_ERA
        [1] => FIELD_YEAR
        [2] => FIELD_MONTH
        [3] => FIELD_DATE
        [4] => FIELD_EXTENDED_YEAR
    )

    Después de vaciar el año, la fecha permanece igual
    15/03/2013 00:00:00
    ya que FIELD_EXTENDED_YEAR sigue definido
    Array
    (
        [0] => FIELD_ERA
        [1] => FIELD_MONTH
        [2] => FIELD_DATE
        [3] => FIELD_EXTENDED_YEAR
    )

    bool(true)
    Después de vaciar el año extendido
    Array
    (
        [0] => FIELD_ERA
        [1] => FIELD_MONTH
        [2] => FIELD_DATE
    )
    15/03/1970 00:00:00

    Después de recalcular los campos,
     el año extendido está definido de nuevo (a 1970)
    Array
    (
        [0] => FIELD_ERA
        [1] => FIELD_MONTH
        [2] => FIELD_DATE
        [3] => FIELD_EXTENDED_YEAR
    )

    Después de llamar a la variante sin argumentos
    Array
    (
    )
    01/01/1970 00:00:00
