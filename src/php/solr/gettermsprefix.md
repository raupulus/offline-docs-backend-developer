---
title: SolrQuery::getTermsPrefix
description: Devuelve el prefijo del término
source_url: https://www.php.net/manual/es/solrquery.gettermsprefix.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gettermsprefix.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79810
---

SolrQuery::getTermsPrefix

Devuelve el prefijo del término

## Descripción

```php
public SolrQuery::getTermsPrefix(): string
```php

Devuelve el prefijo por el que los términos coincedentes deben ser restringidos. Restringirá las coincidencias sólo de los términos que empiecen con el prefijo

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una cadena en caso de éxito y `null` si no se estableció.
