# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class ConferenceSpeaker(WebsiteGenerator):
	website = frappe._dict(
		page_title_field="full_name",
		condition_field="published",
		no_cache=1,
		sitemap=1
	)

	def make_route(self):
		return 'speakers/' + self.scrub(self.full_name)

	def get_context(self, context):
		context.speaker = self