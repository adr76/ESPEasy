Import("env")
import os

# access to global construction environment
#print env

# Dump construction environment (for debug purpose)
#print env.Dump()

# append extra flags to global build environment
# which later will be used to build:
# - project source code
# - frameworks
# - dependent libraries

#env.Append(CPPDEFINES=[
  # ,"NO_HTTP_UPDATER"
  # ,("WEBSERVER_RULES_DEBUG", "0")
#])

#if os.path.isfile('src/Custom.h'):
#  env.Append(CPPDEFINES=["USE_CUSTOM_H"])

env.Append(CPPDEFINES=[
  #"BUILD_GIT='Outdoor-light-unit'",
    
	#"CONTROLLER_SET_ALL",
	"CONTROLLER_SET_NONE",
	"NOTIFIER_SET_NONE",
	"PLUGIN_SET_NONE",
	#"PLUGIN_SET_ONLY_SWITCH",
	"USES_P001",  # Switch
	#"USES_P002",  # ADC
	"USES_P003",  # Pulse
	"USES_P004",  # Dallas DS18b20
	"USES_P005",  # DHT
	#"USES_P010",  # BH1750
	#"USES_P019",  # PCF8574
	#"USES_P020",  # Ser2Net
	"USES_P021",  # Level
	#"USES_P025",  # ADS1115
	"USES_P026",  # SysInfo
	#"USES_P028",  # BME280
	"USES_P029",  # Output
	#"USES_P031",  # SHT1X
	#"USES_P036",  # FrameOLED
	"USES_P037",  # MQTTImport
	#"USES_P049",  # MHZ19
	#"USES_P052",  # SenseAir
	#"USES_P056",  # SDS011-Dust
	#"USES_P059",  # Encoder
	#"USES_P061",  # Keypad
	#"USES_P064",  # APDS9960 Gesture
	#"USES_P067",  # HX711_Load_Cell
	#"USES_P075",  # Nextion
	"USES_P081",  # Cron
	#"USES_P082",  # GPS
	#"USES_P085",  # AcuDC24x
	#"USES_P087",  # Serial Proxy
    
  # RF433  
	"USES_P111",  # RF Input
	#"USES_P112",  # RF Output

	"USES_C005",   # Home Assistant (openHAB) MQTT
	"USES_C008",   # Generic HTTP
	"USES_C010",   # Generic UDP
	"USES_C011",   # Generic HTTP Advanced
	"USES_C013",   # ESPEasy P2P network
	#"USES_C014",   # homie 3 & 4dev MQTT
	"USES_C016",  # Cache Controller
	#"USES_C018",  # TTN/RN2483
])



my_flags = env.ParseFlags(env['BUILD_FLAGS'])
my_defines = my_flags.get("CPPDEFINES")
#defines = {k: v for (k, v) in my_defines}

print("\u001b[32m Custom PIO configuration check \u001b[0m")
# print the defines
print("\u001b[33m CPPDEFINES: \u001b[0m  {}".format(my_defines))
print("\u001b[33m Custom CPPDEFINES: \u001b[0m  {}".format(env['CPPDEFINES']))
print("\u001b[32m ------------------------------- \u001b[0m")


if (len(my_defines) == 0):
  print("\u001b[31m No defines are set, probably configuration error. \u001b[0m")
  raise ValueError



