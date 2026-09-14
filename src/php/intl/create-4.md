---
title: MessageFormatter::create
description: Construye un nuevo formateador de mensajes
source_url: https://www.php.net/manual/es/messageformatter.create.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/create.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42030
---

MessageFormatter::create

MessageFormatter::\_\_construct

msgfmt_create

Construye un nuevo formateador de mensajes

## Descripción

Estilo orientado a objetos (método)

```php
public static MessageFormatter::create(string $locale, string $pattern): MessageFormatter
```php

Estilo orientado a objetos (constructor)

```php
public MessageFormatter::__construct(string $locale, string $pattern)
```

Estilo procedimental

```php
msgfmt_create(string $locale, string $pattern): MessageFormatter
```php

Construye un nuevo formateador de mensajes.

## Parámetros

`locale`  
La configuración local a utilizar para el formato de los argumentos

`pattern`  
La cadena en la que se deben insertar los datos. El modelo utiliza una sintaxis que acepta comillas simples. Ver [Quoting/Escaping](https://unicode-org.github.io/icu/userguide/format_parse/messages/#quotingescaping) para más detalles.

## Valores devueltos

Un objeto de formateador de mensajes `MessageFormatter`, o `null` en caso de fallo.

## Errores/Excepciones

Cuando se invoca como constructor, `IntlException` es lanzado en caso de fallo.

## Ejemplos

Ejemplo con `msgfmt_create`, estilo procedimental

```
<?php
$fmt = msgfmt_create("en_US", "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} singes par arbre");
echo msgfmt_format($fmt, array(4560, 123, 4560/123));
$fmt = msgfmt_create("de", "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum");
echo msgfmt_format($fmt, array(4560, 123, 4560/123));
?>

   
```php

Ejemplo con `msgfmt_create`, estilo procedimental

```
<?php
$fmt = new MessageFormatter("en_US", "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} singes par arbre");
echo $fmt->format(array(4560, 123, 4560/123));
$fmt = new MessageFormatter("de", "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum");
echo $fmt->format(array(4560, 123, 4560/123));
?>

   
```php

El ejemplo anterior mostrará:

       
    4,560 singes sur 123 arbres font 37.073 singes par arbre
    4.560 Affen über 123 Bäume um 37,073 Affen pro Baum

      

## Véase también

`msgfmt_format`, `msgfmt_parse`, `msgfmt_get_error_code`, `msgfmt_get_error_message`
