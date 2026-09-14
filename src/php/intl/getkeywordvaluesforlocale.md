---
title: IntlCalendar::getKeywordValuesForLocale
description: Devuelve el conjunto de valores de palabras clave de configuración regional
source_url: https://www.php.net/manual/es/intlcalendar.getkeywordvaluesforlocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/intlcalendar/getkeywordvaluesforlocale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 330a38c4d
order: 40370
---

IntlCalendar::getKeywordValuesForLocale

Devuelve el conjunto de valores de palabras clave de configuración regional

## Descripción

Estilo orientado a objetos

```php
public static IntlCalendar::getKeywordValuesForLocale(string $keyword, string $locale, bool $onlyCommon): IntlIterator
```php

Estilo procedimental

```php
intlcal_get_keyword_values_for_locale(string $keyword, string $locale, bool $onlyCommon): IntlIterator
```

Para una clave de configuración regional dada, devuelve el conjunto de valores para esta clave que producirían un comportamiento diferente. Por el momento, solo la palabra clave `'calendar'` es soportada.

Esta función requiere ICU 4.2 o posterior.

## Parámetros

`keyword`  
La palabra clave de configuración regional para la cual deben consultarse los valores pertinentes. Solo `'calendar'` es soportado.

`locale`  
La configuración regional sobre la cual debe añadirse el par palabra clave/valor.

`onlyCommon`  
Indica si deben mostrarse únicamente los valores comúnmente utilizados para la configuración regional especificada.

## Valores devueltos

Un iterador que devuelve strings con los valores de palabra clave de configuración regional o `false` si ocurre un error.

## Ejemplos

`IntlCalendar::getKeywordValuesForLocale`

```php
<?php
print_r(
        iterator_to_array(
                IntlCalendar::getKeywordValuesForLocale(
                        'calendar', 'fa_IR', true)));
print_r(
        iterator_to_array(
                IntlCalendar::getKeywordValuesForLocale(
                        'calendar', 'fa_IR', false)));

    
```

El ejemplo anterior mostrará:

    Array
    (
        [0] => persian
        [1] => gregorian
        [2] => islamic
        [3] => islamic-civil
    )
    Array
    (
        [0] => persian
        [1] => gregorian
        [2] => islamic
        [3] => islamic-civil
        [4] => japanese
        [5] => buddhist
        [6] => roc
        [7] => hebrew
        [8] => chinese
        [9] => indian
        [10] => coptic
        [11] => ethiopic
        [12] => ethiopic-amete-alem
    )
