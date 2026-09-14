---
title: La clase Yaf_Config_Ini
source_url: https://www.php.net/manual/es/class.yaf-config-ini.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf-config-ini.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 104560
---

## Introducción

La clase Yaf_Config_Ini permite a los desarrolladores almacenar la información de configuración en un formato INI familiar y leerla en la aplicación utilizando una sintaxis apropiada de objetos anidados. El formato INI está especializado en proporcionar la capacidad de tener una jerarquía de claves de información de configuación y herencia entre secciones de información de configuración. Las jerarquías de información de configuración está soportadas separando las claves con el carácter punto ("."). Una sección puede extender o heredar de otra sección añadiendo al nombre de la sección el carácter dos puntos(":") y el nombre de la sección desde la que se hereda la información.

> [!NOTE]
> Yaf_Config_Ini utiliza la función » parse_ini_file() de PHP. Revise esta documentación para conocer sus comportamientos específicos, los cuales propaga a la clase Yaf_Config_Ini, tales como el manejo de valores especiales como "`true`", "`false`", "yes", "no", y "`null`".

## Sinopsis de la clase

Yaf_Config_Ini

Yaf_Config_Ini

extends

Yaf_Config_Abstract

Iterator

ArrayAccess

Countable

Propiedades

Métodos

Métodos heredados

## Propiedades

`_config`  

`_readonly`  

## Ejemplos

Ejemplo de `Yaf_Config_Ini`

Este ejemplo ilustra el uso básico de la clase Yaf_Config_Ini para cargar la información de configuración desde un fichero INI. En este ejemplo existe información de configuración para el sistema de producción y el sistema de pruebas (staging). Ya que la información de configuración del sistema de pruebas es similar a la de producción, la sección de pruebas hereda de la sección de producción. En este caso, la decisión es arbitraria y podría haber sido escrito a la inversa, con la sección de producción heredando de la sección de pruebas, aunque este puede no ser el caso para situaciones más complejas. Suponga que la información de configuración siguiente está contenida en /ruta/a/config.ini:

```php
; Información de configuración del sitio de producción
[production]
webhost                  = www.example.com
database.adapter         = pdo_mysql
database.params.host     = db.example.com
database.params.username = dbuser
database.params.password = secret
database.params.dbname   = dbname

; La información de configuración del sitio de pruebas hereda del de producción y
; sobrescribe los valores según sea necesario
[staging : production]
database.params.host     = dev.example.com
database.params.username = devuser
database.params.password = devsecret

    
```

```php
<?php
$config = new Yaf_Config_Ini('/ruta/a/config.ini', 'staging');

var_dump($config->database->params->host);
var_dump($config->database->params->dbname);
var_dump($config->get("database.params.username"));
?>

    
```

Resultado del ejemplo anterior es similar a:

    string(15) "dev.example.com"
    string(6) "dbname"
    string(7) "devuser"
