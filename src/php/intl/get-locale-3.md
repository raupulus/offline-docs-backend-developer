---
title: MessageFormatter::getLocale
description: Lee la configuración local con la que el formateador fue creado
source_url: https://www.php.net/manual/es/messageformatter.getlocale.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/get-locale.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42080
---

MessageFormatter::getLocale

msgfmt_get_locale

Lee la configuración local con la que el formateador fue creado

## Descripción

Estilo orientado a objetos

```php
public MessageFormatter::getLocale(): string
```php

Estilo procedimental

```php
msgfmt_get_locale(MessageFormatter $formatter): string
```

Lee la configuración local con la que el formateador fue creado.

## Parámetros

`formatter`  
Un objeto de formateador de mensajes `MessageFormatter`

## Valores devueltos

El nombre de la configuración local

## Ejemplos

Ejemplo con `msgfmt_get_locale`, estilo procedimental

```php
<?php
$fmt = msgfmt_create('en_US', "Nombre {0,number}");
echo msgfmt_get_locale($fmt);
?>

   
```

Ejemplo con `msgfmt_get_locale`, estilo POO

```php
<?php
$fmt = new MessageFormatter('en_US', "Nombre {0,number}");
echo $fmt->getLocale();
?>

   
```

El ejemplo anterior mostrará:

    en_US

      

## Véase también

`msgfmt_create`
