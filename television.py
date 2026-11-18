class Television:

    '''Represents a tv channel'''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''Initializes tv values'''
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self):
        '''Turn tv on or off'''
        self.__status = not self.__status

    # Mute
    def mute(self):
        '''Mute or unmute tv when it's on'''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''Increase the tv channel'''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        '''Decrease the tv channel'''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        '''Increase the tv volume'''
        if self.__status:

            if self.__muted:
                self.__muted = False

                if self.__volume < Television.MAX_VOLUME:
                    self.__volume += 1

            elif self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''Decrease the tv volume'''
        if self.__status:

            if self.__muted:
                self.__muted = False

                if self.__volume > Television.MIN_VOLUME:
                    self.__volume -= 1

            elif self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        '''Return tv details'''
        volume = 0 if self.__muted else self.__volume
        return (
            f'Power = {self.__status}, '
            f'Channel = {self.__channel}, '
            f'Volume = {volume}'
        )
