# This file is part of the Frescobaldi project, http://www.frescobaldi.org/
#
# Copyright (c) 2008 - 2014 by Wilbert Berendsen
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# See http://www.gnu.org/licenses/ for more information.

"""
An Object Editor widget.
"""

from __future__ import unicode_literals

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import app
import objecteditor


class Widget(QWidget):

    def __init__(self, tool):
        super(Widget, self).__init__(tool)
        self.mainwindow = tool.mainwindow()
        
        layout = QVBoxLayout(spacing=1)
        self.setLayout(layout)
        
        self.XOffsetBox = QDoubleSpinBox()
        self.XOffsetBox.setRange(-99,99)
        self.XOffsetBox.setSingleStep(0.1)
        self.XOffsetLabel = l = QLabel()
        l.setBuddy(self.XOffsetBox)
 
        self.YOffsetBox = QDoubleSpinBox()
        self.YOffsetBox.setRange(-99,99)
        self.YOffsetBox.setSingleStep(0.1)
        self.YOffsetLabel = l = QLabel()
        l.setBuddy(self.YOffsetBox)
        
        layout.addWidget(self.XOffsetBox)
        layout.addWidget(self.XOffsetLabel)
        layout.addWidget(self.YOffsetBox)
        layout.addWidget(self.YOffsetLabel)
        
        layout.addStretch(1)

        app.translateUI(self)
        self.loadSettings()
        
        self.connectSlots()
    
    def connectSlots(self):
        import panelmanager
        panelmanager.manager(self.mainwindow).svgview.widget().view.objectDragged.connect(self.setOffset)

    def translateUI(self):
        self.XOffsetLabel.setText(_("X Offset"))
        self.XOffsetBox.setToolTip(_("Display the X Offset"))
        self.YOffsetLabel.setText(_("Y Offset"))
        self.YOffsetBox.setToolTip(_("Display the Y Offset"))
	
    def setOffset(self, x, y):
        """Set the value of the offset externally."""
        self.XOffsetBox.setValue(x)
        self.YOffsetBox.setValue(y)
    
    def loadSettings(self):
        """Called on construction. Load settings and set checkboxes state."""
        s = QSettings()
        s.beginGroup('object_editor')
        
    def saveSettings(self):
        """Called on close. Save settings and checkboxes state."""
        s = QSettings()
        s.beginGroup('object_editor')

