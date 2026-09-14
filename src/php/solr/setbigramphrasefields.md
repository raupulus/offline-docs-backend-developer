---
title: SolrDisMaxQuery::setBigramPhraseFields
description: Define los campos de frase bigrama y sus boosts (y márgenes) utilizando
  el argumento pf2
source_url: https://www.php.net/manual/es/solrdismaxquery.setbigramphrasefields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setbigramphrasefields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77650
---

SolrDisMaxQuery::setBigramPhraseFields

Define los campos de frase bigrama y sus boosts (y márgenes) utilizando el argumento pf2

## Descripción

```php
public SolrDisMaxQuery::setBigramPhraseFields(string $fields): SolrDisMaxQuery
```php

Define los campos de frase bigrama (pf2) y sus boosts (y márgenes)

## Parámetros

`fields`  
Los boosts de campos (los márgenes)

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setBigramPhraseFields`

```
<?php
$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery->setBigramPhraseFields("cat~5.1^2 feature^4.5");
echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&pf2=cat~5.1^2 feature^4.5

## Véase también

SolrDisMaxQuery::setBigramPhraseSlop

SolrDisMaxQuery::addBigramPhraseFields

SolrDisMaxQuery::removeBigramPhraseField

SolrDisMaxQuery::setTrigramPhraseFields
