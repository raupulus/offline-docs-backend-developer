---
title: MessageFormatter::parseMessage
description: Analiza rápidamente una cadena
source_url: https://www.php.net/manual/es/messageformatter.parsemessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/parse-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42100
---

MessageFormatter::parseMessage

msgfmt_parse_message

Analiza rápidamente una cadena

## Descripción

Estilo orientado a objetos

```php
public static MessageFormatter::parseMessage(string $locale, string $pattern, string $message): array
```php

Estilo procedimental

```php
msgfmt_parse_message(string $locale, string $pattern, string $message): array
```

Analiza la cadena de entrada sin crear explícitamente un objeto formateador. Utilice esta función cuando la operación de formato se realiza una sola vez, y no requiere parámetros ni estado.

## Parámetros

`locale`  
La configuración local a utilizar para analizar las partes de la cadena

`pattern`  
El patrón a utilizar para analizar `message`.

`message`  
La `string` a analizar, conforme a `pattern`.

## Valores devueltos

Un `array` que contiene los elementos extraídos, o `false` en caso de error.

## Ejemplos

Ejemplo con `msgfmt_parse_message`, estilo procedimental

```php
<?php
$fmt = msgfmt_parse_message('en_US', "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} signes par arbre",
                            "4,560 singes sur 123 arbres font 37.073 signes par arbre");
var_export($fmt);

$fmt = msgfmt_parse_message('de', "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum",
                            "4.560 Affen über 123 Bäume um 37,073 Affen pro Baum");
var_export($fmt);
?>

   
```

Ejemplo con `msgfmt_parse_message`, estilo POO

```php
<?php
$fmt = MessageFormatter::parseMessage('en_US', "{0,number,integer} singes sur {1,number,integer} arbres font {2,number} signes par arbre",
                            "4,560 singes sur 123 arbres font 37.073 signes par arbre");
var_export($fmt);

$fmt = MessageFormatter::parseMessage('de', "{0,number,integer} Affen über {1,number,integer} Bäume um {2,number} Affen pro Baum",
                            "4.560 Affen über 123 Bäume um 37,073 Affen pro Baum");
var_export($fmt);
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

`msgfmt_create`, `msgfmt_format_message`, `msgfmt_parse`
