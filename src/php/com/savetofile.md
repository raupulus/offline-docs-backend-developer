---
title: COMPersistHelper::SaveToFile
description: Guarda un objeto en un fichero
source_url: https://www.php.net/manual/es/compersisthelper.savetofile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/savetofile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 49ff12041
order: 7600
---

COMPersistHelper::SaveToFile

Guarda un objeto en un fichero

## Descripción

```php
public COMPersistHelper::SaveToFile(string $filename, [bool $remember]): bool
```php

Guarda una copia del objeto en el fichero especificado.

## Parámetros

`filename`  
El nombre del fichero en el que se guardará el objeto.

`remember`  
Indica si el argumento `filename` debe ser utilizado como fichero de trabajo actual. Si `true`, `filename` se convierte en el fichero actual y el objeto debe borrar su indicador de modificación después de la guardado. Si `false`, esta operación de guardado es una operación "Guardar una copia como ...". En este caso, el fichero actual no se modifica y el objeto no debe borrar su indicador de modificación.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una excepción `com_exception` si el objeto asociado no implementa la interfaz COM IPersistFile, o cuando la llamada al método IPersistFile::Save ha fallado.

## Ejemplos

Uso básico de COMPersistHelper::saveToFile

```
<?php
$word = new COM('Word.Application');
$doc = $word->Documents->Add();
$ph = new COMPersistHelper($doc);
$ph->SaveToFile('C:\\Users\\cmb\\Documents\\my.docx');
$word->Quit();
?>

   
```php
