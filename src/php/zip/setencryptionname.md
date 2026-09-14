---
title: ZipArchive::setEncryptionName
description: Establece el método de cifrado de una entrada definida por su nombre
source_url: https://www.php.net/manual/es/ziparchive.setencryptionname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/setencryptionname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108540
---

ZipArchive::setEncryptionName

Establece el método de cifrado de una entrada definida por su nombre

## Descripción

```php
public #[\SensitiveParameter] ZipArchive::setEncryptionName(string $name, int $method, [string $password]): bool
```php

Establece el método de cifrado de una entrada definida por su nombre.

## Parámetros

`name`  
Nombre de la entrada.

`method`  
El método de encriptación definido por una de las constantes ZipArchive::EM\_.

`password`  
Contraseña opcional, se utiliza por defecto cuando falta.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción                   |
|---------|-------------------------------|
| 8.0.0   | `password` ahora es anulable. |

## Ejemplos

Este ejemplo crea un archivo ZIP `test.zip` y añade al archivo `test.txt` encriptado usando el método AES 256.

Archivar y encriptar un archivo

```
<?php
$zip = new ZipArchive();
if ($zip->open('test.zip', ZipArchive::CREATE) === TRUE) {
    $zip->setPassword('secret');
    $zip->addFile('text.txt');
    $zip->setEncryptionName('text.txt', ZipArchive::EM_AES_256);
    $zip->close();
    echo "Ok\n";
} else {
    echo "KO\n";
}
?>

   
```php

## Notas

> [!NOTE]
> Esta función sólo está disponible si se construye con libzip ≥ 1.2.0.

## Véase también

ZipArchive::setPassword, ZipArchive::setEncryptionIndex
