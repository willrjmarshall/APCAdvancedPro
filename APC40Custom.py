import Live
from APC40.APC40 import *

# Will's custom shit
from VUMeters import VUMeters
from RepeatComponent import RepeatComponent
from LooperComponent import LooperComponent

class APC40Custom(APC40):
  def __init__(self, c_instance):
    APC40.__init__(self, c_instance)
    self._custom_initializers()

  def _custom_initializers(self):
      self._setup_repeats()
      self._setup_button_rows()
      # VU Meters
      self.stop_buttons = [ ButtonElement(True, MIDI_NOTE_TYPE, index, 52) for index in range(8) ]
      vu = VUMeters(self)

      #self._setup_looper()


  def _setup_button_rows(self):
    self._button_rows = []
    for scene_index in range(5):
      scene = self._session.scene(scene_index)
      button_row = []
      for track_index in range(8):
        button = ButtonElement(True, MIDI_NOTE_TYPE, track_index, (scene_index + 53))
        button_row.append(button)
        clip_slot = scene.clip_slot(track_index)
        clip_slot.set_triggered_to_play_value(2)
        clip_slot.set_triggered_to_record_value(4)
        clip_slot.set_stopped_value(3)
      self._button_rows.append(button_row)

  def _setup_looper(self):
    looper = LooperComponent(self)
    is_momentary = True
    #pedal = ButtonElement(is_momentary, MIDI_CC_TYPE, 0, 67)
    loop_on = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 0, 99)
    loop_start = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 5, 50)
    double = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 0, 100)
    halve = ButtonElement(is_momentary, MIDI_NOTE_TYPE, 0, 101)
    looper = LooperComponent(self)
    looper.set_shift_button(self._shift_button)
    looper.set_loop_toggle_button(loop_on)
    looper.set_loop_start_button(loop_start)
    looper.set_loop_double_button(double) 
    looper.set_loop_halve_button(halve) 
  
  def _setup_repeats(self):
      self._device_buttons = []
      
      repeat = RepeatComponent(self)
      repeat.set_shift_button(self._shift_button)
