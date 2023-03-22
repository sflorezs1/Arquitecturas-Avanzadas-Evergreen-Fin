from fastapi_crudrouter import TortoiseCRUDRouter
from patrimony_back.models.Asset import Asset, Asset_Pydantic, AssetIn_Pydantic


print(Asset_Pydantic.schema_json(indent=2))

AssetRouter = TortoiseCRUDRouter(
    schema=Asset_Pydantic,
    create_schema=AssetIn_Pydantic,
    db_model=Asset,
    prefix='assets'
)