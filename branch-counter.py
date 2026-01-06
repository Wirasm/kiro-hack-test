#!/usr/bin/env -S uv run python

import argparse
import subprocess
import sys

def count_branches(quiet: bool = False) -> int:
    """
    Count and display all local git branches in the current repository.
    
    Args:
        quiet: If True, only output the count without branch names
    
    Returns:
        int: Number of local branches found, or 0 if error occurs
    """
    try:
        # Execute git branch command to get all local branches
        result = subprocess.run(['git', 'branch'], capture_output=True, text=True, check=True)
        
        # Parse branch names, removing asterisk and whitespace from current branch
        branches = [line.strip().lstrip('* ') for line in result.stdout.splitlines() if line.strip()]
        
        # Handle empty repository case explicitly
        if not branches:
            if not quiet:
                print("No branches found (empty repository)")
            return 0
        
        if quiet:
            print(len(branches))
        else:
            print(f"Found {len(branches)} local branches:")
            for branch in branches:
                print(f"  - {branch}")
            
        return len(branches)
    except subprocess.CalledProcessError:
        if not quiet:
            print("Error: Not in a git repository or git not found")
        return 0
    except Exception as e:
        if not quiet:
            print(f"Error: {e}")
        return 0

def main() -> None:
    """Main entry point with argument parsing for CLI extensibility."""
    parser = argparse.ArgumentParser(description='Count local git branches')
    parser.add_argument('--quiet', '-q', action='store_true', 
                       help='Only output the count, no branch names')
    
    args = parser.parse_args()
    
    count_branches(quiet=args.quiet)
    sys.exit(0)

if __name__ == "__main__":
    main()
