from extractor import extract_information


text = """
Rahul Kumar joined ABC Technologies in July 2026.
"""


result = extract_information(text)

print("Validated Information:")
print(result.model_dump_json(indent=4))