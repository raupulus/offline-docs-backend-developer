---
title: MessageFormatter::format
description: Formatea un mensaje
source_url: https://www.php.net/manual/es/messageformatter.format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42050
---

MessageFormatter::format

msgfmt_format

Formatea un mensaje

## Descripción

Estilo orientado a objetos

```php
public MessageFormatter::format(array $values): string
```php

Estilo procedimental

```php
msgfmt_format(MessageFormatter $formatter, array $values): string
```

Formatea un mensaje sustituyendo los datos en las cadenas de modelo, según las convenciones locales.

## Parámetros

`formatter`  
Un objeto de formateador de mensajes `MessageFormatter`

`values`  
Los argumentos a insertar en las cadenas

## Valores devueltos

La cadena formateada, `false` si ocurre un error.

## Ejemplos

Ejemplo con `msgfmt_format`, estilo procedimental

```php
<?php
$fmt = msgfmt_create("en_US", "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} singes par arbre");
echo msgfmt_format($fmt, array(4560, 123, 4560/123));
$fmt = msgfmt_create("de", "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum");
echo msgfmt_format($fmt, array(4560, 123, 4560/123));
?>

   
```

Ejemplo con `msgfmt_format`, estilo POO

```php
<?php
$fmt = new MessageFormatter("en_US", "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} singes par arbre");
echo $fmt->format(array(4560, 123, 4560/123));
$fmt = new MessageFormatter("de", "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum");
echo $fmt->format(array(4560, 123, 4560/123));
?>

   
```

El ejemplo anterior mostrará:

    4,560 singes sur 123 arbres font 37.073 singes par arbre
    4.560 Affen über 123 Bäume um 37,073 Affen pro Baum

      

## Véase también

`msgfmt_create`, `msgfmt_parse`, `msgfmt_format_message`, `msgfmt_get_error_code`, `msgfmt_get_error_message`
