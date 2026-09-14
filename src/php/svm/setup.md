---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/svm.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svm/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svm
translation_status: ready
translation_reviewed: false
translation_revision: 1ca2d4af9
order: 89670
---

## Instalación/Configuración

## Requisitos

LIBSVM es requerido, y está disponible a través de algunos gestores de paquetes - libsvm-devel para el sistema basado en RPM o libsvm-dev para los basados en Debian. Como alternativa, está disponible directamente desde el sitio web. Si está instalando desde el [sitio web oficial](http://www.csie.ntu.edu.tw/~cjlin/libsvm) algunos pasos son necesarios ya que el paquete no se instala automáticamente. Por ejemplo, suponiendo que la última versión es la 3.1:

    wget http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+tar.gz
    tar xvzf libsvm-3.1.tar.gz
    cd libsvm-3.1
    make lib
    cp libsvm.so.1 /usr/lib
    ln -s libsvm.so.1 libsvm.so
    ldconfig
    ldconfig --print | grep libsvm

      

Este último paso debe mostrar LIBSVM está instalado.

## Instalación

Información sobre la instalación de estas extensiones PECL puede ser encontrada en el capítulo del manual titulado [Instalación de extensiones PECL](#install.pecl). Otra información como notas sobre nuevas versiones, descargas, fuentes de ficheros, información sobre los mantenedores así como un CHANGELOG, pueden ser encontradas aquí: <https://pecl.php.net/package/svm>
