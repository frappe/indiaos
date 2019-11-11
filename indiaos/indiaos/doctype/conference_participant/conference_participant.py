# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ConferenceParticipant(Document):
	def validate(self):
		doc = frappe.get_value("Conference Participant", {'email': self.email})
		if doc:
			raise frappe.exceptions.UniqueValidationError 

	def after_insert(self):
		self.send_mail()

	def send_mail(self):
		email_args = {
			'recipients': self.email,
			'subject': "Here's your ticket for IndiaOS",
			'template': "ticket",
			'args': {
				'full_name': self.full_name,
				'name': self.name
			},
			'now':False
		}
		frappe.enqueue(method=frappe.sendmail, queue='short', timeout=300, is_async=True, **email_args)

@frappe.whitelist(allow_guest=True)
def register(name, email, organization='', event="IndiaOS 2020"):
	part = frappe.new_doc("Conference Participant")
	part.full_name = name
	part.email = email
	part.organization = organization
	part.event = event
	try:
		part.save(ignore_permissions=True)
	except frappe.exceptions.UniqueValidationError:
		return {'status': 'failed', 'reason': 'already-registered'}
	return {'status': 'success'}
