---
title: XSLTProcessor::getSecurityPrefs
description: Obtiene las preferencias de seguridad
source_url: https://www.php.net/manual/es/xsltprocessor.getsecurityprefs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/getsecurityprefs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 07e6a4aaa
order: 104120
---

XSLTProcessor::getSecurityPrefs

Obtiene las preferencias de seguridad

## Descripción

```php
public XSLTProcessor::getSecurityPrefs(): int
```php

Obtiene las preferencias de seguridad.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una máscara de bits compuesta por `XSL_SECPREF_READ_FILE`, `XSL_SECPREF_WRITE_FILE`, `XSL_SECPREF_CREATE_DIRECTORY`, `XSL_SECPREF_READ_NETWORK`, `XSL_SECPREF_WRITE_NETWORK`.
