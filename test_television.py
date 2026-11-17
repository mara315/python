# Test Branch

from television import Television


def test_init():
    tv = Television()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_power_on():
    tv = Television()

    tv.power()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_power_off():
    tv = Television()

    tv.power()
    tv.power()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_mute_when_on():
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.mute()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_unmute_when_on():
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_mute_when_off():
    tv = Television()

    tv.mute()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_unmute_when_off():
    tv = Television()

    tv.mute()
    tv.mute()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_up_when_off():
    tv = Television()

    tv.channel_up()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_up_when_on():
    tv = Television()

    tv.power()
    tv.channel_up()

    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'


def test_channel_up_wraps():
    tv = Television()

    tv.power()

    for _ in range(4):
        tv.channel_up()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_channel_down_when_off():
    tv = Television()

    tv.channel_down()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_channel_down_wraps():
    tv = Television()

    tv.power()
    tv.channel_down()

    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'


def test_volume_up_when_off():
    tv = Television()

    tv.volume_up()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_volume_up_when_on():
    tv = Television()

    tv.power()
    tv.volume_up()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_up_when_muted():
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'


def test_volume_up_maximum():
    tv = Television()

    tv.power()

    for _ in range(5):
        tv.volume_up()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'


def test_volume_down_when_off():
    tv = Television()

    tv.volume_down()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_volume_down_when_on():
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_down_when_muted():
    tv = Television()

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'


def test_volume_down_minimum():
    tv = Television()

    tv.power()

    for _ in range(5):
        tv.volume_down()

    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'