---
title: ldap_search
description: Búsqueda en el servidor LDAP
source_url: https://www.php.net/manual/es/function.ldap-search.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-search.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_revision: b7cbd468c
order: 43510
---

ldap_search

Búsqueda en el servidor LDAP

## Descripción

```php
ldap_search(LDAP\Connection $ldap, array $base, array $filter, [array $attributes], [int $attributes_only], [int $sizelimit], [int $timelimit], [int $deref], [array $controls]): LDAP\Result
```php

Realiza una búsqueda con el filtro `filter` en el directorio `base_dn` con la configuración `LDAP_SCOPE_SUBTREE`. Es equivalente a una búsqueda en el directorio.

También es posible realizar búsquedas en paralelo. En este caso, el primer argumento debe ser un array de instancias de `LDAP\Connection`, en lugar de una sola. Si las búsquedas no deben utilizar todas el mismo DN base y filtro, se puede pasar un array de DN base y/o un array de filtros como argumentos. Estos arrays deben tener el mismo tamaño que el array de instancias de `LDAP\Connection`, ya que las primeras entradas de los arrays se utilizan para una búsqueda, las segundas entradas para otra, y así sucesivamente. Al realizar búsquedas en paralelo, se devuelve un array de instancias de `LDAP\Result`, excepto en caso de error, donde el valor de retorno será `false`.

## Parámetros

`ldap`  
Una instancia de `LDAP\Connection`, devuelta por `ldap_connect`.

`base`  
La base DN para el directorio.

`filter`  
El filtro de búsqueda puede ser simple o avanzado, y utilizar estos operadores booleanos en el formato descrito en la documentación LDAP (consultar [Netscape Directory SDK](https://wiki.mozilla.org/Mozilla_LDAP_SDK_Programmer%27s_Guide/Searching_the_Directory_With_LDAP_C_SDK) o [RFC4515](https://datatracker.ietf.org/doc/html/rfc4515) para más información sobre los filtros).

`attributes`  
Un array de atributos requeridos, por ejemplo `array("mail", "sn", "cn")`. Tenga en cuenta que el "dn" siempre se devuelve, independientemente del tipo de atributo solicitado.

El uso de este argumento es más eficiente que la acción por defecto (que es devolver todos los atributos junto con sus valores asociados). El uso de este argumento debe considerarse por tanto una buena práctica.

`attributes_only`  
Debe establecerse en `1` si solo se solicitan los tipos de atributos. Si se establece en `0`, se recuperan los tipos y los valores de los atributos, lo que corresponde al comportamiento por defecto.

`sizelimit`  
Permite limitar el número de entradas a recuperar. Establecer este argumento a `0` significa que no habrá límite.

> [!NOTE]
> Este argumento no puede sobrescribir la configuración del lado del servidor. Sin embargo, puede establecerse un valor inferior.
>
> Algunos directorios del servidor pueden estar configurados para devolver solo un número determinado de entradas. Si ocurre este comportamiento, el servidor indica que solo se ha devuelto un conjunto de resultados parcial. Este comportamiento también ocurre si se utiliza este argumento para limitar el número de entradas recuperadas.

`timelimit`  
Define el número máximo de segundos permitidos para la búsqueda. Establecer este argumento a `0` significa que no hay límite.

> [!NOTE]
> Este argumento no puede sobrescribir la configuración del lado del servidor pero puede utilizarse para ser más restrictivo.

`deref`  
Especifica el número de alias que deben gestionarse durante la búsqueda. Puede ser uno de los siguientes:

- `LDAP_DEREF_NEVER` - (por defecto) los alias nunca se desreferencian.

- `LDAP_DEREF_SEARCHING` - los alias deben desreferenciarse durante la búsqueda pero no al localizar el objeto base de la búsqueda.

- `LDAP_DEREF_FINDING` - los alias deben desreferenciarse al localizar el objeto base pero no durante la búsqueda.

- `LDAP_DEREF_ALWAYS` - los alias siempre deben desreferenciarse.

`controls`  
Array de [Controles LDAP](#ldap.controls) a enviar con la petición.

## Valores devueltos

Devuelve una instancia de `LDAP\Result`, un array de instancias de `LDAP\Result`, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `ldap` ahora espera una instancia de `LDAP\Connection` ; anteriormente, se esperaba un `resource` `ldap link` válido. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\Result`; anteriormente, se devolvía un `resource`. |
| 8.0.0 | `controls` ahora acepta `null`; anteriormente, su valor predeterminado era `[]`. |
| 7.3.0 | Se añadió soporte para `controls`. |

## Ejemplos

El ejemplo siguiente lee el nombre del servicio, el nombre, el apellido y el email de los empleados de la empresa "Mi Compañía", cuyo nombre o apellido contiene la subcadena: `$person`. Este ejemplo ilustra el uso de filtros para indicar al servidor que realice una búsqueda en dos atributos.

Búsqueda LDAP

```
<?php
// $ds es una instancia válida de conexión LDAP\Connection para un servidor de directorio.

// $person es un nombre o parte de un nombre (por ejemplo, "Jean")

$dn = "o=My Company, c=US";
$filter="(|(sn=$person*)(givenname=$person*))";
$justthese = array("ou", "sn", "givenname", "mail");

$sr=ldap_search($ds, $dn, $filter, $justthese);

$info = ldap_get_entries($ds, $sr);

echo $info["count"]." entradas devueltas\n";
?>

    
```php
