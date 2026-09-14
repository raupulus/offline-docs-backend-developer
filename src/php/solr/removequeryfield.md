---
title: SolrDisMaxQuery::removeQueryField
description: Elimina un campo de consulta (argumento qf)
source_url: https://www.php.net/manual/es/solrdismaxquery.removequeryfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/removequeryfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: faf921403
order: 77620
---

SolrDisMaxQuery::removeQueryField

Elimina un campo de consulta (argumento qf)

## Descripción

```php
public SolrDisMaxQuery::removeQueryField(string $field): SolrDisMaxQuery
```php

Elimina un campo de consulta (argumento qf) añadido por SolrDisMaxQuery::addQueryField

qf: Durante la construcción de DisjunctionMaxQueries a partir de la consulta del usuario, especifica los campos a buscar y los boosts para estos campos.

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::removeQueryField`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery
    ->addQueryField('first', 3)
    ->addQueryField('second', 0.2)
    ->addQueryField('cat');
echo $dismaxQuery . PHP_EOL;
// elimina el campo 'second'
echo $dismaxQuery->removeQueryField('second');
?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&qf=first^3 second^0.2 cat
    q=lucene&defType=edismax&qf=first^3 cat

## Véase también

SolrDisMaxQuery::addQueryField
