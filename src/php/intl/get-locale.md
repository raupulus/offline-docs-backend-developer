---
title: Collator::getLocale
description: Lee el nombre de la configuración local de un collator
source_url: https://www.php.net/manual/es/collator.getlocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/get-locale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39430
---

Collator::getLocale

collator_get_locale

Lee el nombre de la configuración local de un collator

## Descripción

Estilo orientado a objetos

```php
public Collator::getLocale(int $type): string
```php

Estilo procedimental

```php
collator_get_locale(Collator $object, int $type): string
```

Lee el nombre de la configuración local de un collator

## Parámetros

`object`  
Objeto `Collator`.

`type`  
Puede seleccionarse entre un valor válido o un valor literal de la configuración local (utilizando las constantes `Locale::VALID_LOCALE` y `Locale::ACTUAL_LOCALE`, respectivamente).

## Valores devueltos

El nombre de la configuración local para la cual el collator está configurado. Si el collator ha sido configurado a partir de reglas, o si ha ocurrido un error se devuelve `false`.

## Ejemplos

Ejemplo con `collator_get_locale`

```php
<?php
$coll    = collator_create( 'en_US_California' );
$res_val = collator_get_locale( $coll, Locale::VALID_LOCALE );
$res_act = collator_get_locale( $coll, Locale::ACTUAL_LOCALE );
printf( "Valid locale name: %s\nActual locale name: %s\n",
         $res_val, $res_act );
?>

    
```

El ejemplo anterior mostrará:

    Requested locale name: en_US_California
    Valid locale name: en_US
    Actual locale name: en

## Véase también

`collator_create`
