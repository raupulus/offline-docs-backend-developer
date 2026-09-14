---
title: NumberFormatter::getErrorCode
description: Obtener el último código de error del formateador
source_url: https://www.php.net/manual/es/numberformatter.geterrorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/numberformatter/get-error-code.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: bce2cb849
order: 42230
---

NumberFormatter::getErrorCode

numfmt_get_error_code

Obtener el último código de error del formateador

## Descripción

Estilo orientado a objetos

```php
public NumberFormatter::getErrorCode(): int
```php

Estilo procedimental

```php
numfmt_get_error_code(NumberFormatter $formatter): int
```

Obtiene el código de error de la última función ejecutada por el formateador.

## Parámetros

`formatter`  
Objeto `NumberFormatter`.

## Valores devueltos

Devuelve el código de error de la última llamada al formateador.

## Ejemplos

Ejemplo de `numfmt_get_error_code`

```php
<?php
$fmt  = numfmt_create( 'de_DE', NumberFormatter::DECIMAL );
$data = numfmt_format($fmt, 1234567.891234567890000);
if (intl_is_failure(numfmt_get_error_code($fmt))) {
    echo 'Error del formateador';
}
?>

   
```

Ejemplo OO

```php
<?php
$fmt = new NumberFormatter( 'de_DE', NumberFormatter::DECIMAL );
$fmt->format(1234567.891234567890000);
if (intl_is_failure($fmt->getErrorCode())) {
    echo 'Error del formateador';
}
?>

   
```

## Véase también

`numfmt_get_error_message`, `intl_get_error_code`, `intl_is_failure`
