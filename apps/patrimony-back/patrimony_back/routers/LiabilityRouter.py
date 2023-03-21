from fastapi_crudrouter import TortoiseCRUDRouter
from patrimony_back.models.Liability import Liability, Liability_Pydantic, LiabilityIn_Pydantic


LiabilityRouter = TortoiseCRUDRouter(
    schema=Liability_Pydantic,
    create_schema=LiabilityIn_Pydantic,
    db_model=Liability,
    prefix='Liabilitys'
)