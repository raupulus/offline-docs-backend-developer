---
title: ldap_err2str
description: Convertir un número de error de LDAP a una cadena con un mensaje de error
source_url: https://www.php.net/manual/es/function.ldap-err2str.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-err2str.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: 96c9d88ba
order: 43120
---

ldap_err2str

Convertir un número de error de LDAP a una cadena con un mensaje de error

## Descripción

```php
ldap_err2str(int $errno): string
```php

Devuelve una cadena con un mensaje de error explicando el número de error de `errno`. Mientras que los números errno de LDAP están estandarizados, diferentes bibliotecas devuelven aún mensajes de error textuales localizados. Nunca busque un texto con un mensaje de error específico, pero siempre busque un número de error que revisar.

## Parámetros

`errno`  
El número de error.

## Valores devueltos

Devuelve el mensaje de error como una cadena.

## Ejemplos

Enumerando todos los mensajes de error de LDAP

```
<?php
  for ($i=0; $i<100; $i++) {
    printf("Error $i: %s<br />\n", ldap_err2str($i));
  }
?>

    
```php

## Véase también

`ldap_errno`, `ldap_error`
