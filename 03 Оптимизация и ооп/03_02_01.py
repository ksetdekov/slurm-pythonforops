COMPANIES = ["southbridge.ru", "universe.slurm.io"]
# USERS = ["d.krivosheev@slurm.io", "a.egorov@slurm.io", "a.gorina@slurm.io", "d.naumov@notslurm.io",
#          "a.amantaeva@slurm.io", "v.vostrikova@slurm.io"]
USERS = ["d.krivosheev@slurm.io", "a.egorov@slurm.io", "a.gorina@slurm.io", "d.naumov@slurm.io",
         "a.amantaeva@slurm.io", "v.vostrikova@slurm.io"]

if __name__ == '__main__':
    new_emails = []

    for domain in COMPANIES:
        for email in USERS:
            login, old_domain = email.split("@")
            if old_domain != "slurm.io":
                print(f"почта {email} не на корп домене")
                break
            new_emails.append(login + "@" + domain)
        else:
            continue
        break
        # если закончился цикл по естественным причинам
    else:
        print("Все данные были провалидированы")
        print(new_emails)
