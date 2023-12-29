unsend_messages = ['Msg 1', 'Msg 2', 'Msg 3']
send_messages   = []

def send_message(msg_list):
    msg_list.reverse()

    while msg_list:
        current_msg = msg_list.pop()
        show_messages([current_msg])
        send_messages.append(current_msg)

def show_messages(msg_list):
    for msg in msg_list:
        print(msg)

show_messages(unsend_messages)

send_message(unsend_messages[:])

print('Initial messages list: \n')
print(unsend_messages)
print('Send messages list: \n')
print(send_messages)
