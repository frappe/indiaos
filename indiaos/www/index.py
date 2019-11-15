import frappe

def get_context(context):
	context.speakers = frappe.get_list("Conference Speaker", filters={'published': 1}, fields=['photo', 'full_name', 'designation', 'organization'], order_by="full_name", ignore_permissions=True)