---
title: ImagickKernel::addKernel
description: Adjunta otro núcleo a una lista de núcleos
source_url: https://www.php.net/manual/es/imagickkernel.addkernel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imagick/imagickkernel/addkernel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imagick
translation_status: ready
translation_reviewed: true
translation_revision: 1534707f6
order: 37410
---

ImagickKernel::addKernel

Adjunta otro núcleo a una lista de núcleos

## Descripción

```php
public ImagickKernel::addKernel(ImagickKernel $ImagickKernel): void
```php

Adjunta otro núcleo a este núcleo para permitir que ambos sean aplicados en una sola función de morfología o filtro. Devuelve el nuevo núcleo combinado.

## Parámetros

`ImagickKernel`  

## Valores devueltos

## Ejemplos

`ImagickKernel::addKernel`

```
      
<?php
function addKernel($imagePath) {
    $matrix1 = [
        [-1, -1, -1],
        [ 0,  0,  0],
        [ 1,  1,  1],
    ];

    $matrix2 = [
        [-1,  0,  1],
        [-1,  0,  1],
        [-1,  0,  1],
    ];

    $kernel1 = ImagickKernel::fromMatrix($matrix1);
    $kernel2 = ImagickKernel::fromMatrix($matrix2);
    $kernel1->addKernel($kernel2);

    $imagick = new \Imagick(realpath($imagePath));
    $imagick->filter($kernel1);
    header("Content-Type: image/jpg");
    echo $imagick->getImageBlob();

}

?>

      
```php
