---
title: SolrDisMaxQuery::useDisMaxQueryParser
description: Cambia el QueryParser para que sea el DisMax Query Parser
source_url: https://www.php.net/manual/es/solrdismaxquery.usedismaxqueryparser.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/usedismaxqueryparser.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77780
---

SolrDisMaxQuery::useDisMaxQueryParser

Cambia el QueryParser para que sea el DisMax Query Parser

## Descripción

```php
public SolrDisMaxQuery::useDisMaxQueryParser(): SolrDisMaxQuery
```php

Cambia el QueryParser para que sea el DisMax Query Parser

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::useDisMaxQueryParser`

```
<?php

$dismaxQuery = new SolrDisMaxQuery();
$dismaxQuery->useDisMaxQueryParser();
echo $dismaxQuery;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    defType=dismax

## Véase también

SolrDisMaxQuery::useDisMaxQueryParser
