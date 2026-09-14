---
title: SplFileObject::seek
description: Mueve el apuntador interno a la línea específicada
source_url: https://www.php.net/manual/es/splfileobject.seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84580
---

SplFileObject::seek

Mueve el apuntador interno a la línea específicada

## Descripción

```php
public SplFileObject::seek(int $line): void
```php

Mueve el apuntador interno a la línea específicada en el fichero.

## Parámetros

`line`  
El número base cero a mover el apuntador interno.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una `LogicException` si el parámetro `line_pos` es negativo.

## Ejemplos

Ejemplo de SplFileObject::seek

Este ejemplo imprime la tercera línea de el script que se encuentra en la posición 2.

```
<?php
$file = new SplFileObject(__FILE__);
$file->seek(2);
echo $file->current();
?>

    
```php

Resultado del ejemplo anterior es similar a:

    $file->seek(2);

## Véase también

SplFileObject::current, SplFileObject::key, SplFileObject::next, SplFileObject::rewind, SplFileObject::valid
