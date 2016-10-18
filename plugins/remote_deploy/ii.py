import paramiko

result = ""

try:
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect("192.168.101.237", 22, "barry", "123456", timeout=3)

    # stdin, stdout, stderr = ssh.exec_command("ls")
    # result = stdout.read()

    # stdin, stdout, stderr = ssh.exec_command("echo 123456 | sudo -S ls")
    # print stdout.read()

    # stdin, stdout, stderr = ssh.exec_command("")
    # print stdout.read()

    # stdin, stdout, stderr = ssh.exec_command("echo 123456 | sudo -S ls")
    # print stdout.read()

    stdin, stdout, stderr = ssh.exec_command(
        '''
        pwd;
        sudo ls
        sudo ll
        ls /;
        rm -rf fabric;
        rm -rf fabricd;
        rm -rf tests;
        ls

        pwd
        sudo touch kkkk
        ll | grep kkkk
        '''
    )
    print stdout.read()
    print stderr.read()

    ssh.close()

except:

    print("ssh_cmd err.")

print  result
