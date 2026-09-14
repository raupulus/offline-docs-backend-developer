---
title: db2_get_option
description: Recupera el valor de una opción para una consulta o conexión
source_url: https://www.php.net/manual/es/function.db2-get-option.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-get-option.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: true
translation_revision: 020edc73b
order: 30910
---

db2_get_option

Recupera el valor de una opción para una consulta o conexión

## Descripción

```php
db2_get_option(resource $resource, string $option): string
```php

Recupera el valor de una opción especificada para un recurso de consulta o un recurso de conexión.

## Parámetros

`resource`  
Un recurso de consulta válido devuelto por `db2_prepare` o un recurso de conexión válido devuelto por `db2_connect` o `db2_pconnect`.

`option`  
Opciones de consulta o conexión válidas. Las siguientes opciones nuevas están disponibles desde la versión 1.6.0 de ibm_db2. Proporcionan información de seguimiento útil que puede ser establecida durante la ejecución con `db2_get_option`.

> [!NOTE]
> Las versiones anteriores de ibm_db no soportan estas nuevas opciones.
>
> Cuando un valor en cada opción es establecido, algunos servidores pueden no soportar el valor total proporcionado y pueden truncar este valor.
>
> Para asegurar que los datos especificados en cada opción sean convertidos correctamente durante la transmisión hacia una base de datos, utilice solo los caracteres de A a Z, 0 a 9 y los caracteres de subrayado (\_) o punto (.).

`userid`  
`SQL_ATTR_INFO_USERID` : un puntero hacia un `string` utilizado para identificar el identificador de usuario (ID) enviado hacia el servidor de base de datos durante la conexión a DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soportan hasta 16 caracteres. El user-id no debe ser confundido con la identificación user-id; se trata solamente de un propósito de identificación y no debe ser autorizado para permisos.

`acctstr`  
`SQL_ATTR_INFO_ACCTSTR` : un puntero hacia un `string` utilizado para identificar la cuenta del cliente enviada hacia el servidor de base de datos durante la conexión a DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soportan hasta 200 caracteres.

`applname`  
`SQL_ATTR_INFO_APPLNAME` : un puntero hacia un `string` utilizado para identificar el nombre de la aplicación del cliente enviada hacia el servidor de base de datos durante la conexión a DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soportan hasta 32 caracteres.

`wrkstnname`  
`SQL_ATTR_INFO_WRKSTNNAME` : un puntero hacia un `string` utilizado para identificar el nombre de la máquina del cliente enviada hacia el servidor de base de datos durante la conexión a DB2.

> [!NOTE]
> DB2 para servidores z/OS y OS/390 soportan hasta 18 caracteres.

La siguiente tabla especifica qué opciones son compatibles con el tipo de recurso disponible:

<table>
<caption>Matriz recurso parámetro</caption>
<thead>
<tr>
<th style="text-align: center;">Clave</th>
<th style="text-align: center;">Valor</th>
<th colspan="3" style="text-align: center;">Tipo de recurso</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Conexión</td>
<td style="text-align: center;">Consulta</td>
<td style="text-align: center;">Conjunto de resultados</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">userid</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_USERID</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">acctstr</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_ACCTSTR</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">applname</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_APPLNAME</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">wrkstnname</td>
<td style="text-align: center;"><code>SQL_ATTR_INFO_WRKSTNNAME</code></td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">X</td>
<td style="text-align: center;">-</td>
</tr>
</tbody>
</table>

## Valores devueltos

Devuelve la configuración actual de la conexión proporcionada en caso de éxito o `false` si ocurre un error.

## Ejemplos

Establece y recupera los parámetros de un recurso de conexión

```
<?php
/* Parámetros de Conexión */
$database = 'SAMPLE';
$user     = 'db2inst1';
$password = 'ibmdb2';

/* Recuperación del Recurso de Conexión */
$conn = db2_connect($database, $user, $password);

echo "Atributos de conexión pasados con la cadena de caracteres de conexión :\n";

/* Crea un array asociativo de opciones con los pares clave/valor válidos */
/* Asigna los atributos a partir de la cadena de caracteres de conexión */
/* Accede a las opciones especificadas */
$options1 = array('userid' => 'db2inst1');
$conn1 = db2_connect($database, $user, $password, $options1);
$val = db2_get_option($conn1, 'userid');
echo $val . "\n";

$options2 = array('acctstr' => 'account');
$conn2 = db2_connect($database, $user, $password, $options2);
$val = db2_get_option($conn2, 'acctstr');
echo $val . "\n";

$options3 = array('applname' => 'myapp');
$conn3 = db2_connect($database, $user, $password, $options3);
$val = db2_get_option($conn3, 'applname');
echo $val . "\n";

$options4 = array('wrkstnname' => 'workstation');
$conn4 = db2_connect($database, $user, $password, $options4);
$val = db2_get_option($conn4, 'wrkstnname');
echo $val . "\n";

echo "Atributos después de la conexión :\n";

/* Crea un array asociativo de opciones con los pares clave/valor válidos */
/* Asigna los atributos después de que la conexión sea realizada */
/* Accede a las opciones especificadas */
$options5 = array('userid' => 'db2inst1');
$conn5 = db2_connect($database, $user, $password);
$rc = db2_set_option($conn5, $options5, 1);
$val = db2_get_option($conn5, 'userid');
echo $val . "\n";

$options6 = array('acctstr' => 'account');
$conn6 = db2_connect($database, $user, $password);
$rc = db2_set_option($conn6, $options6, 1);
$val = db2_get_option($conn6, 'acctstr');
echo $val . "\n";

$options7 = array('applname' => 'myapp');
$conn7 = db2_connect($database, $user, $password);
$rc = db2_set_option($conn7, $options7, 1);
$val = db2_get_option($conn7, 'applname');
echo $val . "\n";

$options8 = array('wrkstnname' => 'workstation');
$conn8 = db2_connect($database, $user, $password);
$rc = db2_set_option($conn8, $options8, 1);
$val = db2_get_option($conn8, 'wrkstnname');
echo $val . "\n";
?>

   
```php

El ejemplo anterior mostrará:

    Atributos de conexión pasados con la cadena de caracteres de conexión :
    db2inst1
    account
    myapp
    workstation
    Atributos después de la conexión :
    db2inst1
    account
    myapp
    workstation

## Véase también

db2_connect

db2_cursor_type

db2_exec

db2_set_option

db2_pconnect

db2_prepare
