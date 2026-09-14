---
title: CURLFile::__construct
description: Crea un objeto CURLFile
source_url: https://www.php.net/manual/es/curlfile.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/curl/curlfile/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: curl
translation_status: ready
translation_revision: fc9a0a8b2
order: 9690
---

CURLFile::\_\_construct

curl_file_create

Crea un objeto CURLFile

## Descripción

Estilo orientado a objetos

```php
public CURLFile::__construct(string $filename, [string $mime_type], [string $posted_filename])
```php

Estilo procedimental

```php
curl_file_create(string $filename, [string $mime_type], [string $posted_filename]): CURLFile
```

Crea un objeto `CURLFile`, utilizado para subir un fichero con `CURLOPT_POSTFIELDS`.

## Parámetros

`filename`  
Ruta del fichero a subir.

`mime_type`  
Tipo MIME del fichero.

`posted_filename`  
Nombre del fichero a utilizar en los datos subidos.

## Valores devueltos

Devuelve un objeto `CURLFile`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `mime_type` y `posted_filename` ahora son nulos; anteriormente su valor por omisión era `0`. |

## Ejemplos

Ejemplo con `CURLFile::__construct`

Estilo orientado a objetos

```php
<?php
/* http://example.com/upload.php:
<?php var_dump($_FILES); ?>
*/

// Crea un manejador cURL
$ch = curl_init('http://example.com/upload.php');

// Crea un objeto CURLFile
$cfile = new CURLFile('cats.jpg','image/jpeg','test_name');

// Asigna los datos POST
$data = array('test_file' => $cfile);
curl_setopt($ch, CURLOPT_POST,1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

// Ejecuta el manejador
curl_exec($ch);
?>

   
```

Estilo procedimental

```php
<?php
/* http://example.com/upload.php:
<?php var_dump($_FILES); ?>
*/

// Crea un manejador cURL
$ch = curl_init('http://example.com/upload.php');

// Crea un objeto CURLFile
$cfile = curl_file_create('cats.jpg','image/jpeg','test_name');

// Asigna los datos POST
$data = array('test_file' => $cfile);
curl_setopt($ch, CURLOPT_POST,1);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);

// Ejecuta el manejador
curl_exec($ch);
?>

   
```

El ejemplo anterior mostrará:

    array(1) {
      ["test_file"]=>
      array(5) {
        ["name"]=>
        string(9) "test_name"
        ["type"]=>
        string(10) "image/jpeg"
        ["tmp_name"]=>
        string(14) "/tmp/phpPC9Kbx"
        ["error"]=>
        int(0)
        ["size"]=>
        int(46334)
      }
    }

Ejemplo de subida de múltiples ficheros con `CURLFile::__construct`

Estilo orientado a objetos

```php
<?php
$request = curl_init('http://www.example.com/upload.php');
curl_setopt($request, CURLOPT_POST, true);
curl_setopt($request, CURLOPT_SAFE_UPLOAD, true);
curl_setopt($request, CURLOPT_POSTFIELDS, [
    'blob[0]' => new CURLFile(realpath('first-file.jpg'), 'image/jpeg'),
    'blob[1]' => new CURLFile(realpath('second-file.txt'), 'text/plain'),
    'blob[2]' => new CURLFile(realpath('third-file.exe'), 'application/octet-stream'),
]);
curl_setopt($request, CURLOPT_RETURNTRANSFER, true);

echo curl_exec($request);

var_dump(curl_getinfo($request));

   
```

Estilo procedimental

```php
<?php
// procedural
$request = curl_init('http://www.example.com/upload.php');
curl_setopt($request, CURLOPT_POST, true);
curl_setopt($request, CURLOPT_SAFE_UPLOAD, true);
curl_setopt($request, CURLOPT_POSTFIELDS, [
    'blob[0]' => curl_file_create(realpath('first-file.jpg'), 'image/jpeg'),
    'blob[1]' => curl_file_create(realpath('second-file.txt'), 'text/plain'),
    'blob[2]' => curl_file_create(realpath('third-file.exe'), 'application/octet-stream'),
]);
curl_setopt($request, CURLOPT_RETURNTRANSFER, true);

echo curl_exec($request);

var_dump(curl_getinfo($request));

   
```

El ejemplo anterior mostrará:

    array(26) {
      ["url"]=>
      string(31) "http://www.example.com/upload.php"
      ["content_type"]=>
      string(24) "text/html; charset=UTF-8"
      ["http_code"]=>
      int(200)
      ["header_size"]=>
      int(198)
      ["request_size"]=>
      int(196)
      ["filetime"]=>
      int(-1)
      ["ssl_verify_result"]=>
      int(0)
      ["redirect_count"]=>
      int(0)
      ["total_time"]=>
      float(0.060062)
      ["namelookup_time"]=>
      float(0.028575)
      ["connect_time"]=>
      float(0.029011)
      ["pretransfer_time"]=>
      float(0.029121)
      ["size_upload"]=>
      float(3230730)
      ["size_download"]=>
      float(811)
      ["speed_download"]=>
      float(13516)
      ["speed_upload"]=>
      float(53845500)
      ["download_content_length"]=>
      float(811)
      ["upload_content_length"]=>
      float(3230730)
      ["starttransfer_time"]=>
      float(0.030355)
      ["redirect_time"]=>
      float(0)
      ["redirect_url"]=>
      string(0) ""
      ["primary_ip"]=>
      string(13) "0.0.0.0"
      ["certinfo"]=>
      array(0) {
      }
      ["primary_port"]=>
      int(80)
      ["local_ip"]=>
      string(12) "0.0.0.0"
      ["local_port"]=>
      int(34856)
    }

## Véase también

`curl_setopt`
