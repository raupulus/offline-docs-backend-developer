---
title: SolrQuery::__construct
description: Constructor
source_url: https://www.php.net/manual/es/solrquery.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: ecaa21464
order: 78980
---

SolrQuery::\_\_construct

Constructor

## Descripción

```php
public SolrQuery::__construct([string $q])
```php

Constructor.

## Parámetros

`q`  
Consulta de búsqueda opcional

## Valores devueltos

Ninguno.

## Errores/Excepciones

Emite una `SolrIllegalArgumentException` en caso de proporcionar un parámetro no válido.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL solr 2.0.0 | Si `q` fuera inválido, se lanza una `SolrIllegalArgumentException`. Anteriormente se emitía un error. |
