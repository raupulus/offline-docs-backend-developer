---
title: SolrInputDocument::addField
description: Añade un campo al documento
source_url: https://www.php.net/manual/es/solrinputdocument.addfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrinputdocument/addfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78290
---

SolrInputDocument::addField

Añade un campo al documento

## Descripción

```php
public SolrInputDocument::addField(string $fieldName, string $fieldValue, [float $fieldBoostValue]): bool
```php

Para múltiples campos, si se especifica un valor boost válido, el valor especificado será multiplicado por el valor boost actual para este campo.

## Parámetros

`fieldName`  
El nombre del campo

`fieldValue`  
El valor del campo

`fieldBoostValue`  
El boost de tiempo del índice. Ya que este valor no puede ser negativo, se pueden pasar aún valores menores que 1.0 pero deben ser mayores que cero.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
