---
title: SolrCollapseFunction::__construct
description: Constructor
source_url: https://www.php.net/manual/es/solrcollapsefunction.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrcollapsefunction/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 7bade7dc0
order: 77370
---

SolrCollapseFunction::\_\_construct

Constructor

## Descripción

```php
public SolrCollapseFunction::__construct([string $field])
```php

Función de construcción de Collapse.

## Parámetros

`field`  
El nombre del campo a reducir.

Para reducir un resultado, el tipo de campo debe ser un string, un integer o un float.

## Ejemplos

Ejemplo de `SolrCollapseFunction::__construct`

```
<?php

include "bootstrap.php";

$options = array
(
    'hostname' => SOLR_SERVER_HOSTNAME,
    'login'    => SOLR_SERVER_USERNAME,
    'password' => SOLR_SERVER_PASSWORD,
    'port'     => SOLR_SERVER_PORT,
    'path'     => SOLR_SERVER_PATH
);

$client = new SolrClient($options);

$query = new SolrQuery('*:*');

$func = new SolrCollapseFunction('field_name');

$func->setMax('sum(cscore(),field(some_other_field))');
$func->setSize(100);
$func->setNullPolicy(SolrCollapseFunction::NULLPOLICY_EXPAND);

$query->collapse($func);

$queryResponse = $client->query($query);

$response = $queryResponse->getResponse();

print_r($response);

?>

   
```php

## Véase también

SolrQuery::collapse
