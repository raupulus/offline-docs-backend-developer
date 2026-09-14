---
title: PDO::getAttribute
description: Recupera un atributo de una conexión a una base de datos
source_url: https://www.php.net/manual/es/pdo.getattribute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/getattribute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 61890
---

PDO::getAttribute

Recupera un atributo de una conexión a una base de datos

## Descripción

```php
public PDO::getAttribute(int $attribute): mixed
```php

Esta función devuelve el valor de un atributo de una conexión a una base de datos. Para recuperar los atributos PDOStatement, consúltese la función PDOStatement::getAttribute.

Tenga en cuenta que algunas bases de datos/drivers combinados no soportan todos los atributos de conexión.

## Parámetros

`attribute`  
Una de las constantes `PDO::ATTR_*`. Los atributos genéricos que se aplican a las conexiones son los siguientes: `PDO::ATTR_AUTOCOMMIT`, `PDO::ATTR_CASE`, `PDO::ATTR_CLIENT_VERSION`, `PDO::ATTR_CONNECTION_STATUS`, `PDO::ATTR_DRIVER_NAME`, `PDO::ATTR_ERRMODE`, `PDO::ATTR_ORACLE_NULLS`, `PDO::ATTR_PERSISTENT`, `PDO::ATTR_PREFETCH`, `PDO::ATTR_SERVER_INFO`, `PDO::ATTR_SERVER_VERSION`, `PDO::ATTR_TIMEOUT`

Algunos controladores pueden hacer uso de atributos adicionales específicos del controlador. Tenga en cuenta que los atributos específicos del controlador *no deben* ser utilizados con otros controladores.

## Valores devueltos

Una llamada exitosa devuelve el valor del atributo PDO solicitado. Una llamada que ha fallado devuelve `null`.

## Errores/Excepciones

El método PDO::getAttribute puede generar una excepción PDOException cuando el controlador subyacente no soporta el `attribute` solicitado.

## Ejemplos

Recuperación de los atributos de conexión a una base de datos

```
<?php
$conn = new PDO('odbc:sample', 'db2inst1', 'ibmdb2');
$attributes = array(
"AUTOCOMMIT", "ERRMODE", "CASE", "CLIENT_VERSION", "CONNECTION_STATUS",
"ORACLE_NULLS", "PERSISTENT", "PREFETCH", "SERVER_INFO", "SERVER_VERSION",
"TIMEOUT"
);

foreach ($attributes as $val) {
   echo "PDO::ATTR_$val: ";
   echo $conn->getAttribute(constant("PDO::ATTR_$val")) . "\n";
}
?>

    
```php

## Véase también

PDO::setAttribute, PDOStatement::getAttribute, PDOStatement::setAttribute
