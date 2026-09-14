---
title: CURLStringFile::__construct
description: Crea un objeto CURLStringFile
source_url: https://www.php.net/manual/es/curlstringfile.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/curlstringfile/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_reviewed: false
translation_revision: 5017547fe
order: 9800
---

CURLStringFile::\_\_construct

Crea un objeto CURLStringFile

## Descripción

```php
public CURLStringFile::__construct(string $data, string $postname, [string $mime])
```php

Crea un objeto `CURLStringFile`, utilizado para subir un archivo con `CURLOPT_POSTFIELDS`.

## Parámetros

`data`  
Los contenidos a ser subidos.

`postname`  
El nombre del archivo a ser utilizado en los datos subidos.

`mime`  
El tipo MIME del archivo (por defecto es `application/octet-stream`).

## Ejemplos

Ejemplo con `CURLStringFile::__construct`

```
<?php
/* http://example.com/upload.php:
<?php
var_dump($_FILES);
var_dump(file_get_contents($_FILES['test_string']['tmp_name']));
?>
*/

// Crear un recurso cURL
$ch = curl_init('http://example.com/upload.php');

// Crear un objeto CURLStringFile
$cstringfile = new CURLStringFile('test upload contents','test.txt','text/plain');

// Asignar los datos POST
$data = array('test_string' => $cstringfile);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

// Ejecutar el recurso
curl_exec($ch);
?>

   
```php

El ejemplo anterior mostrará:

    array(1) {
      ["test_string"]=>
      array(5) {
        ["name"]=>
        string(8) "test.txt"
        ["type"]=>
        string(10) "text/plain"
        ["tmp_name"]=>
        string(14) "/tmp/phpTtaoCz"
        ["error"]=>
        int(0)
        ["size"]=>
        int(20)
      }
    }
    string(20) "test upload contents"

## Véase también

`curl_setopt`
