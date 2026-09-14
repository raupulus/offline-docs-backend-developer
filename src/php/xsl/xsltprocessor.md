---
title: La clase XSLTProcessor
source_url: https://www.php.net/manual/es/class.xsltprocessor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_reviewed: true
translation_revision: 7532801ce
order: 104240
---

## Introducción

## Sinopsis de la clase

XSLTProcessor

Propiedades

public

bool

doXInclude

false

public

bool

cloneDocument

false

public

int

maxTemplateDepth

public

int

maxTemplateVars

Métodos

## Propiedades

`doXInclude`  
Indica si los xIncludes deben ser realizados.

`cloneDocument`  
Indica si la transformación debe realizarse en un clon del documento.

`maxTemplateDepth`  
La profundidad máxima de recursión de los modelos.

`maxTemplateVars`  
El número máximo de variables en el modelo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Las propiedades `doXInclude` y `cloneDocument` están ahora explícitamente definidas en la clase. |
| 8.4.0 | Propiedades añadidas `maxTemplateDepth` y `maxTemplateVars`. |
