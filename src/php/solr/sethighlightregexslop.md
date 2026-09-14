---
title: SolrQuery::setHighlightRegexSlop
description: Establece el factor por el cual el fragmentador de expresiones regulares
  puede desviarse del tamaño de fragmento ideal
source_url: https://www.php.net/manual/es/solrquery.sethighlightregexslop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightregexslop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: f713e4664
order: 80400
---

SolrQuery::setHighlightRegexSlop

Establece el factor por el cual el fragmentador de expresiones regulares puede desviarse del tamaño de fragmento ideal

## Descripción

```php
public SolrQuery::setHighlightRegexSlop(float $factor): SolrQuery
```php

El factor por el cual el fragmentador de expresiones regulares puede desviarse del tamaño de fragmento ideal (especificado por SolrQuery::setHighlightFragsize) para acomodar la expresión regular

## Parámetros

`factor`  
El factor por el cual el fragmentador de expresiones regulares puede desviarse del tamaño de fragmento ideal

## Valores devueltos

Devuelve el objeto SolrQuery actual si se usó el valor de retorno.
