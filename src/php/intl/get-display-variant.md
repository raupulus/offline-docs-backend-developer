---
title: Locale::getDisplayVariant
description: Devuelve un nombre para la variante de la configuración local
source_url: https://www.php.net/manual/es/locale.getdisplayvariant.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-display-variant.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41920
---

Locale::getDisplayVariant

locale_get_display_variant

Devuelve un nombre para la variante de la configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getDisplayVariant(string $locale, [string $displayLocale]): string
```php

Estilo procedimental

```php
locale_get_display_variant(string $locale, [string $displayLocale]): string
```

Devuelve un nombre para la variante de la configuración local. Si `null` es pasado, se utiliza la configuración local por defecto.

## Parámetros

`locale`  
La configuración local de la cual extraer el nombre de la región.

`displayLocale`  
Un formato opcional para mostrar el nombre de la región.

## Valores devueltos

El nombre de la variante de la `locale`, en el formato `displayLocale`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 8.0.0   | `displayLocale` ahora es nullable. |

## Ejemplos

Ejemplo con `locale_get_display_variant`, procedimental

```php
    
<?php
echo locale_get_display_variant('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo locale_get_display_variant('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo locale_get_display_variant('sl-Latn-IT-nedis', 'de');
?>

   
```

Ejemplo con `locale_get_display_variant`, POO

```php
<?php
echo Locale::getDisplayVariant('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo Locale::getDisplayVariant('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo Locale::getDisplayVariant('sl-Latn-IT-nedis', 'de');
?>

   
```

El ejemplo anterior mostrará:

    Natisone dialect;
    dialecte de Natisone;
    NEDIS
      
      

## Véase también

`locale_get_display_name`, `locale_get_display_language`, `locale_get_display_script`, `locale_get_display_region`
