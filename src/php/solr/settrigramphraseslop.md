---
title: SolrDisMaxQuery::setTrigramPhraseSlop
description: Define el margen de trigramas de frase (parámetro ps3)
source_url: https://www.php.net/manual/es/solrdismaxquery.settrigramphraseslop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/settrigramphraseslop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77760
---

SolrDisMaxQuery::setTrigramPhraseSlop

Define el margen de trigramas de frase (parámetro ps3)

## Descripción

```php
public SolrDisMaxQuery::setTrigramPhraseSlop(string $slop): SolrDisMaxQuery
```php

Define el margen de trigramas de frase (parámetro ps3)

## Parámetros

`slop`  
El margen de frase

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setTrigramPhraseSlop`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery->setTrigramPhraseSlop(2);
echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&ps3=2

## Véase también

SolrDisMaxQuery::addTrigramPhraseField

SolrDisMaxQuery::removeTrigramPhraseField

SolrDisMaxQuery::setTrigramPhraseFields
