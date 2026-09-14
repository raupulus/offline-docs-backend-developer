---
title: SolrServerException::getInternalInfo
description: Devuelve información interna de dónde fue lanzada la excepción
source_url: https://www.php.net/manual/es/solrserverexception.getinternalinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrserverexception/getinternalinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: e9366ee45
order: 80900
---

SolrServerException::getInternalInfo

Devuelve información interna de dónde fue lanzada la excepción

## Descripción

```php
public SolrServerException::getInternalInfo(): array
```php

Devuelve información interna de dónde fue lanzada la excepción.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un array que contiene información interna de dónde se lanzó la excepción. Utilizado solamente con propósitos de depuración para desarrolladores de extensiones.
