---
title: Collator::create
description: Creación de un collator
source_url: https://www.php.net/manual/es/collator.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/collator/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 39390
---

Collator::create

collator_create

Creación de un collator

## Descripción

Estilo orientado a objetos

```php
public static Collator::create(string $locale): Collator
```php

Estilo procedimental

```php
collator_create(string $locale): Collator
```

Las cadenas serán comparadas y ordenadas con convenciones locales.

## Parámetros

`locale`  
La configuración local cuya reglas de collation deben ser respetadas. Valores especiales pueden ser pasados en este argumento: si un `string` vacío es pasado, la configuración local por omisión será utilizada. Si la palabra clave `"root"` es pasada, las reglas [UCA](https://www.unicode.org/reports/tr10/) serán utilizadas.

## Valores devueltos

Retorna una nueva instancia de la clase `Collator`, o `null` en caso de error.

## Ejemplos

Ejemplo con `collator_create`

```php
<?php
$coll = collator_create( 'en_US' );

if( !isset( $coll ) ) {
    printf( "Fallo al crear el collator: %s\n", intl_get_error_message() );
    exit( 1 );
}
?>

    
```

## Véase también

`Collator::__construct`
