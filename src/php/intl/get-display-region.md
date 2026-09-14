---
title: Locale::getDisplayRegion
description: Devuelve un nombre para la región de la configuración local
source_url: https://www.php.net/manual/es/locale.getdisplayregion.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-display-region.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41900
---

Locale::getDisplayRegion

locale_get_display_region

Devuelve un nombre para la región de la configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getDisplayRegion(string $locale, [string $displayLocale]): string
```php

Estilo procedimental

```php
locale_get_display_region(string $locale, [string $displayLocale]): string
```

Devuelve un nombre para la región de la configuración local. Si `null` es pasado, se utiliza la configuración local por defecto.

## Parámetros

`locale`  
La configuración local de la cual se debe extraer el nombre de la región.

`displayLocale`  
Un formato opcional para mostrar el nombre de la región.

## Valores devueltos

El nombre de la región de la `locale`, en el formato `displayLocale`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 8.0.0   | `displayLocale` ahora es nullable. |

## Ejemplos

Ejemplo con `locale_get_display_region`, procedimental

```php
<?php
echo locale_get_display_region('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo locale_get_display_region('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo locale_get_display_region('sl-Latn-IT-nedis', 'de');
?>

   
```

Ejemplo con `locale_get_display_region`, POO

```php
<?php
echo Locale::getDisplayRegion('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo Locale::getDisplayRegion('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo Locale::getDisplayRegion('sl-Latn-IT-nedis', 'de');
?>

   
```

El ejemplo anterior mostrará:

    Italy;
    Italie;
    Italien

      

## Véase también

`locale_get_display_name`, `locale_get_display_language`, `locale_get_display_script`, `locale_get_display_variant`
