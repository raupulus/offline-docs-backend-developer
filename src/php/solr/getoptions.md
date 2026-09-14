---
title: SolrClient::getOptions
description: Devuelve las opciones de cliente establecidas internamente
source_url: https://www.php.net/manual/es/solrclient.getoptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/getoptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 77240
---

SolrClient::getOptions

Devuelve las opciones de cliente establecidas internamente

## Descripción

```php
public SolrClient::getOptions(): array
```php

Devuelve las opciones de cliente establecidas internamente. Muy útil para depurar. Los valores devueltos son de sólo lectura y sólo se pueden establecer cuando el objeto es instanciado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una matriz que contiene todas las opciones para el objeto SolrClient establecido internamente.

## Véase también

SolrClient::\_\_construct
