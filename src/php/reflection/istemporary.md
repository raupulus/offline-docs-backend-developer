---
title: ReflectionExtension::isTemporary
description: Verifica si la extensión es temporal
source_url: https://www.php.net/manual/es/reflectionextension.istemporary.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/istemporary.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ca840c9a6
order: 70280
---

ReflectionExtension::isTemporary

Verifica si la extensión es temporal

## Descripción

```php
public ReflectionExtension::isTemporary(): bool
```php

Verifica si la extensión es temporal.

Una extensión es temporal si es cargada con `dl`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` para las extensiones cargadas por la función `dl`, `false` en caso contrario.

## Véase también

ReflectionExtension::isPersistent
