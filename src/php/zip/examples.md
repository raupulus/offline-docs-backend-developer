---
title: Ejemplos
source_url: https://www.php.net/manual/es/zip.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108020
---

## Ejemplos

Crear un fichero Zip

```php
<?php

$zip = new ZipArchive();
$filename = "./test112.zip";

if ($zip->open($filename, ZipArchive::CREATE)!==TRUE) {
    exit("cannot open <$filename>\n");
}

$zip->addFromString("testfilephp.txt" . time(), "#1 Esto es una cadena de prueba añadida como  testfilephp.txt.\n");
$zip->addFromString("testfilephp2.txt" . time(), "#2 Esto es una cadena de prueba añadida como testfilephp2.txt.\n");
$zip->addFile($thisdir . "/too.php","/testfromfile.php");
echo "numficheros: " . $zip->numFiles . "\n";
echo "estado:" . $zip->status . "\n";
$zip->close();
?>

  
```

Volcar la información del archivo y listarlos

```php
<?php
$za = new ZipArchive();

$za->open('test_with_comment.zip');
print_r($za);
var_dump($za);
echo "numFicheros: " . $za->numFiles . "\n";
echo "estado: " . $za->status  . "\n";
echo "estadosSis: " . $za->statusSys . "\n";
echo "nombreFichero: " . $za->filename . "\n";
echo "comentario: " . $za->comment . "\n";

for ($i=0; $i<$za->numFiles;$i++) {
    echo "index: $i\n";
    print_r($za->statIndex($i));
}
echo "numFichero:" . $za->numFiles . "\n";
?>

  
```

Usando contenedor Zip, leer meta info de OpenOffice

```php
<?php
$reader = new XMLReader();

$reader->open('zip://' . dirname(__FILE__) . '/test.odt#meta.xml');
$odt_meta = array();
while ($reader->read()) {
    if ($reader->nodeType == XMLREADER::ELEMENT) {
        $elm = $reader->name;
    } else {
        if ($reader->nodeType == XMLREADER::END_ELEMENT && $reader->name == 'office:meta') {
            break;
        }
        if (!trim($reader->value)) {
            continue;
        }
        $odt_meta[$elm] = $reader->value;
    }
}
print_r($odt_meta);
?>

  
```

Este ejemplo utiliza la antigua API (PHP 4), abre un fichero ZIP, lee cada fichero del archivo y imprime su contenido. El archivo`test2.zip` usado en este ejmplo es uno de los archivos de prueba la fuente de distribución de ZZIPlib.

Ejemplo del uso de Zip

```php
<?php

$zip = zip_open("/tmp/test2.zip");

if ($zip) {
    while ($zip_entry = zip_read($zip)) {
        echo "Nombre:               " . zip_entry_name($zip_entry) . "\n";
        echo "Tamaño actual del fichero:    " . zip_entry_filesize($zip_entry) . "\n";
        echo "Tamaño comprimido:    " . zip_entry_compressedsize($zip_entry) . "\n";
        echo "Método de compresión: " . zip_entry_compressionmethod($zip_entry) . "\n";

        if (zip_entry_open($zip, $zip_entry, "r")) {
            echo "Contenido del fichero:\n";
            $buf = zip_entry_read($zip_entry, zip_entry_filesize($zip_entry));
            echo "$buf\n";

            zip_entry_close($zip_entry);
        }
        echo "\n";

    }

    zip_close($zip);

}
?>

  
```
