---
title: Introducción
source_url: https://www.php.net/manual/es/security.intro.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/intro.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: 96c9d88ba
order: 109970
---

## Introducción

PHP es un potente lenguaje, y su intérprete, bien como módulo del servidor web o bien como binario CGI, puede acceder a ficheros, ejecutar comandos o abrir conexiones de red desde el servidor. Estas propiedades hacen que, por omisión, sea inseguro todo lo que se ejecute en un servidor web. PHP está diseñado específicamente para ser un lenguaje más seguro para escribir aplicaciones CGI que Perl o C. Partiendo de un correcto ajuste de opciones de configuración para tiempo de ejecución y en tiempo de compilación, y el uso de prácticas de programación apropiadas, pueden proporcionarle la combinación de libertad y de seguridad que necesita.

Dado que hay muchas vías para ejecutar PHP, existen muchas opciones de configuración para controlar su comportamiento. Al haber una extensa selección de opciones se garantiza poder usar PHP para un gran número de propósitos, pero a la vez significa que existen combinaciones que conllevan una configuración menos segura.

La flexibilidad de configuración de PHP rivaliza igualmente con la flexibilidad de su código. PHP puede ser usado para construir completas aplicaciones de servidor, con toda la potencia de un usuario de consola, o se puede usar sólo desde el lado del servidor implicando un menor riesgo dentro de un entorno controlado. El cómo construir ese entorno, y cómo de seguro es, depende del desarrollador PHP.

Este capítulo comienza con algunos consejos generales de seguridad, explica las diferentes combinaciones de opciones de configuración y las situaciones en que pueden ser útiles, y describe diferentes consideraciones relacionadas con la programación de acuerdo a diferentes niveles de seguridad.
