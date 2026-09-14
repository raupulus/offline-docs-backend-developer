---
title: SolrQuery::setHighlightAlternateField
description: Especifica el campo de copia de seguridad a usar
source_url: https://www.php.net/manual/es/solrquery.sethighlightalternatefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightalternatefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80290
---

SolrQuery::setHighlightAlternateField

Especifica el campo de copia de seguridad a usar

## Descripción

```php
public SolrQuery::setHighlightAlternateField(string $field, [string $field_override]): SolrQuery
```php

Si un trozo no se puede generar debido a que no hay términos coincidentes, se puede especificar un campo para usarlo como copia de seguridad del sumario predeterminado

## Parámetros

`field`  
El nombre del campo de copia de seguridad

`field_override`  
El nombre del campo que se va a sobrescribir.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
