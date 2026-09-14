---
title: ps_findfont
description: Carga una fuente
source_url: https://www.php.net/manual/es/function.ps-findfont.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ps/functions/ps-findfont.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ps
translation_status: ready
translation_reviewed: true
translation_revision: b8758b060
order: 65790
---

ps_findfont

Carga una fuente

## Descripción

```php
ps_findfont(resource $psdoc, string $fontname, string $encoding, [bool $embed]): int
```php

`ps_findfont` carga una fuente para su uso posterior. Antes de que el texto sea escrito con la fuente cargada, debe ser fijada con `ps_setfont`. Esta función debe tener el archivo de métricas de la fuente "adobe" para calcular el espacio utilizado por los caracteres. Una fuente que se carga en una página solo estará disponible en esa página. Las fuentes que se utilizarán en todo el documento deben ser cargadas antes de la primera llamada a `ps_begin_page`. La llamada a `ps_findfont` entre páginas hará que esta fuente esté disponible para todas las páginas siguientes.

El nombre del archivo afm debe ser `fontname``.afm`. Si la fuente debe ser incorporada, el archivo `fontname``.pfb` que contiene el dibujo de la fuente también debe estar presente.

La llamada a `ps_findfont` antes de la primera página requiere mostrar el encabezado del postscript que incluye el BoundingBox para el documento completo. Normalmente, el BoundingBox se fija con la primera llamada a `ps_begin_page` que ahora viene después de `ps_findfont`. En consecuencia, el BoundingBox no ha sido fijado y se lanzará un error cuando `ps_findfont` sea llamada. Para prever esta situación, debe llamarse a la función `ps_set_parameter` para fijar el BoundingBox antes de que `ps_findfont` sea llamada.

## Parámetros

`psdoc`  
Identificador de un archivo postscript devuelto por `ps_new`.

`fontname`  
El nombre de la fuente.

`encoding`  
`ps_findfont` intentará cargar el archivo pasado en el argumento `encoding`. Los archivos de codificación tienen la misma sintaxis que los utilizados por `dvips(1)`. Contienen un vector de codificación de fuente (que actualmente no se utiliza, pero que debe estar presente) y una lista de ligaduras adicionales para extender la lista de ligaduras derivadas del archivo AFM.

`encoding` puede ser `null` o una `string` vacía si se desea utilizar la codificación por omisión (TeXBase1).

Si la codificación se establece en `builtin` entonces no habrá codificación adicional y se utilizará la codificación específica de la fuente. Esto es muy útil para fuentes con símbolos.

`embed`  
Si se establece en un valor \>0, la fuente será incorporada en el documento. Esto requiere la presencia del archivo de dibujo (.pfb).

## Valores devueltos

Devuelve un identificador de la fuente o cero en caso de error. El identificador es un número positivo.

## Véase también

`ps_begin_page`, `ps_setfont`
