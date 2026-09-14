---
title: yaz_sort
description: Configura los criterios de búsqueda
source_url: https://www.php.net/manual/es/function.yaz-sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 107960
---

yaz_sort

Configura los criterios de búsqueda

## Descripción

```php
yaz_sort(resource $id, string $criteria): void
```php

Esta función configura los criterios de búsqueda y activa la ordenación Z39.50 .

LLamar a esta función *antes* de `yaz_search`. Utilizar esta función por si sola no tiene ningún efecto. Cuando se usa en conjunción con `yaz_search`, una ordenación Z39.50 se enviará después de que la respuesta de la búsqueda ha sido recibida y antes de que cualquier registro sea recuperado con Z39.50 Present (`yaz_present`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`criteria`  
Un string que toma la forma \<field1 flags1 field2 flags2\> donde field1 especifica los atributos primarios para ordenar, field2 los secundarios, etc..

El campo especifica ya sea combinaciones de atributos numéricos consistentes de pares type=value separados por una coma (p.e. `1=4,2=1`) ; o el campo debe especificar un string con el criterio (p.e. `título`). Los flags son secuencias de los caracteres siguientes que no pueden estar separados por ningún espacio.

`a`  
Ordenar de forma ascendente

`d`  
Ordenar de forma descendente

`i`  
No diferenciar entre mayúsculas o minúsculas en la ordenación

`s`  
Diferenciar entre mayúsculas o minúsculas en la ordenación

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Criterios de Ordenación

Para ordenar con el título de atributo Bib1e, sin diferenciar mayúsculas o minúsculas, y de forma ascendente, utilizar el siguiente criterio de ordenación:

    1=4 ia

        

Si el criterio de ordenación secundario fuera el autor, diferenciando mayúsculas y minúsculas y de forma ascendente, se usaría:

    1=4 ia 1=1003 sa
