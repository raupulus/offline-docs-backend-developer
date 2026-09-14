---
title: SolrQuery::setEchoParams
description: Determina qué tipo de parámetros incluir en la respuesta
source_url: https://www.php.net/manual/es/solrquery.setechoparams.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setechoparams.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80010
---

SolrQuery::setEchoParams

Determina qué tipo de parámetros incluir en la respuesta

## Descripción

```php
public SolrQuery::setEchoParams(string $type): SolrQuery
```php

Ordena a Solr qué tipos de parámetros de solicitud deberían ser incluidos en la respuesta para propósitos de depuración, valores legales incluidos:

\- none - no incluir ningún parámetro de solicitud para la depuración - explicit - incluir los parámetros explícitamete especificados por el cliente en la solicitud - all - incluir todos los parámetros involucrados en esta solicitud, los especificados explícitamente por el cliente, o los implícitos debido a la configuración del gestor de solicitudes.

## Parámetros

`type`  
El tipo de parámetros a incluir

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
