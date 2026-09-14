---
title: DOMNode::C14NFile
description: Canoniza nodos en archivo
source_url: https://www.php.net/manual/es/domnode.c14nfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domnode/c14nfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 2a72c95c0
order: 13910
---

DOMNode::C14NFile

Canoniza nodos en archivo

## Descripción

```php
public DOMNode::C14NFile(string $uri, [bool $exclusive], [bool $withComments], [array $xpath], [array $nsPrefixes]): int
```php

Canoniza nodos en archivo.

## Parámetros

`uri`  
Ruta hacia la cual se creará el archivo.

`exclusive`  
Activa el análisis de los únicos nodos correspondientes al xpath o prefijos de espacio de nombres proporcionados.

`withComments`  
Conserva los comentarios en la salida.

`xpath`  
Un array de XPaths para filtrar los nodos. Cada entrada en este array es un array asociativo con:

- Una clave `query` requerida que contiene la expresión XPath como cadena de caracteres.

- Una clave `namespaces` opcional que contiene un array que mapea los prefijos del espacio de nombres (claves) a los URI del espacio de nombres (valores).

`nsPrefixes`  
Un array de prefijos de espacio de nombres utilizados para filtrar los nodos.

## Valores devueltos

Número de bytes escritos o `false` si ocurre un error

## Véase también

DOMNode::C14N
