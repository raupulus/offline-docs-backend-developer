---
title: SolrDisMaxQuery::addQueryField
description: Añade un campo de consulta con boost opcional (argumento qf)
source_url: https://www.php.net/manual/es/solrdismaxquery.addqueryfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/addqueryfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77550
---

SolrDisMaxQuery::addQueryField

Añade un campo de consulta con boost opcional (argumento qf)

## Descripción

```php
public SolrDisMaxQuery::addQueryField(string $field, [string $boost]): SolrDisMaxQuery
```php

Añade un campo de consulta con boost opcional (argumento qf)

## Parámetros

`field`  
El nombre del campo

`boost`  
El boost opcional. Aumenta la relevancia de los documentos con términos coincidentes.

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::addQueryField`

```
<?php

$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery
    ->addQueryField("location", 4)
    ->addQueryField("price")
    ->addQueryField("sku")
    ->addQueryField("title",3.4)
;
echo $dismaxQuery;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&qf=location^4 price sku title^3.4

## Véase también

SolrDisMaxQuery::removeQueryField
