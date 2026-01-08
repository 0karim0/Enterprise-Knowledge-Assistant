
# =========================
# Paths
# =========================
STAGING_DIR = "data/staging"          # Output of Part 1
FAILED_DIR = "data/failed_docs"       # Docs that fail chunking or embedding

# =========================
# Chunking Configuration
# =========================

# Semantic (flat) chunking
SEMANTIC_CHUNK_SIZE = 800
SEMANTIC_CHUNK_OVERLAP = 150

# Hierarchical chunking
PARENT_CHUNK_SIZE = 2000
PARENT_CHUNK_OVERLAP = 200

CHILD_CHUNK_SIZE = 400
CHILD_CHUNK_OVERLAP = 100

# Chunking strategy
CHUNKING_STRATEGY = "hierarchical"   # "semantic" | "hierarchical"

# =========================
# Embedding Configuration
# =========================

EMBEDDING_PROVIDER = "openai"         # openai | huggingface | local
EMBEDDING_MODEL_NAME = "text-embedding-3-large"
EMBEDDING_VERSION = "v1.0"

# Batch size for embedding generation
EMBEDDING_BATCH_SIZE = 64

# =========================
# Weaviate Configuration
# =========================

WEAVIATE_URL = "http://localhost:8080"
WEAVIATE_INDEX_NAME = "EnterpriseDoc"
WEAVIATE_TIMEOUT = 30

# Enable hybrid search later (Part 3)
ENABLE_HYBRID_SEARCH = True

# =========================
# Metadata Controls
# =========================

# Metadata fields that must exist on every chunk
REQUIRED_METADATA_FIELDS = [
    "file_name",
    "created_time",
    "chunk_type"
]

# Optional metadata fields
OPTIONAL_METADATA_FIELDS = [
    "department",
    "parent_id",
    "confidentiality"
]

# =========================
# Safety & Validation
# =========================

# Minimum chunk length (characters)
MIN_CHUNK_LENGTH = 50

# Drop chunks that are mostly noise
MAX_SPECIAL_CHAR_RATIO = 0.4

# =========================
# Logging
# =========================

LOG_LEVEL = "INFO"
LOG_FILE = "logs/semantic_chunking.log"
