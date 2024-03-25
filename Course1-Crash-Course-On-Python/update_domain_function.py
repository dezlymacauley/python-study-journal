# A company has changed their domain name
# However a lot of the company email addresses are still using the old one
# Write a function that updates a given email address 

# -----------------------------------------------------------------------------

company_email = "goldstonebank@protonmail.com"
print("The previous email address was: " + company_email)

def update_domain(_email_address, _old_domain, _new_domain):
    if "@" + _old_domain in _email_address:
        index = _email_address.index("@" + _old_domain)

        # Get the firs portion of the old email
        new_email = _email_address[:index] + "@" + _new_domain
        return new_email
    else:
        return _email_address

# Use the function to update the original
company_email = update_domain(company_email, "protonmail.com", "proton.me" )
print("The current email address is: " + company_email)

#------------------------------------------------------------------------------
