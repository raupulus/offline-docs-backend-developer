---
title: Protocolos y soporte de Internet
source_url: https://docs.python.org/es/3
source_path: library/internet.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3010
---

# Protocolos y soporte de Internet

Los módulos descritos en este capítulo implementan protocolos de
Internet y son compatibles con la tecnología relacionada. Todos están
implementados en Python. La mayoría de estos módulos requieren la
presencia del módulo dependiente del sistema "socket", que actualmente
es compatible con las plataformas más populares. Aquí hay una
descripción general:

* "webbrowser" --- Convenient web-browser controller

  * Command-line interface

  * Browser controller objects

* "wsgiref" --- WSGI Utilities and Reference Implementation

  * "wsgiref.util" -- WSGI environment utilities

  * "wsgiref.headers" -- WSGI response header tools

  * "wsgiref.simple_server" -- a simple WSGI HTTP server

  * "wsgiref.validate" --- WSGI conformance checker

  * "wsgiref.handlers" -- server/gateway base classes

  * "wsgiref.types" -- WSGI types for static type checking

  * Ejemplos

* "urllib" --- URL handling modules

* "urllib.request" --- Extensible library for opening URLs

  * Objetos Request

  * Objetos OpenerDirector

  * Objetos BaseHandler

  * Objetos HTTPRedirectHandler

  * Objetos HTTPCookieProcessor

  * Objetos ProxyHandler

  * Objetos HTTPPasswordMgr

  * Objetos HTTPPasswordMgrWithPriorAuth

  * Objetos AbstractBasicAuthHandler

  * Objetos HTTPBasicAuthHandler

  * Objetos ProxyBasicAuthHandler

  * Objetos AbstractDigestAuthHandler

  * Objetos HTTPDigestAuthHandler

  * Objetos ProxyDigestAuthHandler

  * Objetos HTTPHandler

  * Objetos HTTPSHandler

  * Objetos FileHandler

  * Objetos DataHandler

  * Objetos FTPHandler

  * Objetos CacheFTPHandler

  * Objetos UnknownHandler

  * Objetos HTTPErrorProcessor

  * Ejemplos

  * Interfaz heredada

  * "urllib.request" Restrictions

* "urllib.response" --- Response classes used by urllib

* "urllib.parse" --- Parse URLs into components

  * Análisis de URL

  * Análisis de seguridad de URL

  * Análisis de bytes codificados ASCII

  * Resultados del análisis estructurado

  * Cita de URL

* "urllib.error" --- Exception classes raised by urllib.request

* "urllib.robotparser" ---  Parser for robots.txt

* "http" --- HTTP modules

  * Códigos de estado HTTP

  * Categoría de estado HTTP

  * Métodos HTTP

* "http.client" --- HTTP protocol client

  * Objetos de "HTTPConnection"

  * Objetos de "HTTPResponse"

  * Ejemplos

  * Objetos de "HTTPMessage"

* "ftplib" --- FTP protocol client

  * Reference

    * FTP objects

    * FTP_TLS objects

    * Module variables

* "poplib" --- POP3 protocol client

  * Objetos POP3

  * Ejemplo POP3

* "imaplib" --- IMAP4 protocol client

  * Objetos de IMAP4

  * Ejemplo IMAP4

* "smtplib" --- SMTP protocol client

  * Objetos SMTP

  * Ejemplo SMTP

* "uuid" --- UUID objects according to **RFC 9562**

  * Uso de la línea de comandos

  * Ejemplo

  * Ejemplo de línea de comandos

* "socketserver" --- A framework for network servers

  * Notas de creación del servidor

  * Objetos de servidor

  * Solicitar objetos de controlador

  * Ejemplos

    * "socketserver.TCPServer" Ejemplo

    * "socketserver.UDPServer" Ejemplo

    * Mixins asincrónicos

* "http.server" --- HTTP servers

  * Command-line interface

  * Security considerations

* "http.cookies" --- HTTP state management

  * Objetos de cookie

  * Objetos Morsel

  * Ejemplo

* "http.cookiejar" --- Cookie handling for HTTP clients

  * CookieJar and FileCookieJar objects

  * Subclases FileCookieJar y co-operación con navegadores web

  * CookiePolicy objects

  * DefaultCookiePolicy objects

  * Cookie objects

  * Ejemplos

* "xmlrpc" --- Módulos XMLRPC para cliente y servidor

* "xmlrpc.client" --- XML-RPC client access

  * Objetos *ServerProxy*

  * Objetos *DateTime*

  * Objetos binarios

  * Objetos Faults

  * Objetos ProtocolError

  * Objetos MultiCall

  * Funciones de Conveniencia

  * Ejemplo de uso de cliente

  * Ejemplo de uso de cliente y servidor

* "xmlrpc.server" --- Basic XML-RPC servers

  * SimpleXMLRPCServer objects

    * SimpleXMLRPCServer example

  * CGIXMLRPCRequestHandler

  * Documentando el servidor XMLRPC

  * DocXMLRPCServer objects

  * DocCGIXMLRPCRequestHandler

* "ipaddress" --- IPv4/IPv6 manipulation library

  * Funciones de fábrica de conveniencia

  * Direcciones IP

    * Objetos de dirección

    * Conversión a cadenas y enteros

    * Operadores

      * Operadores de comparación

      * Operadores aritméticos

  * Definiciones de red IP

    * Prefijo, máscara de red y máscara de host

    * Objetos de red

    * Operadores

      * Operadores lógicos

      * Iteración

      * Redes como contenedores de direcciones

  * Objetos de interfaz

    * Operadores

      * Operadores lógicos

  * Otras funciones de nivel de módulo

  * Excepciones personalizadas
