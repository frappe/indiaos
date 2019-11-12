# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.integrations.utils import get_payment_gateway_controller
from frappe.realtime import publish_realtime

class ConferenceParticipant(Document):
	def before_insert(self):
		doc = frappe.get_value("Conference Participant", {'email': self.email, 'paid': 1})
		if doc:
			raise frappe.exceptions.UniqueValidationError 

	def get_payment_gateway_url(self):
		controller = get_payment_gateway_controller("Razorpay")

		title = "Ticekt Payment for {0}".format(self.name)
		payment_details = {
			"amount": 300,
			"title": title,
			"description": title,
			"reference_doctype": "Conference Participant",
			"reference_docname": self.name,
			"payer_email": frappe.session.user,
			"payer_name": self.full_name,
			"order_id": self.name,
			"currency": "INR"
		}

		# Redirect the user to this url
		return controller.get_payment_url(**payment_details)

	def get_payment_success_message(self):
		return "Your payment was successfully accepted. You can close this window now."

	def on_payment_authorized(self, status_changed_to=None):
		self.paid = 1
		self.save(ignore_permissions=True)
		publish_realtime(self.token, "success")
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
def register(name, email, token, organization='', event="IndiaOS 2020"):
	part = frappe.new_doc("Conference Participant")
	part.full_name = name
	part.email = email
	part.token = token
	part.organization = organization
	part.event = event
	try:
		part.save(ignore_permissions=True)
	except frappe.exceptions.UniqueValidationError:
		return {'status': 'failed', 'reason': 'already-registered'}
	return {'status': 'success', 'redirect_to': part.get_payment_gateway_url() }

