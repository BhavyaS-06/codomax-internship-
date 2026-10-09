import json


def create_sample_json():
    data = {
        "language": "Python",
        "category": "Programming Language",
        "uses": ["Data Analysis", "Artificial Intelligence", "Web Development"]
    }

    # Convert the Python dictionary into a formatted JSON string.
    json_text = json.dumps(data, indent=2)

    # Validate that the JSON string can be parsed.
    json.loads(json_text)
    return json_text


if __name__ == "__main__":
    print(create_sample_json())
