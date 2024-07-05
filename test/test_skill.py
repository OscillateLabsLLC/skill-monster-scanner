# pylint: disable=missing-docstring,missing-module-docstring,redefined-outer-name,unused-argument
import shutil
from os import environ, getenv, makedirs
from os.path import dirname, join
from unittest.mock import Mock, call

import pytest
from genericpath import isdir
from ovos_config.locale import setup_locale
from ovos_plugin_manager.skills import find_skill_plugins
from ovos_utils.fakebus import FakeBus

from skill_monster_scanner import MonsterScannerSkill


@pytest.fixture(scope="session")
def test_skill(test_skill_id="skill-monster-scanner.mikejgray", bus=FakeBus()):
    # Get test skill
    bus.emitter = bus.ee
    bus.run_forever()
    skill_entrypoint = getenv("TEST_SKILL_ENTRYPOINT")
    if not skill_entrypoint:
        skill_entrypoints = list(find_skill_plugins().keys())
        assert test_skill_id in skill_entrypoints
        skill_entrypoint = test_skill_id

    skill = MonsterScannerSkill(skill_id=test_skill_id, bus=bus)
    skill.speak = Mock()
    skill.speak_dialog = Mock()
    skill.play_audio = Mock()
    yield skill
    shutil.rmtree(join(dirname(__file__), "skill_fs"), ignore_errors=False)


@pytest.fixture(scope="function")
def reset_skill_mocks(test_skill):
    # Reset mocks before each test
    test_skill.speak.reset_mock()
    test_skill.speak_dialog.reset_mock()
    test_skill.play_audio.reset_mock()


class TestMonsterScannerSkill():
    test_fs = join(dirname(__file__), "skill_fs")
    data_dir = join(test_fs, "data")
    conf_dir = join(test_fs, "config")
    environ["XDG_DATA_HOME"] = data_dir
    environ["XDG_CONFIG_HOME"] = conf_dir
    if not isdir(test_fs):
        makedirs(data_dir)
        makedirs(conf_dir)
    setup_locale()

    @pytest.mark.parametrize("execution_number", range(100))
    def test_default_no_monsters(self, test_skill, execution_number):
        test_skill.handle_monster_under_bed_intent(Mock())
        assert test_skill.scary is False
        test_skill.speak_dialog.assert_called_with("no_monsters")
        assert call("monsters") not in test_skill.speak_dialog.call_args_list

    def test_sometimes_monsters(self, test_skill):
        test_skill.settings["scary"] = True
        assert test_skill.scary is True
        for _ in range(100):
            test_skill.handle_monster_under_bed_intent(Mock())
        assert call("no_monsters") in test_skill.speak_dialog.call_args_list
        assert call("monsters") in test_skill.speak_dialog.call_args_list

    def test_string_settings_true(self, test_skill):
        test_skill.settings["scary"] = "true"
        assert test_skill.scary is True

    def test_string_settings_false(self, test_skill):
        test_skill.settings["scary"] = "false"
        assert test_skill.scary is False

    def test_string_settings_invalid(self, test_skill):
        test_skill.settings["scary"] = "invalid"
        assert test_skill.scary is False
