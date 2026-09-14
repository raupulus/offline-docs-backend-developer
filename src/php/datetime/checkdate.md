---
title: checkdate
description: Valida una fecha gregoriana
source_url: https://www.php.net/manual/es/function.checkdate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/checkdate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_reviewed: false
translation_revision: 3a8c3e77d
order: 10940
---

checkdate

Valida una fecha gregoriana

## Descripción

```php
checkdate(int $month, int $day, int $year): bool
```php

Comprueba la validez de una fecha formada por los argumentos. Una fecha se considera válida si cada parámetro está propiamente definido.

## Parámetros

`month`  
El mes entre 1 y 12 inclusive.

`day`  
El día que está dentro del número de días del mes `month` dado. Los años `year` bisiestos son tomados en consideración.

`year`  
El año entre 1 y 32767 inclusive.

## Valores devueltos

Devuelve `true` si la fecha dada es válida, si no, devuelve `false`.

## Ejemplos

Ejemplo de `checkdate`

```
<?php
var_dump(checkdate(12, 31, 2000));
var_dump(checkdate(2, 29, 2001));

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Véase también

`mktime`, `strtotime`
