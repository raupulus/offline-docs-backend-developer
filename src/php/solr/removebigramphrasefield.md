---
title: SolrDisMaxQuery::removeBigramPhraseField
description: Elimina un campo de bigrama de frase (argumento pf2)
source_url: https://www.php.net/manual/es/solrdismaxquery.removebigramphrasefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/removebigramphrasefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77590
---

SolrDisMaxQuery::removeBigramPhraseField

Elimina un campo de bigrama de frase (argumento pf2)

## Descripción

```php
public SolrDisMaxQuery::removeBigramPhraseField(string $field): SolrDisMaxQuery
```php

Elimina un campo de bigrama de frase (argumento pf2) que fue previamente añadido utilizando SolrDisMaxQuery::addBigramPhraseField

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::removeBigramPhraseField`

```
<?php

$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery
    ->addBigramPhraseField('cat', 2, 5.1)
    ->addBigramPhraseField('feature', 4.5)
;
echo $dismaxQuery.PHP_EOL;

// elimina el campo cat de pf2
$dismaxQuery
    ->removeBigramPhraseField('cat');
echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&pf2=cat~5.1^2 feature^4.5
    q=lucene&defType=edismax&pf2=feature^4.5

## Véase también

SolrDisMaxQuery::addBigramPhraseField

SolrDisMaxQuery::setBigramPhraseFields

SolrDisMaxQuery::setBigramPhraseSlop
