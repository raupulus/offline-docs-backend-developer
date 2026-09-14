---
title: SolrDisMaxQuery::useEDisMaxQueryParser
description: Cambia el QueryParser para que sea el EDisMax Query Parser
source_url: https://www.php.net/manual/es/solrdismaxquery.useedismaxqueryparser.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/useedismaxqueryparser.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: a56de5a30
order: 77790
---

SolrDisMaxQuery::useEDisMaxQueryParser

Cambia el QueryParser para que sea el EDisMax Query Parser

## Descripción

```php
public SolrDisMaxQuery::useEDisMaxQueryParser(): SolrDisMaxQuery
```php

Cambia el QueryParser para que sea el EDisMax Query Parser. Por omisión, el constructor de consultas utiliza edismax. Si ha sido cambiado utilizando SolrDisMaxQuery::useDisMaxQueryParser, puede ser revertido utilizando este método.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::useEDisMaxQueryParser`

```
<?php

$dismaxQuery = new SolrDisMaxQuery();
$dismaxQuery->useEDisMaxQueryParser();
echo $dismaxQuery;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    defType=edismax
