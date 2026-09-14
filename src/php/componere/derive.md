---
title: Componere\Patch::derive
description: Derivación del parche
source_url: https://www.php.net/manual/es/componere-patch.derive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/componere/componere/patch/derive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: componere
translation_status: ready
translation_revision: 6dcc757d9
order: 8220
---

Componere\Patch::derive

Derivación del parche

## Descripción

```php
public Componere\Patch::derive(object $instance): Patch
```php

Derivará un `Patch` (parche) para la `instance` (instancia) dada

## Parámetros

`instance`  
El objetivo del Parche derivado

## Valores devueltos

`Patch` (parche) para la `instance` (instancia) derivada del `Patch` (parche) actual

## Excepciones

> [!WARNING]
> Lanzará `InvalidArgumentException` si `instance` no es compatible
