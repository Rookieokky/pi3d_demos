""" This is the config file used by PictureFrame. It allows settings to be changed
on the command line when the program is run, or you can alter the default values
here
"""
import argparse

""" function needed to convert str representation of bool values
"""
def str_to_bool(x):
    if len(x) == 0:
        return True # i.e. just arg will set to true
    return not (x.lower()[0] in ('0', 'f', 'n')) # i.e. 0,False,false,No,n

def str_to_tuple(x):
    return tuple(float(v) for v in x.replace("(","").replace(")","").split(","))

# NB the reason that absolute paths are used here is because relative ones can lead
#  to abiguity if the program is started automatically on boot.
parse = argparse.ArgumentParser("start running a picture frame")
parse.add_argument("-a", "--blur_amount",   default=12, type=float, help="larger values than 12 will increase processing load quite a bit")
parse.add_argument("-b", "--blur_edges",    default=False, type=str_to_bool, help="use blurred version of image to fill edges - will override FIT = False")
parse.add_argument("-c", "--check_dir_tm",  default=60.0, type=float, help="time in seconds between checking if the image directory has changed")
parse.add_argument("-d", "--verbose",       default=False, type=str_to_bool, help="show try/exception messages")
parse.add_argument("-e", "--edge_alpha",    default=0.5, type=float, help="background colour at edge. 1.0 would show reflection of image")
parse.add_argument("-f", "--fps",           default=20.0, type=float)
parse.add_argument("-g", "--background",    default=(0.2, 0.2, 0.3, 1.0), type=str_to_tuple, help="RGBA to fill edges when fitting")
parse.add_argument("-j", "--blend_type",    default="blend", choices=["blend", "burn", "bump"], help="type of blend the shader can do")
parse.add_argument("-k", "--keyboard",      default=False, type=str_to_bool, help="set to False when running headless to avoid curses error. True for debugging")
parse.add_argument("-m", "--use_mqtt",      default=False, type=str_to_bool)
parse.add_argument("-n", "--recent_n",      default=10, type=int, help="when shuffling the keep n most recent ones to play before the rest")
parse.add_argument("-o", "--font_file",     default="/home/pi/pi3d_demos/fonts/NotoSans-Regular.ttf")
parse.add_argument("-p", "--pic_dir",       default="/home/pi/pi3d_demos/textures")
parse.add_argument("-q", "--shader",        default="/home/pi/pi3d_demos/shaders/blend_new")
parse.add_argument("-r", "--reshuffle_num", default=5, type=int, help="times through before reshuffling")
parse.add_argument("-s", "--show_names",    default=False, type=str_to_bool, help="text over image with file name")
parse.add_argument("-t", "--fit",           default=True, type=str_to_bool, help="shrink to fit screen i.e. don't crop")
parse.add_argument("-u", "--kenburns",      default=False, type=str_to_bool, help="will set FIT->False and BLUR_EDGES->False")
parse.add_argument("-v", "--time_delay",    default=10.0, type=float, help="time between consecutive slide starts - can be changed by MQTT")
parse.add_argument("-w", "--fade_time",     default=4.0, type=float, help="change time during which slides overlap - can be changed by MQTT")
parse.add_argument("-x", "--shuffle",       default=False, type=str_to_bool, help="shuffle on reloading image files - can be changed by MQTT")
parse.add_argument("-y", "--subdirectory",  default="", help="subdir of pic_dir - can be changed by MQTT")
parse.add_argument("-z", "--blur_zoom",     default=1.0, type=float, help="must be >= 1.0 which expands the backgorund to just fill the space around the image")
args = parse.parse_args()

BLEND_OPTIONS = {"blend":0.0, "burn":1.0, "bump":2.0} # that work with the blend_new fragment shader
## set uppercase CONST style variables that can be accessed from PictureFrame
BLUR_AMOUNT = args.blur_amount
BLUR_EDGES = args.blur_edges
CHECK_DIR_TM = args.check_dir_tm
VERBOSE = args.verbose
EDGE_ALPHA = args.edge_alpha
FPS = args.fps
BACKGROUND = args.background
BLEND_TYPE = BLEND_OPTIONS[args.blend_type]
KEYBOARD = args.keyboard
USE_MQTT = args.use_mqtt
RECENT_N = args.recent_n
FONT_FILE = args.font_file
PIC_DIR = args.pic_dir
SHADER = args.shader
RESHUFFLE_NUM = args.reshuffle_num
SHOW_NAMES = args.show_names
FIT = args.fit
KENBURNS = args.kenburns
TIME_DELAY = args.time_delay
FADE_TIME = args.fade_time
SHUFFLE = args.shuffle
SUBDIRECTORY = args.subdirectory
BLUR_ZOOM = args.blur_zoom

CODEPOINTS = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ., _-/' # limit to 49 ie 7x7 grid_size