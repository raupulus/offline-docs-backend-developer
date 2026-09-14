---
title: oci_new_descriptor
description: Inicializa un nuevo puntero vacío de LOB/FILE de Oracle
source_url: https://www.php.net/manual/es/function.oci-new-descriptor.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-new-descriptor.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_revision: 5e41012cf
order: 57490
---

oci_new_descriptor

Inicializa un nuevo puntero vacío de LOB/FILE de Oracle

## Descripción

```php
oci_new_descriptor(resource $connection, [int $type]): OCILob
```php

Inicializa un nuevo puntero vacío de LOB/FILE de Oracle.

## Parámetros

`connection`  
Un identificador de conexión Oracle, devuelto por la función `oci_connect` o la función `oci_pconnect`.

`type`  
Los valores admitidos para `type` son : `OCI_D_FILE`, `OCI_D_LOB` y `OCI_D_ROWID`.

## Valores devueltos

Devuelve un nuevo recurso LOB o FILE en caso de éxito, o `null` en caso de fallo.

## Ejemplos

Ejemplo con `oci_new_descriptor`

```
<?php
/* Este script está diseñado para ser llamado desde un formulario HTML
 * Espera las variables $user, $password, $table, $where, y $commitsize
 * El script elimina entonces las filas seleccionadas con ROWID y valida
 * la eliminación después de cada grupo de $commitsize filas.
 * (Utilícelo con precaución, ya que no hay posibilidad de deshacer).
 */
$conn = oci_connect($user, $password);
$stmt = oci_parse($conn, "select rowid from $table $where");
$rowid = oci_new_descriptor($conn, OCI_D_ROWID);
oci_define_by_name($stmt, "ROWID", $rowid);
oci_execute($stmt);
while (oci_fetch($stmt)) {
    $nrows = oci_num_rows($stmt);
    $delete = oci_parse($conn, "delete from $table where ROWID = :rid");
    oci_bind_by_name($delete, ":rid", $rowid, -1, OCI_B_ROWID);
    oci_execute($delete);
    echo "$nrows\n";
    if (($nrows % $commitsize) == 0) {
        oci_commit($conn);
    }
}
$nrows = oci_num_rows($stmt);
echo "$nrows deleted...\n";
oci_free_statement($stmt);
oci_close($conn);
?>

    
```php

```
<?php
/* Este script ilustra la carga de columnas de tipo LOB
 * El formulario utilizado en este ejemplo se parece a esto:
 * <form action="upload.php" method="post" enctype="multipart/form-data">
 * <input type="file" name="lob_upload" />
 * ...
 */
  if (!isset($lob_upload) || $lob_upload == 'none'){
?>
<form action="upload.php" method="post" enctype="multipart/form-data">
Upload file: <input type="file" name="lob_upload" /><br />
<input type="submit" value="Upload" /> - <input type="reset" value="Reset" />
</form>
<?php
  } else {

     // $lob_upload contiene el fichero temporal

     // Consulte la sección sobre la subida de ficheros
     // para asegurar sus subidas

     $conn = oci_connect($user, $password);
     $lob = oci_new_descriptor($conn, OCI_D_LOB);
     $stmt = oci_parse($conn, "insert into $table (id, the_blob)
               values(my_seq.NEXTVAL, EMPTY_BLOB()) returning the_blob into :the_blob");
     oci_bind_by_name($stmt, ':the_blob', $lob, -1, OCI_B_BLOB);
     oci_execute($stmt, OCI_DEFAULT);
     if ($lob->savefile($lob_upload)){
        oci_commit($conn);
        echo "BLOB cargado !\n";
     }else{
        echo "Imposible cargar el BLOB\n";
     }
     $lob->free();
     oci_free_statement($stmt);
     oci_close($conn);
  }
?>

    
```php

Ejemplo con `oci_new_descriptor`

```
<?php
/* Llamada a un procedimiento PL/SQL almacenado que toma un clob
 * como entrada.
 * Ejemplo de firma de procedimiento almacenado PL/SQL:
 *
 * PROCEDURE save_data
 *   Argument Name                  Type                    In/Out Default?
 *   ------------------------------ ----------------------- ------ --------
 *   KEY                            NUMBER(38)              IN
 *   DATA                           CLOB                    IN
 *
 */

$conn = oci_connect($user, $password);
$stmt = oci_parse($conn, "begin save_data(:key, :data); end;");
$clob = oci_new_descriptor($conn, OCI_D_LOB);
oci_bind_by_name($stmt, ':key', $key);
oci_bind_by_name($stmt, ':data', $clob, -1, OCI_B_CLOB);
$clob->write($data);
oci_execute($stmt, OCI_DEFAULT);
oci_commit($conn);
$clob->free();
oci_free_statement($stmt);
?>

    
```php

## Véase también

`oci_bind_by_name`
