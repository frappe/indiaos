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
					"name": "Conference Speaker"
				},
				{
					"type": "doctype",
					"name": "Conference Agenda"
				},
				{
					"type": "doctype",
					"name": "Conference Talk"
				},
				{
					"type": "doctype",
					"name": "CFP"
				},
			]
		},
	]
