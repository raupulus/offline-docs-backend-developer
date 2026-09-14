---
title: Consideraciones generales sobre la instalación
source_url: https://www.php.net/manual/es/install.general.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/intro.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_reviewed: true
translation_revision: cf9fc9368
order: 1710
---

## Consideraciones generales sobre la instalación

Antes de instalar PHP, es necesario saber qué se desea hacer con PHP. Existen dos casos de uso que se describen en la sección [¿Qué puede hacer PHP?](#intro-whatcando):

- Sitios Web y aplicaciones Web (script lado-servidor)

- Scripts en línea de comandos

Para la primera tarea, que es con diferencia la más común, se necesitan tres cosas: PHP en sí, un servidor Web y un navegador. Probablemente ya se dispone de un navegador y, dependiendo del sistema operativo, también puede disponer de un servidor Web (i.e. Apache en Linux y macOS o IIS en Windows). También es posible alquilar un espacio a una empresa. De esta manera, no será necesario configurar PHP, sino únicamente escribir los scripts, cargarlos en el servidor y ver el resultado en el navegador.

Si se instala PHP y el servidor por uno mismo, se tienen dos opciones. O bien como un módulo del servidor Web (a través de una interfaz directa llamada SAPI). Los servidores que soportan esta solución incluyen, entre otros, Apache y Microsoft Internet Information Server. Si PHP no soporta la interfaz de módulo del servidor Web, siempre es posible utilizarlo como procesador CGI o FastCGI. Esto significa que se debe configurar el servidor para que utilice el ejecutable CGI de PHP, para que procese los ficheros PHP en el servidor.

Si también se desea utilizar PHP en línea de comandos (escribir scripts de generación de imágenes fuera de línea, por ejemplo, o bien procesar textos en función de la información proporcionada), se necesitará un ejecutable PHP. Para más detalles, lea la sección [escribir aplicaciones PHP en línea de comandos](#features.commandline). En este caso, no se necesitará un servidor Web ni un navegador.

A partir de ahora, esta sección describe la instalación de PHP con un servidor Web en Unix y Windows, ya sea como módulo o como ejecutables CGI.

El código fuente y los ejecutables compilados para ciertos sistemas operativos (incluyendo Windows) están disponibles en <https://www.php.net/downloads.php>.
