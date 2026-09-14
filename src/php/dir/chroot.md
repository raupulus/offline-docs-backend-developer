---
title: chroot
description: Cambia el directorio raíz
source_url: https://www.php.net/manual/es/function.chroot.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dir/functions/chroot.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dir
translation_status: ready
translation_reviewed: false
translation_revision: 625dc345d
order: 12010
---

chroot

Cambia el directorio raíz

## Descripción

```php
chroot(string $directory): bool
```php

Cambia el directorio raíz del proceso actual a `directory`, y cambia el directorio de trabajo actual a "/".

Esta función solo está disponible en sistemas GNU y BSD y cuando se utiliza la SAPI CLI, CGI o Embed. Además, esta función requiere privilegios de administrador.

Llamar a esta función no modifica los valores de las constantes mágicas `__DIR__` y `__FILE__`.

## Parámetros

`directory`  
El directorio al cual cambiar la raíz.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `chroot`

```
<?php
chroot("/path/to/your/chroot/");
echo getcwd();
?>

    
```php

El ejemplo anterior mostrará:

    /

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.

> [!NOTE]
> Esta función no está disponible en los intérpretes PHP compilados con ZTS (Zend Thread Safety) activado. Para verificar si su copia de PHP ha sido compilada con ZTS activado, utilice `php -i` o pruebe la constante incluida `PHP_ZTS`.
