---
title: XSLTProcessor::removeParameter
description: Elimina un parámetro
source_url: https://www.php.net/manual/es/xsltprocessor.removeparameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/removeparameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_reviewed: false
translation_revision: 07e6a4aaa
order: 104170
---

XSLTProcessor::removeParameter

Elimina un parámetro

## Descripción

```php
public XSLTProcessor::removeParameter(string $namespace, string $name): bool
```php

Elimina un parámetro, si ya existía. Esto hará que el procesador use el valor por defecto para el parámetro como está especificado en la hoja de estilos.

## Parámetros

`namespace`  
La URI del namespace para el parámetro XSLT.

`name`  
Nombre local del parámetro XSLT.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`XSLTProcessor::setParameter`, `XSLTProcessor::getParameter`
