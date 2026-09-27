import json
import ollama
from models import EmployeeInfo


def extract_information(text):

    prompt = f"""
Extract employee information from the following text.

Text:
{text}

Extract these fields:
- name
- company
- role
- location
- joining_date

If a field is not available, return "Not Available".

Return only valid JSON.
"""

    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    raw_output = response["message"]["content"]

    data = json.loads(raw_output)

    validated_data = EmployeeInfo(**data)

    return validated_data