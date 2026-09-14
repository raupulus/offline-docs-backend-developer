---
title: La clase Dom\XMLDocument
source_url: https://www.php.net/manual/es/class.dom-xmldocument.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/dom/dom-xmldocument.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: ae7db14ea
order: 12510
---

## Introducción

Representa un documento XML.

## Sinopsis de la clase

final

Dom\XMLDocument

extends

Dom\Document

Constantes heredadas

Propiedades

public

readonly

string

xmlEncoding

public

bool

xmlStandalone

public

string

xmlVersion

public

bool

formatOutput

Propiedades heredadas

Métodos

Aún no documentado

Métodos heredados

Aún no documentado

## Propiedades

> [!NOTE]
> Mientras que la clase `Dom\XMLDocument` permite definir ciertas propiedades para influir en el comportamiento del analizador, esta clase solo utiliza las constantes `LIBXML_*` para configurar el analizador.

`formatOutput`  
Indica correctamente el formato de salida con sangrado y espacio adicional.

## Notas

> [!NOTE]
> La extensión DOM utiliza el codificado UTF-8 al utilizar los métodos o las propiedades. Los métodos del analizador detectan automáticamente el codificado o permiten al llamante especificar un codificado.
