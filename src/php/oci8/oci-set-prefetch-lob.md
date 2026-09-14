---
title: oci_set_prefetch_lob
description: Define la cantidad de datos precargados para cada CLOB o BLOB.
source_url: https://www.php.net/manual/es/function.oci-set-prefetch-lob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/functions/oci-set-prefetch-lob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: true
translation_revision: 35dc939fd
order: 57660
---

oci_set_prefetch_lob

Define la cantidad de datos precargados para cada CLOB o BLOB.

## Descripción

```php
oci_set_prefetch_lob(resource $statement, int $prefetch_lob_size): bool
```php

Define el tamaño del búfer interno utilizado para recuperar cada valor CLOB o BLOB cuando la implementación recupera el localizador LOB interno de Oracle de la base de datos después de una llamada exitosa a `oci_execute` y para cada solicitud de recuperación interna posterior a la base de datos. Aumentar este valor puede mejorar el rendimiento de recuperación de los LOB más pequeños al reducir los viajes entre PHP y la base de datos. El uso de la memoria cambiará.

Este valor afecta a los LOB devueltos como instancias OCILob y también a aquellos devueltos utilizando `OCI_RETURN_LOBS`.

Llamar a `oci_set_prefetch_lob` antes de llamar a `oci_execute`. Si no se hace, se utiliza el valor de [oci8.prefetch_lob_size](#ini.oci8.prefetch-lob-size).

El valor de prefetch LOB debe definirse únicamente con Oracle Database 12.2 o posterior.

## Parámetros

`statement`  
Un identificador de consulta OCI8 creado por la función `oci_parse` y ejecutado por la función `oci_execute`, o un identificador de consulta `REF CURSOR`.

`prefetch_lob_size`  
El número de bytes de cada LOB a precargar, \>= 0

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Cambio del valor de prefetch LOB para una consulta

```
<?php

$conn = oci_connect('hr', 'welcome', 'localhost/XE');

$stid = oci_parse($conn, 'SELECT myclob FROM mytable');
oci_set_prefetch_lob($stid, 100000);  // Establecer antes de llamar a oci_execute()
oci_execute($stid);

echo "<table border='1'>\n";
while ($row = oci_fetch_array($stid, OCI_ASSOC+OCI_RETURN_NULLS+OCI_RETURN_LOBS)) {
    echo "<tr>\n";
    foreach ($row as $item) {
        echo "    <td>".($item !== null ? htmlentities($item, ENT_QUOTES) : "&nbsp;")."</td>\n";
    }
    echo "</tr>\n";
}
echo "</table>\n";

oci_free_statement($stid);
oci_close($conn);

?>

    
```php

## Véase también

La opción ini [oci8.prefetch_lob_size](#ini.oci8.prefetch-lob-size)
