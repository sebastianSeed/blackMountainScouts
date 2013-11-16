class MyContactForm(ContactForm):
    subject_intro = "URGENT: "
    template_name = "contact_email.html"