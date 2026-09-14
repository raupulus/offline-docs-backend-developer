---
title: db2_pclose
description: Cierra una conexión persistente a la base de datos
source_url: https://www.php.net/manual/es/function.db2-pclose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-pclose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30970
---

db2_pclose

Cierra una conexión persistente a la base de datos

## Descripción

```php
db2_pclose(resource $connection): bool
```php

Esta función cierra una conexión DB2, creada con `db2_pconnect` y libera los recursos correspondientes del servidor.

> [!NOTE]
> Esta función no está disponible en i5/OS en respuesta a solicitudes de administración i5/OS.

Si se tiene una conexión persistente DB2 creada con la función `db2_pconnect`, puede utilizarse esta función para cerrar la conexión. Para evitar costos significativos de conexión, esta función solo debe utilizarse en casos raros, donde la conexión se haya vuelto inactiva, o cuando la conexión persistente no será utilizada por un largo tiempo.

## Parámetros

`connection`  
Un recurso de conexión DB2 activo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Cerrar una conexión DB2 persistente

El ejemplo a continuación muestra cómo cerrar una conexión en un servidor IBM DB2 i5/OS.

```
<?php
$conn = db2_pconnect('', '', '');
$rc = db2_pclose($conn);
if ($rc) {
    echo "La conexión fue cerrada correctamente.";
}
?>

   
```php

El ejemplo anterior mostrará:

    La conexión fue cerrada correctamente.

## Véase también

db2_close

db2_pconnect
