__author__ = 'Alexey'


class MessageParsingError(Exception):
    pass


class Message(object):
    """
    Class represents chat message
    >>> a = Message()
    >>> a.get_words()
    Traceback (most recent call last):
    ...
    messages.MessageParsingError: Message text is not set
    >>> a.set_text("I don't know, what is this!")
    >>> a.get_words()
    ["don't", 'know', 'what', 'this']
    """
    def __init__(self):
        self._text = None
        self._author = None

    def set_text(self, text):
        self._text = text

    def set_author(self, author):
        self._author = author

    def get_author(self):
        return self._author

    def get_words(self):
        if self._text is None:
            raise MessageParsingError("Message text is not set")
        return [word.strip("!.,?").lower() for word in self._text.split() if len(word) > 3]


class Messages(object):
    """
    Collection of chat messages, (type: Message)
    >>> from minimock import Mock
    >>> message = Mock('message')
    >>> message.FromDisplayName = 'name'
    >>> message.Body = 'one test text'
    >>> raw_list = [message, message, message]

    >>> m = Messages()
    >>> m.collect(raw_list)
    >>> len(m.get())
    3
    >>> m.get()[0].get_author() == 'name'
    True
    >>> m.get()[0].get_words()
    ['test', 'text']
    """
    _messages = []

    def collect(self, raw_list):
        for raw_message in raw_list:
            m = Message()
            m.set_author(raw_message.FromDisplayName)
            m.set_text(raw_message.Body)
            self._messages.append(m)

    def get(self):
        return self._messages
