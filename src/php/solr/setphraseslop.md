---
title: SolrDisMaxQuery::setPhraseSlop
description: Define el margen por defecto en las consultas de frase (parámetro ps)
source_url: https://www.php.net/manual/es/solrdismaxquery.setphraseslop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setphraseslop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: a56de5a30
order: 77710
---

SolrDisMaxQuery::setPhraseSlop

Define el margen por defecto en las consultas de frase (parámetro ps)

## Descripción

```php
public SolrDisMaxQuery::setPhraseSlop(string $slop): SolrDisMaxQuery
```php

Define el margen por defecto en las consultas de frase construidas con los campos "pf", "pf2" y/o "pf3" (afecta al boosting). parámetro "ps"

## Parámetros

`slop`  

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setPhraseSlop`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');

$dismaxQuery->setPhraseSlop(4);
echo $dismaxQuery.PHP_EOL;

?>

   
```php

El ejemplo anterior mostrará:

    q=lucene&defType=edismax&ps=4
