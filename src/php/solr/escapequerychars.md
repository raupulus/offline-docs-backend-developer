---
title: SolrUtils::escapeQueryChars
description: Escapa un string de consulta lucene
source_url: https://www.php.net/manual/es/solrutils.escapequerychars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrutils/escapequerychars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b95d28e6e
order: 80960
---

SolrUtils::escapeQueryChars

Escapa un string de consulta lucene

## Descripción

```php
public static SolrUtils::escapeQueryChars(string $str): string
```php

Lucene soporta el escape de caracteres especiales que son parte de la sintaxis de la consulta.

La lista actual de caracteres especiales es:

\+ - && \|\| ! ( ) { } \[ \] ^ " ~ \* ? : \\ /

Estos caracteres son parte de la sintaxis de la consulta y deben ser escapados

## Parámetros

`str`  
Este es el string de consulta a ser escapda.

## Valores devueltos

Devuelve el string escapado o `false` si ocurre un error.
