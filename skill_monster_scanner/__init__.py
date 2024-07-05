from random import randint

from ovos_bus_client.message import Message
from ovos_workshop.decorators import intent_handler
from ovos_workshop.intents import IntentBuilder
from ovos_workshop.skills import OVOSSkill

DEFAULT_SETTINGS = {
    "scary": False,
}


class MonsterScannerSkill(OVOSSkill):
    """Monster scanner skill for OpenVoiceOS/Neon.AI. This skill is designed to
    help children who are afraid of monsters under the bed. It can be
    configured to be scary or not scary. If it is not scary, it will
    reassure the child that there are no monsters under the bed. If it
    is scary, it will sometimes tell the child that there are monsters under the
    bed.
    """

    def initialize(self):
        """Initialize the skill. This method is called after the init is superclassed."""
        # merge default settings
        # self.settings is a jsondb, which extends the dict class and adds helpers like merge
        self.settings.merge(DEFAULT_SETTINGS, new_only=True)

    @property
    def scary(self):
        """Dynamically get the scary setting from the skill settings file.
        If you want to be a monster, you can change the scary setting to True.
        Defaults to False - why do you want to scare kids?!?!?!?!?!?!?!
        """
        scary = self.settings.get("scary", False)
        if isinstance(scary, str):
            if scary.lower() == "true":
                return True
            if scary.lower() == "false":
                return False
            self.log.info("Invalid setting for scary: %s, returning False", scary)
            return False
        if isinstance(scary, bool):
            return scary
        self.log.info("Invalid setting for scary: %s, returning False", scary)
        return False

    @intent_handler(
        IntentBuilder("MonsterScannerIntent")
        .require("monsters")
        .require("bed")
        .optionally("under")
        .optionally("search")
    )
    def handle_monster_under_bed_intent(self, message: Message):
        """Handler for the MonsterScannerIntent. This intent is triggered when
        the user asks if there are monsters under the bed."""
        self.log.debug("MonsterScannerIntent triggered with message: %s", message)
        if self.scary is False:
            self.speak_dialog("no_monsters")
        else:
            monsters = randint(0, 1)
            if monsters == 0:
                self.speak_dialog("no_monsters")
            else:
                self.speak_dialog("monsters")
