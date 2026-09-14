---
title: SolrDisMaxQuery::setTrigramPhraseFields
description: Define directamente los campos de trigramas de frase (argumento pf3)
source_url: https://www.php.net/manual/es/solrdismaxquery.settrigramphrasefields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/settrigramphrasefields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77750
---

SolrDisMaxQuery::setTrigramPhraseFields

Define directamente los campos de trigramas de frase (argumento pf3)

## Descripción

```php
public SolrDisMaxQuery::setTrigramPhraseFields(string $fields): SolrDisMaxQuery
```php

Define directamente los campos de trigramas de frase (argumento pf3)

## Parámetros

`fields`  
Los campos de trigramas de frase

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setTrigramPhraseFields`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery->setTrigramPhraseFields('cat~5.1^2 feature^4.5');
echo $dismaxQuery.PHP_EOL;

?>

   
```php

El ejemplo anterior mostrará:

    q=lucene&defType=edismax&pf3=cat~5.1^2 feature^4.5

## Véase también

SolrDisMaxQuery::addTrigramPhraseField

SolrDisMaxQuery::removeTrigramPhraseField

SolrDisMaxQuery::setTrigramPhraseSlop
