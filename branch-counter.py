#!/usr/bin/env -S uv run python

import subprocess
import sys

def count_branches():
    try:
        # Get all local branches
        result = subprocess.run(['git', 'branch'], capture_output=True, text=True, check=True)
        branches = [line.strip().lstrip('* ') for line in result.stdout.strip().split('\n') if line.strip()]
        
        print(f"Found {len(branches)} local branches:")
        for branch in branches:
            print(f"  - {branch}")
            
        return len(branches)
    except subprocess.CalledProcessError:
        print("Error: Not in a git repository or git not found")
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    count = count_branches()
    sys.exit(0)
