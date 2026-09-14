---
title: SolrDocument::valid
description: Comprueba si la posición actual del puntero interno es aún válida
source_url: https://www.php.net/manual/es/solrdocument.valid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/valid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78130
---

SolrDocument::valid

Comprueba si la posición actual del puntero interno es aún válida

## Descripción

```php
public SolrDocument::valid(): bool
```php

Comprueba si la posición actual del puntero interno es aún válida. Se usa durante operaciones foreach.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` en caso de éxito y `false` si la posición actual ya no es válida.
