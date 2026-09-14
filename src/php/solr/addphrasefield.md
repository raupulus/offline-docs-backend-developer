---
title: SolrDisMaxQuery::addPhraseField
description: Añade una frase de campo (argumento pf)
source_url: https://www.php.net/manual/es/solrdismaxquery.addphrasefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/addphrasefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77540
---

SolrDisMaxQuery::addPhraseField

Añade una frase de campo (argumento pf)

## Descripción

```php
public SolrDisMaxQuery::addPhraseField(string $field, string $boost, [string $slop]): SolrDisMaxQuery
```php

Añade una frase de campo (argumento pf)

## Parámetros

`field`  
El nombre del campo

`boost`  

`slop`  

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::addPhraseField`

```
<?php
$dismaxQuery = new SolrDisMaxQuery("lucene");
$dismaxQuery
    ->addPhraseField('cat', 3, 1)
    ->addPhraseField('third', 4, 2)
    ->addPhraseField('source', 55)
;
echo $dismaxQuery;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&pf=cat~1^3 third~2^4 source^55

## Véase también

SolrDisMaxQuery::removePhraseField

SolrDisMaxQuery::setPhraseFields
