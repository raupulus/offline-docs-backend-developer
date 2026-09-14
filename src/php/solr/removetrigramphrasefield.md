---
title: SolrDisMaxQuery::removeTrigramPhraseField
description: Elimina un campo de frase de trigramas (argumento pf3)
source_url: https://www.php.net/manual/es/solrdismaxquery.removetrigramphrasefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/removetrigramphrasefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77630
---

SolrDisMaxQuery::removeTrigramPhraseField

Elimina un campo de frase de trigramas (argumento pf3)

## Descripción

```php
public SolrDisMaxQuery::removeTrigramPhraseField(string $field): SolrDisMaxQuery
```php

Elimina un campo de frase de trigramas (argumento pf3)

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::removeTrigramPhraseField`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery
->addTrigramPhraseField('cat', 2, 5.1)
->addTrigramPhraseField('feature', 4.5)
;
echo $dismaxQuery.PHP_EOL;
// inverso
$dismaxQuery
->removeTrigramPhraseField('cat');
echo $dismaxQuery.PHP_EOL;

?>

   
```php

El ejemplo anterior mostrará:

    q=lucene&defType=%s&pf3=cat~5.1^2 feature^4.5
    q=lucene&defType=%s&pf3=feature^4.5

## Véase también

SolrDisMaxQuery::addTrigramPhraseField

SolrDisMaxQuery::setTrigramPhraseFields

SolrDisMaxQuery::setTrigramPhraseSlop
