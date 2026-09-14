---
title: ldap_get_attributes
description: Lee los atributos de una entrada
source_url: https://www.php.net/manual/es/function.ldap-get-attributes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-get-attributes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: c97d168c2
order: 43260
---

ldap_get_attributes

Lee los atributos de una entrada

## Descripción

```php
ldap_get_attributes(LDAP\Connection $ldap, LDAP\ResultEntry $entry): array
```php

Lee los atributos y los valores para una entrada de un resultado de búsqueda.

Una vez que se ha identificado una entrada en un directorio, se pueden obtener más información sobre ella con esta función. Podría ser utilizada en el marco de una aplicación que mapea los directorios y las entradas. En numerosas aplicaciones, se buscan entradas que posean un atributo preciso, sin preocuparse por los otros atributos.

    return_value["count"] = número de atributos en la entrada
    return_value[0] = primer atributo
    return_value[n] = n-ésimo atributo

    return_value["attribute"]["count"] = número de valores del atributo
    return_value["attribute"][0] = primera valor del atributo
    return_value["attribute"][i] = (i+1)-ésimo valor del atributo

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`entry`  
Una instancia de `LDAP\ResultEntry`.

## Valores devueltos

Devuelve el detalle de las informaciones de una entrada bajo la forma de un array multidimensional.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | El parámetro `entry` ahora espera una instancia de `LDAP\ResultEntry` ; anteriormente, se esperaba un `resource` `ldap result entry` válido. |

## Ejemplos

Muestra la lista de atributos de una entrada

```
<?php
// $ds debe ser una instancia de conexión LDAP\Connection válida

// $sr es una búsqueda válida, resultante de una operación
// previa

$entry = ldap_first_entry($ds, $sr);

$attrs = ldap_get_attributes($ds, $entry);

echo $attrs["count"] . " atributos en esta entrada :<p>";

for ($i=0; $i < $attrs["count"]; $i++) {
    echo $attrs[$i] . "<br />";
}
?>

    
```php

## Véase también

`ldap_first_attribute`, `ldap_next_attribute`
