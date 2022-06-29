"""
===== Welcome to CRM Application =====
[S]how: Show all users info
[A]dd: Add new user
[Q]uit: Quit The Application
[F]ind: Find a user
[D]elete: Delete a user
[E]dit: Edit a user
======================================
"""

from db_config import Message

# ユーザー一覧表示
def user_display():
    for msg in Message.select():
        print(f"Name: {msg.Name} Age: {msg.Age}")


# 新規ユーザー追加
def add_user():
    name = input("New user name >")
    age = int(input("New user age >"))

    # ユーザ重複していないか確認
    check_result = dup_search(name)
    if check_result == True:
        Message.create(Name=name, Age=age)

        print(f"Add new user: {name}")

        return name


# 終了する
def quit_application():

    print("Bye!")


# 重複確認
def dup_search(name):
    name_list = []

    for msg in Message.select():
        name_list.append(msg.Name)

    # 重複があるかflagを立てて確認（ループ後０のままであれば重複なし）
    flag = 0
    for r in name_list:

        if r == name:
            flag += 1

    if flag == 0:
        return True

    else:
        print(f"Duplicated user name {name}")
        return False


# ユーザー検索機能
def find_user():
    name = input("User name >")

    flag = 0
    for msg in Message.select():

        if msg.Name == name:
            print(f"Name: {msg.Name} Age: {msg.Age}")
            flag += 1

    if flag == 0:
        print(f"Sorry, {name} is not found")


# ユーザー削除機能
def delete_user():
    name = input("User name >")

    # ユーザが登録されているか確認
    dup_check = dup_search(name)

    if dup_check == False:
        msg = Message.select().where(Message.Name == name).get()
        msg.delete_instance()

        print(f"User {name} is deleted")

    else:
        print(f"Sorry, {name} is not found")


# ユーザー編集機能を追加
def edit_user():
    name = input("User name >")

    msg = Message.select().where(Message.Name == name).get()
    msg.user = "Tom Ford"
    msg.save()


def main():

    print(open("input_info.txt").read())

    # この書き方が微妙にうまくいかない。なぜ？
    # print(
    #     "===== Welcome to CRM Application =====\n",
    #     "[S]how: Show all users info\n[A]dd: Add new user\n[Q]uit: Quit The Application\n",
    #     "[F]ind: Find a user\n[D]elete: Delete a user\n[U]pdate: Update a user\n",
    #     "======================================",
    # )

    category = input("Your command > ")

    if category == "S":
        user_display()

    elif category == "A":
        add_user()

    elif category == "Q":
        quit_application()

    elif category == "F":
        find_user()

    elif category == "D":
        delete_user()

    elif category == "E":
        edit_user()

    else:
        print(f"{category}: command not found")


if __name__ == "__main__":
    main()
