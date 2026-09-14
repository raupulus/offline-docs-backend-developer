---
title: ldap_add
description: Añade una entrada en un directorio LDAP
source_url: https://www.php.net/manual/es/function.ldap-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: d72d71b65
order: 42980
---

ldap_add

Añade una entrada en un directorio LDAP

## Descripción

```php
ldap_add(LDAP\Connection $ldap, string $dn, array $entry, [array $controls]): bool
```php

Añade una entrada en un directorio LDAP.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
El nombre DN de la entrada LDAP.

`entry`  
Un array con la información sobre la nueva entrada. Estos valores están indexados individualmente. En caso de valores múltiples para un atributo, están indexados numéricamente, comenzando desde 0.

```
<?php
$entry["attribute1"] = "value";
$entry["attribute2"][0] = "value1";
$entry["attribute2"][1] = "value2";
?>
     
        
```php

`controls`  
Array de [Controles LDAP](#ldap.controls) para enviar con la petición.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Se añadió soporte para `controls`. |

## Ejemplos

Ejemplo completo con identificación LDAP

```
<?php
$ds = ldap_connect("localhost");  // se asume que el servidor LDAP está en el servidor local

if ($ds) {
    // Conexión con una identidad que permite modificaciones
    $r = ldap_bind($ds, "cn=root, o=My Company, c=US", "secret");

    // Prepara los datos
    $info["cn"] = "John Jones";
    $info["sn"] = "Jones";
    $info["objectclass"] = "person";

    // Añade los datos al directorio
    $r = ldap_add($ds, "cn=John Jones, o=My Company, c=US", $info);

    ldap_close($ds);
} else {
    echo "No es posible conectarse al servidor LDAP";
}
?>

    
```php

## Notas

> [!NOTE]
> Esta función es segura para sistemas binarios.

## Véase también

`ldap_add_ext`, `ldap_delete`
