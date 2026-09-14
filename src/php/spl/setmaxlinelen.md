---
title: SplFileObject::setMaxLineLen
description: Establecer la longitud máxima de una línea
source_url: https://www.php.net/manual/es/splfileobject.setmaxlinelen.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/setmaxlinelen.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84610
---

SplFileObject::setMaxLineLen

Establecer la longitud máxima de una línea

## Descripción

```php
public SplFileObject::setMaxLineLen(int $maxLength): void
```php

Establece la longitud máxima de una línea a ser leída.

## Parámetros

`maxLength`  
La longitud de una línea.

## Valores devueltos

No se retorna ningún valor.

## Errores/Excepciones

Lanza una excepción `DomainException` cuando `maxLength` es menor que cero.

## Ejemplos

Ejemplo de SplFileObject::setMaxLineLen

```
<?php
$file = new SplFileObject("lipsum.txt");
$file->setMaxLineLen(20);
foreach ($file as $line) {
    echo $line . "\n";
}
?>

    
```php

Contenido de lipsum.txt

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Duis nec sapien felis, ac sodales nisl.
Nulla vitae magna vitae purus aliquet consequat.

    
```php

Resultado del ejemplo anterior es similar a:

    Lorem ipsum dolor s
    it amet, consectetu
    r adipiscing elit.

    Duis nec sapien fel
    is, ac sodales nisl
    .

    Nulla vitae magna v
    itae purus aliquet
    consequat.

## Véase también

SplFileObject::getMaxLineLen
