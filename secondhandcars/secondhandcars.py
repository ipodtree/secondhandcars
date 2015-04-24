# -*- coding: utf-8 -*-
##############################################################################
#
#    Second Hand Cars module for OpenERP
#    Copyright (C) 2013 Guillaume RIVIERE.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
from datetime import datetime
import time


class secondhandcars_brand(osv.osv):
    """ Brand of cars """
    _name = "secondhandcars.brand"
    _description = "Brands of cars"
    _columns = {
        'name': fields.char('Brand name', size=64, required=True), 
	'international url': fields.char('International URL', size=128, required=True),
        'local url': fields.char('Local URL', size=128, required=True),
	'brandmodel url':fields.char('Brandmodel URL', size=128, required=True),
    }
    _sql_constraints = [
        ('name', 'unique(name)', 'The name of the brand must be unique')
    ]
    _order = 'name asc'

class secondhandcars_model(osv.osv):
    """ Model of cars """
    _name = "secondhandcars.model"
    _description = "Models of cars"
    _columns = {
        'brand_id': fields.many2one('secondhandcars.brand', 'Brand ID', required=True, readonly=False),
        'name': fields.char('Model name', size=64, required=True), 
        'last_year': fields.char('The last year of production', size=64, required=False),
    }
    _sql_constraints = [
        ('name', 'unique(name)', 'The name of the model must be unique')
    ]
    _order = 'name asc'

class secondhandcars_car(osv.osv):
    """ List of cars """
    _name="secondhandcars.car"
    _description="Lists of cars"
    _columns = {
        'create_uid':fields.many2one('res.users', 'Creator', required=True, readonly=True),
        'immatriculation':fields.char('Immatriculation Code', size=64, required=True),
	'model_ids':fields.many2one('secondhandcars.model', 'Model ID', required=True, readonly=False),
        'km_in':fields.integer('Km In', size=64, required=True),
	'km_out':fields.integer('Km Out', size=64, required=True),
        'price':fields.char('Price', size=64, required=True),
        'doors':fields.char('Doors Number', size=64, required=True),
	'seats':fields.char('Seats Number', size=64, required=True),
        'energy':fields.selection((('G1','Gasoline'),('D','Diesel'),('G2','Gaz'),('E','Electricity'),('H','Hybrid')),'Engine Energy', required=True),
   	'state': fields.selection([
	    ('draft', 'New'),
            ('repair', 'In repair'),
            ('ready', 'Ready'),
            ('cancel', 'Unsold'),
	    ('sold', 'Sold')],
            'Status', readonly=True, track_visibility='onchange',
        ),
	'date_draft':fields.datetime('Draft date',required=False),
	'date_repaired':fields.datetime('Repaired date',required=False),
	'date_cancel':fields.datetime('Store date',required=False),
	'date_sold':fields.datetime('Sold date',required=False),
   }

    _defaults = {
        'state': lambda *a: 'draft',
    }
    _order = 'immatriculation asc'

    def car_cancel(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state': 'cancel','date_cancel': datetime.now()}, context=context)

    def car_repair(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'repair'}, context=context)

    def car_sold(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'sold','date_sold': datetime.now()}, context=context)
   
    def car_ready(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'ready','date_repaired': datetime.now()}, context=context)

    def car_draft(self, cr, uid, ids, context={}):
        return self.write(cr, uid, ids, {'state': 'draft','date_draft': datetime.now()}, context=context)



