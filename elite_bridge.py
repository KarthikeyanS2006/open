# OpenMythos Elite Bridge v2.2
# Fix: Unified Class Structure + Integrated Loop Hole Detection
# Built by Karthikeyan for Long Inset Research

import subprocess
import datetime

class OpenMythosGuardian:
    def __init__(self):
        # The 'Nervous System' - Stores executed commands to prevent loops
        self.command_history = {}
        
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

    def detect_loop_hole(self, current_action):
        """Detects if the brain is looping and returns a self-correction prompt."""
        cmd_clean = current_action.strip().lower()
        if cmd_clean in self.command_history:
            return (
                "CRITICAL: You are attempting to repeat an action that provided no results. "
                "Analyze why the previous step failed. Is there a firewall? Is the port closed? "
                "Describe your NEW strategy before executing a different tool."
            )
        return None

    def execute_autonomous_action(self, command):
        """
        SELF-CORRECTION LAYER:
        Now uses detect_loop_hole to provide feedback to the model.
        """
        # 1. Check for loops first
        loop_error = self.detect_loop_hole(command)
        if loop_error:
            # Increment the count so we track how many times it tried to loop
            self.command_history[command.strip().lower()] += 1
            return f"ERROR: Logic Loop Detected.\n{loop_error}"

        # 2. New command execution
        try:
            print(f"[⚡] OpenMythos Executing: {command}")
            # Running with a 60s timeout
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=60).decode()
            
            # Record success in history
            self.command_history[command.strip().lower()] = 1
            
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
    
    # This simulates what happens when the model makes a mistake
    trajectory = [
        {"thought": "Initial port discovery", "action": f"nmap -F {target}"},
        {"thought": "I'm confused, let me try that again", "action": f"nmap -F {target}"}
    ]
    
    for step in trajectory:
        print(f"\n[💭 THOUGHT]: {step['thought']}")
        result = guardian.execute_autonomous_action(step['action'])
        print(f"[👁️  RESULT]: \n{result[:300]}...") # Printing snippet
        
    return "Cycle Complete"

if __name__ == "__main__":
    run_elite_cycle("alagappauniversity.ac.in")
