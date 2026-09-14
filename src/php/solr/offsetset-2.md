---
title: SolrObject::offsetSet
description: Establece el valor de una propiedad
source_url: https://www.php.net/manual/es/solrobject.offsetset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrobject/offsetset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78600
---

SolrObject::offsetSet

Establece el valor de una propiedad

## Descripción

```php
public SolrObject::offsetSet(string $property_name, string $property_value): void
```php

Establece el valor de una propiedad. Se usa cuando el objeto es tratado como una matriz. Este objeto es de sólo lectura. Esto nunva debería intentarse.

## Parámetros

`property_name`  
El nombre de la propiedad.

`property_value`  
El nuevo valor.

## Valores devueltos

Nada.
