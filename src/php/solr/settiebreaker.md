---
title: SolrDisMaxQuery::setTieBreaker
description: Define el parámetro de Tie Breaker (parámetro tie)
source_url: https://www.php.net/manual/es/solrdismaxquery.settiebreaker.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/settiebreaker.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77740
---

SolrDisMaxQuery::setTieBreaker

Define el parámetro de Tie Breaker (parámetro tie)

## Descripción

```php
public SolrDisMaxQuery::setTieBreaker(string $tieBreaker): SolrDisMaxQuery
```php

Define el parámetro de Tie Breaker (parámetro tie)

## Parámetros

`tieBreaker`  
El parámetro *tie* especifica un valor float (que debería ser algo mucho menor que 1) para ser utilizado como criterio de desempate en las consultas DisMax.

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setTieBreaker`

```
<?php

$dismaxQuery = new SolrDisMaxQuery();
$dismaxQuery->setTieBreaker(0.1);

echo $dismaxQuery;

?>

   
```php

El ejemplo anterior mostrará:

    defType=edismax&tie=0.1
