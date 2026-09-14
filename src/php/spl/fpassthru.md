---
title: SplFileObject::fpassthru
description: Imprimir todos los datos restantes en un apuntador de fichero
source_url: https://www.php.net/manual/es/splfileobject.fpassthru.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fpassthru.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84400
---

SplFileObject::fpassthru

Imprimir todos los datos restantes en un apuntador de fichero

## Descripción

```php
public SplFileObject::fpassthru(): int
```php

Lee hasta el final en el puntero de el fichero dado de la posición actual y escribe el resultado a el búfer de salida.

Puede que se necesite llamar a SplFileObject::rewind para reiniciar el puntero del fichero al inicio del fichero si se tienen datos escritos en el fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el número de caracteres leídos del `handle` y pasados a través de la salida.

## Ejemplos

Ejemplo de SplFileObject::fpassthru

```
<?php

// Abrir el fichero en modo binario
$file = new SplFileObject("./img/ok.png", "rb");

// Enviar las cabeceras de permisos
header("Content-Type: image/png");
header("Content-Length: " . $file->getSize());

// Volcar la imagen y fin del script
$file->fpassthru();
exit;

?>

    
```php

## Véase también

`fpassthru`
