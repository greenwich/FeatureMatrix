__author__ = 'green'

import raw_message
from messages import Messages
from messages_matrix import MessagesMatrixBuilder

msg = Messages()
msg.collect(raw_message.messages)

fm = MessagesMatrixBuilder()
fm.count_words(msg)
print(fm._message_owners)
print(fm.get_matrix())

