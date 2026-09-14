---
title: SplFileObject::fgetc
description: Obtiene un caracter del fichero
source_url: https://www.php.net/manual/es/splfileobject.fgetc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fgetc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84350
---

SplFileObject::fgetc

Obtiene un caracter del fichero

## Descripción

```php
public SplFileObject::fgetc(): string
```php

Obtiene un caracter del fichero.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un string conteniendo un solo caracter leído de el fichero o `false` si es el final del fichero.

> [!WARNING]
> Esta función puede retornar `false`, pero también puede retornar un valor equivalente a `false`. Por favor, lea la sección sobre los [booleanos](#language.types.boolean) para más información. Utilice el [operador ===](#language.operators.comparison) para probar el valor de retorno exacto de esta función.

## Ejemplos

Ejemplo de SplFileObject::fgetc

```
<?php
$fichero = new SplFileObject('texto.txt');
while (false !== ($char = $fichero->fgetc())) {
    echo "$char\n";
}
?>

    
```php

## Véase también

SplFileObject::fgets
