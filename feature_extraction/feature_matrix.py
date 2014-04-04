__author__ = 'Alexey'

class MessagesFeatureMatrixBuilder(object):
    """
    Class builds Feature Matrix
    >>> from minimock import mock, Mock
    >>> from messages import Message
    >>> message1 = Message()
    >>> message1.set_text("Operator Give me the number for 911")
    >>> message1.set_author("Homer")
    >>> message2 = Message()
    >>> message2.set_text("Operator is a motion short film")
    >>> message2.set_author("Internet")
    >>> messages = [message1, message2]
    >>> mock = Mock('Messages()')
    >>> mock.get = lambda : messages

    >>> f = MessagesFeatureMatrixBuilder()
    >>> f.count_words(mock)
    >>> m = f.get_matrix()

    >>> m1 = m[1]
    >>> m1.sort()
    >>> m1
    ['film', 'give', 'motion', 'number', 'operator', 'short']

    >>> m2 = m[0][1]
    >>> m2.sort()
    >>> m2
    [0, 0, 1, 1, 1, 1]
    """
    def __init__(self):
        self._all_words = {}
        self._message_words = []
        self._message_owners = []

    def count_words(self, messages):
        i = 0
        for message in messages.get():
            self._message_words.append({})
            self._message_owners.append(message.get_author())
            for word in message.get_words():
                self._all_words.setdefault(word, 0)
                self._all_words[word] += 1
                self._message_words[i].setdefault(word,0)
                self._message_words[i][word] += 1
            i += 1
        pass

    def get_matrix(self):
        vector = []
        for word in self._all_words.keys():
            vector.append(word)

        return [[(word in w and w[word] or 0) for word in vector] for w in self._message_words], vector


