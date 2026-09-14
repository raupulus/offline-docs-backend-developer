---
title: SolrClient::rollback
description: Revierte todos los añadidos/eliminados hechos en el índice desde el último
  envío
source_url: https://www.php.net/manual/es/solrclient.rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 77290
---

SolrClient::rollback

Revierte todos los añadidos/eliminados hechos en el índice desde el último envío

## Descripción

```php
public SolrClient::rollback(): SolrUpdateResponse
```php

Revierte todos los añadidos/eliminados hechos en el índice desde el último envío. No llama a ningún escuchador de eventos ni crea un buscador nuevo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto SolrUpdateResponse en caso de éxito o lanza una excepción SolrClientException en caso de fallo.

## Véase también

SolrClient::commit, SolrClient::optimize
