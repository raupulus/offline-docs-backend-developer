---
title: WeakReference::get
description: Obtiene un objeto débilmente referenciado
source_url: https://www.php.net/manual/es/weakreference.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/weakreference/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: d27fdfe8f
order: 4350
---

WeakReference::get

Obtiene un objeto débilmente referenciado

## Descripción

```php
public WeakReference::get(): object
```php

Se obtiene un objeto débilmente referenciado. Si el objeto ya ha sido destruido, devuelve `null`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el referenciado `object`, o `null` si el objeto ha sido destruido.
