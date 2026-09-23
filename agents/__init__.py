# Mock agent implementations

class ReferralAgent:
    def run_l1(self, cc, pi, case_id=None):
        return {"dept_l1": "Internal Medicine"}
    def run_l2(self, cc, pi, dept_l1, case_id=None):
        return {"dept_l2": ["Cardiology"]}

class ReferralVerifier:
    pass

class DoctorAgent:
    VALID_PHYSICAL_EXAMS = ["Heart Rate", "Blood Pressure"]
    VALID_AUXILIARY_EXAMS = ["ECG", "Blood Test"]
    
    def run(self, **kwargs):
        return {
            "hypothesis_illness": [{"name": "Hypertension", "confidence": 0.9}],
            "physical_exams": ["Blood Pressure"],
            "auxiliary_exams": ["ECG"]
        }
        
    def get_physical_exam_from_gt(self, gt_physical, predicted_exams):
        return {"Blood Pressure": "120/80"}

class ImagingAgent:
    def __init__(self, img_base_dir):
        self.img_base_dir = img_base_dir
        
    def run(self, **kwargs):
        return {
            "imaging_results": {"ECG": "Normal sinus rhythm"},
            "non_imaging_results": {"Blood Test": "Normal"}
        }

class DiagnosisAgent:
    def run(self, **kwargs):
        return {
            "updated_hypothesis": [{"name": "Hypertension", "confidence": 0.95}],
            "diagnosis_result": ["Hypertension"],
            "missing_evidence": []
        }

class TreatmentAgent:
    def run(self, **kwargs):
        return {
            "treatment_plan": ["Lisinopril 10mg daily"]
        }
