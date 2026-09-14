---
title: COMPersistHelper::LoadFromFile
description: Carga un objeto desde un fichero
source_url: https://www.php.net/manual/es/compersisthelper.loadfromfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/compersisthelper/loadfromfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: e8ac70bf5
order: 7580
---

COMPersistHelper::LoadFromFile

Carga un objeto desde un fichero

## Descripción

```php
public COMPersistHelper::LoadFromFile(string $filename, [int $flags]): bool
```php

Abre el fichero especificado e inicializa un objeto a partir del contenido del fichero.

## Parámetros

`filename`  
El nombre del fichero desde el cual cargar el objeto.

`flags`  
El modo de acceso a utilizar al abrir el fichero. Los valores posibles son extraídos de la [enumeración STGM](https://docs.microsoft.com/en-us/windows/win32/stg/stgm-constants). El método puede tratar este valor como una sugerencia, añadiendo permisos más restrictivos si es necesario. Si `flags` es `0`, la implementación debe abrir el fichero utilizando los permisos por omisión.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Se lanza una excepción `com_exception` si el objeto asociado no implementa la interfaz COM IPersistFile, o cuando la llamada al método IPersistFile::Load ha fallado.
