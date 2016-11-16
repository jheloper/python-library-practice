import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('hamegg.com', 22, 'your_user', key_filename='/home/your_user/.ssh/id_rsa')
sftp = ssh.open_sftp()

sftp.put('local_file', 'remote_file')

sftp.chmod('remote_file', 0o0755)

sftp.get('remote_file', 'local_file')

sftp.close()
ssh.close()
