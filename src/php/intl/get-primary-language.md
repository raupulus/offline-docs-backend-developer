---
title: Locale::getPrimaryLanguage
description: Lee el idioma principal de la configuración local
source_url: https://www.php.net/manual/es/locale.getprimarylanguage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-primary-language.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41940
---

Locale::getPrimaryLanguage

locale_get_primary_language

Lee el idioma principal de la configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getPrimaryLanguage(string $locale): string
```php

Estilo procedimental

```php
locale_get_primary_language(string $locale): string
```

Lee el idioma principal de la configuración local.

## Parámetros

`locale`  
La configuración local de la cual se debe extraer el idioma principal.

## Valores devueltos

El código de idioma asociado al idioma.

Devuelve `null` cuando la longitud de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo con `locale_get_primary_language`, procedimental

```php
<?php
echo locale_get_primary_language('zh-Hant');
?>

   
```

Ejemplo con `locale_get_primary_language`, POO

```php
<?php
echo Locale::getPrimaryLanguage('zh-Hant');
?>

   
```

El ejemplo anterior mostrará:

    zh

      

## Véase también

`locale_get_script`, `locale_get_region`, `locale_get_all_variants`
