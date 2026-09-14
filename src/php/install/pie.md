---
title: Instalación de PIE y extensiones de terceros
source_url: https://www.php.net/manual/es/install.pie.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/pie.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: b75966249
order: 1770
---

## Instalación de PIE y extensiones de terceros

## Introducción a PIE

[PIE](https://github.com/php/pie) es un instalador para PHP que permite instalar extensiones PHP de terceros, que luego pueden ser fácilmente instaladas y actualizadas. Aprovecha el repositorio de extensiones PHP de [Packagist](https://packagist.org) para encontrar el código fuente para compilar la extensión, o un binario de Windows para descargar, si existe. Si descarga el código fuente, también sabe cómo compilarlo e instalarlo.

Tras [instalar los requisitos y PIE en sí](https://github.com/php/pie?tab=readme-ov-file#what-do-i-need-to-get-started), puede instalar la [extensión MongoDB](#mongodb.mongodb) ejecutando el siguiente comando en la línea de comandos.

Instalación de la extensión MongoDB con PIE

```php
pie install mongodb/mongodb-extension

   
```

La documentación de ["Uso de PIE"](https://php.github.io/pie/#docs/usage) profundiza más en este tema.
