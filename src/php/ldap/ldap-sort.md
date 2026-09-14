---
title: ldap_sort
description: Ordena las entradas de un resultado LDAP lado-cliente
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: e706a6b55
order: 43540
---

ldap_sort

Ordena las entradas de un resultado LDAP lado-cliente

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.0.0 y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
ldap_sort(resource $link, resource $result, string $sortfilter): bool
```php

Ordena el resultado de una búsqueda LDAP, retornado por la función `ldap_search`.

Como esta función ordena los valores retornados lado-cliente, es posible que no se obtengan los resultados esperados si se alcanza `sizelimit` ya sea del servidor o definido en `ldap_search`.

## Parámetros

`link`  
Un `resource` LDAP, retornado por `ldap_connect`.

`result`  
Un identificador de búsqueda LDAP, retornado por la función `ldap_search`.

`sortfilter`  
El atributo a utilizar como clave durante el ordenamiento.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción                     |
|---------|---------------------------------|
| 8.0.0   | Esta función ha sido eliminada. |

## Ejemplos

Ordena el resultado de una búsqueda.

Ordenamiento LDAP

```
<?php
// $ds es un identificador de enlace válido (ver ldap_connect)

$dn        = 'ou=example,dc=org';
$filter    = '(|(sn=Doe*)(givenname=John*))';
$justthese = array('ou', 'sn', 'givenname', 'mail');

$sr = ldap_search($ds, $dn, $filter, $justthese);

// Ordena
ldap_sort($ds, $sr, 'sn');

// Obtención de los datos
$info = ldap_get_entries($ds, $sr);

    
```php
