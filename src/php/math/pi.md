---
title: pi
description: Devuelve el valor de pi
source_url: https://www.php.net/manual/es/function.pi.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/pi.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: true
translation_revision: 761d72245
order: 44820
---

pi

Devuelve el valor de pi

## Descripción

```php
pi(): float
```php

Devuelve una aproximación de pi. Asimismo, puede utilizarse la constante `M_PI`, que devuelve un resultado idéntico a la función `pi`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor de pi como `float`.

## Ejemplos

Ejemplo con `pi`

```
<?php
echo pi(), PHP_EOL; // 3.1415926535898
echo M_PI, PHP_EOL; // 3.1415926535898
?>

    
```php
