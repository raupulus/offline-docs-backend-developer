---
title: Locale::getRegion
description: Devuelve un código para la región de la configuración local
source_url: https://www.php.net/manual/es/locale.getregion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-region.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41950
---

Locale::getRegion

locale_get_region

Devuelve un código para la región de la configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getRegion(string $locale): string
```php

Estilo procedimental

```php
locale_get_region(string $locale): string
```

Devuelve un código para la región de la configuración local.

## Parámetros

`locale`  
La configuración local de la que se debe extraer el código de región.

## Valores devueltos

El código de región para la configuración local, o bien `null` en caso de error.

Devuelve `null` cuando la longitud de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo con `locale_get_region`, procedimental

```php
<?php
echo locale_get_region('de-CH-1901');
?>

   
```

Ejemplo con `locale_get_region`, POO

```php
<?php
echo Locale::getRegion('de-CH-1901');
?>

   
```

El ejemplo anterior mostrará:

    CH

      

## Véase también

`locale_get_primary_language`, `locale_get_script`, `locale_get_all_variants`
