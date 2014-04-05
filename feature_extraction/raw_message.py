__author__ = 'green'

class RawMessage(object):
    """
    Stub class for raw messages, probably they will be Skype messages
    """

    FromDisplayName = None
    Body = None



phrases_dict = {'bart':
        ["I Didn't Do It!",
         "I'm Bart Simpson, Who the Hell are You?"],

           'homer':
               ["Oh, my God!",
                "Holy Moly!",
                "Stupid Flanders",
                "BART!"],

           'marge':
           ["Bart, my special little guy."],

           'lisa':
           ["If anyone wants me, I'll be in my room.",
            "Quit it, Bart!",
            "Fantastic!"]
}

messages = []

for name, phrases in phrases_dict.items():
    for phrase in phrases:
        message = RawMessage()
        message.FromDisplayName = name
        message.Body = phrase
        messages.append(message)