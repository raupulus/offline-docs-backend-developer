---
title: SolrDisMaxQuery::setBoostFunction
description: Define una función de Boost (argumento bf)
source_url: https://www.php.net/manual/es/solrdismaxquery.setboostfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setboostfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: a56de5a30
order: 77670
---

SolrDisMaxQuery::setBoostFunction

Define una función de Boost (argumento bf)

## Descripción

```php
public SolrDisMaxQuery::setBoostFunction(string $function): SolrDisMaxQuery
```php

Define una función de Boost (argumento bf).

Las funciones (con boosts opcionales) que serán incluidas en la petición del usuario para influir en el score. Cualquier función soportada nativamente por Solr puede ser utilizada, con un valor de boost. Por ejemplo:

recip(rord(myfield),1,2,3)^1.5

## Parámetros

`function`  

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setBoostFunction`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');

$boostRecentDocsFunction = "recip(ms(NOW,mydatefield),3.16e-11,1,1)";
$dismaxQuery->setBoostFunction($boostRecentDocsFunction);

echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&bf=recip(ms(NOW,mydatefield),3.16e-11,1,1)
