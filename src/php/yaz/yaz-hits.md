---
title: yaz_hits
description: Devuelve el número de éxitos de la última búsqueda
source_url: https://www.php.net/manual/es/function.yaz-hits.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-hits.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107860
---

yaz_hits

Devuelve el número de éxitos de la última búsqueda

## Descripción

```php
yaz_hits(resource $id, [array $searchresult]): int
```php

`yaz_hits`Devuelve el número de éxitos de la última búsqueda.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`searchresult`  
Array de resultados para obtener información de resultados de búsqueda detallada.

## Valores devueltos

Devuelve el número de éxitos de la última búsqueda o 0 si no se ha realizado ninguna búsqueda.

La matriz de resultados de búsqueda (si se suministra) contiene información que es devuelta por un servidor Z39.50 en el formato SearchResult-1 parte de una respuesta de búsqueda. El formato SearchResult-1 puede utilizarse para obtener información acerca de recuentos de éxitos para varias partes de la consulta (subconsulta). En particular, es posible obtener recuentos de éxitos para los términos de búsqueda individuales en una consulta. Información para la primer subconsulta está en \$array\[0\], segunda subconsulta en \$array\[1\], y así sucesivamente.

| Elemento              | Descripción                                        |
|-----------------------|----------------------------------------------------|
| `id`                  | Sub consulta ID2 (string)                          |
| `count`               | Conteo resultados / éxitos (integer)               |
| `subquery.term`       | Término sub consulta(string)                       |
| `interpretation.term` | Interpretación de término de sub consulta (string) |
| `recommendation.term` | Término recomendado de sub consulta (string)       |

Miembros de searchresult

> [!NOTE]
> El centro de SearchResult requiere PECL YAZ 1.0.5 o posterior y YAZ 2.1.9 o posterior.

> [!NOTE]
> Muy pocas implementaciones Z39.50 soportan la instalación de SearchResult.
