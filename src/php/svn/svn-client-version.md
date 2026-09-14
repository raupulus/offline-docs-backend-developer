---
title: svn_client_version
description: Obtiene la versión de las bibliotecas cliente SVN
source_url: https://www.php.net/manual/es/function.svn-client-version.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-client-version.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 89950
---

svn_client_version

Obtiene la versión de las bibliotecas cliente SVN

## Descripción

```php
svn_client_version(): string
```php

Obtiene la versión de las bibliotecas cliente SVN.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Número de la versión, habitualmente en el formato x.y.z.

## Ejemplos

Ejemplo de uso

```
<?php
echo svn_client_version();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    1.3.1

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.
