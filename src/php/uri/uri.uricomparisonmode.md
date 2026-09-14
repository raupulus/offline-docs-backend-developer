---
title: La enumeración Uri\UriComparisonMode
source_url: https://www.php.net/manual/es/enum.uri-uricomparisonmode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uri/uri.uricomparisonmode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uri
translation_status: ready
translation_revision: 9e2dd56cb
order: 100110
---

## Introducción

Especifica si el componente `fragment` debe afectar al resultado de una comparación de URI.

Si el fragmento se excluye de la comparación, dos URIs se compararán como si ninguna de ellas tuviera un componente `fragment`.

## Sinopsis del enum

Uri

UriComparisonMode

IncludeFragment

El componente

fragment

se incluye en la comparación.

ExcludeFragment

El componente

fragment

se excluye de la comparación.
