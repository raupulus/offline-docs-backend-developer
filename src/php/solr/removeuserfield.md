---
title: SolrDisMaxQuery::removeUserField
description: Elimina un campo del parámetro de campo de usuario (uf)
source_url: https://www.php.net/manual/es/solrdismaxquery.removeuserfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdismaxquery/removeuserfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 03da6cade
order: 77640
---

SolrDisMaxQuery::removeUserField

Elimina un campo del parámetro de campo de usuario (uf)

## Descripción

```php
public SolrDisMaxQuery::removeUserField(string $field): SolrDisMaxQuery
```php

Elimina un campo del parámetro de campo de usuario (uf)

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrDisMaxQuery`

## Ejemplos

Ejemplo de `SolrDisMaxQuery::removeUserField`

```
<?php

$dismaxQuery = new SolrDisMaxQuery('lucene');
$dismaxQuery
->addUserField('cat')
->addUserField('text')
->addUserField('*_dt')
;
echo $dismaxQuery.PHP_EOL;

// elimina el campo llamado 'text'
$dismaxQuery
->removeUserField('text');
echo $dismaxQuery.PHP_EOL;

?>

   
```php

Resultado del ejemplo anterior es similar a:

    q=lucene&defType=%s&uf=cat text *_dt
    q=lucene&defType=%s&uf=cat *_dt

## Véase también

SolrDisMaxQuery::addUserField

SolrDisMaxQuery::setUserFields
