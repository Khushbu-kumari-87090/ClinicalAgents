import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(PROJECT_ROOT, "prompts")
CASES_DIR = os.path.join(PROJECT_ROOT, "cases")
IMG_BASE_DIR = os.path.join(PROJECT_ROOT, "datasets", "MedImg")
DEFAULT_DATASET_PATH = os.path.join(PROJECT_ROOT, "datasets", "filtered_data_test_set.json")
EXPERIENCE_GUIDE_PATH = os.path.join(PROJECT_ROOT, "experience_guide.json")
EXPERIENCE_CDC_PATH = os.path.join(PROJECT_ROOT, "experience_cdc.json")

# LLM Configs
LLM_CONFIG = {"model": "gpt-4o-mini", "api_key": "dummy", "base_url": "https://api.openai.com/v1"}
JUDGE_CONFIG = {"model": "gpt-4o-mini", "api_key": "dummy", "base_url": "https://api.openai.com/v1"}
MCTS_PLANNING_CONFIG = {"model": "gpt-4o-mini", "api_key": "dummy", "base_url": "https://api.openai.com/v1"}
MCTS_ROLLOUT_CONFIG = {"model": "gpt-4o-mini-rollout", "api_key": "dummy", "base_url": "https://api.openai.com/v1"}

LLM_MAX_TOKENS = 1000
LLM_TEMPERATURE = 0.7
JUDGE_MAX_TOKENS = 1000
API_TIMEOUT = 60

# MCTS Configs
MCTS_ALPHA = 0.5
MCTS_BETA = 0.5
MCTS_D = 5
MCTS_DELTA_MAX = 0.5
MCTS_ETA = 2
MCTS_GAMMA = 0.1
MCTS_GAMMA_D = 0.99
MCTS_K = 2
MCTS_LAMBDA_PUCT = 1.0
MCTS_N_SIM = 2
MCTS_ROLLOUT_CALL_CAP_PER_SEARCH = 0
MCTS_ROLLOUT_CALL_CAP_TOTAL = 0
MCTS_WARM_START = True

# Benchmark / Orchestrator Mode
DEBUG = True
BATCH_SIZE = 32
BENCHMARK_MAX_SAMPLES = None
BENCHMARK_SAMPLE_POSITION = "head"
BENCHMARK_SEED = 42
MAX_RECHECK_PER_CASE = 1
DOCLENS_AGGREGATION = "f1"
FORCE_FINALIZATION = True
