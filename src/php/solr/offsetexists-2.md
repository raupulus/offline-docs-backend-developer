---
title: SolrObject::offsetExists
description: Comprueba si la propiedad existe
source_url: https://www.php.net/manual/es/solrobject.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrobject/offsetexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78580
---

SolrObject::offsetExists

Comprueba si la propiedad existe

## Descripción

```php
public SolrObject::offsetExists(string $property_name): bool
```php

Comprueba si la propiedad existe. Se usa cuando el objeto es tratado como una matriz.

## Parámetros

`property_name`  
El nombre de la propiedad.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
