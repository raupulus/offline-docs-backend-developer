---
title: Swoole\Atomic::cmpset
description: Compara y define el valor del objeto atómico.
source_url: https://www.php.net/manual/es/swoole-atomic.cmpset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/swoole/swoole/atomic/cmpset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: swoole
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 90760
---

Swoole\Atomic::cmpset

Compara y define el valor del objeto atómico.

## Descripción

```php
public Swoole\Atomic::cmpset(int $cmp_value, int $new_value): int
```php

## Parámetros

`cmp_value`  
El valor a comparar con el valor actual del objeto atómico.

`new_value`  
El valor a definir en el objeto atómico si el valor de cmp_value es el mismo que el valor actual del objeto atómico.

## Valores devueltos

El nuevo valor del objeto atómico.
