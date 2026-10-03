class ExperienceMemory:
    def __init__(self, guide_path=None, cdc_path=None, held_out_case_ids=None, allow_dataset_fallback=False, guide_retriever=None):
        self.available = False
        
    def freeze(self):
        return self
        
    def retrieve(self, state):
        return {
            "knowledge": [],
            "potential_missing_evidence": [],
            "retrieved_guidelines": [],
            "retrieved_cdc_cases": [],
            "evidence_importance": {},
            "retrieval_backend": "mock"
        }
