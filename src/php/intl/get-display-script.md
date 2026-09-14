---
title: Locale::getDisplayScript
description: Devuelve el nombre del script de la configuración local
source_url: https://www.php.net/manual/es/locale.getdisplayscript.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/locale/get-display-script.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 41910
---

Locale::getDisplayScript

locale_get_display_script

Devuelve el nombre del script de la configuración local

## Descripción

Estilo orientado a objetos

```php
public static Locale::getDisplayScript(string $locale, [string $displayLocale]): string
```php

Estilo procedimental

```php
locale_get_display_script(string $locale, [string $displayLocale]): string
```

Devuelve el nombre del script de la configuración local. Si `null` es pasado, se utiliza la configuración local por omisión.

## Parámetros

`locale`  
La configuración local de la cual se debe devolver el script.

`displayLocale`  
Un formato opcional para mostrar el nombre del script.

## Valores devueltos

Muestra el nombre del script de la `locale` en el formato indicado por `displayLocale`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                        |
|---------|------------------------------------|
| 8.0.0   | `displayLocale` ahora es nullable. |

## Ejemplos

Ejemplo con `locale_get_display_script`, procedimental

```php
<?php
echo locale_get_display_script('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo locale_get_display_script('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo locale_get_display_script('sl-Latn-IT-nedis', 'de');
?>

   
```

Ejemplo con `locale_get_display_script`, POO

```php
<?php
echo Locale::getDisplayScript('sl-Latn-IT-nedis', 'en');
echo ";\n";
echo Locale::getDisplayScript('sl-Latn-IT-nedis', 'fr');
echo ";\n";
echo Locale::getDisplayScript('sl-Latn-IT-nedis', 'de');
?>

   
```

El ejemplo anterior mostrará:

    Latin;
    latin;
    Lateinisch

      

## Véase también

`locale_get_display_name`, `locale_get_display_language`, `locale_get_display_region`, `locale_get_display_variant`
