---
title: IntlCalendar::getAvailableLocales
description: Devuelve un array de locales para los cuales hay datos disponibles
source_url: https://www.php.net/manual/es/intlcalendar.getavailablelocales.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getavailablelocales.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: dfd68fd22
order: 40310
---

IntlCalendar::getAvailableLocales

Devuelve un array de locales para los cuales hay datos disponibles

## Descripción

Estilo orientado a objetos

```php
public static IntlCalendar::getAvailableLocales(): array
```php

Estilo procedimental

```php
intlcal_get_available_locales(): array
```

Proporciona la lista de locales para los cuales están instalados los calendarios. A partir de ICU 51, es la lista de todos los locales ICU instalados.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` de `string`, uno para cada locale.

## Ejemplos

`IntlCalendar::getAvailableLocales`

```php
<?php
print_r(IntlCalendar::getAvailableLocales());

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => af
        [1] => af_NA
        [2] => af_ZA
        [3] => agq
        [4] => agq_CM
        [5] => ak
        [6] => ak_GH
        [7] => am
        [8] => am_ET
        [9] => ar
        [10] => ar_001
        [11] => ar_AE
        [12] => ar_BH
        [13] => ar_DJ
        … output abbreviated …
        [595] => zh_Hant_HK
        [596] => zh_Hant_MO
        [597] => zh_Hant_TW
        [598] => zu
        [599] => zu_ZA
    )
