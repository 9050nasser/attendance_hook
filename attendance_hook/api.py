import frappe
@frappe.whitelist()
def login():
    y = frappe.db.get_value("Employee", {"user_id": frappe.session.user}, "name")
    shift = frappe.get_doc("Employee", y)
    if y and shift:
        x = frappe.new_doc("Employee Checkin")
        x.employee = y
        x.log_type = "IN"
        x.insert()
        return print(f"Done IN {x.name}")
    
@frappe.whitelist()
def logout():
    y = frappe.db.get_value("Employee", {"user_id": frappe.session.user}, "name")
    shift = frappe.get_doc("Employee", y)

    if y and shift:
        x = frappe.new_doc("Employee Checkin")
        x.employee = y
        x.log_type = "OUT"
        x.insert()
        return print(f"Done OUT {x.name}")