---
title: Locale::getAllVariants
description: Lista todas las variantes de una configuración local
source_url: https://www.php.net/manual/es/locale.getallvariants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-all-variants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41860
---

Locale::getAllVariants

locale_get_all_variants

Lista todas las variantes de una configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getAllVariants(string $locale): array
```php

Estilo procedimental

```php
locale_get_all_variants(string $locale): array
```

Lista todas las variantes de una configuración local

## Parámetros

`locale`  
La configuración local de la que se deben extraer las variantes

## Valores devueltos

Un `array` que contiene la lista de todas las variantes de una configuración local, o bien `null` si no existen.

Devuelve `null` cuando la longitud de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo con `locale_get_all_variants`, procedimental

```php
<?php
$arr = locale_get_all_variants('sl_IT_NEDIS_ROJAZ_1901');
var_export( $arr );
?>

   
```

Ejemplo con `locale_get_all_variants`, POO

```php
<?php
$arr = Locale::getAllVariants('sl_IT_NEDIS_ROJAZ_1901');
var_export( $arr );
?>

   
```

El ejemplo anterior mostrará:

    array (
        0 => 'NEDIS',
        1 => 'ROJAZ',
        2 => '1901',
    )

      

## Véase también

`locale_get_primary_language`, `locale_get_script`, `locale_get_region`
