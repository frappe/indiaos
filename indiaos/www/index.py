import frappe

no_cache = 1

def get_context(context):
	speakers = frappe.get_list("Conference Speaker", fields=['name', 'photo', 'full_name', 'designation', 'organization', 'published', 'route'], order_by="full_name", ignore_permissions=True)
	context.talks = frappe.get_list("Conference Talk", filters={'show_on_home_page': 1, 'published': 1},  fields=['*'], ignore_permissions=True, order_by="talk_title")
	context.speakers = { speaker.name: speaker for speaker in speakers }