---
title: SolrClient::system
description: Obtener información del Servidor Solr
source_url: https://www.php.net/manual/es/solrclient.system.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrclient/system.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 7050d9626
order: 77320
---

SolrClient::system

Obtener información del Servidor Solr

## Descripción

```php
public SolrClient::system(): void
```php

Obtener información del Servidor Solr

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un objeto `SolrGenericResponse` en caso de éxito.

## Errores/Excepciones

Lanza una `SolrClientException` si el cliente falló, o si hubo un problema con la conexión.

Lanza una `SolrServerException` si el Servidor Solr falló al satisfacer la consulta.
