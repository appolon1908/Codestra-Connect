import subprocess,sys
raise SystemExit(subprocess.run([sys.executable,"-m","unittest","discover","-s","tests/unit","-p","test_*.py","-v"]).returncode)
