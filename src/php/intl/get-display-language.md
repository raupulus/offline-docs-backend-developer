---
title: Locale::getDisplayLanguage
description: Devuelve un nombre adecuado para mostrar un nombre de idioma
source_url: https://www.php.net/manual/es/locale.getdisplaylanguage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-display-language.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41880
---

Locale::getDisplayLanguage

locale_get_display_language

Devuelve un nombre adecuado para mostrar un nombre de idioma

## Descripción

Estilo orientado a objetos

```php
public static Locale::getDisplayLanguage(string $locale, [string $displayLocale]): string
```php

Estilo procedimental

```php
locale_get_display_language(string $locale, [string $displayLocale]): string
```

Devuelve un nombre adecuado para mostrar un nombre de idioma. Si se pasa el valor `null` como argumento, se utiliza la configuración local por omisión.

## Parámetros

`locale`  
La configuración local de la cual se debe devolver el nombre del idioma

`displayLocale`  
Un formato opcional para mostrar el nombre del idioma.

## Valores devueltos

El nombre del idioma a mostrar para la `locale`, en el formato definido por `displayLocale`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 8.0.0   | `displayLocale` ahora es nullable. |

## Ejemplos

Ejemplo con `locale_get_display_language`, procedimental

```php
<?php
echo locale_get_display_language('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo locale_get_display_language('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo locale_get_display_language('sl-Latn-IT-nedis', 'de');
?>

   
```

Ejemplo con `locale_get_display_language`, POO

```php
<?php
echo Locale::getDisplayLanguage('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo Locale::getDisplayLanguage('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo Locale::getDisplayLanguage('sl-Latn-IT-nedis', 'de');
?>

   
```

El ejemplo anterior mostrará:

    Slovenian;
    slov\xc3\xa8ne;
    Slowenisch

      

## Véase también

`locale_get_display_name`, `locale_get_display_script`, `locale_get_display_region`, `locale_get_display_variant`
