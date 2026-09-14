---
title: SolrQuery::setTimeAllowed
description: El tiempo permitido para que la búsqueda finalice
source_url: https://www.php.net/manual/es/solrquery.settimeallowed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/settimeallowed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80730
---

SolrQuery::setTimeAllowed

El tiempo permitido para que la búsqueda finalice

## Descripción

```php
public SolrQuery::setTimeAllowed(int $timeAllowed): SolrQuery
```php

El tiempo permitido para que la búsqueda finalice. Este valor sólo se aplica a la búsqueda y no a las solicitudes en general. Se mide en milisegundos. Los valores menores o iguales a cero implican la no restricción de tiempo. Se pueden devolver resultados parciales, si los hubiera.

## Parámetros

`timeAllowed`  
El tiempo permitido para que la búsqueda finalice.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
