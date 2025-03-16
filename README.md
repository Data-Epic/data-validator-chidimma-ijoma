# Data Validator Package  
This Python package offers a straightforward solution for validating personal data such as emails, phone numbers, dates, and URLs. It leverages regular expressions and date parsing to ensure data accuracy, making it easy to incorporate into your projects.  

---

## 🚀 Key Features  
- **Email Validation:** Ensures email addresses follow the standard format.  
- **Phone Number Validation:** Supports validation for both local and international phone numbers.  
- **Date Validation:** Checks dates against common format, `DD/MM/YYYY`, and validates actual calendar dates.  
- **URL Validation:** Verifies that URLs are correctly structured.  
--- 


## ⚙️ Installation  
Clone the repository and navigate to the project directory:  

```bash
git clone https://github.com/Data-Epic/data-validator-chidimma-ijoma.git
cd Data_Validator_Package
```
--- 

## 🛠️ Usage Example
Here's how to use the Data Validator package:
```python
from data_validator.validator import DataValidator

# Create a DataValidator instance
validator = DataValidator()

# Validate values
validator.validate_email("nevusijoma@gmail.com")
validator.validat_phone("+2348012345678")
validator.validate_date("12-03-2025")
validator.validate_url("https://example.com")
```
--- 

## 📄 License
This project is licensed under the MIT License.


## 📬 Contact
For questions, suggestions, or feedback, please open an issue or reach out via nevusijoma@gmail.com.