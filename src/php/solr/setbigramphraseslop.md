---
title: SolrDisMaxQuery::setBigramPhraseSlop
description: Define el margen de Bigram Phrase (parámetro ps2)
source_url: https://www.php.net/manual/es/solrdismaxquery.setbigramphraseslop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setbigramphraseslop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: a56de5a30
order: 77660
---

SolrDisMaxQuery::setBigramPhraseSlop

Define el margen de Bigram Phrase (parámetro ps2)

## Descripción

```php
public SolrDisMaxQuery::setBigramPhraseSlop(string $slop): SolrDisMaxQuery
```php

Define el margen de Bigram Phrase (parámetro ps2). Un margen por omisión para los campos de frase Bigram.

## Parámetros

`slop`  

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setBigramPhraseSlop`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');

$dismaxQuery->setBigramPhraseSlop(5);
echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&ps2=5
