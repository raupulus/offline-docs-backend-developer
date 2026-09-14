---
title: SolrQuery::addGroupSortField
description: Añade un campo de ordenación de grupo (argumento group.sort)
source_url: https://www.php.net/manual/es/solrquery.addgroupsortfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addgroupsortfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: be295015d
order: 78900
---

SolrQuery::addGroupSortField

Añade un campo de ordenación de grupo (argumento group.sort)

## Descripción

```php
public SolrQuery::addGroupSortField(string $field, [int $order]): SolrQuery
```php

Permite ordenar los documentos de grupo, utilizando el campo de ordenación de grupo (argumento group.sort).

## Parámetros

`field`  
El nombre del campo

`order`  
Orden ASC/DESC, utiliza las constantes SolrQuery::ORDER\_\*.

## Valores devueltos

## Ejemplos

Ejemplo de `SolrQuery::addGroupSortField`

```
<?php

$solrQuery = new SolrQuery('*:*');
$solrQuery
    ->setGroup(true)
    ->addGroupSortField('price', SolrQuery::ORDER_ASC);

echo $solrQuery;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=*:*&group=true&group.sort=price asc

## Véase también

SolrQuery::setGroup

SolrQuery::addGroupField

SolrQuery::addGroupFunction

SolrQuery::addGroupQuery

SolrQuery::setGroupFacet

SolrQuery::setGroupOffset

SolrQuery::setGroupLimit

SolrQuery::setGroupMain

SolrQuery::setGroupNGroups

SolrQuery::setGroupTruncate

SolrQuery::setGroupFormat

SolrQuery::setGroupCachePercent
