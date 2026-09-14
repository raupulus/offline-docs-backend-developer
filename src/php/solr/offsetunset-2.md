---
title: SolrObject::offsetUnset
description: Desestablece el valor de la propiedad
source_url: https://www.php.net/manual/es/solrobject.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrobject/offsetunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: a4645fd63
order: 78610
---

SolrObject::offsetUnset

Desestablece el valor de la propiedad

## Descripción

```php
public SolrObject::offsetUnset(string $property_name): void
```php

Desestablece el valor de la propiedad. Se emplea cuando el objeto es tratado como un array. Este objeto es de sólo lectura. Esto nunca debe intentarse.

## Parámetros

`property_name`  
El nombre de la propiedad.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de SolrObject::offsetUnset

```
<?php
/* ... */
?>

    
```php

Resultado del ejemplo anterior es similar a:

    ...
