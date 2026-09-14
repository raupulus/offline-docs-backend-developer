---
title: SolrDisMaxQuery::removePhraseField
description: Elimina un campo de frase (argumento pf)
source_url: https://www.php.net/manual/es/solrdismaxquery.removephrasefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/removephrasefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: faf921403
order: 77610
---

SolrDisMaxQuery::removePhraseField

Elimina un campo de frase (argumento pf)

## Descripción

```php
public SolrDisMaxQuery::removePhraseField(string $field): SolrDisMaxQuery
```php

Elimina un campo de frase (argumento pf) que fue añadido previamente utilizando SolrDisMaxQuery::addPhraseField

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::removePhraseField`

```
<?php
$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery
    ->addPhraseField('first', 3, 1)
    ->addPhraseField('second', 4, 1)
    ->addPhraseField('cat', 55);
echo $dismaxQuery . PHP_EOL;
echo $dismaxQuery->removePhraseField('second');
?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&pf=first~1^3 second~1^4 cat^55
    q=lucene&defType=edismax&pf=first~1^3 cat^55

## Véase también

SolrDisMaxQuery::addPhraseField

SolrDisMaxQuery::setPhraseFields
