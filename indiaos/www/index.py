import frappe

def get_context(context):
	context.speakers = frappe.get_list("Conference Speaker", fields=['photo', 'full_name', 'designation', 'organization', 'published'], order_by="full_name", ignore_permissions=True)