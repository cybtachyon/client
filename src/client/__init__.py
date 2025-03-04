# Initialize logging system
import logging

from config import Settings
from .player import Player

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)

# Initialize all important globals
LOBBY_HOST = Settings.get('lobby/host')
LOBBY_PORT = Settings.get('lobby/port')
LOCAL_REPLAY_PORT = Settings.get('lobby/relay/port')

class ClientState:
    '''
    Various states the client can be in.
    '''
    SHUTDOWN  = -666  #Going... DOWN!
    DROPPED   = -2 # Connection lost
    REJECTED  = -1
    NONE      = 0
    ACCEPTED  = 1
    CREATED   = 2
    OUTDATED  = 9000
    UPTODATE  = 9001 #It's over nine thousaaand!

from _clientwindow import ClientWindow as Client

instance = Client()
