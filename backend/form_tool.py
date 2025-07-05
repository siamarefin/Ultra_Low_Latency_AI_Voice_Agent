from typing import Optional, Dict, Union
import re

class FormTool:
    def __init__(self):
        self.form_open: bool = False
        self.form_data: Dict[str, str] = {
            'name': '',
            'email': ''
        }
    
    def _validate_email(self, email: str) -> bool:
        """Validate email format.
        
        Args:
            email: Email address to validate
            
        Returns:
            bool: True if email is valid, False otherwise
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    def open_form(self) -> Dict[str, str]:
        """Opens the form for filling.
        
        Returns:
            Dict containing status and message
        """
        self.form_open = True
        return {"status": "success", "message": "Form opened successfully"}
    
    def fill_form(self, name: Optional[str] = None, email: Optional[str] = None) -> Dict[str, Union[str, Dict[str, str]]]:
        """Fills form fields with provided data.
        
        Args:
            name: Optional name to fill
            email: Optional email to fill
            
        Returns:
            Dict containing status, message and form data
            
        Raises:
            ValueError: If email format is invalid
        """
        if not self.form_open:
            return {"status": "error", "message": "Please open the form first"}
        
        if name is not None:
            if not name.strip():
                return {"status": "error", "message": "Name cannot be empty"}
            self.form_data['name'] = name.strip()
            
        if email is not None:
            email = email.strip().lower()
            if not email:
                return {"status": "error", "message": "Email cannot be empty"}
            if not self._validate_email(email):
                return {"status": "error", "message": "Invalid email format"}
            self.form_data['email'] = email
            
        return {
            "status": "success",
            "message": "Form updated",
            "data": self.form_data
        }
    
    def get_form_status(self) -> Dict[str, Union[bool, Dict[str, str]]]:
        """Returns current form status and data.
        
        Returns:
            Dict containing form open status and current data
        """
        return {
            "is_open": self.form_open,
            "data": self.form_data
        }