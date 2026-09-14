---
title: SensitiveParameterValue::__debugInfo
description: Protege el valor sensible contra una exposición accidental
source_url: https://www.php.net/manual/es/sensitiveparametervalue.debuginfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/sensitiveparametervalue/debuginfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 47f7daf79
order: 3870
---

SensitiveParameterValue::\_\_debugInfo

Protege el valor sensible contra una exposición accidental

## Descripción

```php
public SensitiveParameterValue::__debugInfo(): array
```php

Devuelve un `array` vacío para proteger el valor sensible contra una exposición accidental al utilizar `var_dump`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` vacío.

## Ejemplos

Pasar un objeto `SensitiveParameterValue` a `var_dump`

```
<?php
$s = new \SensitiveParameterValue('secret');

var_dump($s);
?>

    
```php

El ejemplo anterior mostrará:

    object(SensitiveParameterValue)#1 (0) {
    }
