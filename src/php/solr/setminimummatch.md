---
title: SolrDisMaxQuery::setMinimumMatch
description: Define el mínimo "Should" Match (mm)
source_url: https://www.php.net/manual/es/solrdismaxquery.setminimummatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setminimummatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77690
---

SolrDisMaxQuery::setMinimumMatch

Define el mínimo "Should" Match (mm)

## Descripción

```php
public SolrDisMaxQuery::setMinimumMatch(string $value): SolrDisMaxQuery
```php

Define el parámetro de coincidencia mínima "Should" (mm). Si el operador de consulta por omisión es AND, entonces mm=100%, si el operador de consulta por omisión (q.op) es OR, entonces mm=0%.

## Parámetros

`value`  
El valor/expresión de coincidencia mínima

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setMinimumMatch`

```
<?php

$dismaxQuery = new SolrDisMaxQuery("lucene");
// 75% de las cláusulas de consulta deben coincidir
$dismaxQuery->setMinimumMatch("75%");
echo $dismaxQuery . PHP_EOL;

?>

   
```php

El ejemplo anterior mostrará:

    q=lucene&defType=edismax&mm=75%
