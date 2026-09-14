---
title: ldap_count_entries
description: Cuenta el número de entradas tras una búsqueda
source_url: https://www.php.net/manual/es/function.ldap-count-entries.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-count-entries.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: cf27955fc
order: 43070
---

ldap_count_entries

Cuenta el número de entradas tras una búsqueda

## Descripción

```php
ldap_count_entries(LDAP\Connection $ldap, LDAP\Result $result): int
```php

Devuelve el número de entradas encontradas en el resultado `result_identifier`, sobre la conexión `link_identifier`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`result`  
Una instancia de `LDAP\Result`, devuelta por `ldap_list` o `ldap_search`.

## Valores devueltos

Devuelve el número de entradas en el resultado, o `-1` en caso de error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `LDAP\Result` ; anteriormente, se esperaba un `resource` `ldap result` válido. |

## Ejemplos

Ejemplo con `ldap_count_entries`

Obtener el número de entradas en el resultado.

```
// $ds debe ser una instancia de conexión LDAP\Connection válida

$dn        = 'ou=example,dc=org';
$filter    = '(|(sn=Doe*)(givenname=John*))';
$justthese = array('ou', 'sn', 'givenname', 'mail');

$sr = ldap_search($ds, $dn, $filter, $justthese);

var_dump(ldap_count_entries($ds, $sr));

    
```php

Resultado del ejemplo anterior es similar a:

    int(1)
