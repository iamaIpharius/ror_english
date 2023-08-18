import os
import re

template = """
set_technology = {
	infantry_weapons = 1
	infantry_weapons1 = 1
	tech_support = 1
	tech_engineers = 1
	tech_recon = 1
	tech_field_hospital = 1
	tech_logistics_company = 1
	tech_military_police = 1
	tech_maintenance_company = 1
	basic_train = 1
	armored_train = 1
	railway_gun = 1
	wartime_train = 1
	
	gw_artillery = 1
	artillery1 = 1
	
	early_fighter = 1
	fighter1 = 1
	airship_bomber = 1
	early_bomber = 1
	scout_plane = 1
	aircraft_engine = 1
	tank_design = 1
	mechanical_engineering = 1
		interwar_artillery = 1
		howitzer1 = 1
		infantry_weapons2 = 1
		improved_infantry_weapons = 1
		support_weapons = 1
		support_weapons2 = 1
		motorised_infantry = 1
		#doctrines
		# trench_warfare = 1
		# machine_gun_defence = 1
		# cavalry_support = 1
		# mobile_support = 1
		# trade_interdiction = 1
		# convoy_interdiction_ti = 1
		# unrestricted_submarine_warfare = 1
		# raider_patrols = 1
		#air
		# formation_flying = 1
		#electronics
		electrical_engineering = 1
		radio = 1
		analytical_engine = 1
		generator_battery = 1
		basic_cryptography = 1
		basic_cryptanalysis = 1
		#industry
		early_machine_tools = 1
		machine_tools2 = 1
		fortification1 = 1
		fortification2 = 1
		excavation1 = 1
		excavation2 = 1
		oil_production1 = 1
		oil_production2 = 1
		fuel_silos = 1
		construction1 = 1
		construction2 = 1
		industrial_complex1 = 1
		dispersed_industry = 1
		dispersed_industry2 = 1
}
if = {
	limit = {
		has_dlc = "No Step Back"
	}
	set_technology = {
		early_armored_car = 1
		basic_armored_car = 1
	}
}
if = {
	limit = {
		NOT = {
			has_dlc = "No Step Back"
		}
	}
	set_technology = {
		legacy_early_armored_car = 1
		legacy_basic_armored_car = 1
	}
}
if = {
	limit = {
		NOT = {
			has_dlc = "Man the Guns"
		}
	}
	set_technology = {
		early_destroyer = 1
		early_heavy_cruiser = 1
		early_battleship = 1
		early_light_cruiser = 1
		early_submarine = 1
		basic_destroyer = 1
		basic_heavy_cruiser = 1
		basic_heavy_cruiser = 1
		basic_battleship = 1
		basic_light_cruiser = 1
		basic_submarine = 1
	}
}
if = {
	limit = {
		has_dlc = "Man the Guns"
	}
	set_technology = {
		early_ship_hull_light = 1
		basic_ship_hull_light = 1
		early_ship_hull_cruiser = 1
		basic_ship_hull_cruiser = 1
		basic_cruiser_armor_scheme = 1
		early_ship_hull_heavy = 1
		basic_ship_hull_heavy = 1
		basic_heavy_armor_scheme = 1
		early_ship_hull_submarine = 1
		basic_ship_hull_submarine = 1
		basic_battery = 1
		basic_light_battery =1
		basic_medium_battery = 1
		basic_heavy_battery = 1
		basic_secondary_battery = 1
		basic_torpedo = 1
	}
}
"""

old_text_pattern = r'set_technology = \{\s(.*)\}'


def get_nums(file):
    start_num = 0
    end_num = 0
    for num_line, line in enumerate(file):
        if line.startswith("set_technology"):
            start_num = num_line
        elif line.startswith("}") and end_num < start_num:
            end_num = num_line
            break
        else:
            continue
    return start_num, end_num


directory = os.getcwd()
print(directory)
for filename in os.listdir(directory):
    if filename.endswith(".txt"):

        with open(filename, 'r') as f:
            text = f.read()
            numbers = get_nums(f)
            print(filename, numbers)
