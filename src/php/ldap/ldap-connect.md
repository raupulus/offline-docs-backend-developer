---
title: ldap_connect
description: Conexión a un servidor LDAP
source_url: https://www.php.net/manual/es/function.ldap-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/functions/ldap-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: false
translation_revision: ca23605a1
order: 43040
---

ldap_connect

Conexión a un servidor LDAP

## Descripción

```php
ldap_connect([string $uri]): LDAP\Connection
```php

> [!WARNING]
> A partir de PHP 8.3.0, la firma *siguiente* está obsoleta.

```php
ldap_connect([string $host], [int $port]): LDAP\Connection
```

Crea una instancia `LDAP\Connection` y verifica si el `uri` proporcionado es plausible.

> [!NOTE]
> Esta función no abre *ninguna* conexión. Verifica si los parámetros dados son plausibles y pueden ser utilizados para abrir una conexión cuando sea necesario.

## Parámetros

`uri`  
Un URI LDAP completo de la forma `LDAP://hostname:port` o `LDAPS://hostname:port` para el cifrado SSL.

También puede proporcionarse varios URI LDAP separados por un espacio como una cadena

Tenga en cuenta que `hostname:port` no es un URI LDAP soportado ya que falta el esquema.

`host`  
El nombre de host al que conectarse.

`port`  
El puerto utilizado para la conexión.

## Valores devueltos

Devuelve una instancia de `LDAP\Connection` cuando el URI LDAP parece plausible. Se trata de un control sintáctico de los parámetros proporcionados, pero el servidor(s) no será contactado. Si la verificación sintáctica falla, devuelve `false`. `ldap_connect` devolverá entonces una instancia de `LDAP\Connection` ya que no se conectará pero solo inicializará los parámetros de conexión. Actualmente, la conexión se realiza con la siguiente llamada a las funciones `ldap_*`, habitualmente con la función `ldap_bind`.

Sin argumentos, entonces se devolverá la instancia `LDAP\Connection` de la última conexión ya abierta.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Llamar a `ldap_connect` con más de dos argumentos está ahora obsoleto. |
| 8.3.0 | Llamar a `ldap_connect` con `hostname` y `port` separados está ahora obsoleto. |
| 8.1.0 | Ahora devuelve una instancia de `LDAP\Connection` ; anteriormente, se esperaba una `resource`. |

## Ejemplos

Ejemplo de conexión a un servidor LDAP

```php
<?php

// Variables LDAP
$ldapuri = "ldap://ldap.example.com:389";  // su ldap-uri

// Conexión LDAP
$ldapconn = ldap_connect($ldaphost, $ldapport)
          or die("Esta LDAP-URI no ha sido analizable");

?>

    
```

Ejemplo de conexión a un servidor LDAP SSL

```php
<?php

// Asegúrese de que el host es correcto
// y que tiene un certificado válido
$ldaphost = "ldaps://ldap.example.com/";

// Conexión LDAP
$ldapconn = ldap_connect($ldaphost)
          or die("Esta LDAP-URI no ha sido analizable");

?>

    
```

## Véase también

`ldap_bind`
