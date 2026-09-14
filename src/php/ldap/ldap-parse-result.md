---
title: ldap_parse_result
description: Extrae información de un resultado
source_url: https://www.php.net/manual/es/function.ldap-parse-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-parse-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b7cbd468c
order: 43460
---

ldap_parse_result

Extrae información de un resultado

## Descripción

```php
ldap_parse_result(LDAP\Connection $ldap, LDAP\Result $result, int $error_code, [string $matched_dn], [string $error_message], [array $referrals], [array $controls]): bool
```php

Analiza un resultado de búsqueda LDAP.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`result`  
Una instancia de `LDAP\Result`, devuelta por `ldap_list` o `ldap_search`.

`error_code`  
Una referencia a una variable que será valorizada con el código de error LDAP en el resultado, o con `0` si no ha ocurrido ningún error.

`matched_dn`  
Una referencia a una variable que será valorizada con el DN correspondiente si ha sido reconocido en la consulta, de lo contrario, valdrá `null`.

`error_message`  
Una referencia a una variable que será valorizada con el mensaje de error LDAP en el resultado, o con una cadena vacía si no ha ocurrido ningún error.

`referrals`  
Una referencia a una variable que será valorizada con un array conteniendo las cadenas de referencia en el resultado, o un array vacío si no se devuelve ninguna referencia.

`controls`  
Un array de Controles LDAP que han sido enviados con la respuesta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `result` ahora espera una instancia de `LDAP\Result` ; anteriormente, se esperaba un `resource` `ldap result` válido. |
| 7.3.0 | Se ha añadido soporte para `controls`. |

## Ejemplos

Ejemplo con `ldap_parse_result`

```
     
<?php
$result = ldap_search($ldap, "cn=userref,dc=my-domain,dc=com", "(cn=user*)");
$errcode = $dn = $errmsg = $refs =  null;
if (ldap_parse_result($ldap, $result, $errcode, $dn, $errmsg, $refs)) {
    // realice algunas acciones con $errcode, $dn, $errmsg y $refs
}
?>
     
    
```php
