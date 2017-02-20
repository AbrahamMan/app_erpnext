# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

from frappe.model.document import Document

class DeliveryNoteItem(Document):
	def validate(self):
		self.get_item_weight()

	def get_item_weight():
		item = frappe.get_doc("Item", self.item_code)
		self.net_weight = item.net_weight
		self.weight_uom = item.weight_uom