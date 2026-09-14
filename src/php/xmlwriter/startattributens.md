---
title: XMLWriter::startAttributeNs
description: Crea un atributo para el espacio de nombres
source_url: https://www.php.net/manual/es/xmlwriter.startattributens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/startattributens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_revision: 4a742792d
order: 103730
---

XMLWriter::startAttributeNs

xmlwriter_start_attribute_ns

Crea un atributo para el espacio de nombres

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::startAttributeNs(string $prefix, string $name, string $namespace): bool
```php

Estilo procedimental

```php
xmlwriter_start_attribute_ns(XMLWriter $writer, string $prefix, string $name, string $namespace): bool
```

Crea un atributo para el espacio de nombres.

## Parámetros

`writer`  
Únicamente para llamadas procedimentales. La instancia `XMLWriter` que es modificada. Este objeto proviene de una llamada a `xmlwriter_open_uri` o `xmlwriter_open_memory`.

`prefix`  
El prefijo para el espacio de nombres.

`name`  
El nombre del atributo.

`namespace`  
La URI del espacio de nombres. Si el `namespace` vale `null`, la declaración del espacio de nombres será omitida.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `writer` ahora espera una instancia de `XMLWriter` anteriormente, se esperaba una `resource`. |
| 8.0.0 | `prefix` es ahora nullable. |

## Véase también

XMLWriter::startAttribute, XMLWriter::endAttribute, XMLWriter::writeAttribute, XMLWriter::writeAttributeNs
