---
title: yaz_search
description: Prepara una búsqueda
source_url: https://www.php.net/manual/es/function.yaz-search.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-search.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 107940
---

yaz_search

Prepara una búsqueda

## Descripción

```php
yaz_search(resource $id, string $type, string $query): bool
```php

`yaz_search` prepara una búsqueda en la conexión dada.

Como `yaz_connect` esta función es no bloqueante y únicamente prepara una búsqueda para ser ejecutada posteriormente cuando se llame a la función `yaz_wait` .

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`type`  
Este parámetro representa el tipo de la consulta - únicamente `"rpn"` está soportado ahora, en cuyo caso el tercer argumento especifica una consulta de tipo Type-1 en notación de prefijo de consulta.

`query`  
La consulta RPN es una representación textual de la consulta Type-1 tal y como está definida por el estandard Z39.50 . Sin embargo, en la representación del texto utilizada por YAZ se necesita una notación de prefijo, es decir que el operador precede a los operandos. El string de la consulta es una secuencia de tokens donde se ignora el espacio en blanco a menos que esté rodeado de dobles comillas. Los Tokens que empiecen con una arroba (`@`) se considerarán operadores, de otro modo, se tratarán como términos de búsqueda.

| Sintaxis | Descripción |
|----|----|
| `@and` query1 query2 | intersección de las consultas query1 y query2 |
| `@or` query1 query2 | unión de las consultas query1 y query2 |
| `@not` query1 query2 | query1 y no query2 |
| `@set` name | conjunto resultado de referencia |
| `@attrset` set query | especifica el conjunto de atributos para la consulta. Esta construcción sólo se permite una sola vez - en el inicio de la consulta |
| `@attr` \[set\] type=value query | aplica atributos a la consulta. El tipo y valor son enteros especificando el tipo del atributo y valor del atributo respectivamente. El conjunto, si se informa, especifica el conjunto atributo. |

Operadores RPN

Se muestra más información sobre atributos en el sitio [Z39.50 Maintenance Agency](http://www.loc.gov/z3950/agency/defns/bib1.html).

> [!NOTE]
> Si se desea utilizar una notación más amigable, utilizar el interpretador CCL - functiones `yaz_ccl_conf` y `yaz_ccl_parse`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplos de consulta

Se puede buscar por términos sencillos, como en el caso siguiente:

    computer

        

que busca documentos donde aparece "computer" . No se han especificado atributos.

La consulta

    "knuth donald"

        

busca documentos donde aparece "knuth donald" (suponiendo que el servidor soporta búsqueda de frases).

Esta consulta aplica dos atributos para la misma frase.

    @attr 1=1003 @attr 4=1 "knuth donald"

El primer atributo es de tipo type 1 (usa Bib-1), el valor del atributo es 1003 (Autor). El segundo atributo es de tipo type 4 (estructura), valor 1 (frase), así que debe buscar documentos donde Donald Knuth es el autor.

La consulta

    @and @or a b @not @or c d e

        

en notación infija tendría el aspecto: `(a or b) and ((c or d) not e)`.

Otro ejemplo, más complejo:

    @attrset gils @and @attr 1=4 art @attr 1=2000 company

        

La consulta utiliza el conjunto de atributos GILS . La consulta busca documentos en los que `art` aparece en el título (GILS,BIB-1) y en los que `company` aparece como Distributor (GILS).
