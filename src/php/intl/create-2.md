---
title: IntlDateFormatter::create
description: Crea un formateador de fecha
source_url: https://www.php.net/manual/es/intldateformatter.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_revision: c142be811
order: 39540
---

IntlDateFormatter::create

datefmt_create

IntlDateFormatter::\_\_construct

Crea un formateador de fecha

## Descripción

Estilo orientado a objetos

```php
public static IntlDateFormatter::create(string $locale, [int $dateType], [int $timeType], [IntlTimeZone $timezone], [IntlCalendar $calendar], [string $pattern]): IntlDateFormatter
```php

Estilo orientado a objetos (constructor)

```php
public IntlDateFormatter::__construct(string $locale, [int $dateType], [int $timeType], [IntlTimeZone $timezone], [IntlCalendar $calendar], [string $pattern])
```

Estilo procedimental

```php
datefmt_create(string $locale, [int $dateType], [int $timeType], [IntlTimeZone $timezone], [IntlCalendar $calendar], [string $pattern]): IntlDateFormatter
```php

Crea un formateador de fecha.

## Parámetros

`locale`  
La configuración local a utilizar para formatear y analizar o `null` para utilizar el valor especificado en la configuración ini [intl.default_locale](#ini.intl.default-locale).

`dateType`  
El tipo de fecha a utilizar (`none`, `short`, `medium`, `long`, `full`). Es una de las [constantes IntlDateFormatter](#intl.intldateformatter-constants).

`timeType`  
Formato de hora determinado por una de las [constantes de IntlDateFormatter](#intl.intldateformatter-constants). El valor por omisión es `IntlDateFormatter::FULL`.

`timezone`  
El identificador de la zona horaria. Por omisión, (esto también será el valor por omisión que se utilizará si se proporciona `null`) será el devuelto por la función `date_default_timezone_get` o, si es aplicable, el de objeto `IntlCalendar` pasado al argumento `calendar`. Este identificador debe ser un identificador válido en la base de datos ICU, o un identificador que represente una zona horaria explícita, como `GMT-05:30`.

Este argumento también puede ser un objeto `IntlTimeZone` o un objeto `DateTimeZone`.

`calendar`  
Calendario a utilizar para el formato o el análisis. El valor por omisión es `null`, lo que corresponde a la constante `IntlDateFormatter::GREGORIAN`. Puede ser una de las [constantes de calendario IntlDateFormatter](#intl.intldateformatter-constants.calendartypes) o un `IntlCalendar`. Cualquier objeto `IntlCalendar` pasado será clonado; no será modificado por `IntlDateFormatter`. Determinará el tipo de calendario utilizado (gregoriano, islámico, persa, etc.) y si `null` es proporcionado en el argumento `timezone`, la zona horaria también será utilizada.

`pattern`  
El patrón a utilizar para el formato o el análisis. Los patrones disponibles están documentados en <https://unicode-org.github.io/icu/userguide/format_parse/datetime/>.

## Valores devueltos

El objeto `IntlDateFormatter` creado, o `null` si ocurre un error.

## Errores/Excepciones

Se lanza una ValueError si `locale` es inválido.

## Historial de cambios

| Versión | Descripción                                                  |
|---------|--------------------------------------------------------------|
| 8.4.0   | Se lanza una ValueError si `locale` es inválido.             |
| 8.1.0   | Los argumentos `dateType` y `timeType` ahora son opcionales. |

## Ejemplos

Ejemplo con `datefmt_create`, procedimental

```
<?php
$fmt = datefmt_create( "en_US" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
    'America/Los_Angeles', IntlDateFormatter::GREGORIAN  );
echo "El primer formato mostrado es ".datefmt_format( $fmt , 0);
$fmt = datefmt_create( "de-DE" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
    'America/Los_Angeles',IntlDateFormatter::GREGORIAN  );
echo "El segundo formato mostrado es  ".datefmt_format( $fmt , 0);

$fmt = datefmt_create( "en_US" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
     'America/Los_Angeles',IntlDateFormatter::GREGORIAN  ,"MM/dd/yyyy");
echo "El primer formato se muestra con el patrón: ".datefmt_format( $fmt , 0);
$fmt = datefmt_create( "de-DE" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
     'America/Los_Angeles',IntlDateFormatter::GREGORIAN  ,"MM/dd/yyyy");
echo "El segundo formato se muestra con el patrón: ".datefmt_format( $fmt , 0);
?>

   
```php

Ejemplo con `datefmt_create`, POO

```
<?php
$fmt = new IntlDateFormatter( "en_US" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
    'America/Los_Angeles',IntlDateFormatter::GREGORIAN  );
echo "El primer formato mostrado es ".$fmt->format(0);
$fmt = new IntlDateFormatter( "de-DE" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
    'America/Los_Angeles',IntlDateFormatter::GREGORIAN  );
echo "El segundo formato mostrado es ".$fmt->format(0);

$fmt = new IntlDateFormatter( "en_US" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
     'America/Los_Angeles',IntlDateFormatter::GREGORIAN  ,"MM/dd/yyyy");
echo "El primer formato se muestra con el patrón: ".$fmt->format(0);
$fmt = new IntlDateFormatter( "de-DE" ,IntlDateFormatter::FULL, IntlDateFormatter::FULL,
      'America/Los_Angeles',IntlDateFormatter::GREGORIAN , "MM/dd/yyyy");
echo "El segundo formato se muestra con el patrón: ".$fmt->format(0);
?>

   
```php

Ejemplo de manejo de configuración local inválida

```
<?php
try {
    $fmt = new IntlDateFormatter(
        'locale_invalido',
        IntlDateFormatter::FULL,
        IntlDateFormatter::FULL,
        'je_ne_sais_pas',
        IntlDateFormatter::GREGORIAN,
    );
} catch (\Error $e) {
    // ...
}
?>

   
```php

El ejemplo anterior mostrará:

    El primer formato mostrado es Wednesday, December 31, 1969 4:00:00 PM PT
    El segundo formato mostrado es Mittwoch, 31. Dezember 1969 16:00 Uhr GMT-08:00
    El primer formato se muestra con el patrón: 12/31/1969
    El segundo formato se muestra con el patrón: 12/31/1969
             
      

## Véase también

`datefmt_format`, `datefmt_parse`, `datefmt_get_error_code`, `datefmt_get_error_message`
