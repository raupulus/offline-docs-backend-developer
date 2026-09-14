---
title: Locale::getDisplayName
description: Devuelve un nombre de visualización correcto para una configuración local
source_url: https://www.php.net/manual/es/locale.getdisplayname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-display-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41890
---

Locale::getDisplayName

locale_get_display_name

Devuelve un nombre de visualización correcto para una configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getDisplayName(string $locale, [string $displayLocale]): string
```php

Estilo procedimental

```php
locale_get_display_name(string $locale, [string $displayLocale]): string
```

Devuelve un nombre de visualización correcto para una configuración local. Si `locale` es `null`, se utiliza la configuración local por omisión.

## Parámetros

`locale`  
La configuración local de la que se debe devolver un nombre de visualización.

`displayLocale`  
Un formato de visualización opcional

## Valores devueltos

El nombre de visualización de la configuración local, en el formato dado por `displayLocale`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 8.0.0   | `displayLocale` ahora es nullable. |

## Ejemplos

Ejemplo con `locale_get_display_name`, procedimental

```php
<?php
echo locale_get_display_name('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo locale_get_display_name('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo locale_get_display_name('sl-Latn-IT-nedis', 'de');
?>

   
```

Ejemplo con `locale_get_display_name`, POO

```php
<?php
echo Locale::getDisplayName('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo Locale::getDisplayName('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo Locale::getDisplayName('sl-Latn-IT-nedis', 'de');
?>

   
```

El ejemplo anterior mostrará:

    Slovenian (Latin, Italy, Natisone dialect);
    slov\xc3\xa8ne (latin, Italie, dialecte de Natisone);
    Slowenisch (Lateinisch, Italien, NEDIS)

## Véase también

`locale_get_display_language`, `locale_get_display_script`, `locale_get_display_region`, `locale_get_display_variant`
