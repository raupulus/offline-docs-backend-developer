---
title: libxml_get_external_entity_loader
description: Devuelve el cargador de entidades externas actual
source_url: https://www.php.net/manual/es/function.libxml-get-external-entity-loader.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/functions/libxml-get-external-entity-loader.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: true
translation_revision: dea05ca00
order: 43680
---

libxml_get_external_entity_loader

Devuelve el cargador de entidades externas actual

## Descripción

```php
libxml_get_external_entity_loader(): callable
```php

Devuelve el cargador de entidades externas definido previamente por `libxml_set_external_entity_loader`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

El cargador de entidades externas definido previamente por `libxml_set_external_entity_loader`. Si esta función nunca ha sido llamada, o si fue llamada con `null`, se devolverá `null`.

## Véase también

libxml_set_external_entity_loader
