---
title: MessageFormatter::getErrorMessage
description: Lee el mensaje de error de la última operación
source_url: https://www.php.net/manual/es/messageformatter.geterrormessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/messageformatter/get-error-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: true
translation_revision: 1976eae0d
order: 42070
---

MessageFormatter::getErrorMessage

msgfmt_get_error_message

Lee el mensaje de error de la última operación

## Descripción

Estilo orientado a objetos

```php
public MessageFormatter::getErrorMessage(): string
```php

Estilo procedimental

```php
msgfmt_get_error_message(MessageFormatter $formatter): string
```

Lee el mensaje de error de la última operación del formateador de mensajes.

## Parámetros

`formatter`  
Un objeto de formateador de mensajes `MessageFormatter`

## Valores devueltos

La descripción del último error.

## Ejemplos

Ejemplo con `msgfmt_get_error_message`, estilo procedimental

```php
<?php
$fmt = msgfmt_create("en_US", "{0, number} singes sur {1, number} arbres");
$str = msgfmt_format($fmt, array());
if(!$str) {
    echo "Error: ".msgfmt_get_error_message($fmt) . " (" . msgfmt_get_error_code($fmt) . ")\n";
}
?>

   
```

Ejemplo con `msgfmt_get_error_message`, estilo POO

```php
<?php
$fmt = new MessageFormatter("en_US", "{0, number} singes sur {1, number} arbres");
$str = $fmt->format(array());
if(!$str) {
    echo "Error: ".$fmt->getErrorMessage() . " (" . $fmt->getErrorCode() . ")\n";
}
?>

   
```

El ejemplo anterior mostrará:

    Error: msgfmt_format: not enough parameters: U_ILLEGAL_ARGUMENT_ERROR (1)

      

## Véase también

`msgfmt_get_error_code`, `intl_get_error_code`, `intl_is_failure`
