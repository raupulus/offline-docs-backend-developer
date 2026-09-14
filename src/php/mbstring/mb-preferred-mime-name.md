---
title: mb_preferred_mime_name
description: Detecta la codificación MIME
source_url: https://www.php.net/manual/es/function.mb-preferred-mime-name.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-preferred-mime-name.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45330
---

mb_preferred_mime_name

Detecta la codificación MIME

## Descripción

```php
mb_preferred_mime_name(string $encoding): string
```php

Obtiene el nombre de la codificación MIME de una cadena.

## Parámetros

`encoding`  
La codificación a verificar.

## Valores devueltos

El nombre de la codificación MIME para la codificación `encoding`, o `false` si no se prevé ningún juego de caracteres para la `encoding` dada.

## Ejemplos

Ejemplo con `mb_preferred_mime_name`

```
<?php
$outputenc = "sjis-win";
mb_http_output($outputenc);
ob_start("mb_output_handler");
header("Content-Type: text/html; charset=" . mb_preferred_mime_name($outputenc));
?>

    
```php
