---
title: cubrid_load_from_glo
description: Liga una donnée
source_url: https://www.php.net/manual/es/function.cubrid-load-from-glo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/cubrid/oldaliases/cubrid-load-from-glo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: cubrid
translation_status: ready
translation_reviewed: false
translation_revision: 22492de2e
order: 9540
---

cubrid_load_from_glo

Liga una donnée

## Descripción

```php
cubrid_load_from_glo(resource $conn_identifier, string $oid, string $file_name): int
```php

La función `cubrid_load_from_glo` se utiliza para leer una donnée desde una instancia glo, y la guarda en un fichero dado.

## Parámetros

`conn_identifier`  
Identificador de conexión.

`oid`  
Oid de la instancia glo desde la cual se desea leer la donnée.

`file_name`  
Nombre del fichero donde se debe realizar la guarda de la donnée.

## Valores devueltos

`true` cuando el proceso es un éxito.

`false` cuando el proceso ha fallado.

## Ejemplos

Ejemplo con `cubrid_load_from_glo`

```
<?php
$req = cubrid_execute ($con, "select image from person where id=1");
if ($req) {
   list ($oid) = cubrid_fetch($req);
   cubrid_close_request($req);
   $res = cubrid_load_from_glo ($con, $oid, "output.jpg");
   if ($res) {
      echo "imagen cambiada con éxito";
   }
}
?>

   
```php

## Notas

> [!NOTE]
> Por razones de compatibilidad ascendente, el siguiente alias obsoleto puede ser utilizado: `cubrid_load_from_glo`

> [!NOTE]
> Esta función ha sido eliminada desde CUBRID 3.1.

## Véase también

cubrid_new_glo

cubrid_save_to_glo

cubrid_send_glo
