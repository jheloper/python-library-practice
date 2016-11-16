import subprocess
from subprocess import Popen, PIPE

result = subprocess.call(['echo', 'Hello World!'])
print(result)

# shell=True 지정 시 셸을 커쳐 명령어가 실행됨.
result2 = subprocess.call(['exit 1'], shell=True)
print(result2)

# check_call : 정상 종료가 아니라면 예외 발생.
# subprocess.check_call(['exit 1'], shell=True)

cmd = 'echo Hello World!'
p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
# 자식 프로세스의 표준 출력을 얻는 방법으로는 communicate() 말고 stdout.read() 등을 지원하나 출력 데이터의 양이 클 경우 데드락이
# 발생할 수 있으므로 communicate()를 사용하는 것이 좋다.
# stdout_data, stderr_data = p.communicate()
# print(stdout_data)

# 자식 프로세스의 출력을 다른 자식 프로세스의 입력으로 전달하는 처리. 앞선 프로세스의 출력을 다음 프로세스의 입력으로 전달하면 됨.
cmd2 = 'tr "[:upper:]" "[:lower:]"'
p2 = Popen(cmd2, shell=True, stdin=p.stdout, stdout=PIPE, stderr=PIPE)
stdout_data2, stderr_data2 = p2.communicate()
print(stdout_data2)
