# -*- coding: utf-8 -*-
###############################################################################
#
#   Copyright (C) 2014-TODAY Akretion <http://www.akretion.com>.
#     All Rights Reserved
#     @author David BEAL <david.beal@akretion.com>
#     @author Sebastien BEAU <sebastien.beau@akretion.com>
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from csv import Dialect
from _csv import QUOTE_NONE


BACKEND_VERSION = 'bleckmann'

ENCODING = 'utf-8'


class LogisticDialect(Dialect):
    """Describe the usual properties of CSV files."""
    delimiter = ';'
    escapechar = '\\'
    quotechar = '"'
    doublequote = True
    quoting = QUOTE_NONE
    skipinitialspace = False
    lineterminator = '\n'
