from bson import ObjectId
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, val):
        if not ObjectId.is_valid(val):
            raise ValueError("Invalid ObjectId")
        return ObjectId(val)

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        schema: JsonSchemaValue,
        handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        return {"type": "string"}