---
title: mailparse_determine_best_xfer_encoding
description: Obtiene la mejor forma de codificar
source_url: https://www.php.net/manual/es/function.mailparse-determine-best-xfer-encoding.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mailparse/functions/mailparse-determine-best-xfer-encoding.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mailparse
translation_status: ready
translation_revision: 01bd007b0
order: 44310
---

mailparse_determine_best_xfer_encoding

Obtiene la mejor forma de codificar

## Descripción

```php
mailparse_determine_best_xfer_encoding(resource $fp): string
```php

Encuentra la mejor forma de codificar el contenido leído del apuntador de archivo dado.

## Parámetros

`fp`  
Un apuntador de archivo válido, que reciba operaciones de búsqueda.

## Valores devueltos

Devuelve una de las codificaciones de caracteres soportadas por el módulo [mbstring](#ref.mbstring).

## Ejemplos

Ejemplo de `mailparse_determine_best_xfer_encoding`

```
<?php

$aa = fopen('alguncorreo.eml', 'r');
echo 'Mejor codificación: ' . mailparse_determine_best_xfer_encoding($aa);

?>

   
```php

Resultado del ejemplo anterior es similar a:

    Mejor codificación: 7bit
