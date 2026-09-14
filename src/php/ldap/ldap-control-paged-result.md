---
title: ldap_control_paged_result
description: Envía un control de paginación LDAP
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-control-paged-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: e706a6b55
order: 43060
---

ldap_control_paged_result

Envía un control de paginación LDAP

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.4.0, y fue *ELIMINADA* a partir de PHP 8.0.0. En su lugar, se debe utilizar el parámetro `controls` de `ldap_search`. Véase también [LDAP Controls](#ldap.controls) para más detalles.

## Descripción

```php
ldap_control_paged_result(resource $link, int $pagesize, [bool $iscritical], [string $cookie]): bool
```php

Activa la paginación LDAP enviando el control de paginación (tamaño de la página, cookie,...).

## Parámetros

`link`  
Un `resource` LDAP, devuelto por `ldap_connect`.

`pagesize`  
El número de entradas por página.

`iscritical`  
Indica si la paginación es crítica o no. Si es `true`, y si el servidor no soporta la paginación, la búsqueda no devolverá ningún resultado.

`cookie`  
Una estructura opaca enviada por el servidor (`ldap_control_paged_result_response`).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                         |
|---------|-------------------------------------|
| 8.0.0   | Esta función ha sido eliminada.     |
| 7.4.0   | Esta función se ha vuelto obsoleta. |

## Ejemplos

El ejemplo siguiente muestra la manera de recuperar la primera página de una búsqueda paginada con una sola entrada por página.

Paginación LDAP

```
     
     <?php
     // $ds es un identificador de enlace válido (ver ldap_connect)
     ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3);

     $dn        = 'ou=example,dc=org';
     $filter    = '(|(sn=Doe*)(givenname=John*))';
     $justthese = array('ou', 'sn', 'givenname', 'mail');

     // activa la paginación con un tamaño de página de 1.
     ldap_control_paged_result($ds, 1);

     $sr = ldap_search($ds, $dn, $filter, $justthese);

     $info = ldap_get_entries($ds, $sr);

     echo $info['count'] . ' entradas devueltas' . PHP_EOL;
     
    
```php

El ejemplo siguiente muestra la manera de recuperar todos los resultados paginados con 100 entradas por página.

Paginación LDAP

```
     
     <?php
     // $ds es un identificador de enlace válido (ver ldap_connect)
     ldap_set_option($ds, LDAP_OPT_PROTOCOL_VERSION, 3);

     $dn        = 'ou=example,dc=org';
     $filter    = '(|(sn=Doe*)(givenname=John*))';
     $justthese = array('ou', 'sn', 'givenname', 'mail');

     // activa la paginación con un tamaño de página de 100.
     $pageSize = 100;

     $cookie = '';
     do {
         ldap_control_paged_result($ds, $pageSize, true, $cookie);

         $result  = ldap_search($ds, $dn, $filter, $justthese);
         $entries = ldap_get_entries($ds, $result);

         foreach ($entries as $e) {
             echo $e['dn'] . PHP_EOL;
         }

         ldap_control_paged_result_response($ds, $result, $cookie);

     } while($cookie !== null && $cookie != '');
     
    
```php

## Notas

> [!NOTE]
> El control de paginación es una funcionalidad del protocolo LDAPv3.

## Véase también

`ldap_control_paged_result_response`, [RFC2696 : Extensión de control LDAP para una manipulación simplificada de los resultados paginados](https://datatracker.ietf.org/doc/html/rfc2696)
