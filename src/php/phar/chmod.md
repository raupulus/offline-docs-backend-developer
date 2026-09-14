---
title: PharFileInfo::chmod
description: Fija los bits de permiso específicos de los ficheros
source_url: https://www.php.net/manual/es/pharfileinfo.chmod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/PharFileInfo/chmod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: f03806fcd
order: 64710
---

PharFileInfo::chmod

Fija los bits de permiso específicos de los ficheros

## Descripción

```php
public PharFileInfo::chmod(int $perms): void
```php

`PharFileInfo::chmod` permite fijar los bits de ejecución de los ficheros, así como los de solo lectura. Los de escritura son ignorados ya que se fijan al inicio por la variable INI [phar.readonly](#ini.phar.readonly). Al igual que con todas las funcionalidades que modifican el contenido de un phar, la variable INI [phar.readonly](#ini.phar.readonly) debe estar en off para tener éxito si el fichero se encuentra dentro de un archivo `Phar`. Los ficheros dentro de un archivo `PharData` no tienen esta restricción.

## Parámetros

`perms`  
Los permisos (ver `chmod`)

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Un ejemplo con `PharFileInfo::chmod`

```
<?php
// se asegura de que el phar no exista
@unlink('nouveauphar.phar');
try {
    $p = new Phar('nouveauphar.phar', 0, 'nouveauphar.phar');
    $p['fichier.sh'] = '#!/usr/local/lib/php
    <?php echo "salut"; ?>';
    // establece el bit de ejecución
    $p['fichier.sh']->chmod(0555);
    var_dump($p['fichier.sh']->isExecutable());
} catch (Exception $e) {
    echo 'No puede crear/modificar el phar: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
