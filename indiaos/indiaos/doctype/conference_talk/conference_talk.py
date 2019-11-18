# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class ConferenceTalk(WebsiteGenerator):
	website = frappe._dict(
		page_title_field="talk_title",
		condition_field="published",
		no_cache=1,
		sitemap=1
	)

	def make_route(self):
		return 'talks/' + self.scrub(self.talk_title)

	def get_context(self, context):
		context.speaker = frappe.get_doc("Conference Speaker", self.speaker)