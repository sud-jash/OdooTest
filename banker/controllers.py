# -*- coding: utf-8 -*-
from openerp import http

# class Banker(http.Controller):
#     @http.route('/banker/banker/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/banker/banker/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('banker.listing', {
#             'root': '/banker/banker',
#             'objects': http.request.env['banker.banker'].search([]),
#         })

#     @http.route('/banker/banker/objects/<model("banker.banker"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('banker.object', {
#             'object': obj
#         })