---
title: chmod
description: Cambia el modo del fichero
source_url: https://www.php.net/manual/es/function.chmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/chmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 5eb55cda5
order: 23290
---

chmod

Cambia el modo del fichero

## Descripción

```php
chmod(string $filename, int $permissions): bool
```php

Reemplaza el modo del fichero `filename` por el modo `permissions`.

## Parámetros

`filename`  
Ruta hacia el fichero.

`permissions`  
Se debe tener en cuenta que el modo `permissions` es considerado como un número en notación octal, por lo que, para asegurarse, se puede prefigurar el modo `permissions` con un cero. Las cadenas como "g+w" no funcionarán correctamente:

```
<?php
chmod("/somedir/somefile", 755);   // notación decimal: probablemente incorrecto
chmod("/somedir/somefile", "u+rwx,go+rx"); // string: incorrecto
chmod("/somedir/somefile", 0755);  // notación octal: valor del modo correcto
?>

        
```php

El argumento `permissions` se compone de tres valores octales que especifican los derechos para el propietario, el grupo del propietario y los demás, respectivamente. Cada componente puede ser calculado sumando los derechos deseados. El número 1 otorga los derechos de ejecución, el número 2 los derechos de escritura y el número 4 los derechos de lectura. Simplemente sume estos números para especificar los derechos deseados. También puede leer el manual de los sistemas Unix con `man 1 chmod` y `man 2 chmod`.

```
<?php
// Lectura y escritura para el propietario, nada para los demás
chmod("/somedir/somefile", 0600);

// Lectura y escritura para el propietario, lectura para los demás
chmod("/somedir/somefile", 0644);

// Todo para el propietario, lectura y ejecución para los demás
chmod("/somedir/somefile", 0755);

// Todo para el propietario, lectura y ejecución para el grupo, nada para los demás
chmod("/somedir/somefile", 0750);
?>

        
```php

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

En caso de error, se emite un error `E_WARNING`.

## Notas

> [!NOTE]
> El usuario actual es el usuario con el que PHP funciona. Probablemente sea diferente del usuario que se utiliza en modo Shell o FTP. El modo solo puede ser modificado por el usuario al que pertenece el fichero en la mayoría de los sistemas.

> [!NOTE]
> Esta función no funciona con los [archivos remotos](#features.remote-files), ya que el archivo examinado debe ser accesible en el sistema de archivos del servidor.

## Véase también

`chown`, `chgrp`, `fileperms`, `stat`
