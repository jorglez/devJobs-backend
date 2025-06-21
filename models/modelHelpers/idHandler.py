from bson import ObjectId
from pydantic_core import core_schema
from pydantic import GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(cls.validate)

    @classmethod
    def validate(cls, val) -> ObjectId:
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