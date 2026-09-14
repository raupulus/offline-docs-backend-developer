---
title: SolrClient::setServlet
description: Cambia el servlet especificado a un nuevo valor
source_url: https://www.php.net/manual/es/solrclient.setservlet.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/setservlet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 77310
---

SolrClient::setServlet

Cambia el servlet especificado a un nuevo valor

## Descripción

```php
public SolrClient::setServlet(int $type, string $value): bool
```php

Cambia el servlet especificado a un nuevo valor

## Parámetros

`type`  
Uno de los siguientes tipos:

\- SolrClient::SEARCH_SERVLET_TYPE - SolrClient::UPDATE_SERVLET_TYPE - SolrClient::THREADS_SERVLET_TYPE - SolrClient::PING_SERVLET_TYPE - SolrClient::TERMS_SERVLET_TYPE

`value`  
El nuevo valor para el servlet

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
