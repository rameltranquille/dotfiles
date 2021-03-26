import os, subprocess, psutil, time
from datetime import datetime
from suntime import Sun

from typing import List

from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
mod2 = "mod1"
terminal = "alacritty"

fg = "#F7BFC0"
bg = "#0F161E"
bg2 = "#45425C"
alt = "#A29AC3"
alt2 = "#FCDACE"
alt3 = "#FB676E"
black = "#000000"
green = "#00ff00"
red = "#ff0000"

longi = 40.71
lati = -74.00
def solunar(longi, lati):
    sun = Sun(longi, lati)
    today_sr = sun.get_sunrise_time().hour - 5 # subtract 5 for UTC to EST
    today_ss = sun.get_sunset_time().hour - 5
    current_time = time.localtime().tm_hour
    
    sunout = current_time < today_ss and current_time > today_sr

    if sunout:
        wp ="~/.config/qtile/wallpapers/87897.jpg"
    else:
        wp ="~/.config/qtile/wallpapers/skbvzdkr6ni61.jpg"

    return wp


keys = [
    # Free Keys: q, e, t, y
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "g", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Sizing (Q-Y)
    Key([mod], "q", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod], "w", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod], "e", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod], "r", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "t", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "y", lazy.layout.maximize(), desc="Maximize current windows"),

    # Screens (A-F)
    Key([mod], "a", lazy.to_screen(0), desc="Move to first screen"),
    Key([mod], "s", lazy.to_screen(1), desc="Move to second screen"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),

    # Bottom Row: Spawning Apps (Z-M)
    Key([mod], "z", lazy.spawn("spotify"), desc="Open Spotify"),
    Key([mod], "x", lazy.spawn("firefox"), desc="Open Firefox"),
    Key([mod], "c", lazy.spawn("passmenu"), desc="Open Passmenu"),
    Key([mod], "v", lazy.spawn("alacritty -e vim"), desc="Open vim"),
    Key([mod], "b", lazy.spawn("alacritty -e bpytop"), desc="Open htop"),
    Key([mod], "n", lazy.spawn("pavucontrol"), desc="spawn pavucontrol"),
    Key([mod], "m", lazy.spawn("dmenu_run_i"), desc="Run Dmenu_run_i"),
    # I, O, P: Volume
    Key([mod], "i", lazy.spawn('amixer -D pulse sset Master 5%+'),
        desc="Increase volume"),
    Key([mod], "o", lazy.spawn('amixer -D pulse sset Master 5%-'),
        desc="Decrease volume"),
    Key([mod], "p", lazy.spawn('amixer -q set IEC958 toggle'),
        desc="Mute and Unmute volume"),
    # Other
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "space", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

]

g1 = Group(
        "1st",
        layout="Columns",
        spawn=[
            "firefox",
            "alacritty -e vim /home/ramel/schedule.md",
            ]
        )
g2 = Group( "2nd")
g3 = Group( "game", layout='max',)
g4 = Group( "dev", spawn="alacritty -e vim")

groups = [g1, g2, g3, g4]

for index, grp in enumerate(groups):

    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(index+1), lazy.group[grp.name].toscreen(),
            desc="Switch to group {}".format(grp.name)),

        # mod1 + shift + letter of group = switch to
        # & move focused window to group
        Key([mod, "shift"], str(index+1), lazy.window.togroup(grp.name),
            desc="move focused window to group".format(grp.name)),

        Key([mod, "control"], str(index+1), lazy.window.togroup(
            grp.name,
            switch_group=True),
            desc="moved focused window to group and switch to group")
    ])


layouts = [
    layout.Columns(num_columns=3, border_focus=fg, border_width=3,
        margin=5, border_normal=bg),
    layout.Max(),
    # layout.MonadTall(num_columns=2, border_focus=fg, border_width=3,
        # margin=5, border_normal=bg),
    # layout.Bsp(num_columns=2, border_focus=fg, border_width=3,
        # margin=5, border_normal=bg),
]


widget_defaults = dict(
    background=bg,
    foreground=fg,
    font='jetbrains mono light',
    fontsize=10,
    padding=3,
)
extension_defaults = widget_defaults.copy()


class Stats(widget.base.InLoopPollText):

    def __init__(self, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.update_interval = 1

    def get_cpuload(self):
        loadavg = psutil.getloadavg()
        load_percents = [round(x / psutil.cpu_count() * 100.0, 2) for x in loadavg]
        return "LA: {}%".format(load_percents)

    def get_temp(self):
        temp_lst = psutil.sensors_temperatures()
        temp = temp_lst['k10temp']
        current_temp = temp[1].current
        return "{}*C".format(current_temp)

    def get_storage(self):
        st = psutil.disk_usage("/")
        freegb = st.free / 1000000000
        freegb_perc = st.used / st.total * 100
        return "{}GB Free".format(round(freegb))

    def poll(self):
        stat = [self.get_cpuload(), self.get_storage(), self.get_temp(),]
        return " | ".join(stat)


class Todo(widget.base.InLoopPollText):

    def __init__(self, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.update_interval = 1

    def poll(self):
        main_task = os.system("todo | grep -a 1 | sed \'s/\\x1b\\[[0-9;]*m//g\' > /home/ramel/.config/qtile/list.txt")
        fline = open("/home/ramel/.config/qtile/list.txt", "r").readline().rstrip()
        for i in "1234567890":
            fline = fline.lstrip("{} | ".format(i))
        return "task:" + fline


sep = widget.Sep(linewidth=1, size_percent=80)

screens = [
        Screen(
            top=bar.Bar(
                [
                    widget.CurrentLayout(), sep,
                    widget.Prompt(prompt="Run: "),
                    widget.GroupBox(
                        active=fg,
                        inactive=bg,
                        # visible_groups = ["1st", "2nd", "game", "dev"],
                        this_current_screen_border=alt3,
                        other_current_screen_border=alt3),
                    sep,
                    widget.WindowName(),
                    widget.Chord(
                        chords_colors={
                            'launch': (black, green),
                        },
                        name_transform=lambda name: name.upper(),
                    ),
                    widget.Notify(foreground=alt3, foreground_urgent=alt2),
                    # widget.Countdown(format='{H}h:{M}m:{S}s'),
                    widget.Clock(
                        format='%m-%d-%y %a %I:%M %p',
                        foreground=fg),
                    widget.Systray(),
                    widget.CurrentScreen(
                        active_color=alt,
                        inactive_color=alt),
                    ],
                18
                ),
            bottom=bar.Bar(
                [
                    widget.Net(format='{down}↓↑{up}'), sep,
                    widget.CPU(), sep,
                    Stats(), sep,
                    widget.Memory(format='Mem: {MemPercent}%'), sep,
                    widget.PulseVolume(volume_app="pavucontrol"), sep,
                    Todo(), sep,
                    # Ticky(),

                ],
                18,
                background=bg
                ),
            wallpaper=solunar(longi, lati),
            wallpaper_mode="fill"
            ),
        Screen(
            top=bar.Bar(
                [
                    widget.CurrentLayout(),
                    widget.WindowName(),
                    ],
                18
                ),
            wallpaper=solunar(longi, lati),
            wallpaper_mode="fill"
            )
]


@hook.subscribe.startup_complete
def autostart():
    subprocess.run('/home/daewi/.config/qtile/autostart.sh')


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

kgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "QTILE"
