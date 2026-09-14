---
title: SensitiveParameterValue::getValue
description: Devuelve el valor sensible
source_url: https://www.php.net/manual/es/sensitiveparametervalue.getvalue.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/sensitiveparametervalue/getvalue.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: dfb5ffae0
order: 3880
---

SensitiveParameterValue::getValue

Devuelve el valor sensible

## Descripción

```php
public SensitiveParameterValue::getValue(): mixed
```php

Devuelve el valor sensible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El valor sensible.

## Ejemplos

Ejemplo de `SensitiveParameterValue::getValue`

```
<?php
$s = new \SensitiveParameterValue('secret');

echo "El valor protegido es: ", $s->getValue(), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    El valor protegido es: secret
