---
title: IntlDateFormatter::formatObject
description: Formatea un objeto
source_url: https://www.php.net/manual/es/intldateformatter.formatobject.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/dateformatter/formatobject.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39560
---

IntlDateFormatter::formatObject

datefmt_format_object

Formatea un objeto

## Descripción

Estilo orientado a objetos

```php
public static IntlDateFormatter::formatObject(IntlCalendar $datetime, [array $format], [string $locale]): string
```php

Estilo procedimental

```php
datefmt_format_object(IntlCalendar $datetime, [array $format], [string $locale]): string
```

Esta función permite el formato de un objeto `IntlCalendar` o de un objeto `DateTime` sin haber creado previamente un objeto `IntlDateFormatter`.

El objeto `IntlDateFormatter` temporal creado tomará el desplazamiento horario desde el objeto pasado. La base de datos de desplazamientos horarios interna a PHP no será utilizada - ICU será utilizado en su lugar. El identificador de desplazamiento horario utilizado en los objetos `DateTime` debe existir también en la base de datos ICU.

## Parámetros

`datetime`  
Un objeto de tipo `IntlCalendar` o de tipo `DateTime`. La información de desplazamiento horario en el objeto será utilizada.

`format`  
Formato de la fecha/hora. Puede ser un array con dos elementos (primero el estilo de la fecha, luego el estilo de la hora, utilizando una de las constantes siguientes: `IntlDateFormatter::NONE`, `IntlDateFormatter::SHORT`, `IntlDateFormatter::MEDIUM`, `IntlDateFormatter::LONG`, `IntlDateFormatter::FULL`), un tipo `int` con el valor de una de estas constantes (en cuyo caso, será utilizado tanto para la fecha como para la hora), o un tipo `string` con el formato descrito en la [documentación ICU](https://unicode-org.github.io/icu/userguide/format_parse/datetime/#datetime-format-syntax). Si `null` es proporcionado, el estilo por defecto será utilizado.

`locale`  
La configuración local a utilizar, o `null` para utilizar la [configuración local por defecto](#ini.intl.default-locale).

## Valores devueltos

Una cadena de caracteres que contiene el resultado o `false` si ocurre un error.

## Ejemplos

Ejemplo con `IntlDateFormatter::formatObject`

```php
<?php
/* El desplazamiento horario por defecto no es significativo;
   se toma desde el objeto */
ini_set('date.timezone', 'UTC');

/* La configuración local por defecto se toma desde la configuración ini */
ini_set('intl.default_locale', 'fr_FR');

$cal = IntlCalendar::fromDateTime("2013-06-06 17:05:06 Europe/Dublin");
echo "défault :\n\t",
        IntlDateFormatter::formatObject($cal),
        "\n";

echo "long \$format (complet) :\n\t",
        IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL),
        "\n";

echo "array \$format (ninguno, complet) :\n\t",
        IntlDateFormatter::formatObject($cal, array(
                IntlDateFormatter::NONE,
                IntlDateFormatter::FULL)),
        "\n";

echo "string \$format (d 'de' MMMM y):\n\t",
        IntlDateFormatter::formatObject($cal, "d 'de' MMMM y", 'en_US'),
        "\n";

echo "con DateTime :\n\t",
        IntlDateFormatter::formatObject(
                new DateTime("2013-09-09 09:09:09 Europe/Madrid"),
                IntlDateFormatter::FULL,
                'es_ES'),
        "\n";

    
```

El ejemplo anterior mostrará:

    défault :
        6 junio 2013 17:05:06
    long $format (complet):
        jueves 6 junio 2013 17:05:06 hora de verano irlandesa
    array $format (ninguno, complet):
        17:05:06 hora de verano irlandesa
    string $format (d 'de' MMMM y):
        6 de June 2013
    con DateTime :
        lunes, 9 de septiembre de 2013 09:09:09 Hora de verano de Europa central
