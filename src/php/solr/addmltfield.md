---
title: SolrQuery::addMltField
description: Establece un campo para usarlo para similitud
source_url: https://www.php.net/manual/es/solrquery.addmltfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addmltfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 78920
---

SolrQuery::addMltField

Establece un campo para usarlo para similitud

## Descripción

```php
public SolrQuery::addMltField(string $field): SolrQuery
```php

Mapea a mlt.fl. Especifica que un campo debería ser usado para similitud.

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usa el valor de retorno.
