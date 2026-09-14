---
title: db2_autocommit
description: Devuelve o modifica el estado AUTOCOMMIT de la conexión a la base de
  datos
source_url: https://www.php.net/manual/es/function.db2-autocommit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-autocommit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30620
---

db2_autocommit

Devuelve o modifica el estado AUTOCOMMIT de la conexión a la base de datos

## Descripción

```php
db2_autocommit(resource $connection, [int $value]): int
```php

Modifica o lee el comportamiento de AUTOCOMMIT de la conexión especificada.

## Parámetros

`connection`  
Una variable de conexión a una base de datos válida devuelta por `db2_connect` o `db2_pconnect`.

`value`  
Una de las constantes siguientes :

`DB2_AUTOCOMMIT_OFF`  
Desactiva AUTOCOMMIT.

`DB2_AUTOCOMMIT_ON`  
Activa AUTOCOMMIT.

## Valores devueltos

Cuando `db2_autocommit` recibe solo `connection` como argumento, la función devuelve un entero representando el estado actual de AUTOCOMMIT de la conexión proporcionada. Un valor de `DB2_AUTOCOMMIT_OFF` indica que AUTOCOMMIT está desactivado, mientras que un valor de `DB2_AUTOCOMMIT_ON` indica que AUTOCOMMIT está activado.

Cuando `db2_autocommit` recibe ambos argumentos `connection` y `autocommit`, la función intenta modificar el estado AUTOCOMMIT al estado `autocommit` de la conexión proporcionada. Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Obtención del valor de AUTOCOMMIT para una conexión

En el siguiente ejemplo, se prueba una conexión que fue inicializada con el estado AUTOCOMMIT desactivado utilizando la función `db2_autocommit`.

```
<?php
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF);
$conn = db2_connect($database, $user, $password, $options);
$ac = db2_autocommit($conn);
if ($ac == DB2_AUTOCOMMIT_OFF) {
    print "$ac -- AUTOCOMMIT está desactivado.";
} else {
    print "$ac -- AUTOCOMMIT está activado.";
}
?>

    
```php

El ejemplo anterior mostrará:

    0 -- AUTOCOMMIT está desactivado.

Modificación del valor de AUTOCOMMIT para una conexión

En el siguiente ejemplo, se cambia el comportamiento de una conexión que fue previamente inicializada con el estado AUTOCOMMIT desactivado al activar el estado AUTOCOMMIT.

```
<?php
$options = array('autocommit' => DB2_AUTOCOMMIT_OFF);
$conn = db2_connect($database, $user, $password, $options);

// Activa AUTOCOMMIT
$rc = db2_autocommit($conn, DB2_AUTOCOMMIT_ON);
if ($rc) {
    print "Activación AUTOCOMMIT exitosa.\n";
}

// Verificación del estado AUTOCOMMIT
$ac = db2_autocommit($conn);
if ($ac == DB2_AUTOCOMMIT_OFF) {
    print "$ac -- AUTOCOMMIT está desactivado.";
} else {
    print "$ac -- AUTOCOMMIT está activado.";
}
?>

    
```php

El ejemplo anterior mostrará:

    Activación AUTOCOMMIT exitosa.
    1 -- AUTOCOMMIT está activado.

## Véase también

db2_connect

db2_pconnect
