---
title: XSLTProcessor::setSecurityPrefs
description: Establece las preferencias de seguridad
source_url: https://www.php.net/manual/es/xsltprocessor.setsecurityprefs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xsl/xsltprocessor/setsecurityprefs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xsl
translation_status: ready
translation_revision: 07e6a4aaa
order: 104200
---

XSLTProcessor::setSecurityPrefs

Establece las preferencias de seguridad

## Descripción

```php
public XSLTProcessor::setSecurityPrefs(int $preferences): int
```php

Establece las preferencias de seguridad.

## Parámetros

`preferences`  
Las nuevas preferencias de seguridad. Las siguientes constantes pueden combinarse con OR: `XSL_SECPREF_READ_FILE`, `XSL_SECPREF_WRITE_FILE`, `XSL_SECPREF_CREATE_DIRECTORY`, `XSL_SECPREF_READ_NETWORK`, `XSL_SECPREF_WRITE_NETWORK`. Alternativamente, `XSL_SECPREF_NONE` o se puede pasar `XSL_SECPREF_DEFAULT`.

## Valores devueltos

Devuelve las antiguas preferencias de seguridad.
