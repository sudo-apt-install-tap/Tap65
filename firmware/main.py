from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

# ----------------------------
# will change!
# ----------------------------

keyboard.col_pins = (
    "GP0", "GP1", "GP2", "GP3", "GP4",
    "GP5", "GP6", "GP7", "GP8", "GP9",
    "GP10", "GP11", "GP12", "GP13"
)

keyboard.row_pins = (
    "GP14",
    "GP15",
    "GP16",
    "GP17",
    "GP18",
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ----------------------------
# Layers
# ----------------------------

keyboard.keymap = [

# Base Layer
[
KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,

KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,

KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,

KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP,

KC.LCTL, KC.LGUI, KC.LALT,
KC.SPC,
KC.RALT, KC.MO(1), KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,
],

# Function Layer
[
KC.GRV, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL,

KC.TRNS, KC.TRNS, KC.UP, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

KC.TRNS, KC.LEFT, KC.DOWN, KC.RGHT, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,

KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.PGUP,

KC.TRNS, KC.TRNS, KC.TRNS,
KC.TRNS,
KC.TRNS, KC.TRNS, KC.TRNS, KC.HOME, KC.PGDN, KC.END,
]

]

if __name__ == "__main__":
    keyboard.go()
