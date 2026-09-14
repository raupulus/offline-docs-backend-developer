---
title: com La clase com
source_url: https://www.php.net/manual/es/class.com.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/com.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 4d17b7b49
order: 7530
---

## Introducción

La clase com permite instanciar un objeto COM compatible OLE y llamar a sus métodos y acceder a sus propiedades.

## Sinopsis de la clase

com

extends

variant

Métodos

## Métodos sobrecargados

El objeto devuelto es un objeto sobrecargado, lo que significa que PHP no ve ningún método fijo como lo hace con las clases habituales; en lugar de eso, cada acceso a una propiedad o método se realiza a través de COM.

PHP detectará automáticamente los métodos que aceptan argumentos por referencia, y convertirá automáticamente las variables PHP clásicas en una forma que pueda ser pasada por referencia. Esto significa que se pueden llamar a los métodos de forma natural; no se requiere ningún esfuerzo adicional en el código.

## Ejemplos com

Ejemplo com (1)

```php
<?php
// iniciar Word
$word = new com("word.application") or die("No se ha podido instanciar Word");
echo "Word cargado, versión {$word->Version}\n";

// traerlo al frente
$word->Visible = 1;

// abrir un documento vacío
$word->Documents->Add();

// hacer cosas
$word->Selection->TypeText("Esto es una prueba...");
$word->Documents[1]->SaveAs("Prueba inútil.doc");

// cerrar Word
$word->Quit();

// liberar el objeto
$word = null;
?>

    
```

Ejemplo com (2)

```php
<?php

$conn = new com("ADODB.Connection") or die("No se ha podido iniciar ADO");
$conn->Open("Provider=SQLOLEDB; Data Source=localhost;
Initial Catalog=database; User ID=user; Password=password");

$rs = $conn->Execute("SELECT * FROM sometable");    // Recordset

$num_columns = $rs->Fields->Count();
echo $num_columns . "\n";

for ($i=0; $i < $num_columns; $i++) {
    $fld[$i] = $rs->Fields($i);
}

$rowcount = 0;
while (!$rs->EOF) {
    for ($i=0; $i < $num_columns; $i++) {
        echo $fld[$i]->value . "\t";
    }
    echo "\n";
    $rowcount++;            // incrementar rowcount
    $rs->MoveNext();
}

$rs->Close();
$conn->Close();

$rs = null;
$conn = null;

?>

     
```
