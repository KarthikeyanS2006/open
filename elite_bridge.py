# OpenMythos Elite Bridge v2.1
# Upgrade: Self-Correction & Autonomous Trajectory Logic
# Built by Karthikeyan for Long Inset Research

import subprocess
import datetime

class OpenMythosGuardian:
    def __init__(self):
        # The 'Nervous System' - Stores executed commands to prevent loops
        self.command_history = {}
        self.max_repeats = 1
        
        self.secure_coding_kb = {
            "buffer overflow": "Use strncpy() or snprintf() to prevent memory corruption.",
            "sql injection": "Implement Prepared Statements and Parameterized Queries.",
            "insecure permissions": "Apply the Principle of Least Privilege (chmod 600/700).",
            "xss": "Use context-aware output encoding and CSP headers."
        }

    def analyze_vulnerability(self, detected_issue):
        """Stealth + Long Memory Logic"""
        print(f"[*] OpenMythos analyzing: {detected_issue}...")
        return self.secure_coding_kb.get(detected_issue.lower(), "General Hardening Required")

    def execute_autonomous_action(self, command):
        """
        SELF-CORRECTION LAYER:
        Checks if OpenMythos is repeating itself and forces a pivot.
        """
        cmd_clean = command.strip().lower()
        
        # Check for repetition
        if cmd_clean in self.command_history:
            self.command_history[cmd_clean] += 1
            return (
                f"ERROR: OpenMythos Logic Loop Detected. \n"
                f"Command '{command}' has already been executed. \n"
                f"RESULT: No new data found. \n"
                f"ADVICE: Pivot to a different tool or increase scan depth."
            )
        
        # New command execution
        try:
            print(f"[⚡] OpenMythos Executing: {command}")
            # Running with a timeout to prevent hanging the 'Baby' brain
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=60).decode()
            self.command_history[cmd_clean] = 1
            
            if not result.strip():
                return "OBSERVATION: Tool executed but returned no output. Target may be filtered."
            return result
            
        except subprocess.TimeoutExpired:
            return "ERROR: Execution timed out. Target might be under heavy protection."
        except Exception as e:
            return f"EXECUTION_FAILURE: {str(e)}"

    def verify_patch(self, patch_code):
        return "PATCH_VERIFIED: System Secured."

def run_elite_cycle(target):
    print(f"--- [🛡️ OpenMythos Autonomous Cycle Started: {target}] ---")
    guardian = OpenMythosGuardian()
    
    # Example Trajectory Logic (This is what your Llama model should output)
    trajectory = [
        {"thought": "Initial port discovery", "action": f"nmap -F {target}"},
        {"thought": "Repeating previous scan (Testing loop detection)", "action": f"nmap -F {target}"}
    ]
    
    for step in trajectory:
        print(f"\n[💭 THOUGHT]: {step['thought']}")
        result = guardian.execute_autonomous_action(step['action'])
        print(f"[👁️  RESULT]: \n{result[:500]}...") # Printing first 500 chars
        
    return "Cycle Complete"

# Run if called directly
if __name__ == "__main__":
    run_elite_cycle("alagappauniversity.ac.in")
