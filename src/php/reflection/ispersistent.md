---
title: ReflectionExtension::isPersistent
description: Verifica si la extensión es persistente
source_url: https://www.php.net/manual/es/reflectionextension.ispersistent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/reflection/reflectionextension/ispersistent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: reflection
translation_status: ready
translation_reviewed: false
translation_revision: ca840c9a6
order: 70270
---

ReflectionExtension::isPersistent

Verifica si la extensión es persistente

## Descripción

```php
public ReflectionExtension::isPersistent(): bool
```php

Verifica si la extensión es persistente.

Una extensión es persistente cuando es cargada utilizando `php.ini`. Una extensión es temporal, no persistente, cuando es cargada con `dl`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` para las extensiones cargadas por el mecanismo de [`extensions`](#ini.extension), `false` en caso contrario.

## Véase también

ReflectionExtension::isTemporary
