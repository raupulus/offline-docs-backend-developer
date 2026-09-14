---
title: cubrid_send_glo
description: Lee los datos desde una instancia glo
source_url: https://www.php.net/manual/es/function.cubrid-send-glo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/oldaliases/cubrid-send-glo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9570
---

cubrid_send_glo

Lee los datos desde una instancia glo

## Descripción

```php
cubrid_send_glo(resource $conn_identifier, string $oid): int
```php

La función `cubrid_send_glo` se utiliza para leer los datos desde una instancia glo y los envía a la salida estándar de PHP.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
Oid de la instancia glo desde la cual se leen los datos.

## Valores devueltos

`true` en caso de éxito.

`false` en caso de fallo.

## Ejemplos

Ejemplo con `cubrid_send_glo`

```
<?php
$req = cubrid_execute ($con, "select image from person where id =1");
if ($req) {
  list ($oid) = cubrid_fetch($req);
  cubrid_close_request($req);
  Header ("Content-type: image/jpeg");
  cubrid_send_glo ($con, $oid);
}
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `cubrid_send_glo`

> [!NOTE]
> Esta función ha sido eliminada desde CUBRID 3.1.

## Véase también

cubrid_new_glo

cubrid_save_to_glo

cubrid_load_from_glo
