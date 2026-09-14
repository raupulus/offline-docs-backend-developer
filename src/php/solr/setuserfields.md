---
title: SolrDisMaxQuery::setUserFields
description: Define el parámetro de campos de usuario (uf)
source_url: https://www.php.net/manual/es/solrdismaxquery.setuserfields.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/setuserfields.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 16b2b1ea9
order: 77770
---

SolrDisMaxQuery::setUserFields

Define el parámetro de campos de usuario (uf)

## Descripción

```php
public SolrDisMaxQuery::setUserFields(string $fields): SolrDisMaxQuery
```php

Define el parámetro de campos de usuario (uf)

Campos de usuario: Especifica los campos de esquema que el usuario final está autorizado a consultar.

## Parámetros

`fields`  
Los nombres de los campos separados por un espacio

Este parámetro admite caracteres comodín.

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::setUserFields`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery->setUserFields('field1 field2 *_txt');
echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=edismax&uf=field1 field2 *_txt

## Véase también

SolrDisMaxQuery::addUserField

SolrDisMaxQuery::removeUserField
