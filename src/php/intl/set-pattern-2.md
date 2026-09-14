---
title: MessageFormatter::setPattern
description: Configura el patrón utilizado por el formateador
source_url: https://www.php.net/manual/es/messageformatter.setpattern.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/set-pattern.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42120
---

MessageFormatter::setPattern

msgfmt_set_pattern

Configura el patrón utilizado por el formateador

## Descripción

Estilo orientado a objetos

```php
public MessageFormatter::setPattern(string $pattern): bool
```php

Estilo procedimental

```php
msgfmt_set_pattern(MessageFormatter $formatter, string $pattern): bool
```

Configura el patrón utilizado por el formateador.

## Parámetros

`formatter`  
Un objeto de formateador de mensajes `MessageFormatter`

`pattern`  
La cadena de patrón utilizada por el formateador de mensajes. El patrón utiliza una sintaxis que acepta comillas; Ver [Quoting/Escaping](https://unicode-org.github.io/icu/userguide/format_parse/messages/#quotingescaping) para más detalles.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `msgfmt_set_pattern`, estilo procedimental

```php
<?php
$fmt = msgfmt_create( "en_US", "{0, number} singes sur {1, number} arbres" );
echo "Patrón por omisión : '" . msgfmt_get_pattern( $fmt ) . "'\n";
echo "Resultado formateado : " . msgfmt_format( $fmt, array(123, 456) ) . "\n";

msgfmt_set_pattern( $fmt, "{0, number} arbres accueillant {1, number} singes" );
echo "Nuevo patrón :'" . msgfmt_get_pattern( $fmt ) . "'\n";
echo "Número formateado : " . msgfmt_format( $fmt, array(123, 456) ) . "\n";
?>

   
```

Ejemplo con `msgfmt_set_pattern`, estilo POO

```php
<?php
$fmt = new MessageFormatter( "en_US", "{0, number} singes sur {1, number} arbres" );
echo "Patrón por omisión : '" . $fmt->getPattern() . "'\n";
echo "Resultado formateado : " . $fmt->format(array(123, 456)) . "\n";

$fmt->setPattern("{0, number} arbres accueillant {1, number} singes" );
echo "Nuevo patrón :'" . $fmt->getPattern() . "'\n";
echo "Número formateado : " . $fmt->format(array(123, 456)) . "\n";
?>

   
```

El ejemplo anterior mostrará:

    Patrón por omisión : '{0,number} singes sur {1,number} arbres'
    Resultado formateado : 123 singes sur 456 arbres
    Nuevo patrón :'{0,number} arbres accueillant {1,number} singes'
    Número formateado : 123 arbres accueillant 456 singes

      

## Véase también

`msgfmt_create`, `msgfmt_get_pattern`
