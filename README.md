---
date: 2024-04-12T18:03:11.820385
author: AutoGPT <info@agpt.co>
---

# correcthorsebatterystaple

To create a tool that returns a random XKCD comic every time it is called and uses GPT-4 Vision to explain the comic, we can follow these steps leveraging the selected tech stack (Python, FastAPI, PostgreSQL, and Prisma). First, we'll need to fetch a random comic from XKCD using Python. Given the lack of a direct API for random comics, we generate a random comic number based on the current total number of XKCD comics and fetch it via 'https://xkcd.com/{random_number}/info.0.json'. Since my last update doesn't include an actual 'GPT-4 Vision API', we'd simulate this part by outlining how we might integrate such a feature if it were available, focusing on sending the image to the API and processing its description in a human-understandable format. The FastAPI framework will serve as the backbone of our application, handling HTTP requests and responses. We will define an endpoint such as '/random-xkcd' which, upon being called, executes our comic fetching logic. After obtaining the comic, assuming the existence of a 'GPT-4 Vision API', we would send the comic's image for analysis and extract a description. This description, along with the comic's image and title, will then be presented to the user. For persistence, such as tracking which comics have been fetched or storing generated descriptions, we'd leverage PostgreSQL with Prisma as the ORM for structured data handling and efficient database interactions. However, it's important to note that as of my last update, a 'GPT-4 Vision API' by OpenAI or a similar entity was not available for public use. Thus, the explanation part would have to wait until such a technology becomes accessible, or we'd leverage other existing vision APIs with capabilities to analyze and describe images.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'correcthorsebatterystaple'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
