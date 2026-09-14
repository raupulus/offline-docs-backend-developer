---
title: posix_getcwd
description: Nombre de la ruta del directorio actual
source_url: https://www.php.net/manual/es/function.posix-getcwd.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/posix/functions/posix-getcwd.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: posix
translation_status: ready
translation_reviewed: false
translation_revision: f8854f6a6
order: 65160
---

posix_getcwd

Nombre de la ruta del directorio actual

## Descripción

```php
posix_getcwd(): string
```php

Obtiene el nombre de ruta absoluta del directorio de trabajo actual del script. En caso de error se establece errno, que puede ser verificado usando `posix_get_last_error`

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `string` del nombre de la ruta absoluta en caso de éxito. En caso de error devuelve `false` y se establece errno, que puede ser verificado con `posix_get_last_error`.

## Ejemplos

Ejemplo de `posix_getcwd`

Este ejemplo devolverá la ruta absoluta del directorio actual de trabajo del script.

```
<?php
echo 'Mi directorio actual de trabajo es '.posix_getcwd();
?>

    
```php

## Notas

> [!NOTE]
> Esta función puede fallar si
>
> - El permiso de Lectura o Búsqueda fue denegado
>
> - El nombre de la ruta ya no existe
