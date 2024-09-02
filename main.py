import subprocess
​
def run_one_api():
# 设置工作目录
working_directory = "/var/task/app"
# 设置要运行的命令，修改日志目录为 /tmp
command = "./one-api --port 8080 --log-dir /tmp"
​
try:
# 使用 subprocess.run 执行命令并指定工作目录
result = subprocess.run(command, cwd=working_directory, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("Output:", result.stdout)
except subprocess.CalledProcessError as e:
print(f"Command failed with error: {e.stderr}")
​
if __name__ == "__main__":
run_one_api()
