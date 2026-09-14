---
title: odbc_connect
description: Conectar a una fuente de datos
source_url: https://www.php.net/manual/es/function.odbc-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_revision: c68bcb2af
order: 98700
---

odbc_connect

Conectar a una fuente de datos

## Descripción

```php
#[\SensitiveParameter] odbc_connect(string $dsn, [string $user], [string $password], [int $cursor_option]): Odbc\Connection
```php

El identificador de conexión devuelto por esta función es necesario para otras funciones ODBC. Puede tener múltiples conexiones abiertas a la vez siempre que utilicen diferentes bases de datos o diferentes credenciales.

Con algunos controladores ODBC, ejecutar un procedimiento almacenado complejo puede fallar con un error similar a: "No se puede abrir un cursor en un procedimiento almacenado que tenga algo más que una única sentencia SELECT". Usar SQL_CUR_USE_ODBC puede evitar ese error. Además, algunos controladores no soportan el parámetro opcional row_number en `odbc_fetch_row`. SQL_CUR_USE_ODBC podría ayudar en ese caso también.

## Parámetros

`dsn`  
El nombre de la fuente de datos para la conexión. Alternativamente, se puede usar una cadena de conexión sin DSN.

`user`  
El nombre de usuario. Este parámetro se ignora si `dsn` contiene `uid`. Para conectar sin especificar un `user`, use `null`.

`password`  
La contraseña. Este parámetro se ignora si `dsn` contiene `pwd`. Para conectar sin especificar una `password`, use `null`.

`cursor_option`  
Esto establece el tipo de cursor a utilizar para esta conexión. Este parámetro normalmente no es necesario, pero puede ser útil para solucionar problemas con algunos controladores ODBC.

Las siguientes constantes están definidas para cursortype:

- SQL_CUR_USE_IF_NEEDED

- SQL_CUR_USE_ODBC

- SQL_CUR_USE_DRIVER

## Valores devueltos

Devuelve una conexión ODBC, o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Esta función ahora devuelve una instancia de `Odbc\Connection`; anteriormente, se devolvía un `resource`. |
| 8.4.0 | `user` y `password` ahora pueden ser nulos, también son opcionales y valen por defecto `null`. |
| 8.4.0 | Anteriormente, el uso de una cadena vacía para `password` no incluía `pwd` en la cadena de conexión generada para `dsn` . Ahora, `pwd` se incluye en la cadena de conexión, con un valor de cadena vacía. Para restaurar el comportamiento anterior, `password` puede ser definido como `null`. |
| 8.4.0 | Anteriormente, si `dsn` contenía `uid` o `pwd` , entonces los parámetros `user` y `password` eran ignorados. Ahora, `user` solo es ignorado si `dsn` contiene `uid`, y `password` solo es ignorado si `dsn` contiene `pwd`. |

## Ejemplos

Conexiones sin DSN

```
<?php
// Microsoft SQL Server usando el controlador ODBC SQL Native Client 10.0 - permite conexión a SQL 7, 2000, 2005 y 2008
$connection = odbc_connect("Driver={SQL Server Native Client 10.0};Server=$server;Database=$database;", $user, $password);

// Microsoft Access
$connection = odbc_connect("Driver={Microsoft Access Driver (*.mdb)};Dbq=$mdbFilename", $user, $password);

// Microsoft Excel
$excelFile = realpath('C:/ExcelData.xls');
$excelDir = dirname($excelFile);
$connection = odbc_connect("Driver={Microsoft Excel Driver (*.xls)};DriverId=790;Dbq=$excelFile;DefaultDir=$excelDir" , '', '');
?>

    
```php

## Véase también

Para conexiones persistentes: `odbc_pconnect`
