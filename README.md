# Rangmanch Reviews API

A FastAPI service for creating and managing theatre reviews for Pune Rangmanch.

## Setup

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Endpoints

| Method   | Path                           | Description                                      |
| -------- | ------------------------------ | ------------------------------------------------ |
| `POST`   | `/reviews/`                    | Create a review                                  |
| `GET`    | `/reviews/`                    | List reviews, optionally filtered by `play_name` |
| `GET`    | `/reviews/{review_id}`         | Get a review by ID                               |
| `PATCH`  | `/reviews/{review_id}`         | Update a review                                  |
| `DELETE` | `/reviews/{review_id}`         | Delete a review                                  |
| `GET`    | `/reviews/average/{play_name}` | Get average rating and review count for a play   |

Example average-rating request:

```text
GET /reviews/average/chaicode
```

Example response:

```json
{
  "play_name": "chaicode",
  "average_rating": 3.67,
  "total_reviews": 3
}
```

## Review fields

- `play_name`: Name of the play
- `reviewer_name`: Name of the reviewer
- `rating`: Integer from 2 to 5
- `comment`: Review text
