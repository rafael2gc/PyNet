def show_messages(messages):
    for message in messages:
        print(message)


def send_messages(list_msgs, sent_msgs):
    while list_msgs:
        x = list_msgs.pop()
        print(f"\n{x}")
        sent_msgs.append(x)
sent_msgs = []
msg = ['O rato roeu a roupa do rei de roma', 'nao sabe beber, bebe leite', 'em caminho de paca, tatu caminha dentro']
print("\nEnvio individual de cada mensagem")
send_messages(msg[:], sent_msgs)

print("\nLista de mensagens enviadas")
show_messages(sent_msgs)



print("\nLista ORIGINAL")
for y in msg:
    print(y)
