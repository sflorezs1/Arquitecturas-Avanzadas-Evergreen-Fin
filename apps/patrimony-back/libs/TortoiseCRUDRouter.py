from typing import Any
from fastapi_crudrouter import TortoiseCRUDRouter as OLD_TortoiseCRUDRouter
from fastapi_crudrouter.core.tortoise import CALLABLE, Model, NOT_FOUND

class TortoiseCRUDRouter(OLD_TortoiseCRUDRouter):
    def _get_one(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(item_id: Any) -> Model:
            model = await self.db_model.filter(id=item_id).first()

            if model:
                return model
            else:
                raise NOT_FOUND

        return route
    
    def _update(self, *args: Any, **kwargs: Any) -> CALLABLE:
        async def route(
            item_id: Any, model: self.update_schema  # type: ignore
        ) -> Model:
            await self.db_model.filter(id=item_id).update(
                **model.dict(exclude_unset=True)
            )
            return await self._get_one()(item_id)

        return route
    
