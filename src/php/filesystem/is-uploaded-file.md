---
title: is_uploaded_file
description: Indica si el archivo fue subido mediante HTTP POST
source_url: https://www.php.net/manual/es/function.is-uploaded-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/is-uploaded-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: c1bb7dd16
order: 23790
---

is_uploaded_file

Indica si el archivo fue subido mediante HTTP POST

## Descripción

```php
is_uploaded_file(string $filename): bool
```php

Devuelve `true` si el archivo nombrado por `filename` fue subido mediante HTTP POST. Esto es útil para intentar asegurarse de que un usuario malicioso no ha intentado engañar al script haciéndole trabajar con archivos con los que no debiera de estar trabajando--por ejemplo, `/etc/passwd`.

Este tipo de comprobación es especialmente importante si hay alguna posibilidad de que nada hecho con los archivos subidos pueda revelar su contenido al usuario, o incluso a otros usuarios en el mismo sistema.

Para un funcionamiento apropiado, la función `is_uploaded_file` necesita un argumento como `$_FILES['archivo_usuario']['tmp_name']`, - el nombre del archivo subido de la máquina del cliente `$_FILES['archivo_usuario']['name']` no funciona.

## Parámetros

`filename`  
El nombre de archivo que se va a comprobar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `is_uploaded_file`

```
<?php

if (is_uploaded_file($_FILES['archivo_usuario']['tmp_name'])) {
   echo "Archivo ". $_FILES['archivo_usuario']['name'] ." subido con éxtio.\n";
   echo "Monstrar contenido\n";
   readfile($_FILES['archivo_usuario']['tmp_name']);
} else {
   echo "Posible ataque del archivo subido: ";
   echo "nombre del archivo '". $_FILES['archivo_usuario']['tmp_name'] . "'.";
}

?>
    
```php

## Véase también

`move_uploaded_file`, `$_FILES`, Véase [Manejo de subidas de archivos](#features.file-upload) para un sencillo ejemplo de uso.
