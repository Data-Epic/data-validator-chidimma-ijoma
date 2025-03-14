import re #Regular Expression module to be used for validations

class DataValidator:
    """
    A class for validating personal data entries such as emails, phone numbers, dates, and URLs.
    """

    def validate_email(email):
        """
        Validates if the provided string is a valid email address.

        Parameters:
            email (str): The email address to validate.

        Returns:
            bool: True if valid, False if not.
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'  # Regular expression pattern for validating email
        return bool(re.match(pattern, email))