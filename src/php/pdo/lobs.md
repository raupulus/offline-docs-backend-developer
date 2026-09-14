---
title: Los objetos grandes (LOB)
source_url: https://www.php.net/manual/es/pdo.lobs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/lobs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: true
translation_revision: eae19eb5f
order: 61810
---

## Los objetos grandes (LOB)

En algún momento de su aplicación, podría ser necesario almacenar grandes cantidades de datos en la base de datos. « Grande » significa típicamente datos de aproximadamente 4 ko o más, aunque algunas bases de datos pueden manejar más de 32 ko antes de que los datos se consideren « grandes ». Los objetos grandes pueden ser de naturaleza textual o binaria. PDO permite trabajar con este tipo de grandes datos utilizando el código tipo `PDO::PARAM_LOB` en las llamadas a las funciones PDOStatement::bindParam o PDOStatement::bindColumn. `PDO::PARAM_LOB` solicita a PDO que transforme los datos en un flujo que pueda ser manipulado utilizando la [API PHP de flujos](#ref.stream).

Mostrar una imagen desde una base de datos

Este ejemplo vincula un LOB en una variable llamada \$lob y lo envía al navegador utilizando la función `fpassthru`. Dado que un LOB se representa como un flujo, las funciones como `fgets`, `fread` y `stream_get_contents` pueden ser utilizadas en este flujo.

```php
<?php
$db = new PDO('odbc:SAMPLE', 'db2inst1', 'ibmdb2');
$stmt = $db->prepare("select contenttype, imagedata from images where id=?");
$stmt->execute(array($_GET['id']));
$stmt->bindColumn(1, $type, PDO::PARAM_STR, 256);
$stmt->bindColumn(2, $lob, PDO::PARAM_LOB);
$stmt->fetch(PDO::FETCH_BOUND);

header("Content-Type: $type");
fpassthru($lob);
?>

   
```

Insertar una imagen en una base de datos

Este ejemplo abre un fichero y pasa el puntero de fichero a PDO para insertarlo como LOB. PDO hará lo posible por recuperar el contenido del fichero e insertarlo en la base de datos de la manera más eficiente posible.

```php
<?php
$db = new PDO('odbc:SAMPLE', 'db2inst1', 'ibmdb2');
$stmt = $db->prepare("insert into images (id, contenttype, imagedata) values (?, ?, ?)");
$id = get_new_id(); // función para asignar un nuevo ID

// asumamos que obtenemos un fichero desde un formulario
// puede encontrar más detalles en la documentación de PHP

$fp = fopen($_FILES['file']['tmp_name'], 'rb');

$stmt->bindParam(1, $id);
$stmt->bindParam(2, $_FILES['file']['type']);
$stmt->bindParam(3, $fp, PDO::PARAM_LOB);

$db->beginTransaction();
$stmt->execute();
$db->commit();
?>

   
```

Insertar una imagen en una base de datos Oracle

Oracle requiere una sintaxis ligeramente diferente para insertar un LOB desde un fichero. Asimismo, es esencial realizar la inserción dentro de una transacción, de lo contrario, el nuevo LOB será insertado con una longitud de cero:

```php
<?php
$db = new PDO('oci:', 'scott', 'tiger');
$stmt = $db->prepare("insert into images (id, contenttype, imagedata) " .
"VALUES (?, ?, EMPTY_BLOB()) RETURNING imagedata INTO ?");
$id = get_new_id(); // función para asignar un nuevo ID

// asumamos que obtenemos un fichero desde un formulario
// puede encontrar más detalles en la documentación de PHP

$fp = fopen($_FILES['file']['tmp_name'], 'rb');

$stmt->bindParam(1, $id);
$stmt->bindParam(2, $_FILES['file']['type']);
$stmt->bindParam(3, $fp, PDO::PARAM_LOB);

$db->beginTransaction();
$stmt->execute();
$db->commit();
?>

   
```
