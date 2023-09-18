class UserKeys:
    def __init__(self, username, publicKey, privateKey):
        self._username = username
        self._publicKey = publicKey
        self._privateKey = privateKey

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def publicKey(self):
        return self._publicKey

    @publicKey.setter
    def publicKey(self, value):
        self._publicKey = value

    @property
    def privateKey(self):
        return self._privateKey

    @privateKey.setter
    def privateKey(self, value):
        self._privateKey = value
