from db_config import Message

name_list = []
for msg in Message.select():
    name_list.append(msg.Name)

print(name_list)


