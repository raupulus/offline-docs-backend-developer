---
title: Ejemplos
source_url: https://www.php.net/manual/es/radius.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/radius/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: radius
translation_status: ready
translation_reviewed: false
translation_revision: 9ac4d06c0
order: 67530
---

## Ejemplos

¿Cómo iniciar?

- Obtener un recurso radius

- Configurar la librería

- Crear la petición

- Poner atributos

- Enviar la petición

- Recibir atributos

- Cerrar el recurso radius (opcional)

También sirve echar un vistazo a los ejemplos en este paquete.

El paquete contiene un ejemplo de script php. Este script demuestra como autenticar con radius utilizando PAP o CHAP (md5). Si se autentica con servidores Microsoft Radius entonces no le será posible utilizar CHAP (md5). Si quisiera autenticarse con servidores Microsoft tiene que utilizar MS-CHAPv1 o MS-CHAPv2, pero es más complicado, porque usted necesita md4, sha1 y des para generar los datos correctos. Los ejemplos adjuntos demuestran todos los métodos de autenticación, incluyendo MS-CHAPv1 y MS-CHAPv2. Para tener funcionando MS-CHAP necesita las extensiones [mcrypt](#ref.mcrypt) y [mhash](#ref.mhash) iniciando con la version 1.2 de este paquete, la extensión mcrypt ya no es necesaria.
