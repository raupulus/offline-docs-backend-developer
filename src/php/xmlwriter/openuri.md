---
title: XMLWriter::openUri
description: Crea un nuevo XMLWriter, utilizando el URI fuente para la visualización
source_url: https://www.php.net/manual/es/xmlwriter.openuri.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmlwriter/xmlwriter/openuri.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmlwriter
translation_status: ready
translation_reviewed: true
translation_revision: 525aa5f19
order: 103680
---

XMLWriter::openUri

xmlwriter_open_uri

Crea un nuevo XMLWriter, utilizando el URI fuente para la visualización

## Descripción

Estilo orientado a objetos

```php
public XMLWriter::openUri(string $uri): bool
```php

Estilo procedimental

```php
xmlwriter_open_uri(string $uri): XMLWriter
```

Crea un nuevo `XMLWriter`, utilizando el `uri` para la visualización.

## Parámetros

`uri`  
El URI del `resource` para la visualización.

## Valores devueltos

Estilo orientado a objetos : Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Estilo procedimental : Devuelve una nueva instancia de `XMLWriter` para su uso futuro con las funciones xmlwriter en caso de éxito, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | Esta función ahora devuelve una instancia de `XMLWriter` en caso de éxito. Anteriormente, se devolvía un `resource` en este caso. |

## Ejemplos

Escribir directamente XML

Es posible escribir directamente XML utilizando la [envoltura de flujo php://output](#wrappers.php.output).

```php
<?php
$out = new XMLWriter();
$out->openURI('php://output');
?>

   
```

## Notas

> [!NOTE]
> En Windows, los ficheros abiertos con esta función están bloqueados hasta que el objeto XMLWriter sea liberado.

## Véase también

XMLWriter::openMemory
