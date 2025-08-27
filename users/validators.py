import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 10:
            raise ValidationError(_("Password must be at least 10 characters long."))

        if not re.findall('[A-Z]', password):
            raise ValidationError(_("Password must contain at least 1 uppercase letter."))

        if not re.findall('[a-z]', password):
            raise ValidationError(_("Password must contain at least 1 lowercase letter."))

        if not re.findall('[0-9]', password):
            raise ValidationError(_("Password must contain at least 1 digit."))

        if not re.findall('[^A-Za-z0-9]', password):
            raise ValidationError(_("Password must contain at least 1 special character."))
        
    def get_help_text(self):
        return _(
            "Your password must contain at least 10 characters, including an uppercase, "
            "a lowercase, a digit, and a special character."
        )
