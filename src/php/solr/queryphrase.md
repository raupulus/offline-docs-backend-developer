---
title: SolrUtils::queryPhrase
description: Prepara una frase desde una cadena lucene sin escapar
source_url: https://www.php.net/manual/es/solrutils.queryphrase.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrutils/queryphrase.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 80980
---

SolrUtils::queryPhrase

Prepara una frase desde una cadena lucene sin escapar

## Descripción

```php
public static SolrUtils::queryPhrase(string $str): string
```php

Prepara una frase desde una cadena lucene sin escapar.

## Parámetros

`str`  
La frase lucene.

## Valores devueltos

Devuelve la frase entre comillas dobles.
