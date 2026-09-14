---
title: SolrDisMaxQuery::setBoostQuery
description: Define directamente el parámetro de consulta de boost (bq)
source_url: https://www.php.net/manual/es/solrdismaxquery.setboostquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setboostquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77680
---

SolrDisMaxQuery::setBoostQuery

Define directamente el parámetro de consulta de boost (bq)

## Descripción

```php
public SolrDisMaxQuery::setBoostQuery(string $q): SolrDisMaxQuery
```php

Define el parámetro de consulta de boost (bq)

## Parámetros

`q`  
consulta

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setBoostQuery`

```
<?php
$dismaxQuery = new SolrDisMaxQuery("lucene");

$dismaxQuery->setBoostQuery('cat:electronics manu:local^2');
echo $dismaxQuery.PHP_EOL;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&bq=cat:electronics manu:local^2

## Véase también

SolrDisMaxQuery::addBoostQuery

SolrDisMaxQuery::removeBoostQuery
