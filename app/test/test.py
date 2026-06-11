from app.services.embedding_service import generate_embedding

print(len(generate_embedding("User likes Solana")))
