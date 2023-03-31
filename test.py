__all__ = ['test']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['Base64', 'ASN1DOM', 'hi', 'maxLength', 'asn1', 'v_text', 'Hex'])
var.put('v_text', Js('bYIBrjCCAaoCAQEGBijTFgEACDGCAZswEQIBARMMMDc1MDk4MDA0ODQ4MBYCAQIMEVRy4bqnbiBU\n4bqlbiBUw6BpMA8CAQMTCjI1LzEyLzE5OTgwCAIBBAwDTmFtMA8CAQUMClZp4buHdCBOYW0wCQIB\nBgwES2luaDALAgEHDAZLaMO0bmcwJwIBCAwiQW4gS2jDoW5oLCBDaMOidSBUaMOgbmgsIELhur9u\nIFRyZTBCAgEJDD0xMzAvMiwgVOG7lSA2LCBLaHUgUGjhu5EgMSwgVMOibiBNYWksIEJpw6puIEjD\nsmEsIMSQ4buTbmcgTmFpMDcCAQoMMk7hu5F0IHJ14buTaSBDOjJjbSBkxrDhu5tpIHNhdSDEkXXD\ntGkgbeG6r3QgcGjhuqNpMA8CAQsTCjEyLzA4LzIwMjEwDwIBDAwKMjUvMTIvMjAyMzA2AgENMBUM\nE1Ry4bqnbiBU4bqlbiBUaMOgbmgwGgwYTMOibSBUaOG7iyBMxrDGoW5nIFTDrG5oMAMCAQ4wDgIB\nDxMJMjcyNjk3MDI0MBUCARATEDAyOTREMEU0RTUzRDAwMDA=\n'))
# var.put('Base64', var.get('require')(Js('@lapo/asn1js/base64')))
# var.put('Hex', var.get('require')(Js('@lapo/asn1js/hex')))
var.put('maxLength', Js(10240.0))
var.put('ASN1DOM', var.get('require')(Js('./dom')))
var.get('console').callprop('log', var.get('Base64').get('re').callprop('test', var.get('v_text')))
var.put('hi', var.get('Base64').callprop('unarmor', var.get('v_text')))
var.put('asn1', var.get('ASN1DOM').callprop('decode', var.get('hi'), Js(0.0)))
var.get('console').callprop('log', var.get('asn1').callprop('toVText'))
pass


# Add lib to the module scope
test = var.to_python()