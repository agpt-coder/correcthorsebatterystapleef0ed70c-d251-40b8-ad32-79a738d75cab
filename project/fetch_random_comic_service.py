import httpx
import prisma
import prisma.models
from pydantic import BaseModel


class FetchRandomComicResponse(BaseModel):
    """
    Response model containing the comic information alongside its AI-generated explanation.
    """

    comic_id: str
    comic_number: int
    title: str
    img_url: str
    alt_text: str
    explanation: str
    created_at: str


async def fetch_random_comic() -> FetchRandomComicResponse:
    """
    Fetches a random comic from XKCD and stores it in the database with an AI-generated explanation.

    Args:


    Returns:
    FetchRandomComicResponse: Response model containing the comic information alongside its AI-generated explanation.
    """
    async with httpx.AsyncClient() as client:
        latest_response = await client.get("https://xkcd.com/info.0.json")
        latest_data = latest_response.json()
        max_num = latest_data["num"]
        import random

        random_comic_num = random.randint(1, max_num)
        response = await client.get(f"https://xkcd.com/{random_comic_num}/info.0.json")
        comic_data = response.json()
        explanation = "This is a simulated explanation. An actual AI model would provide insights here."
        comic = await prisma.models.Comic.prisma().create(
            data={
                "comicNumber": comic_data["num"],
                "title": comic_data["title"],
                "imgUrl": comic_data["img"],
                "altText": comic_data["alt"],
                "explanation": explanation,
            }
        )
        response = FetchRandomComicResponse(
            comic_id=comic.id,
            comic_number=comic.comicNumber,
            title=comic.title,
            img_url=comic.imgUrl,
            alt_text=comic.altText,
            explanation=comic.explanation,
            created_at=comic.createdAt.isoformat(),
        )
        return response
