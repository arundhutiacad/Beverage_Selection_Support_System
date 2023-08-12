import subprocess

def run_commands():
    uvicorn_cmd = "uvicorn app:app --reload"
    uvicorn_process = subprocess.Popen(uvicorn_cmd, shell=True)
    uvicorn_process.wait()  # Wait for uvicorn to finish before proceeding

    npm_cmd = "npm start"
    dir_ch = "cd /Users/raj/Code/starbucks/client/src"
    dir_process = subprocess.Popen(dir_ch, shell=True)
    dir_process.wait()  # Wait for directory change to finish

    npm_process = subprocess.Popen(npm_cmd, shell=True)
    npm_process.wait()  # Wait for npm start to finish

if __name__ == "__main__":
    run_commands()
