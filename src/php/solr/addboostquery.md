---
title: SolrDisMaxQuery::addBoostQuery
description: Añade un campo de consulta de boost con valor y boost opcionales (argumento
  bq)
source_url: https://www.php.net/manual/es/solrdismaxquery.addboostquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/addboostquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77530
---

SolrDisMaxQuery::addBoostQuery

Añade un campo de consulta de boost con valor y boost opcionales (argumento bq)

## Descripción

```php
public SolrDisMaxQuery::addBoostQuery(string $field, string $value, [string $boost]): SolrDisMaxQuery
```php

Añade un campo de consulta de boost con valor \[y boost\] (argumento bq)

## Parámetros

`field`  

`value`  

`boost`  

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::addBoostQuery`

```
<?php

$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery
    ->addBoostQuery('cat', 'clothing', 2)
    ->addBoostQuery('cat', 'electronics', 5.1)
;
echo $dismaxQuery.PHP_EOL;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&bq=cat:clothing^2 cat:electronics^5.1

## Véase también

SolrDisMaxQuery::removeBoostQuery

SolrDisMaxQuery::setBoostQuery
