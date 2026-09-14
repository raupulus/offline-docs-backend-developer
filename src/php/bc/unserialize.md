---
title: BcMath\Number::__unserialize
description: Deserializa un argumento de datos en un objeto BcMath\Number
source_url: https://www.php.net/manual/es/bcmath-number.unserialize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/bc/bcmath/number/unserialize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: bc
translation_status: ready
translation_reviewed: false
translation_revision: c7e83fbbb
order: 6190
---

BcMath\Number::\_\_unserialize

Deserializa un argumento de datos en un objeto BcMath\Number

## Descripción

```php
public BcMath\Number::__unserialize(array $data): void
```php

Deserializa un argumento de datos en un objeto `BcMath\Number`.

## Parámetros

`data`  
El argumento de datos serializado como un `array` asociativo.

## Errores/Excepciones

Este método lanza una ValueError si se pasan datos serializados inválidos.

## Véase también

BcMath\Number::\_\_construct

BcMath\Number::serialize
