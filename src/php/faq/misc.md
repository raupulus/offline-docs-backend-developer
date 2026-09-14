---
title: Preguntas Varias
source_url: https://www.php.net/manual/es/faq.misc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: faq/misc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: faq
translation_status: ready
translation_revision: 3e08a8aae
order: 1490
---

## Preguntas Varias

Puede que existan algunas preguntas que no podemos colocar en otras categorías. Este es el lugar en donde puede encontrarlas.

**Q:** ¿Cómo puedo manipular los manuales comprimidos mediante bz2 en Windows?

**A:** Si no cuenta con una herramienta de archivación que pueda manejar archivos bz2, [descargue](https://www.sourceware.org/bzip2/) la herramienta de línea de comandos de RedHat (por favor refiérase a la inforamción presentada más adelante).

Si no desea usar una herramienta de línea de comandos, puede probar herramientas gratuitas como [Stuffit Expander](http://www.stuffit.com/), [UltimateZip](http://www.ultimatezip.com/), [7-Zip](http://www.7-zip.org/), o [Quick Zip](http://www.quickzip.org/). Si dispone de herramientas como [WinRAR](http://www.rarlab.com/) o [Power Archiver](http://www.powerarchiver.com/), puede descomprimir fácilmente archivos bz2 con ellas. Si usa Total Commander (anteriormente Windows Commander), un módulo adicional para ese programa se encuentra disponible de forma gratuita desde el sitio de [Total Commander](http://www.ghisler.com/).

La herramienta bzip2 de línea de comandos por Redhat:

Los usuarios de Win2k Sp2 deben obtener la versión más reciente, 1.0.2, todos los demás usuarios de Windows deben obtener la versión 1.00. Después de la descarga, renombre el ejecutable a bzip2.exe. Para mayor conveniencia, colóquelo en un directorio que sea parte de sus rutas predeterminadas, p.ej. C:\Windows, en donde C representa la unidad en donde se encuentra su instalación de Windows.

Nota: lang representa su lenguaje, y x el formato deseado, p.ej: pdf. Para descomprimir el archivo php_manual_lang.x.bz2 siga las siguientes instrucciones:

- abra una ventana con el intérprete de comandos

- cambie de directorio hacia la carpeta en donde almacenó el archivo php_manual_lang.x.bz2 descargado

- invoque bzip2 -d php_manual_lang.x.bz2, extrayendo de este modo php_manual_lang.x en la misma carpeta

En caso de que haya descargado el archivo php_manual_lang.tar.bz2 con varios archivos html en su interior, el procedimiento es el mismo. La única diferencia es que recibe un archivo php_manual_lang.tar. Se conoce que el formato tar es tratado por la mayoría de archivadores en Windows, como por ejemplo [WinZip](http://www.winzip.com/).
