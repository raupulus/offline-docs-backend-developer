---
title: Phar::setStub
description: Utilizado para especificar el cargador PHP o el contenedor de carga de
  un archivo Phar
source_url: https://www.php.net/manual/es/phar.setstub.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/phar/Phar/setStub.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: phar
translation_status: ready
translation_reviewed: false
translation_revision: d7056bd09
order: 64380
---

Phar::setStub

Utilizado para especificar el cargador PHP o el contenedor de carga de un archivo Phar

## Descripción

```php
public Phar::setStub(resource $stub, [int $length]): true
```php

> [!NOTE]
> Este método requiere que la variable de configuración INI `phar.readonly` esté definida a `0` para funcionar con los objetos `Phar` . De lo contrario, se lanzará una excepción `PharException`.

Este método se utiliza para añadir un cargador PHP a un nuevo archivo Phar, o para reemplazar el contenedor de carga de un archivo Phar existente.

El contenedor de carga de un archivo Phar se utiliza cuando un archivo es incluido directamente como en este ejemplo:

```
    
<?php
include 'myphar.phar';
?>
    
   
```php

o mediante una simple ejecución:

        
    php myphar.phar
        
       

El cargador no se utiliza cuando un fichero es incluido a través del flujo `phar` como esto:

```
   
<?php
include 'phar://monphar.phar/unfchier.php';
?>
   
  
```php

## Parámetros

`stub`  
Una cadena o un `resource` de flujo abierto a utilizar como contenedor ejecutable para este archivo phar.

`length`  
Longitud de `stub` en bytes.

> [!WARNING]
> Pasar el argumento `length` con un `resource` en el primer argumento está *OBSOLETO* a partir de PHP 8.3.0. Utilizar `$phar->setStub(stream_get_contents($resource))` en su lugar.

## Valores devueltos

Retorna siempre `true`.

## Errores/Excepciones

Una excepción `UnexpectedValueException` es lanzada si [phar.readonly](#ini.phar.readonly) está activado en el php.ini. Una excepción `PharException` es lanzada si se encuentran problemas al escribir los cambios en el disco.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | El tipo de retorno es ahora `true`, anteriormente era `bool`. |
| 8.3.0 | Llamar a Phar::setStub con una `resource` y una `length` ahora está obsoleto. Tales llamadas deberían ser reemplazadas por: `$phar->setStub(stream_get_contents($resource));` |

## Ejemplos

Un ejemplo con `Phar::setStub`

```
<?php

try {
    $p = new Phar(dirname(__FILE__) . '/nouveau.phar', 0, 'nouveau.phar');
    $p['a.php'] = '<?php var_dump("Salut");';
    $p->setStub('<?php var_dump("Premier"); Phar::mapPhar("nouveau.phar"); __HALT_COMPILER(); ?>');
    include 'phar://nouveau.phar/a.php';
    var_dump($p->getStub());

    $p['b.php'] = '<?php var_dump("Tout le monde");';
    $p->setStub('<?php var_dump("Second"); Phar::mapPhar("nouveau.phar"); __HALT_COMPILER(); ?>');
    include 'phar://nouveau.phar/b.php';
    var_dump($p->getStub());
} catch (Exception $e) {
    echo 'Error al escribir nuevo.phar: ', $e;
}
?>

    
```php

El ejemplo anterior mostrará:

    string(5) "Salut"
    string(79) "<?php var_dump("Premier"); Phar::mapPhar("nouveau.phar"); __HALT_COMPILER(); ?>"
    string(13) "Tout le monde"
    string(78) "<?php var_dump("Second"); Phar::mapPhar("nouveau.phar"); __HALT_COMPILER(); ?>"

## Véase también

`Phar::getStub`, `Phar::createDefaultStub`
