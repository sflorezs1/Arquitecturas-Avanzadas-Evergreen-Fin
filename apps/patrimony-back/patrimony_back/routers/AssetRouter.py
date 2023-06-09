from libs.TortoiseCRUDRouter import TortoiseCRUDRouter
from patrimony_back.models import AssetType
from patrimony_back.models.Asset import Asset, Asset_Pydantic, AssetIn_Pydantic

AssetRouter = TortoiseCRUDRouter(
    schema=Asset_Pydantic,
    create_schema=AssetIn_Pydantic,
    db_model=Asset,
    prefix='assets'
)
