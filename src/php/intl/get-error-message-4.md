---
title: NumberFormatter::getErrorMessage
description: Lee el último mensaje de error del formateador
source_url: https://www.php.net/manual/es/numberformatter.geterrormessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/get-error-message.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42240
---

NumberFormatter::getErrorMessage

numfmt_get_error_message

Lee el último mensaje de error del formateador

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::getErrorMessage(): string
```php

Estilo procedimental

```php
numfmt_get_error_message(NumberFormatter $formatter): string
```

Lee el mensaje de error generado por la última función del formateador.

## Parámetros

`formatter`  
El objeto `NumberFormatter`.

## Valores devueltos

Devuelve el mensaje de error de la última llamada al formateador.

## Ejemplos

Ejemplo con `numfmt_get_error_message`, Estilo procedimental

```php
<?php
$fmt = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
$data = numfmt_format($fmt, 1234567.891234567890000);
if(intl_is_failure(numfmt_get_error_code($fmt))) {
    report_error("Error de formateador");
}
?>

   
```

Ejemplo con `numfmt_get_error_code`, estilo POO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
$fmt->format(1234567.891234567890000);
if(intl_is_failure($fmt->getErrorCode())) {
    report_error("Error de formateador");
}
?>

   
```

## Véase también

`numfmt_get_error_code`, `intl_get_error_code`, `intl_is_failure`
