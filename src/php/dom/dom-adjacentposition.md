---
title: La enumeración Dom\AdjacentPosition
source_url: https://www.php.net/manual/es/enum.dom-adjacentposition.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-adjacentposition.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 89c7c0709
order: 12250
---

## Introducción

La enumeración AdjacentPosition se utiliza para especificar dónde, en relación con el elemento contextual, debe realizarse la inserción utilizando Dom\Element::insertAdjacentElement o Dom\Element::insertAdjacentText.

## Sinopsis del enum

AdjacentPosition

BeforeBegin

Insertar antes del elemento contextual. Esto solo es posible si el elemento está en un documento y tiene un padre.

AfterBegin

Insertar antes del primer hijo del elemento contextual.

BeforeEnd

Insertar después del último hijo del elemento contextual.

AfterEnd

Insertar después del elemento contextual. Esto solo es posible si el elemento está en un documento y tiene un padre.
