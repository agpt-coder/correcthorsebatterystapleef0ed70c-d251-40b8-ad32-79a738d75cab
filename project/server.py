import logging
from contextlib import asynccontextmanager

import project.fetch_random_comic_service
import project.generate_ai_explanation_service
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import Response
from prisma import Prisma

logger = logging.getLogger(__name__)

db_client = Prisma(auto_register=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_client.connect()
    yield
    await db_client.disconnect()


app = FastAPI(
    title="correcthorsebatterystaple",
    lifespan=lifespan,
    description="To create a tool that returns a random XKCD comic every time it is called and uses GPT-4 Vision to explain the comic, we can follow these steps leveraging the selected tech stack (Python, FastAPI, PostgreSQL, and Prisma). First, we'll need to fetch a random comic from XKCD using Python. Given the lack of a direct API for random comics, we generate a random comic number based on the current total number of XKCD comics and fetch it via 'https://xkcd.com/{random_number}/info.0.json'. Since my last update doesn't include an actual 'GPT-4 Vision API', we'd simulate this part by outlining how we might integrate such a feature if it were available, focusing on sending the image to the API and processing its description in a human-understandable format. The FastAPI framework will serve as the backbone of our application, handling HTTP requests and responses. We will define an endpoint such as '/random-xkcd' which, upon being called, executes our comic fetching logic. After obtaining the comic, assuming the existence of a 'GPT-4 Vision API', we would send the comic's image for analysis and extract a description. This description, along with the comic's image and title, will then be presented to the user. For persistence, such as tracking which comics have been fetched or storing generated descriptions, we'd leverage PostgreSQL with Prisma as the ORM for structured data handling and efficient database interactions. However, it's important to note that as of my last update, a 'GPT-4 Vision API' by OpenAI or a similar entity was not available for public use. Thus, the explanation part would have to wait until such a technology becomes accessible, or we'd leverage other existing vision APIs with capabilities to analyze and describe images.",
)


@app.post(
    "/generate-explanation",
    response_model=project.generate_ai_explanation_service.GenerateExplanationResponse,
)
async def api_post_generate_ai_explanation(
    comic_id: str, comic_url: str, comic_title: str
) -> project.generate_ai_explanation_service.GenerateExplanationResponse | Response:
    """
    Generates an explanation for a given XKCD comic image.
    """
    try:
        res = await project.generate_ai_explanation_service.generate_ai_explanation(
            comic_id, comic_url, comic_title
        )
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )


@app.get(
    "/random-xkcd",
    response_model=project.fetch_random_comic_service.FetchRandomComicResponse,
)
async def api_get_fetch_random_comic() -> project.fetch_random_comic_service.FetchRandomComicResponse | Response:
    """
    Fetches a random comic from XKCD and stores it in the database with an AI-generated explanation.
    """
    try:
        res = await project.fetch_random_comic_service.fetch_random_comic()
        return res
    except Exception as e:
        logger.exception("Error processing request")
        res = dict()
        res["error"] = str(e)
        return Response(
            content=jsonable_encoder(res),
            status_code=500,
            media_type="application/json",
        )
