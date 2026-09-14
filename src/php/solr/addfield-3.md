---
title: SolrQuery::addField
description: Especifica qué campos devolver en el resultado
source_url: https://www.php.net/manual/es/solrquery.addfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 78850
---

SolrQuery::addField

Especifica qué campos devolver en el resultado

## Descripción

```php
public SolrQuery::addField(string $field): SolrQuery
```php

Este método se usa para especificar un conjunto de campos a devolver, restingiendo así la cantidad de información en la respuesta.

Puede ser llamado múltiples veces, una por cada nombre de campo.

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

Devuelve el objeto SolrQuery actual
