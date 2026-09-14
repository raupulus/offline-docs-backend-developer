---
title: MessageFormatter::getPattern
description: Lee el modelo utilizado por el formateador de mensajes
source_url: https://www.php.net/manual/es/messageformatter.getpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/get-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42090
---

MessageFormatter::getPattern

msgfmt_get_pattern

Lee el modelo utilizado por el formateador de mensajes

## Descripción

Estilo orientado a objetos

```php
public MessageFormatter::getPattern(): string
```php

Estilo procedimental

```php
msgfmt_get_pattern(MessageFormatter $formatter): string
```

Lee el modelo utilizado por el formateador de mensajes.

## Parámetros

`formatter`  
Un objeto de formateador de mensajes `MessageFormatter`

## Valores devueltos

La `string` de modelo del formateador de mensajes, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `msgfmt_get_pattern`, estilo procedimental

```php
<?php
$fmt = msgfmt_create( "en_US", "{0, number} singes sur {1, number} arbres" );
echo "Modelo por omisión : '" . msgfmt_get_pattern( $fmt ) . "'\n";
echo "Resultado de formato :  " . msgfmt_format( $fmt, array(123, 456) ) . "\n";

msgfmt_set_pattern( $fmt, "{0, number} arbres hosting {1, number} singes" );
echo "Nuevo modelo :  '" . msgfmt_get_pattern( $fmt ) . "'\n";
echo "Resultado de formato : " . msgfmt_format( $fmt, array(123, 456) ) . "\n";
?>

   
```

Ejemplo con `msgfmt_get_pattern`, estilo POO

```php
<?php
$fmt = new MessageFormatter( "en_US", "{0, number} singes sur {1, number} arbres" );
echo "Modelo por omisión : '" . $fmt->getPattern() . "'\n";
echo "Resultado de formato :  " . $fmt->format(array(123, 456)) . "\n";

$fmt->setPattern("{0, number} arbres hosting {1, number} singes" );
echo "Nuevo modelo :  '" . $fmt->getPattern() . "'\n";
echo "Resultado de formato : " . $fmt->format(array(123, 456)) . "\n";
?>

   
```

El ejemplo anterior mostrará:

    Modelo por omisión : '{0,number} singes sur {1,number} arbres'
    Resultado de formato :  123 singes sur 456 arbres
    Nuevo modelo :  '{0,number} arbres hosting {1,number} singes'
    Resultado de formato : 123 arbres hosting 456 singes

      

## Véase también

`msgfmt_create`, `msgfmt_set_pattern`
