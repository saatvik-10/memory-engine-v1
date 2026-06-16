# Memory Engine V1

Memory Engine V1 is a FastAPI app for storing, listing, fetching, searching, ingesting, and reflecting on memories. It uses SQLAlchemy with PostgreSQL, pgvector embeddings, and a Sentence Transformers model for semantic similarity.

## What is implemented

The app exposes these routes:

- `POST /memory` creates a memory record.
- `GET /memory` returns all stored memories.
- `GET /memory/{id}` returns one memory by UUID.
- `POST /memory/search` runs cosine-similarity search over stored embeddings.
- `POST /memory/check` returns whether a text should be extracted.
- `POST /ingest` runs the ingestion pipeline for a message.
- `POST /reflect` generates reflections from stored memories.

## Storage model

Each stored memory contains:

- id
- memory text
- type
- category
- importance
- confidence
- embedding
- created_at
- updated_at

The public response model does not include the embedding field.

## Ingestion flow

The ingestion pipeline is deterministic and currently works like this:

```text
Message
↓
should_extract
↓
extract_memories
↓
judge_memories
↓
find_similar_memory
↓
reinforce_memory or create memory
```

Current behavior:

- `should_extract` checks for keywords such as learning, interested, working, building, prefer, hate, love, goal, want, plan, exploring, and studying.
- `extract_memories` currently returns the full message as a single lowercase memory candidate.
- `judge_memories` currently passes candidates through unchanged.
- `classify_memory` uses keyword matching and returns one of `learning`, `interest`, `preference`, `goal`, `project`, or `general`.
- `calculate_importance` maps categories to fixed scores.
- `calculate_confidence` maps memory text to fixed scores.
- Similar memories are reinforced when cosine similarity is above `0.85`.
- Reinforcement increases confidence by `0.05` up to `1.0` and updates `updated_at`.

## Search

Search embeds the query with `BAAI/bge-small-en-v1.5`, compares it with all stored memory embeddings using cosine similarity, filters results below `0.5`, sorts by score, and returns the top `k` results.

## Reflection

Reflection is template-based.

- Categories with templates are `learning`, `project`, `preference`, and `interest`.
- A reflection is considered only after at least `3` memories exist in the same category.
- Existing reflections are skipped.
- The current implementation creates at most one reflection per call and returns immediately after creating it.

## Tech stack

- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- pgvector
- Sentence Transformers

## Current limitations

This codebase is a deterministic prototype.

- The extractor is keyword-based.
- The judge is a pass-through.
- The classifier is keyword-based.
- The reflection engine uses fixed templates.
- The project currently stores embeddings for semantic search, but it does not use an LLM-based memory pipeline.

## Example memory

```json
{
  "id": "uuid",
  "memory": "user is learning solana",
  "type": "semantic",
  "category": "learning",
  "importance": 0.85,
  "confidence": 0.9,
  "created_at": "2025-01-01T12:00:00",
  "updated_at": "2025-01-10T14:00:00"
}
```
