---
title: Instalación de Composer y paquetes de terceros
source_url: https://www.php.net/manual/es/install.composer.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/composer.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: false
translation_revision: 3678a6db1
order: 1660
---

## Instalación de Composer y paquetes de terceros

## Introducción a Composer

[Composer](https://getcomposer.org/) es un administrador de dependencias para PHP, lo cual hace posible definir el uso de paquetes de código de terceros en un proyecto, facilitando su instalación y actualización. El cual se beneficia de la característica integrada de [autocarga de clases](#language.oop5.autoload) de PHP, repositorios de paquetes de PHP como [Packagist](https://packagist.org), y convenciones comunes de diseño y codificación del proyecto.

Por ejemplo, si una aplicación o sitio web en PHP necesita trabajar con valores UUID, el [paquete `ramsey/uuid` de Ben Ramsey](https://packagist.org/packages/ramsey/uuid) el cual implementa los tipos de UUID ampliamente conocidos y utilizados, y definidos en [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122) podrían ser utilizados.

Brevemente, esto se hace creando un archivo `composer.json` en el proyecto, y usando Composer para instalar la última versión del paquete, e incluyendo el script de autocarga de Composer para hacerlo disponible al código. La [documentación "Basic Usage" (Uso básico) de Composer](https://getcomposer.org/doc/01-basic-usage.md) profundiza en esto.

`composer.json` el cual incluye un solo paquete.

```php
{
    "require": {
        "ramsey/uuid": "^4.7"
    }
}

   
```
