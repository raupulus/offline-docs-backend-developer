---
title: virtual
description: Efectúa una subpetición Apache
source_url: https://www.php.net/manual/es/function.virtual.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apache/functions/virtual.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apache
translation_status: ready
translation_reviewed: true
translation_revision: a331ac8a8
order: 4830
---

virtual

Efectúa una subpetición Apache

## Descripción

```php
virtual(string $uri): bool
```php

`virtual` es una función específica del servidor Apache. Es similar a la directiva "`<!--#include virtual...-->`" cuando se utiliza el módulo `mod_include` de Apache. Esta función efectúa una subpetición Apache. Es muy útil cuando se desea analizar scripts CGI, archivos `.shtml` o cualquier otro tipo de archivo a través del servidor Apache. Se debe tener en cuenta que al utilizarse con scripts CGI, estos deben generar un encabezado válido, es decir, al menos un encabezado `Content-Type`.

Para ejecutar una subpetición, todos los búferes son detenidos y vaciados hacia el navegador, los encabezados restantes también lo son.

## Parámetros

`uri`  
El archivo sobre el cual se ejecutará el comando virtual.

## Valores devueltos

Ejecuta un comando virtual en caso de éxito o devuelve `false` en caso de error.

## Ejemplos

Ver la función `apache_note` para un ejemplo.

## Notas

> [!WARNING]
> La cadena requerida puede ser pasada al archivo incluido, pero `$_GET` es copiado desde el script padre y solo la variable `$_SERVER['QUERY_STRING']` es transmitida al pasar la cadena requerida. La cadena requerida pasada funciona únicamente bajo Apache 2. Los archivos solicitados no son listados en los logs de acceso de Apache.

> [!NOTE]
> Las variables de entorno establecidas en el archivo solicitado no son visibles en el archivo llamador.

> [!NOTE]
> Esta función puede ser utilizada sobre archivos PHP. Sin embargo, se recomienda utilizar `include` o `require` para archivos PHP.

## Véase también

`apache_note`
