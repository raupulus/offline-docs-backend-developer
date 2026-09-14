---
title: SolrDocument::getInputDocument
description: Devuelve un SolrInputDocument equivalente al objeto
source_url: https://www.php.net/manual/es/solrdocument.getinputdocument.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/getinputdocument.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: e41806c30
order: 77950
---

SolrDocument::getInputDocument

Devuelve un SolrInputDocument equivalente al objeto

## Descripción

```php
public SolrDocument::getInputDocument(): SolrInputDocument
```php

Devuelve un SolrInputDocument equivalente al objeto. Esto es útil si se desea reenviar/actualizar un documento recuperado desde una consulta.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto SolrInputDocument en caso de éxito y `null` en caso de fallo.
