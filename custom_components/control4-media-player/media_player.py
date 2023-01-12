""" Control4-mediaplayer """

from .control4Amp import control4AmpChannel

import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from homeassistant.components.media_player import (
    ENTITY_ID_FORMAT,
    PLATFORM_SCHEMA,
    MediaPlayerEntity
)

from homeassistant.components.media_player.const import (
    SUPPORT_TURN_OFF,
    SUPPORT_TURN_ON,  
    SUPPORT_VOLUME_SET,
    SUPPORT_VOLUME_STEP,
    SUPPORT_VOLUME_MUTE,
    SUPPORT_SELECT_SOURCE
)

from homeassistant.const import (
    ATTR_ENTITY_ID,
    ATTR_FRIENDLY_NAME,
    CONF_NAME,
    STATE_OFF,
    STATE_ON,
)

_LOGGER = logging.getLogger(__name__)

#This sets the name used in configuration.yaml
CONF_ON_VOLUME = "on_volume"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_CHANNEL = "channel"
CONF_SOURCE_LIST = "source_list"

DEFAULT_PORT = 8750
DEFAULT_VOLUME = 5
DEFAULT_SOURCE_LIST = ['1','2','3','4']

SUPPORT_CONTROL4 = (
    SUPPORT_VOLUME_SET \
    | SUPPORT_VOLUME_STEP \
    | SUPPORT_TURN_ON \
    | SUPPORT_TURN_OFF \
    | SUPPORT_SELECT_SOURCE \
    | SUPPORT_VOLUME_MUTE
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_NAME): cv.string,
        vol.Optional(CONF_ON_VOLUME, default=DEFAULT_VOLUME): cv.positive_int,
        vol.Required(CONF_HOST): cv.string,
        vol.Required(CONF_CHANNEL): cv.positive_int,
        vol.Optional(CONF_PORT, default=DEFAULT_PORT): cv.port,
        vol.Optional(CONF_SOURCE_LIST, default=DEFAULT_SOURCE_LIST): cv.ensure_list
    }
)




async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    entity_name = config.get(CONF_NAME)
    on_volume = config.get(CONF_ON_VOLUME)
    host = config.get(CONF_HOST)
    port = config.get(CONF_PORT)
    channel = config.get(CONF_CHANNEL)
    source_list = config.get(CONF_SOURCE_LIST)

    async_add_entities([Control4MediaPlayer(entity_name, on_volume, host, port, channel,source_list)],)

class Control4MediaPlayer(MediaPlayerEntity):
    #Research at https://developers.home-assistant.io/docs/core/entity/media-player/
    #_attr_device_class = 

    def __init__(self, name, on_volume, host, port, channel,source_list):
        #self.hass = hass
        self._domain = __name__.split(".")[-2]
        self._name = name
        self._source = 1
        self._source_list = source_list
        self._on_volume = on_volume / 100
        self._mute_volume = on_volume / 100
        self._state = STATE_OFF
        self._available = True
        self._muted = False
        
        self._ampChannel = control4AmpChannel(host, port, channel)

    async def async_update(self):
        # Not sure if update(self) is required.
        _LOGGER.warn("update...")

    @property
    def should_poll(self):
        return False

    @property
    def icon(self) -> str | None:
        """Return the icon."""
        return "mdi:speaker"
    
    @property
    def is_volume_muted(self):
        return self._muted

    @property
    def name(self):
        """Return the name of the device."""
        return self._name

    @property
    def state(self):
        """Return the state of the device."""
        return self._state

    @property
    def source(self):
        return self._source

    @property
    def source_list(self):
        return self._source_list

    @property
    def volume_level(self):
        """Volume level of the media player (0..1)."""
        return self._ampChannel.volume 

    @property
    def supported_features(self):
        """Flag media player features that are supported."""
        return SUPPORT_CONTROL4

    async def async_mute_volume(self, mute: bool) -> None:
        """Mute (true) or unmute (false) media player."""
        if mute:
            self._muted = True
            self._mute_volume = self._ampChannel.volume
            self._ampChannel.volume  = 0 
            _LOGGER.warn("volume set to  zero to mute")
        else:
            self._muted = False
            self._ampChannel.volume  = self._mute_volume 
            _LOGGER.warn("volume set to pre-mute level")
        self.schedule_update_ha_state()

    async def async_select_source(self,source):
        self._source = source
        self._ampChannel.source = self._source_list.index(source) + 1
        self.schedule_update_ha_state()
        _LOGGER.warn("Source index is " + str(self._source_list.index(source) + 1))
        _LOGGER.warn("Source set to " + str(self._source))

    async def async_turn_on(self):
        _LOGGER.warn("Turning on...")
        self._ampChannel.volume = self._on_volume
        result = self._ampChannel.turn_on()
        self._state = STATE_ON
        self.schedule_update_ha_state()

    async def async_turn_off(self):
        _LOGGER.warn("Turning off...")
        self._ampChannel.volume = self._on_volume
        result = self._ampChannel.turn_off()
        self._state = STATE_OFF 
        self.schedule_update_ha_state()

    async def async_volume_up(self):
        self._ampChannel.volume = self._ampChannel.volume + .01
        self.schedule_update_ha_state()
        _LOGGER.warn("volume set to " + str(self._ampChannel.volume))

    async def async_volume_down(self):
        self._ampChannel.volume = self._ampChannel.volume - .01
        self.schedule_update_ha_state()
        _LOGGER.warn("volume set to " + str(self._ampChannel.volume))

    async def async_set_volume_level(self, volume):
        self._ampChannel.volume  = volume 
        self.schedule_update_ha_state()
        _LOGGER.warn("volume set to " + str(self._ampChannel.volume))
