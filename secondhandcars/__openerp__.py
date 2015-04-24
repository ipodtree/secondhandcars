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

{
    'name': 'Secondhandcars',
    'version': '0.1',
    'category': 'Second Hand Cars',
    'description': """
This module is intended for the management of a list of second hand cars
========================================================================

This module allows managers, vendors, mechanics, and cleaners to organize
their activity in order to to receive, examine, repair, clean and sale
second hand cars.

Once installed, check the user's access rights for 'Second Hand Cars' and then
check the main menu 'Second Hand Cars'.

Main Features
-------------
* Add a brand name
* Add a model of car
* Manage a list of second hand cars
""",
    'author': 'Guillaume RIVIERE',
    'website': 'http://www.guillaumeriviere.name',
    'depends': ['mail'],
    'data': [
        'security/secondhandcars_security.xml',
        'security/ir.model.access.csv',
        'secondhandcars_view.xml',
        'secondhandcars_workflow.xml',
    ],
    'demo': ['secondhandcars_data.xml'],
    'test':[],
    'installable': True,
    'application': True,
    'images': [],
}

