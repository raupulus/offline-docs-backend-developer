---
title: RarArchive::getComment
description: Obtener comentarios de texto desde el archivo RAR
source_url: https://www.php.net/manual/es/rararchive.getcomment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/getcomment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68410
---

RarArchive::getComment

rar_comment_get

Obtener comentarios de texto desde el archivo RAR

## Descripción

Estilo orientado a objetos (method):

```php
public RarArchive::getComment(): string
```php

Estilo procedimental:

```php
rar_comment_get(RarArchive $rarfile): string
```

Obtener (global) comentario almacenado en el archivo RAR. Este puede ser de hasta 64 KiB de longitud.

> [!NOTE]
> Esta extensión no es compatible con los comentarios en el nivel de entrada.

## Parámetros

`rarfile`  
Un objeto `RarArchive`, abierto con `rar_open`.

## Valores devueltos

Devuelve el comentario o `null` si no hay ninguno.

> [!NOTE]
> RAR no tiene actualmente soporte para comentarios unicode. La codificación de los resultados de esta función no es especificado, pero esta debe ser probablemente Windows-1252.

## Ejemplos

Estilo orientado a objetos

```php
<?php
$rar_arch = RarArchive::open('commented.rar');
echo $rar_arch->getComment();
?>

    
```

Resultado del ejemplo anterior es similar a:

    This is the comment of the file commented.rar.

Estilo procedimental

```php
<?php
$rar_arch = rar_open('commented.rar');
echo rar_comment_get($rar_arch);
?>

    
```
