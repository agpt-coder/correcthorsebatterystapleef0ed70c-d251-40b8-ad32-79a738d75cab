import prisma
import prisma.models
from pydantic import BaseModel


class GenerateExplanationResponse(BaseModel):
    """
    Response model that returns the AI-generated narrative explanation for the requested comic.
    """

    explanation: str
    confidence_score: float


async def generate_ai_explanation(
    comic_id: str, comic_url: str, comic_title: str
) -> GenerateExplanationResponse:
    """
    Generates an explanation for a given XKCD comic image.

    This function simulates calling an AI to generate a narrative explanation for a given comic,
    then stores this explanation alongside the comic details in a database. For the sake of this
    example, a fixed explanation is created, along with a mock confidence score.

    Args:
        comic_id (str): Unique identifier of the XKCD comic for which an explanation is requested.
        comic_url (str): The URL to the comic image.
        comic_title (str): The title of the comic, providing contextual information for generating the explanation.

    Returns:
        GenerateExplanationResponse: Response model that returns the AI-generated narrative explanation for the requested comic.

    Example:
        generate_ai_explanation("some-comic-id", "https://example.com/some-comic.png", "A Funny prisma.models.Comic")
        > GenerateExplanationResponse(explanation="A detailed AI-generated explanation about 'A Funny prisma.models.Comic'", confidence_score=0.95)
    """
    mock_explanation = f"AI-generated explanation for '{comic_title}'"
    mock_confidence_score = 0.95
    existing_explanation = await prisma.models.AIExplanation.prisma().find_unique(
        where={"comicId": comic_id}
    )
    if not existing_explanation:
        await prisma.models.AIExplanation.prisma().create(
            data={"explanation": mock_explanation, "comicId": comic_id}
        )
    return GenerateExplanationResponse(
        explanation=mock_explanation, confidence_score=mock_confidence_score
    )
