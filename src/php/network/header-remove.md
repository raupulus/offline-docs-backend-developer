---
title: header_remove
description: Elimina un encabezado HTTP
source_url: https://www.php.net/manual/es/function.header-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/header-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: 4e6f0774f
order: 56380
---

header_remove

Elimina un encabezado HTTP

## Descripción

```php
header_remove([string $name]): void
```php

Elimina un encabezado HTTP previamente añadido con `header`.

## Parámetros

`name`  
El nombre del encabezado a eliminar. Si es `null`, todos los encabezados definidos previamente son eliminados.

> [!NOTE]
> Este argumento no distingue entre mayúsculas y minúsculas.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción               |
|---------|---------------------------|
| 8.0.0   | `name` ahora es nullable. |

## Ejemplos

Eliminar un encabezado HTTP con `header_remove`

```
<?php
header("X-Foo: Bar");
header("X-Bar: Baz");
header_remove("X-Foo");
?>

    
```php

Resultado del ejemplo anterior es similar a:

    X-Bar: Baz

Eliminar todos los encabezados HTTP con `header_remove`

```
<?php
header("X-Foo: Bar");
header("X-Bar: Baz");
header_remove();
?>

    
```php

Resultado del ejemplo anterior es similar a:

## Notas

> [!CAUTION]
> Esta función elimina *todos* los encabezados configurados por PHP, incluyendo cookies, sesiones y los encabezados `X-Powered-By`.

> [!NOTE]
> Los encabezados solo serán accesibles y se mostrarán cuando se utilice un SAPI que los soporte.

## Véase también

`header`, `headers_sent`
