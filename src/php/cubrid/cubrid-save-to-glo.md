---
title: cubrid_save_to_glo
description: Guarda un fichero en una instancia glo
source_url: https://www.php.net/manual/es/function.cubrid-save-to-glo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/oldaliases/cubrid-save-to-glo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9560
---

cubrid_save_to_glo

Guarda un fichero en una instancia glo

## Descripción

```php
cubrid_save_to_glo(resource $conn_identifier, string $oid, string $file_name): int
```php

La función `cubrid_save_to_glo` se utiliza para guardar un fichero en una instancia glo.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
Oid de la instancia glo en la que se guardará el fichero.

`file_name`  
El nombre del fichero a guardar.

## Valores devueltos

`true` en caso de éxito.

`false` en caso de fallo.

## Ejemplos

Ejemplo con `cubrid_save_to_glo`

```
<?php
$req = cubrid_execute ($con, "select image from person where id=1");
if ($req) {
   list ($oid) = cubrid_fetch($req);
   cubrid_close_request($req);
   $res = cubrid_save_to_glo ($con, $oid, "input.jpg");
   if ($res) {
      echo "imagen cambiada con éxito";
   }
}
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `cubrid_save_to_glo`

> [!NOTE]
> Esta función ha sido eliminada desde CUBRID 3.1.

## Véase también

cubrid_new_glo

cubrid_load_from_glo

cubrid_send_glo
