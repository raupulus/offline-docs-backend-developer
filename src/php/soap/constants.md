---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/soap.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/soap/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: soap
translation_status: ready
translation_revision: 7c4e8d821
order: 75050
---

## Constantes predefinidas

Estas constantes son definidas por esta extensión, y solo están disponibles si esta extensión ha sido compilada con PHP, o bien cargada en tiempo de ejecución.

| Constante | Valor | Descripción |
|----|----|----|
| `SOAP_1_1` (`int`) | 1 | Especifica el uso de SOAP 1.1 cuando se pasa como opción `soap_version` a SoapServer::\_\_construct o SoapClient::\_\_construct. |
| `SOAP_1_2` (`int`) | 2 | Especifica el uso de SOAP 1.2 cuando se pasa como opción `soap_version` a SoapServer::\_\_construct o SoapClient::\_\_construct. |
| `SOAP_PERSISTENCE_SESSION` (`int`) | 1 | Especifica el uso del encodado SOAP cuando se pasa como opción `use` al método SoapClient::\_\_construct. |
| `SOAP_PERSISTENCE_REQUEST` (`int`) | 2 | Especifica el uso de un encodado específico del servicio cuando se pasa como opción `use` a SoapClient::\_\_construct. |
| `SOAP_FUNCTIONS_ALL` (`int`) | 999 | Obsoleta a partir de PHP 8.4.0. |
| `SOAP_ENCODED` (`int`) | 1 | Especifica el uso de un enlace de estilo RPC cuando se pasa como opción `style` a SoapClient::\_\_construct. |
| `SOAP_LITERAL` (`int`) | 2 | Especifica el uso de un enlace de tipo documento cuando se pasa como valor `style` de la opción a SoapClient::\_\_construct. |
| `SOAP_RPC` (`int`) | 1 |  |
| `SOAP_DOCUMENT` (`int`) | 2 |  |
| `SOAP_ACTOR_NEXT` (`int`) | 1 |  |
| `SOAP_ACTOR_NONE` (`int`) | 2 |  |
| `SOAP_ACTOR_UNLIMATERECEIVER` (`int`) | 3 |  |
| `SOAP_COMPRESSION_ACCEPT` (`int`) | 32 | Especifica el uso del encabezado "Accept-Encoding" cuando se pasa como parte de [ la opción `compression` ](#soapclient.construct.options.compression) a SoapClient::\_\_construct. |
| `SOAP_COMPRESSION_GZIP` (`int`) | 0 | Especifica el uso de la compresión deflate cuando se transmite en el marco de [ la opción `compression` ](#soapclient.construct.options.compression) del método SoapClient::\_\_construct. |
| `SOAP_COMPRESSION_DEFLATE` (`int`) | 16 | Especifica el uso de la compresión deflate cuando se transmite en el marco de [ la opción `compression` ](#soapclient.construct.options.compression) del método SoapClient::\_\_construct. |
| `SOAP_AUTHENTICATION_BASIC` (`int`) | 0 | Especifica el uso de la autenticación HTTP Basic cuando se pasa como opción `authentication` a SoapClient::\_\_construct. |
| `SOAP_AUTHENTICATION_DIGEST` (`int`) | 1 | Especifica el uso de la autenticación HTTP Digest cuando se pasa como opción `authentication` a SoapClient::\_\_construct. |
| `SOAP_SSL_METHOD_TLS` (`int`) | 0 | Utilizada con la opción obsoleta [ `ssl_method` ](#soapclient.construct.options.ssl-method) de SoapClient::\_\_construct. |
| `SOAP_SSL_METHOD_SSLv2` (`int`) | 1 | Utilizada con la opción [ `ssl_method` ](#soapclient.construct.options.ssl-method) obsoleta en el método SoapClient::\_\_construct. |
| `SOAP_SSL_METHOD_SSLv3` (`int`) | 2 | Utilizada con la opción obsoleta [ `ssl_method` ](#soapclient.construct.options.ssl-method) para SoapClient::\_\_construct. |
| `SOAP_SSL_METHOD_SSLv23` (`int`) | 3 | Utilizada con la opción obsoleta [ `ssl_method` ](#soapclient.construct.options.ssl-method) para SoapClient::\_\_construct. |
| `UNKNOWN_TYPE` (`int`) | 999998 |  |
| `XSD_STRING` (`int`) | 101 |  |
| `XSD_BOOLEAN` (`int`) | 102 |  |
| `XSD_DECIMAL` (`int`) | 103 |  |
| `XSD_FLOAT` (`int`) | 104 |  |
| `XSD_DOUBLE` (`int`) | 105 |  |
| `XSD_DURATION` (`int`) | 106 |  |
| `XSD_DATETIME` (`int`) | 107 |  |
| `XSD_TIME` (`int`) | 108 |  |
| `XSD_DATE` (`int`) | 109 |  |
| `XSD_GYEARMONTH` (`int`) | 110 |  |
| `XSD_GYEAR` (`int`) | 111 |  |
| `XSD_GMONTHDAY` (`int`) | 112 |  |
| `XSD_GDAY` (`int`) | 113 |  |
| `XSD_GMONTH` (`int`) | 114 |  |
| `XSD_HEXBINARY` (`int`) | 115 |  |
| `XSD_BASE64BINARY` (`int`) | 116 |  |
| `XSD_ANYURI` (`int`) | 117 |  |
| `XSD_QNAME` (`int`) | 118 |  |
| `XSD_NOTATION` (`int`) | 119 |  |
| `XSD_NORMALIZEDSTRING` (`int`) | 120 |  |
| `XSD_TOKEN` (`int`) | 121 |  |
| `XSD_LANGUAGE` (`int`) | 122 |  |
| `XSD_NMTOKEN` (`int`) | 123 |  |
| `XSD_NAME` (`int`) | 124 |  |
| `XSD_NCNAME` (`int`) | 125 |  |
| `XSD_ID` (`int`) | 126 |  |
| `XSD_IDREF` (`int`) | 127 |  |
| `XSD_IDREFS` (`int`) | 128 |  |
| `XSD_ENTITY` (`int`) | 129 |  |
| `XSD_ENTITIES` (`int`) | 130 |  |
| `XSD_INTEGER` (`int`) | 131 |  |
| `XSD_NONPOSITIVEINTEGER` (`int`) | 132 |  |
| `XSD_NEGATIVEINTEGER` (`int`) | 133 |  |
| `XSD_LONG` (`int`) | 134 |  |
| `XSD_INT` (`int`) | 135 |  |
| `XSD_SHORT` (`int`) | 136 |  |
| `XSD_BYTE` (`int`) | 137 |  |
| `XSD_NONNEGATIVEINTEGER` (`int`) | 138 |  |
| `XSD_UNSIGNEDLONG` (`int`) | 139 |  |
| `XSD_UNSIGNEDINT` (`int`) | 140 |  |
| `XSD_UNSIGNEDSHORT` (`int`) | 141 |  |
| `XSD_UNSIGNEDBYTE` (`int`) | 142 |  |
| `XSD_POSITIVEINTEGER` (`int`) | 143 |  |
| `XSD_NMTOKENS` (`int`) | 144 |  |
| `XSD_ANYTYPE` (`int`) | 145 |  |
| `XSD_ANYXML` (`int`) | 147 |  |
| `APACHE_MAP` (`int`) | 200 |  |
| `SOAP_ENC_OBJECT` (`int`) | 301 |  |
| `SOAP_ENC_ARRAY` (`int`) | 300 |  |
| `XSD_1999_TIMEINSTANT` (`int`) | 401 |  |
| `XSD_NAMESPACE` (`string`) | http://www.w3.org/2001/XMLSchema |  |
| `XSD_1999_NAMESPACE` (`string`) | http://www.w3.org/1999/XMLSchema |  |
| `SOAP_SINGLE_ELEMENT_ARRAYS` (`int`) | 1 | Utilizada con la [ opción `features` ](#soapclient.construct.options.features) en el método SoapClient::\_\_construct. |
| `SOAP_WAIT_ONE_WAY_CALLS` (`int`) | 2 | Utilizada con la [ opción `features` ](#soapclient.construct.options.features) en el método SoapClient::\_\_construct. |
| `SOAP_USE_XSI_ARRAY_TYPE` (`int`) | 4 | Utilizada con la [ opción `features` ](#soapclient.construct.options.features) en el método SoapClient::\_\_construct. |
| `WSDL_CACHE_NONE` (`int`) | 0 | Desactiva el caché WSDL cuando se utiliza en la opción de configuración [soap.wsdl_cache](#ini.soap.wsdl-cache) o en la opción `wsdl_cache` de SoapClient::\_\_construct y SoapServer::\_\_construct. |
| `WSDL_CACHE_DISK` (`int`) | 1 | Indica el uso del caché WSDL en memoria únicamente cuando se utiliza en la opción de configuración [soap.wsdl_cache](#ini.soap.wsdl-cache) o la opción `wsdl_cache` de SoapClient::\_\_construct y SoapServer::\_\_construct. |
| `WSDL_CACHE_MEMORY` (`int`) | 2 | Especifica el uso del caché WSDL en memoria RAM únicamente cuando se utiliza en la opción de configuración [soap.wsdl_cache](#ini.soap.wsdl-cache) o la opción `wsdl_cache` de SoapClient::\_\_construct y SoapServer::\_\_construct. |
| `WSDL_CACHE_BOTH` (`int`) | 3 | Especifica el uso de los cachés WSDL en memoria y en disco cuando se utiliza en la opción de configuración [soap.wsdl_cache](#ini.soap.wsdl-cache) o la opción `wsdl_cache` de SoapClient::\_\_construct y SoapServer::\_\_construct. |

Constantes SOAP
