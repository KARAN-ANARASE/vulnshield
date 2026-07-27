import subprocess
import os

class SystemService:
    def check_host(self, host):
        # SAST: Command Injection
        command = f"ping -c 1 {host}"
        return subprocess.check_output(command, shell=True).decode()

    def run_calculation(self, formula):
        # SAST: Dangerous use of eval()
        return eval(formula)

    def read_config(self, config_path):
        # SAST: Path Traversal / Unsafe File Operations
        with open(config_path, 'r') as f:
            return f.read()
            
    def insecure_deserialization(self, data):
        # SAST: Insecure Deserialization (Pickle)
        import pickle
        return pickle.loads(data)
