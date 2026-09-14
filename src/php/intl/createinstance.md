---
title: IntlCalendar::createInstance
description: Crea un nuevo objeto IntlCalendar
source_url: https://www.php.net/manual/es/intlcalendar.createinstance.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/createinstance.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 40240
---

IntlCalendar::createInstance

Crea un nuevo objeto IntlCalendar

## Descripción

Estilo orientado a objetos

```php
public static IntlCalendar::createInstance([IntlTimeZone $timezone], [string $locale]): IntlCalendar
```php

Estilo procedimental

```php
intlcal_create_instance([IntlTimeZone $timezone], [string $locale]): IntlCalendar
```

Al proporcionar una zona horaria y una configuración local, este método crea un objeto `IntlCalendar`. Este método factoriel puede devolver una subclase de la clase `IntlCalendar`.

El calendario creado representará la instancia del tiempo en el momento en que fue creado, basado en el tiempo del sistema. Los campos pueden ser vaciados con el método `IntCalendar::clear` sin argumentos. Ver también el método `IntlGregorianCalendar::__construct`.

## Parámetros

`timezone`  
La zona horaria a utilizar.

`locale`  
Una configuración local a utilizar, o `null` para utilizar la [configuración local por defecto](#ini.intl.default-locale).

## Valores devueltos

La instancia del objeto `IntlCalendar` creado, o `null` si ocurre un error.

## Ejemplos

Ejemplo con `IntlCalendar::createInstance`

```php
<?php
ini_set('intl.default_locale', 'es_ES');
ini_set('date.timezone', 'Europe/Madrid');

$cal = IntlCalendar::createInstance();
echo "Sin argumentos\n";
var_dump(get_class($cal),
        IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL));
echo "\n";

echo "Zona horaria explícita\n";
$cal = IntlCalendar::createInstance(IntlTimeZone::getGMT());
var_dump(get_class($cal),
        IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL));
echo "\n";

echo "Configuración local explícita (con el calendario)\n";
$cal = IntlCalendar::createInstance(NULL, 'es_ES@calendar=persian');
var_dump(get_class($cal),
        IntlDateFormatter::formatObject($cal, IntlDateFormatter::FULL));

    
```

El ejemplo anterior mostrará:

    Sin argumentos
    string(21) "IntlGregorianCalendar"
    string(68) "martes 18 de junio de 2013 14:11:02 Hora de verano de Europa Central"

    Zona horaria explícita
    string(21) "IntlGregorianCalendar"
    string(45) "martes 18 de junio de 2013 12:11:02 GMT+00:00"

    Configuración local explícita (con el calendario)
    string(12) "IntlCalendar"
    string(70) "martes 28 de Khordad de 1392 14:11:02 Hora de verano de Europa Central"

## Véase también

IntlGregorianCalendar::\_\_construct
