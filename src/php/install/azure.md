---
title: Azure App services
source_url: https://www.php.net/manual/es/install.cloud.azure.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/cloud/azure.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: e8ac70bf5
order: 1620
---

## Azure App services

PHP es frecuentemente utilizado en Azure App Services (alias Microsoft Azure, Windows Azure, Azure Web Apps).

Azure App Services gestiona los pools de servidores Web Windows para alojar su aplicación Web, como alternativa a la gestión de su propio servidor Web en sus propias VM de cálculo Azure u otros servidores.

PHP ya está activado para su sitio web automático Azure App Services. En el portal de Azure, seleccione su sitio Web, y puede elegir la versión de PHP a utilizar. Es posible que desee elegir una versión más reciente que la predeterminada.

Como tal, PHP y las extensiones se ejecutan en Azure App Services de la misma manera que lo harían en otros servidores Windows. Sin embargo, la interfaz de gestión para Azure app services es diferente:

- Portal de Azure: crear, modificar y eliminar los sitios Web. [Portal de Azure](https://portal.azure.com/)
- Tablero de Kudu: si el sitio Web tiene la URL `nombre_del_sitio.azurewebsites.net`, el tablero de Kudu es `https://nombre_del_sitio.scm.azurewebsites.net/`. El tablero ofrece acceso a las funcionalidades de depuración, a la gestión de los ficheros y a las extensiones del sitio. Las extensiones de sitio son un mecanismo de Azure para agregar programas adicionales, como versiones preliminares de PHP, a un sitio Web.
- No se puede utilizar el gestor de servicios de Internet, el gestor de servidor o RDP.

También existe un SDK PHP, que permitirá utilizar los numerosos servicios de Azure desde su código PHP. Ver [Azure SDK para PHP](https://github.com/Azure/azure-sdk-for-php).

Para más información, ver [Centro de desarrolladores de PHP de Azure](https://azure.microsoft.com/en-us/develop/php/)

## WinCache

WinCache está activado por omisión en Azure App Services y se recomienda dejarlo activado. Si instala su propia versión de PHP, debe activar WinCache.

## Build personalizada de PHP

Puede cargar su propia versión de PHP en su D:\Home (C:\\ no es accesible en escritura). Luego, en el portal de Azure, defina SCRIPT_PROCESSOR para .php en la ruta de acceso absoluta al fichero php-cgi.exe en su build personalizada.
