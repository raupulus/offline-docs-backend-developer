---
title: SolrDisMaxQuery::setQueryAlt
description: Define la consulta alternativa (parámetro q.alt)
source_url: https://www.php.net/manual/es/solrdismaxquery.setqueryalt.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setqueryalt.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 8e2cfbdce
order: 77720
---

SolrDisMaxQuery::setQueryAlt

Define la consulta alternativa (parámetro q.alt)

## Descripción

```php
public SolrDisMaxQuery::setQueryAlt(string $q): SolrDisMaxQuery
```php

Define la consulta alternativa (parámetro q.alt)

Cuando el parámetro *q* principal no está especificado o está vacío, el parámetro *q.alt* es utilizado

## Parámetros

`q`  
la cadena de consulta

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setQueryAlt`

```
<?php

$dismaxQuery = new SolrDisMaxQuery();
$dismaxQuery->setQueryAlt('*:*');

?>

   
```php

Resultado del ejemplo anterior es similar a:

    defType=edismax&q.alt=*:*&q=
