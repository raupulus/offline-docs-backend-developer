---
title: SolrException::getInternalInfo
description: Devuelve información interna de donde se lanzó la excepción
source_url: https://www.php.net/manual/es/solrexception.getinternalinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrexception/getinternalinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78180
---

SolrException::getInternalInfo

Devuelve información interna de donde se lanzó la excepción

## Descripción

```php
public SolrException::getInternalInfo(): array
```php

Devuelve información interna de donde se lanzó la excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una matriz que contiene información interna de donde el error fue lanzado. Usado únicamente para depurar por desarrolladores de extensiones.
