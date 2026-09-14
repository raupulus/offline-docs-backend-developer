---
title: ldap_escape
description: Escapa una cadena para usarla en un filtro LDAP o un DN
source_url: https://www.php.net/manual/es/function.ldap-escape.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-escape.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: bc90525a5
order: 43150
---

ldap_escape

Escapa una cadena para usarla en un filtro LDAP o un DN

## Descripción

```php
ldap_escape(string $value, [string $ignore], [int $flags]): string
```php

Escapa la cadena `value` para usarla en el contexto implicado por el argumento `flags`.

## Parámetros

`value`  
El valor a escapar.

`ignore`  
Los caracteres a ignorar durante el escape.

`flags`  
El contexto en el que la cadena escapada será utilizada: `LDAP_ESCAPE_FILTER` para los filtros a usar con `ldap_search`, o `LDAP_ESCAPE_DN` para los DNs. Si no se pasa ningún flag, todos los caracteres son escapados.

## Valores devueltos

Devuelve la cadena escapada.

## Ejemplos

Al construir un filtro LDAP, debe usarse ldap_escape con el flag LDAP_ESCAPE_FILTER.

Buscar una dirección de correo electrónico

```
<?php
// $ds debe ser una instancia válida de LDAP\Connection

// $mail es una dirección de correo electrónico proporcionada por el usuario en un formulario

$base   = "o=My Company, c=US";
$filter = "(mail=".ldap_escape($mail, "", LDAP_ESCAPE_FILTER).")";

$sr = ldap_search($ds, $base, $filter, array("sn", "givenname", "mail"));

$info = ldap_get_entries($ds, $sr);

echo $info["count"]." entradas devueltas\n";
?>

    
```php
