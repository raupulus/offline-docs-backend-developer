---
title: WeakReference::create
description: Crea una nueva referencia débil
source_url: https://www.php.net/manual/es/weakreference.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/weakreference/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 430a41f57
order: 4340
---

WeakReference::create

Crea una nueva referencia débil

## Descripción

```php
public static WeakReference::create(object $object): WeakReference
```php

Crea una nueva `WeakReference`.

## Parámetros

`object`  
El objeto a ser referenciado débilmente.

## Valores devueltos

Devuelve una nueva `WeakReference`, o la instancia existente si ya había una `WeakReference` al mismo objeto.
