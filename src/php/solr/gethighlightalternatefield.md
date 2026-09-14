---
title: SolrQuery::getHighlightAlternateField
description: Devuelve el campo remarcado para usarlo como copia de seguridad o como
  predeterminado
source_url: https://www.php.net/manual/es/solrquery.gethighlightalternatefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightalternatefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79370
---

SolrQuery::getHighlightAlternateField

Devuelve el campo remarcado para usarlo como copia de seguridad o como predeterminado

## Descripción

```php
public SolrQuery::getHighlightAlternateField([string $field_override]): string
```php

Devuelve el campo remarcado para usarlo como copia de seguridad o como predeterminado. Acepta una sobrescritura opcional.

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve una cadena en caso de éxito y `null` si no se estableció.
