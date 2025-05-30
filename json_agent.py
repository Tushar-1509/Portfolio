
from jsonschema import validate, ValidationError

target_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "amount": {"type": "number"},
        "date": {"type": "string", "format": "date"}
    },
    "required": ["name", "amount", "date"]
}

def json_agent(data):
    try:
        validate(data, target_schema)
        return {"status": "ok", "data": data}
    except ValidationError as e:
        return {"status": "error", "message": str(e)}
