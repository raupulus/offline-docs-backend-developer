---
title: SolrResponse::setParseMode
description: Establece el modo de análisis
source_url: https://www.php.net/manual/es/solrresponse.setparsemode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrresponse/setparsemode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 80870
---

SolrResponse::setParseMode

Establece el modo de análisis

## Descripción

```php
public SolrResponse::setParseMode([int $parser_mode]): bool
```php

Establece el modo de análisis.

## Parámetros

`parser_mode`  
SolrResponse::PARSE_SOLR_DOC analiza los documentos en instancias de SolrDocument. SolrResponse::PARSE_SOLR_OBJ convierte un documento a un objeto SolrObjects.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
