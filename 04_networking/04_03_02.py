from sys import stdout
import paramiko


def main():
    key = paramiko.RSAKey.from_private_key_file("~/.ssh/id_rsa")
    with paramiko.SSHClient() as ssh_client:
        ssh_client.load_system_host_keys() # установить политику дефолтную
        # ssh_client.load_system_host_keys(filename="")
        # ssh_client.set_missing_host_key_policy(paramiko.WarningPolicy) # кидает предупреждение
        # ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy) # добавить в список хостов


        ssh_client.connect(hostname="localhost", port=2222,
                           username="service_user", password="q1w2e3")

        # ssh_client.invoke_shell() # это терминал прямо 
        stdin, stdout, stderr = ssh_client.exec_command("ls -la /")
        # print(stdout.read().decode("utf-8"))
        stdin, stdout, stderr = ssh_client.exec_command("echotests")
        # print(stdout.read()) # будет вечно ждать закрытия потока вывода
        print(stdout.readline()) # считать только первую строку. это полезно, когда знаем что json - в одну строку целекоам
        stdin.write("Hello\n")
        print(stdout.readline())
        stdin.write("Hello world\n")
        stdin.flush() # forcefully uncache and write to stdin
        print(stdout.readline())


if __name__ == '__main__':
    main()
