---
title: 2. Uso de Python en plataformas Unix
source_url: https://docs.python.org/es/3
source_path: using/unix.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: using
order: 5100
---

# 2. Uso de Python en plataformas Unix

## 2.1. Obteniendo e instalando la última versión de Python

### 2.1.1. En Linux

Python comes preinstalled on most Linux distributions, and is
available as a package on all others.  However there are certain
features you might want to use that are not available on your distro's
package.  You can compile the latest version of Python from source.

In the event that the latest version of Python doesn't come
preinstalled and isn't in the repositories as well, you can make
packages for your own distro.  Have a look at the following links:

Ver también:

  https://www.debian.org/doc/manuals/maint-guide/first.en.html
     para usuarios de Debian

  https://en.opensuse.org/Portal:Packaging
     para los usuarios de OpenSuse

  https://docs.fedoraproject.org/en-US/package-
  maintainers/Packaging_Tutorial_GNU_Hello/
     para los usuarios de Fedora

  https://slackbook.org/html/package-management-making-packages.html
     para los usuarios de Slackware

#### 2.1.1.1. Installing IDLE

In some cases, IDLE might not be included in your Python installation.

* For Debian and Ubuntu users:

     sudo apt update
     sudo apt install idle

* For Fedora, RHEL, and CentOS users:

     sudo dnf install python3-idle

* For SUSE and OpenSUSE users:

     sudo zypper install python3-idle

* For Alpine Linux users:

     sudo apk add python3-idle

### 2.1.2. En FreeBSD y OpenBSD

* Usuarios FreeBSD, para añadir al paquete use:

     pkg install python3

* Usuarios OpenBSD, para añadir al paquete use:

     pkg_add -r python

     pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/<insert your architecture here>/python-<version>.tgz

  Por ejemplo, los usuarios de i386 obtienen la versión 2.5.1 de
  Python usando:

     pkg_add ftp://ftp.openbsd.org/pub/OpenBSD/4.2/packages/i386/python-2.5.1p2.tgz

## 2.2. Construyendo Python

Ver también:

  If you want to contribute to CPython, refer to the devguide, which
  includes build instructions and other tips on setting up
  environment.

If you want to compile CPython yourself, first thing you should do is
get the source. You can download either the latest release's source or
grab a fresh clone. You will also need to install the build
requirements.

El proceso de construcción consta de los comandos habituales:

   ./configure
   make
   make install

Opciones de configuración y las advertencias para plataformas Unix
específicas están ampliamente documentadas en el archivo README.rst en
la raíz del árbol de fuentes de Python.

Advertencia:

  "make install" puede sobreescribir o enmascarar el binario
  "python3". Por lo tanto se recomienda "make altinstall" en lugar de
  "make install" debido a que sólo instala
  "*exec_prefix*/bin/python*version*".

## 2.3. Rutas y archivos relacionados con Python

Estos están sujetos a diferencias según las convenciones de
instalación locales; "prefix" y "exec_prefix" son dependientes de la
instalación y deben interpretarse como en el software GNU; pueden ser
iguales.

Por ejemplo, en la mayoría de los sistemas Linux, el valor
predeterminado para ambos es "/usr".

+-------------------------------------------------+--------------------------------------------+
| Archivo/directorio                              | Significado                                |
|=================================================|============================================|
## | "*exec_prefix*/bin/python3"                     | Ubicación recomendada del intérprete.      |

| "*prefix*/lib/python*version*",                 | Ubicaciones recomendadas de los            |
| "*exec_prefix*/lib/python*version*"             | directorios que contienen los módulos      |
## |                                                 | estándar.                                  |

| "*prefix*/include/python*version*",             | Ubicaciones recomendadas de los            |
| "*exec_prefix*/include/python*version*"         | directorios que contienen los archivos de  |
|                                                 | inclusión necesarios para desarrollar      |
|                                                 | extensiones de Python e incrustar el       |
## |                                                 | intérprete.                                |

## 2.4. Miscelánea

Para usar fácilmente los scripts de Python en Unix, debe hacerlos
ejecutables, p. ej. con

   $ chmod +x script

y coloque una línea *Shebang* adecuada en la parte superior del
script. Una buena opción es usualmente

   #!/usr/bin/env python3

que busca el intérprete de Python en el conjunto "PATH". Sin embargo,
algunos Unices puede que no tengan el comando **env**, por lo que es
posible que deba codificar "/usr/bin/python3" como la ruta intérprete.

Para usar comandos de shell en sus scripts de Python, mire el módulo
"subprocess".

## 2.5. OpenSSL personalizado

1. Para utilizar la configuración de OpenSSL de su proveedor y el
   almacén de confianza del sistema, busque el directorio con el
   archivo "openssl.cnf" o el enlace simbólico en "/etc". En la
   mayoría de las distribuciones, el archivo está en "/etc/ssl" o
   "/etc/pki/tls". El directorio también debe contener un archivo
   "cert.pem" y / o un directorio "certs".

      $ find /etc/ -name openssl.cnf -printf "%h\n"
      /etc/ssl

2. Descargue, compile e instale OpenSSL. Asegúrese de utilizar
   "install_sw" y no "install". El destino "install_sw" no anula
   "openssl.cnf".

      $ curl -O https://www.openssl.org/source/openssl-VERSION.tar.gz
      $ tar xzf openssl-VERSION
      $ pushd openssl-VERSION
      $ ./config \
          --prefix=/usr/local/custom-openssl \
          --libdir=lib \
          --openssldir=/etc/ssl
      $ make -j1 depend
      $ make -j8
      $ make install_sw
      $ popd

3. Construir Python con OpenSSL personalizado (consulte las opciones
   configure "--with-openssl" y "--with-openssl-rpath")

      $ pushd python-3.x.x
      $ ./configure -C \
          --with-openssl=/usr/local/custom-openssl \
          --with-openssl-rpath=auto \
          --prefix=/usr/local/python-3.x.x
      $ make -j8
      $ make altinstall

Nota:

  Las versiones de parche de OpenSSL tienen una ABI compatible con
  versiones anteriores. No es necesario volver a compilar Python para
  actualizar OpenSSL. Es suficiente reemplazar la instalación
  personalizada de OpenSSL con una versión más nueva.
