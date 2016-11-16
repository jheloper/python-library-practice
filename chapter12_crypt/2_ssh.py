import paramiko

# 우분투에서 paramiko 모듈 설치하여 실행. 실행 과정 중에서 libffi-dev, libssl-dev 설치 필요했음.

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('hamegg.com', 22, 'your_user', key_filename='/home/your_user/.ssh/id_rsa')

stdin, stdout, stderr = ssh.exec_command('ls -l /home')

for line in stdout:
    print(line, end="")

ssh.close()
