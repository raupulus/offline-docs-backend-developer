---
title: SolrDisMaxQuery::addBigramPhraseField
description: Añade un campo de bigrama de frase (argumento pf2)
source_url: https://www.php.net/manual/es/solrdismaxquery.addbigramphrasefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/addbigramphrasefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77520
---

SolrDisMaxQuery::addBigramPhraseField

Añade un campo de bigrama de frase (argumento pf2)

## Descripción

```php
public SolrDisMaxQuery::addBigramPhraseField(string $field, string $boost, [string $slop]): SolrDisMaxQuery
```php

Añade un campo de bigrama de frase (argumento pf2) Formato de salida: campo~slop^boost OU campo^boost Slop es opcional

## Parámetros

`field`  

`boost`  

`slop`  

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::addBigramPhraseField`

```
<?php

$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery
    ->addBigramPhraseField('cat', 2, 5.1)
    ->addBigramPhraseField('feature', 4.5)
;
echo $dismaxQuery;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&pf2=cat~5.1^2 feature^4.5

## Véase también

SolrDisMaxQuery::removeBigramPhraseField

SolrDisMaxQuery::setBigramPhraseFields

SolrDisMaxQuery::setBigramPhraseSlop
