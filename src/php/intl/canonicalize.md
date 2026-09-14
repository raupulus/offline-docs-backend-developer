---
title: Locale::canonicalize
description: Canoniza la cadena que representa la configuración local
source_url: https://www.php.net/manual/es/locale.canonicalize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/canonicalize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 14a6825b9
order: 41830
---

Locale::canonicalize

locale_canonicalize

Canoniza la cadena que representa la configuración local

## Descripción

```php
public static Locale::canonicalize(string $locale): string
```php

Convierte el string de configuración regional pasada al formato ICU.

Esto no necesariamente indica ni devuelve una configuración regional válida. Es solo una versión de la entrada que se ha estandarizado según las reglas de ICU.

El comportamiento de esta función depende de la versión de ICU que PHP esté utilizando (`INTL_ICU_VERSION`).

## Parámetros

`locale`  
String de configuración regional original.

## Valores devueltos

Cadena canonicalizada en la configuración local.

Devuelve `null` cuando la longitud de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo de `locale_canonicalize`

```
echo Locale::canonicalize('en-US.utf8') . "\n";
echo Locale::canonicalize('totally-not-valid') . "\n";

   
```php

Resultado del ejemplo anterior es similar a:

    en_US
    totally_NOT_VALID
