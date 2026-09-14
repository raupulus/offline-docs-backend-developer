---
title: ldap_get_values
description: Lee todos los valores de una entrada LDAP
source_url: https://www.php.net/manual/es/function.ldap-get-values.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-get-values.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: e50e79746
order: 43310
---

ldap_get_values

Lee todos los valores de una entrada LDAP

## Descripción

```php
ldap_get_values(LDAP\Connection $ldap, LDAP\ResultEntry $entry, string $attribute): array
```php

Lee todos los valores del atributo de una entrada en un resultado.

La llamada a esta función requiere una `entry` y debe ser precedida por una búsqueda LDAP, y una de las funciones que permiten acceder a una entrada.

La aplicación debe contener información que permita leer ciertos atributos (como "nombre" o "mail"), o bien deberá utilizarse la función `ldap_get_attributes` para saber cuáles son los atributos que existen para una entrada dada.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`entry`  
Una instancia de `LDAP\ResultEntry`.

`attribute`  

## Valores devueltos

Devuelve un array de valores para el atributo, o `false` en caso de error. El número de valores devueltos está disponible en el índice 'count' del array devuelto. Los valores son accesibles individualmente, con los índices numéricos del array. La indexación comienza en `0`.

LDAP permite más de una entrada por atributo, lo que permite almacenar varias direcciones de correo electrónico por persona, utilizando solo una etiqueta "mail":

\
    return_value\["count"\] = número de valores del atributo\
    return_value\[0\] = primer valor del atributo\
    return_value\[i\] = i-ésimo valor del atributo\

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `entry` ahora espera una instancia de `LDAP\ResultEntry` ; anteriormente, se esperaba un `resource` `ldap result entry` válido. |

## Ejemplos

Lista todas las valores del atributo "mail" de una entrada

```
<?php
// $ds debe ser una instancia de conexión LDAP\Connection válida

// $sr debe ser un recurso de resultado válido, obtenido con una de las funciones de
//     búsqueda LDAP.

// $entry es una entrada LDAP válida, obtenida con una de las funciones
//        LDAP que devuelve una entrada

$values = ldap_get_values($ds, $entry,"mail");

echo $values["count"] . " direcciones de correo para esta entrada.<br />";

for ($i=0; $i < $values["count"]; $i++) {
    echo $values[$i] . "<br />";
}
?>

    
```php

## Véase también

`ldap_get_values_len`
