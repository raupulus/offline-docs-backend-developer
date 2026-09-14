---
title: MessageFormatter::parse
description: Analiza una cadena según el modelo
source_url: https://www.php.net/manual/es/messageformatter.parse.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/parse.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42110
---

MessageFormatter::parse

msgfmt_parse

Analiza una cadena según el modelo

## Descripción

Estilo orientado a objetos

```php
public MessageFormatter::parse(string $string): array
```php

Estilo procedimental

```php
msgfmt_parse(MessageFormatter $formatter, string $string): array
```

Analiza la cadena `value` y devuelve los elementos extraídos en forma de `array`.

## Parámetros

`formatter`  
Un objeto de formateador de mensajes `MessageFormatter`

`string`  
La `string` a analizar.

## Valores devueltos

Un `array` que contiene los elementos extraídos, o `false` en caso de error.

## Ejemplos

Ejemplo con `msgfmt_parse`, estilo procedimental

```php
<?php
$fmt = msgfmt_create('en_US', "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} signes par arbre");
$res = msgfmt_parse($fmt, "4,560 singes sur 123 arbres font 37.073 singes par arbre");
var_export($res);

$fmt = msgfmt_create('de', "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum");
$res = msgfmt_parse($fmt, "4.560 Affen über 123 Bäume um 37,073 Affen pro Baum");
var_export($res);
?>

   
```

Ejemplo con `msgfmt_parse`, estilo POO

```php
<?php
$fmt = new MessageFormatter('en_US', "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} signes par arbre");
$res = $fmt->parse("4,560 singes sur 123 arbres font 37.073 singes par arbre");
var_export($res);

$fmt = new MessageFormatter('de', "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum");
$res = $fmt->parse("4.560 Affen über 123 Bäume um 37,073 Affen pro Baum");
var_export($res);
?>

   
```

El ejemplo anterior mostrará:

    array (
      0 => 4560,
      1 => 123,
      2 => 37.073,
    )
    array (
      0 => 4560,
      1 => 123,
      2 => 37.073,
    )

      

## Véase también

`msgfmt_create`, `msgfmt_format`, `msgfmt_parse_message`
