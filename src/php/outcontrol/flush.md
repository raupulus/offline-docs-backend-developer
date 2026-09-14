---
title: flush
description: Vacía los búferes de salida del sistema
source_url: https://www.php.net/manual/es/function.flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: false
translation_revision: 77ae3334a
order: 59730
---

flush

Vacía los búferes de salida del sistema

## Descripción

```php
flush(): void
```php

Vacía los búferes de escritura del sistema de PHP y del backend utilizado por PHP (por ejemplo: CGI, un servidor web). En un entorno de línea de comandos, `flush` intentará vaciar únicamente el contenido de los búferes, mientras que en un contexto web, los encabezados y el contenido de los búferes son vaciados.

> [!NOTE]
> `flush` puede no poder sortear el esquema de almacenamiento en búfer del servidor web y no tiene ningún efecto sobre un almacenamiento en búfer lado-cliente en el navegador.

> [!NOTE]
> Esta función no tiene ningún efecto sobre los gestores de salida de nivel usuario tales como aquellos iniciados por `ob_start` o `output_add_rewrite_var`.

> [!WARNING]
> `flush` puede interferir con los gestores de salida que definen y envían encabezados en un contexto web (por ejemplo, `ob_gzhandler`) al enviar encabezados antes de que estos gestores puedan hacerlo.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción                                                       |
|---------|-------------------------------------------------------------------|
| 8.4.0   | El envío de encabezados sin cuerpo tendrá éxito ahora en FastCGI. |

## Véase también

`ob_flush`, `ob_clean`, `ob_end_flush`, `ob_end_clean`
