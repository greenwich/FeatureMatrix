__author__ = 'green'

import raw_message
from messages import Messages
from feature_matrix import MessagesFeatureMatrixBuilder

msg = Messages()
msg.collect(raw_message.messages)

fm = MessagesFeatureMatrixBuilder()
fm.count_words(msg)
print(fm._message_owners)
print(fm.get_matrix())

