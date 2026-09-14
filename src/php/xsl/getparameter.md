---
title: XSLTProcessor::getParameter
description: Obtiene el valor de un parámetro
source_url: https://www.php.net/manual/es/xsltprocessor.getparameter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/getparameter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 07e6a4aaa
order: 104110
---

XSLTProcessor::getParameter

Obtiene el valor de un parámetro

## Descripción

```php
public XSLTProcessor::getParameter(string $namespace, string $name): string
```php

Obtiene un parámetro si ha sido previamente establecido por `XSLTProcessor::setParameter`.

## Parámetros

`namespace`  
La URI del namespace del parámetro XSLT.

`name`  
El nombre local del parámetro XSLT.

## Valores devueltos

El valor del parámetro (como un string), o `false` si no está definido.

## Véase también

`XSLTProcessor::setParameter`, `XSLTProcessor::removeParameter`
