---
title: SolrDisMaxQuery::removeBoostQuery
description: Elimina una parte de consulta de boost por nombre de campo (bq)
source_url: https://www.php.net/manual/es/solrdismaxquery.removeboostquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/removeboostquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77600
---

SolrDisMaxQuery::removeBoostQuery

Elimina una parte de consulta de boost por nombre de campo (bq)

## Descripción

```php
public SolrDisMaxQuery::removeBoostQuery(string $field): SolrDisMaxQuery
```php

Elimina una parte de consulta de boost por nombre de campo, solo si SolrDisMaxQuery::addBoostQuery ha sido utilizado.

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::removeBoostQuery`

```
<?php

$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery
    ->addBoostQuery('cat', 'electronics', 5.1)
    ->addBoostQuery('cat', 'hard drive')
;
echo $dismaxQuery.PHP_EOL;
// elimina la parte de consulta de boost con el campo 'cat'
$dismaxQuery
->removeBoostQuery('cat');
echo $dismaxQuery . PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&bq=cat:electronics^5.1 cat:hard drive
    q=lucene&defType=edismax&bq=cat:hard drive

## Véase también

SolrDisMaxQuery::addBoostQuery

SolrDisMaxQuery::setBoostQuery
