---
title: XSLTProcessor::hasExsltSupport
description: Determina si PHP tiene soporte para EXSLT
source_url: https://www.php.net/manual/es/xsltprocessor.hasexsltsupport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/hasexsltsupport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_reviewed: false
translation_revision: 07e6a4aaa
order: 104130
---

XSLTProcessor::hasExsltSupport

Determina si PHP tiene soporte para EXSLT

## Descripción

```php
public XSLTProcessor::hasExsltSupport(): bool
```php

Este método determina si PHP se compiló con la [librería EXSLT](https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Comprobando si tiene EXSLT

```
<?php

$proc = new XSLTProcessor;
if (!$proc->hasExsltSupport()) {
    die('EXSLT no disponible');
}

// aquí las líneas de código con EXSLT..

?>

    
```php
