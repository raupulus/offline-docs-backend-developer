---
title: cubrid_new_glo
description: Crea una instancia glo
source_url: https://www.php.net/manual/es/function.cubrid-new-glo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/oldaliases/cubrid-new-glo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9550
---

cubrid_new_glo

Crea una instancia glo

## Descripción

```php
cubrid_new_glo(resource $conn_identifier, string $class_name, string $file_name): string
```php

La función `cubrid_new_glo` se utiliza para crear una instancia glo en la clase solicitada (clase glo). El glo creado es de tipo LO y se almacena en el fichero `file_name`.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`class_name`  
Nombre de la clase en la que se desea crear el glo.

`file_name`  
El nombre del fichero en el que se desea guardar el nuevo glo creado.

## Valores devueltos

OID de la instancia creada en caso de éxito.

`false` en caso de fallo.

## Ejemplos

Ejemplo con `cubrid_new_glo`

```
<?php
$oid = cubrid_new_glo ($con, "glo", "input.jpg");
if ($oid){
   // El tipo de la columna "image" es "object"
   $req = cubrid_execute ($con, "insert into person(image) values($oid)");
   if ($req) {
      echo "imagen insertada con éxito";
      cubrid_close_request ($req);
      cubrid_commit($con);
   }
}
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `cubrid_new_glo`

> [!NOTE]
> Esta función ha sido eliminada desde CUBRID 3.1.

## Véase también

cubrid_save_to_glo

cubrid_load_from_glo

cubrid_send_glo
