---
title: SolrInputDocument::merge
description: Fusiona un documento con otro
source_url: https://www.php.net/manual/es/solrinputdocument.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrinputdocument/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b8758b060
order: 78440
---

SolrInputDocument::merge

Fusiona un documento con otro

## Descripción

```php
public SolrInputDocument::merge(SolrInputDocument $sourceDoc, [bool $overwrite]): bool
```php

Fusiona un documento con otro.

## Parámetros

`sourceDoc`  
El documento fuente.

`overwrite`  
Si esto es `true` reemplazará los campos coincidentes del documento destino.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. En el futuro, esto será modificado para que devuelva el número de campos del documento nuevo.
