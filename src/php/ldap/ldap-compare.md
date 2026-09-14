---
title: ldap_compare
description: Comparar una entrada con valores de atributos
source_url: https://www.php.net/manual/es/function.ldap-compare.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-compare.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b7cbd468c
order: 43020
---

ldap_compare

Comparar una entrada con valores de atributos

## Descripción

```php
ldap_compare(LDAP\Connection $ldap, string $dn, string $attribute, string $value, [array $controls]): bool
```php

Permite comparar el valor `value` del atributo `attribute` con el valor del mismo atributo de la entrada `dn`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`dn`  
El DN de la entrada LDAP.

`attribute`  
El nombre del atributo.

`value`  
El valor a comparar.

`controls`  
Array de [Controles LDAP](#ldap.controls) a enviar con la petición.

## Valores devueltos

Devuelve `true` si el valor `value` coincide, de lo contrario, devuelve `false`. Devuelve -1 si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Se añadió soporte para `controls`. |

## Ejemplos

El siguiente ejemplo muestra cómo verificar que dos contraseñas coinciden, siendo una de ellas la de una entrada del servidor LDAP.

Ejemplo completo de verificación de contraseña con LDAP

```
<?php

$ds=ldap_connect("localhost");  // debe ser un servidor LDAP válido!

if ($ds) {

    // Autenticación
    if (ldap_bind($ds)) {

        // Preparación de datos
        $dn = "cn=Matti Meikku, ou=My Unit, o=My Company, c=FI";
        $value = "secretpassword";
        $attr = "password";

        // Comparación de valores
        $r=ldap_compare($ds, $dn, $attr, $value);

        if ($r === -1) {
            echo "Error: " . ldap_error($ds);
        } elseif ($r === true) {
            echo "Contraseña correcta.";
        } elseif ($r === false) {
            echo "¡Mal elegido! ¡Contraseña incorrecta!";
        }

    } else {
        echo "No se pudo conectar al servidor LDAP.";
    }

    ldap_close($ds);

} else {
    echo "No se pudo conectar al servidor LDAP.";
}
?>

    
```php

## Notas

> [!WARNING]
> `ldap_compare` NO puede ser utilizado para comparar valores binarios.
