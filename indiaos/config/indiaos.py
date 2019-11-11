from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Conference Participant"
				},
				{
					"type": "doctype",
					"name": "CFP"
				}
			]
		},
	]
