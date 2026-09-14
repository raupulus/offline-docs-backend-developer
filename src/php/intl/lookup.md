---
title: Locale::lookup
description: Búsqueda en la lista de la mejor lengua
source_url: https://www.php.net/manual/es/locale.lookup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/lookup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41980
---

Locale::lookup

locale_lookup

Búsqueda en la lista de la mejor lengua

## Descripción

Estilo orientado a objetos

```php
public static Locale::lookup(array $languageTag, string $locale, [bool $canonicalize], [string $defaultLocale]): string
```php

Estilo procedimental

```php
locale_lookup(array $languageTag, string $locale, [bool $canonicalize], [string $defaultLocale]): string
```

Búsqueda en la lista `languageTag` de la mejor lengua, para la configuración local especificada por `locale`, según el algoritmo de la RFC 4647.

## Parámetros

`languageTag`  
Un `array` que contiene una lista de lenguas a comparar con la configuración local `locale`. Se permite un máximo de 100 elementos.

`locale`  
La configuración local a utilizar para realizar la búsqueda.

`canonicalize`  
Si `true` los argumentos serán convertidos a su forma canónica antes de su búsqueda.

`defaultLocale`  
La configuración local a utilizar si no se encuentra ninguna solución.

## Valores devueltos

La lengua más cercana que haya sido encontrada en la lista, o bien el valor por defecto.

Devuelve `null` cuando la longitud de `locale` excede `INTL_MAX_LOCALE_LEN`.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 7.4.0   | `defaultLocale` ahora es nullable. |

## Ejemplos

Ejemplo con `locale_lookup`, procedimental

```php
<?php
$arr = array(
    'de-DEVA',
    'de-DE-1996',
    'de',
    'de-De'
);
echo locale_lookup($arr, 'de-DE-1996-x-prv1-prv2', true, 'en_US');
?>

   
```

Ejemplo con `Locale::lookup`, POO

```php
<?php
$arr = array(
    'de-DEVA',
    'de-DE-1996',
    'de',
    'de-De'
);
echo Locale::lookup($arr, 'de-DE-1996-x-prv1-prv2', true, 'en_US');
?>

   
```

El ejemplo anterior mostrará:

    de_de_1996

      

## Véase también

`locale_filter_matches`
