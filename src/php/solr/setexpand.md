---
title: SolrQuery::setExpand
description: Activa/desactiva el componente Expand
source_url: https://www.php.net/manual/es/solrquery.setexpand.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setexpand.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 418e95fc8
order: 80020
---

SolrQuery::setExpand

Activa/desactiva el componente Expand

## Descripción

```php
public SolrQuery::setExpand(bool $value): SolrQuery
```php

Activa/desactiva el componente Expand.

## Parámetros

`value`  
Un flag booleano

## Valores devueltos

`SolrQuery`

## Ejemplos

Ejemplo de `SolrQuery::setExpand`

```
<?php

$query = new SolrQuery('lucene');

$query
    ->setExpand(true)
    ->setExpandRows(50)
    ->setExpandQuery('text:product')
    ->addExpandFilterQuery('manu:apple')
    ->addExpandFilterQuery('inStock:true')
    ->addExpandSortField('score', SolrQuery::ORDER_DESC)
    ->addExpandSortField('title', SolrQuery::ORDER_ASC);

echo $query.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&expand=true&expand.rows=50&expand.q=text:product&expand.fq=manu:apple&expand.fq=inStock:true&expand.sort=score desc,title asc

## Véase también

SolrQuery::addExpandSortField

SolrQuery::removeExpandSortField

SolrQuery::setExpandRows

SolrQuery::setExpandQuery

SolrQuery::addExpandFilterQuery

SolrQuery::removeExpandFilterQuery
