---
title: Locale::filterMatches
description: Verifica si el tag de idioma coincide con una configuración local
source_url: https://www.php.net/manual/es/locale.filtermatches.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/filter-matches.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41850
---

Locale::filterMatches

locale_filter_matches

Verifica si el tag de idioma coincide con una configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::filterMatches(string $languageTag, string $locale, [bool $canonicalize]): bool
```php

Estilo procedimental

```php
locale_filter_matches(string $languageTag, string $locale, [bool $canonicalize]): bool
```

Verifica si el filtro `languageTag` coincide con la `locale` según la RFC 4647, y su algoritmo de filtrado simple.

## Parámetros

`languageTag`  
El tag de idioma a verificar

`locale`  
El intervalo de idioma objetivo

`canonicalize`  
Si `true`, los argumentos serán convertidos a su forma canónica antes de la búsqueda.

## Valores devueltos

`true` si `locale` acepta `languageTag`, y `false` de lo contrario.

Devuelve `null` cuando la longitud de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Ejemplos

Ejemplo con `locale_filter_matches`, procedimental

```php
<?php
echo (locale_filter_matches('de-DEVA','de-DE', false)) ? "Coincide" : "No coincide";
echo '; ';
echo (locale_filter_matches('de-DE_1996','de-DE', false)) ? "Coincide" : "No coincide";
?>

   
```

Ejemplo con `locale_filter_matches`, POO

```php
<?php
echo (Locale::filterMatches('de-DEVA','de-DE', false)) ? "Coincide" : "No coincide";
echo '; ';
echo (Locale::filterMatches('de-DE-1996','de-DE', false)) ? "Coincide" : "No coincide";
?>

   
```

El ejemplo anterior mostrará:

    No coincide; Coincide

      

## Véase también

`locale_lookup`
