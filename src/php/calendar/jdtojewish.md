---
title: jdtojewish
description: Convierte el número de días del calendario Juliano a fecha del calendario
  judío
source_url: https://www.php.net/manual/es/function.jdtojewish.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/calendar/functions/jdtojewish.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: calendar
translation_status: ready
translation_reviewed: true
translation_revision: 1ae151672
order: 6650
---

jdtojewish

Convierte el número de días del calendario Juliano a fecha del calendario judío

## Descripción

```php
jdtojewish(int $julian_day, [bool $hebrew], [int $flags]): string
```php

Convierte un número de días del calendario Juliano a calendario judío.

## Parámetros

`julian_day`  
Un número de día Juliano en forma de `int`.

`hebrew`  
Si el argumento `hebrew` está definido como `true`, el argumento `flags` se utiliza para el hebreo, formato de salida basado en una `string` codificada ISO-8859-8.

`flags`  
Una máscara a nivel de bits que puede consistir en `CAL_JEWISH_ADD_ALAFIM_GERESH`, `CAL_JEWISH_ADD_ALAFIM` y `CAL_JEWISH_ADD_GERESHAYIM`.

## Valores devueltos

La fecha judía, en forma de `string` "mes/día/año", o una `string` de fecha hebrea codificada ISO-8859-8, dependiendo del argumento `hebrew`.

## Ejemplos

Ejemplo con `jdtojewish`

```
<?php
$jd = gregoriantojd(10, 8, 2002);
echo jdtojewish($jd, true), PHP_EOL,
     jdtojewish($jd, true, CAL_JEWISH_ADD_GERESHAYIM), PHP_EOL,
     jdtojewish($jd, true, CAL_JEWISH_ADD_ALAFIM), PHP_EOL,
     jdtojewish($jd, true,CAL_JEWISH_ADD_ALAFIM_GERESH), PHP_EOL;
?>

    
```php

El ejemplo anterior mostrará:

    ב חשון התשסג
    ב' חשון התשס"ג
    ב חשון ה אלפים תשסג
    ב חשון ה'תשסג

## Véase también

`jewishtojd`, `cal_from_jd`
