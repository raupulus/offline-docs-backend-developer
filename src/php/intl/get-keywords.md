---
title: Locale::getKeywords
description: Lee las palabras clave de la configuración local
source_url: https://www.php.net/manual/es/locale.getkeywords.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-keywords.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41930
---

Locale::getKeywords

locale_get_keywords

Lee las palabras clave de la configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getKeywords(string $locale): array
```php

Estilo procedimental

```php
locale_get_keywords(string $locale): array
```

Lee las palabras clave de la configuración local.

## Parámetros

`locale`  
La configuración local de la cual extraer las palabras clave.

## Valores devueltos

Un `array` asociativo que contiene los pares clave-valor para esta configuración local.

Devuelve `null` cuando la longitud de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo con `locale_get_keywords`, procedimental

```php
<?php
$keywords_arr = locale_get_keywords('de_DE@currency=EUR;collation=PHONEBOOK');
if ($keywords_arr) {
    foreach ($keywords_arr as $key => $value) {
        echo "$key = $value\n";
    }
}
?>

   
```

Ejemplo con `locale_get_keywords`, POO

```php
<?php
$keywords_arr = Locale::getKeywords('de_DE@currency=EUR;collation=PHONEBOOK');
if ($keywords_arr) {
    foreach ($keywords_arr as $key => $value) {
        echo "$key = $value\n";
    }
}
?>

   
```

El ejemplo anterior mostrará:

    collation = PHONEBOOK
    currency = EUR

      

## Véase también

`locale_get_all_variants`
