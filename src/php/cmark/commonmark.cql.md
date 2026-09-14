---
title: La clase CommonMark\CQL
source_url: https://www.php.net/manual/es/class.commonmark-cql.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cmark/commonmark.cql.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cmark
translation_status: ready
translation_reviewed: false
translation_revision: 7cecc752c
order: 7150
---

## Introducción

El CommonMark Query Language es un DSL para describir cómo viajar a través de un árbol de nodos CommonMark implementado como un analizador y un compilador para un pequeño conjunto de instrucciones, y una máquina virtual para ejecutar estas instrucciones.

Rutas:

En su forma más simplista, una consulta CQL combina las siguientes rutas y `/` para describir cómo viajar a través de un árbol: firstChild, lastChild, previous, next, parent Por ejemplo, `/firstChild/lastChild` viaja al último nodo hijo del primer nodo hijo.

Bucle

CQL puede ser instruido para bucles, por ejemplo a través de los hijos de, o los hermanos de un nodo particular, utilizando la ruta `children`, o `siblings`. Por ejemplo, `/firstChild/children` viajará a todos los hijos del primer nodo hijo.

Subconsultas

CQL puede ser instruido para viajar utilizando una subconsulta como `[/firstChild]`. Por ejemplo, `/firstChild/children[/firstChild]` viajará al primer nodo hijo de todos los hijos del primer nodo hijo.

Restricciones de bucle

Al buclar, CQL puede ser instruido para restringir la ruta recorrida a los nodos de un tipo particular. Por ejemplo `/children(BlockQuote)` viajará a los hijos de un nodo donde el tipo es `BlockQuote`. Los siguientes tipos son reconocidos (insensibles a mayúsculas y minúsculas): BlockQuote, List, Item, CodeBlock, HtmlBlock, CustomBlock, Paragraph, Heading, ThematicBreak, Text, SoftBreak, LineBreak, Code, HtmlInline, CustomInline, Emphasis, Strong, Link, Image Los tipos pueden ser utilizados como una unión, por ejemplo `/children(BlockQuote|List)` viajará a los hijos de un nodo donde el tipo es `BlockQuote` o `List`. Los tipos, o uniones de tipos, también pueden ser negados. Por ejemplo `/children(~BlockQuote)` viajará a los hijos de un nodo donde el tipo no es `BlockQuote`, y `/children(~BlockQuote|Paragraph)` viajará a los hijos de un nodo donde el tipo no es `BlockQuote` o `Paragraph`.

Restricciones de rutas

CQL puede ser instruido para crear un bucle para viajar a un nodo de un tipo particular, a una ruta particular. Por ejemplo, `/firstChild(BlockQuote)` viajará al primer nodo hijo donde el tipo es `BlockQuote`. Tenga en cuenta que como otros bucles para `children` y `siblings`, este tipo de ruta solo puede ser seguido por una subconsulta.

Notas de implementación

Aunque CQL ha sido implementado como parte de la extensión PHP CommonMark, está separado de PHP y no utiliza la máquina virtual de PHP o la representación interna de los valores.

## Sinopsis de la clase

CommonMark\CQL

CommonMark\CQL

Constructor

Métodos
