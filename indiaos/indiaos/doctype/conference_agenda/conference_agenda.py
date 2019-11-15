# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class ConferenceAgenda(WebsiteGenerator):
	website = frappe._dict(
		page_title_field="name",
		condition_field="published",
		no_cache=1,
		sitemap=1
	)

	def validate(self):
		if self.published:
			frappe.msgprint("Publishing All Talks and Speakers", "Publishing")
			talks = [item.talk for item in self.schedule if item.talk]
			for talk in talks:
				doc = frappe.get_doc("Conference Talk", talk)
				doc.published = True
				doc.save()

	def get_context(self, context):
		speakers = frappe.get_list("Conference Speaker", fields=['name', 'photo', 'full_name', 'designation', 'organization', 'published', 'route'], order_by="full_name", ignore_permissions=True)
		talks = frappe.get_list("Conference Talk", fields=['talk_title', 'speaker', 'short_summary', 'talk_type'], order_by="sequence", ignore_permissions=True)
		context.schedule = self.schedule
		context.talks = { talk.talk_title: talk for talk in talks }
		context.speakers = { speaker.name: speaker for speaker in speakers }


