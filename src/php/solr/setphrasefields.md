---
title: SolrDisMaxQuery::setPhraseFields
description: Define los campos de frase y sus boosts (y slops) utilizando el parámetro
  pf2
source_url: https://www.php.net/manual/es/solrdismaxquery.setphrasefields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setphrasefields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77700
---

SolrDisMaxQuery::setPhraseFields

Define los campos de frase y sus boosts (y slops) utilizando el parámetro pf2

## Descripción

```php
public SolrDisMaxQuery::setPhraseFields(string $fields): SolrDisMaxQuery
```php

Define los campos de frase (pf) y sus boosts (y slops)

## Parámetros

`fields`  
Los campos, los boosts \[, slops\]

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setPhraseFields`

```
<?php
$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery->setPhraseFields("cat~5.1^2 feature^4.5");
echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&pf=cat~5.1^2 feature^4.5

## Véase también

SolrDisMaxQuery::addPhraseFields

SolrDisMaxQuery::removePhraseField
