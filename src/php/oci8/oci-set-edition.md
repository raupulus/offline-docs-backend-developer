---
title: oci_set_edition
description: Define la edición de la base de datos
source_url: https://www.php.net/manual/es/function.oci-set-edition.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-edition.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: d26548d33
order: 57640
---

oci_set_edition

Define la edición de la base de datos

## Descripción

```php
oci_set_edition(string $edition): bool
```php

Define la edición de los objetos de la base de datos a utilizar por las conexiones.

La edición Oracle permite que versiones concurrentes de las aplicaciones se ejecuten utilizando el mismo nombre de esquema y objetos. Esto es práctico para actualizar sistemas en vivo.

Llame a la función `oci_set_edition` antes de llamar a una función como `oci_connect`, `oci_pconnect` o `oci_new_connect`.

Si se define una edición pero no es válida en la base de datos, cualquier intento de conexión fallará incluso si la función `oci_set_edition` devuelve un estado de éxito.

Al utilizar conexiones persistentes, si una conexión con la edición solicitada ya existe, será reutilizada. De lo contrario, se creará una conexión persistente diferente.

## Parámetros

`edition`  
Nombre de la edición Oracle, previamente creada con el comando SQL "`CREATE EDITION`".

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

2 scripts pueden utilizar diferentes versiones de myfunc() al mismo momento

```
<?php

// Archivo 1

echo "Versión 1 de la aplicación\n";

oci_set_edition('ORA$BASE');
$c = oci_connect('hr', 'welcome', 'localhost/XE');

$s = oci_parse($c, "begin :r := myfunc(); end;");
oci_bind_by_name($s, ":r", $r, 20);
oci_execute($s);
echo "El resultado es $r\n";

?>
```php

```
<?php

// Archivo 2

echo "Versión 2 de la aplicación\n";

oci_set_edition('E1');
$c = oci_connect('hr', 'welcome', 'localhost/XE');

$s = oci_parse($c, "begin :r := myfunc(); end;");
oci_bind_by_name($s, ":r", $r, 20);
oci_execute($s);
echo "El resultado es $r\n";

?>

    
```php

## Notas

> [!NOTE]
> Esta función está disponible para Oracle 11*g*R2 y versiones posteriores.

> [!CAUTION]
> Para evitar inconsistencias de datos o errores inesperados, no se utilice la consulta ALTER SESSION SET EDITION para cambiar una edición en las conexiones persistentes.

> [!CAUTION]
> Para evitar inconsistencias de datos o errores inesperados al utilizar ediciones y [DRCP](#oci8.connection) con Oracle 11.2.0.1, mantenga una correspondencia uno-a-uno entre [oci8.connection_class](#ini.oci8.connection-class) y el nombre de la edición utilizado por sus aplicaciones. Cada servidor para una clase de conexión dada debe ser utilizado con una sola edición. Esta restricción fue eliminada en Oracle 11.2.0.2.
