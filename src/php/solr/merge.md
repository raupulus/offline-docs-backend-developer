---
title: SolrDocument::merge
description: Fusiona la fuente con el objeto SolrDocument actual
source_url: https://www.php.net/manual/es/solrdocument.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b8758b060
order: 77990
---

SolrDocument::merge

Fusiona la fuente con el objeto SolrDocument actual

## Descripción

```php
public SolrDocument::merge(SolrDocument $sourceDoc, [bool $overwrite]): bool
```php

Fusiona la fuente con el objeto SolrDocument actual.

## Parámetros

`sourceDoc`  
El documento fuente.

`overwrite`  
Si esto es `true` los campos con el mismo nombre que los del documento destino serán sobrescritos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
