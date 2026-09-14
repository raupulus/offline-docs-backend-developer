---
title: SolrDisMaxQuery::addUserField
description: Añade un campo al parámetro de campo usuario (uf)
source_url: https://www.php.net/manual/es/solrdismaxquery.adduserfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/adduserfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77570
---

SolrDisMaxQuery::addUserField

Añade un campo al parámetro de campo usuario (uf)

## Descripción

```php
public SolrDisMaxQuery::addUserField(string $field): SolrDisMaxQuery
```php

Añade un campo al parámetro de campo usuario (uf)

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::addUserField`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery
->addUserField('cat')
->addUserField('text')
->addUserField('*_dt');

echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&uf=cat text *_dt

## Véase también

SolrDisMaxQuery::removeUserField

SolrDisMaxQuery::setUserFields
