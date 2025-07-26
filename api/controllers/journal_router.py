import logging
from typing import AsyncGenerator
from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.responses import JSONResponse
from api.repositories.postgres_repository import PostgresDB
from api.services import EntryService


router = APIRouter()


async def get_entry_service() -> AsyncGenerator[EntryService, None]:

    async with PostgresDB() as db:
        yield EntryService(db)

@router.get("/")
def root():
	return {"message": "API is working"}

@router.post("/entries")
async def create_entry(request: Request, entry: dict, entry_service: EntryService = Depends(get_entry_service)):

    entry_data = {
        k: v for k, v in entry.items()
        if k not in ['id', 'created_at', 'updated_at']
    }
    async with PostgresDB() as db:
        entry_service = EntryService(db)
        try:
            enriched_entry = await entry_service.create_entry(entry_data)
            await entry_service.db.create_entry(enriched_entry)

        except HTTPException as e:

            if e.status_code == 409:
                raise HTTPException(
                    status_code=409, detail="You already have an entry for today."
                )
            raise e
    return JSONResponse(content={"detail": "Entry created successfully"}, status_code=201)


@router.get("/entries")
async def get_all_entries(request: Request):
    async with PostgresDB() as db:
        entry_service = EntryService(db)
        entries = await entry_service.get_entries()
        if not entries:
            raise HTTPException(status_code=404, detail="Entry not found")
    return entries

  
@router.get("/entries/{entry_id}")
async def get_entry(request: Request, entry_id: str):
    async with PostgresDB() as db:
        entry_service = EntryService(db)
        entry = await entry_service.get_entry(entry_id)
        if not entry:
            raise HTTPException(status_code=404, detail="Entry not found")
        return entry


@router.put("/entries/{entry_id}")
async def update_entry(request: Request, entry_id: str, entry_update: dict):
    async with PostgresDB() as db:
        entry_service = EntryService(db)
        result = await entry_service.update_entry(entry_id, entry_update)
    if not result:
        raise HTTPException(status_code=404, detail="Entry not found")
    return result


@router.delete("/entries/{entry_id}")
async def delete_entry(request: Request, entry_id: str):
    del_entry_id = entry_id
    async with PostgresDB() as db:
        entry_service = EntryService(db)
        if not entry_id:
            raise HTTPException(status_code=404, detail="Entry not found")
        await entry_service.delete_entry(entry_id)
        return {"detail": "Entry deleted"}


@router.delete("/entries")
async def delete_all_entries(request: Request):

    async with PostgresDB() as db:
        entry_service = EntryService(db)
        await entry_service.delete_all_entries()

    return {"detail": "All entries deleted"}
