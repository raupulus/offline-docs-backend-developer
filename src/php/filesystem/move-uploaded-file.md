---
title: move_uploaded_file
description: Mueve un archivo subido a una nueva ubicación
source_url: https://www.php.net/manual/es/function.move-uploaded-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/move-uploaded-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 23880
---

move_uploaded_file

Mueve un archivo subido a una nueva ubicación

## Descripción

```php
move_uploaded_file(string $filename, string $destination): bool
```php

Esta función intenta asegurarse de que el archivo designado por `filename` es un archivo subido válido (lo que significa que fue subido mediante el mecanismo de subida HTTP POST de PHP). Si el archivo es válido, será movido al nombre de archivo dado por `destination`.

El orden de comprobación es especialmente importante si hay cualquier posibilidad de que cualquier cosa hecha con los archivos subidos pueda revelar su contenido al usuario, o incluso a otros usuarios en el mismo sistema.

## Parámetros

`filename`  
El nombre de archivo del archivo subido.

`destination`  
El destino del archivo movido.

## Valores devueltos

Devuelve `true` en caso de éxito.

Si `filename` no es un archivo válido subido, no sucederá ninguna acción, y `move_uploaded_file` devolverá `false`.

Si `filename` es un archivo subido válido, pero no puede ser movido por algunas razones, no sucederá ninguna acción, y `move_uploaded_file` devolverá `false`. Adicionalmente, se emitirá un aviso.

## Ejemplos

Subida de múltiples archivos

```
<?php
$uploads_dir = '/uploads';
foreach ($_FILES["pictures"]["error"] as $key => $error) {
    if ($error == UPLOAD_ERR_OK) {
        $tmp_name = $_FILES["pictures"]["tmp_name"][$key];
        // basename() puede evitar ataques de denegación de sistema de ficheros;
        // podría ser apropiada más validación/saneamiento del nombre del fichero
        $name = basename($_FILES["pictures"]["name"][$key]);
        move_uploaded_file($tmp_name, "$uploads_dir/$name");
    }
}
?>

    
```php

## Notas

> [!NOTE]
> `move_uploaded_file` es compatible con [open_basedir](#ini.open-basedir). Sin embargo, las restricciones sólo están impuestas para la ruta `dest` para permitir mover los archivos subidos en los cuales `filename` pueda tener conflictos con tales restricciones. `move_uploaded_file` garantiza la seguridad de esta operación permitiendo que sólo aquellos archivos subidos a través de PHP sean movidos.

> [!WARNING]
> Si el archivo destino ya existe se sobrescribirá.

## Véase también

`is_uploaded_file`, `rename`, Véase [Manejo de subidas de archivos](#features.file-upload) para un sencillo ejemplo de uso
