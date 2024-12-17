
def parse_map(data, line):
    arr = []
    line += 1
    while line < len(data) and data[line].strip() != "":
        arr += [[int(d) for d in data[line].split() if d != " "]]
        line += 1
    line += 1

    return arr, line

def lookup_map(arr, val):
    if not arr:
        return val

    for dest, src, rng in arr:
        if src <= val <= src + rng:
            diff = val - src
            target = dest + diff
            return target

    return val

def lookup_map_2(arr, val, range):
    if not arr:
        return val

    res = []

    for dest, src, rng in arr:
        # if to the left of (src + rng)
        if val <= src <= val + range <= src + rng:
            diff = val + range - src
            res += [(dest, diff)]
            range -= diff
        # if to the right of (src + rng)
        elif src <= val <= src + rng <= val + range:
            diff = (src + rng) - val
            offset = val - src
            res += [(dest + offset, diff)]
            val += diff
        # if we are in the middle of (src + rng)
        elif src <= val <= val + range <= src + rng:
            offset = val - src
            res += [(dest + offset, range)]
            range = 0
            break
        # if (src + rng) is in the middle of us
        elif val <= src <= src + rng <= val + range:
            res += [(dest, rng)]
            res += lookup_map_2(arr, val, src - val)
            res += lookup_map_2(arr, src + rng, val + range - (src + rng))
            return res
    if range > 0:
        res += [(val, range)]
    return res

def solution(data):
    seeds = [int(s) for s in data[0].split(":")[1].split()]

    line = 2
    seed_to_soil, line = parse_map(data, line)
    soil_to_fertilizer, line = parse_map(data, line)
    fertilizer_to_water, line = parse_map(data, line)
    water_to_light, line = parse_map(data, line)
    light_to_temparature, line = parse_map(data, line)
    temparature_to_humidity, line = parse_map(data, line)
    humitidy_to_location, line = parse_map(data, line)

    min_location = float("inf")
    for s in seeds:
        soil = lookup_map(seed_to_soil, s)
        if soil:
            fertilizer = lookup_map(soil_to_fertilizer, soil)
            if fertilizer:
                water = lookup_map(fertilizer_to_water, fertilizer)
                if water:
                    light = lookup_map(water_to_light, water)
                    if light:
                        temparature = lookup_map(light_to_temparature, light)
                        if temparature:
                            humidity = lookup_map(temparature_to_humidity, temparature)
                            if humidity:
                                location = lookup_map(humitidy_to_location, humidity)
                                print("seed %d found in location %d" % (s, location))
                                min_location = min(min_location, location)

    return min_location

# range testing - pass ranges down from map to map
def solution2(data):
    seeds = [int(s) for s in data[0].split(":")[1].split()]
    paired = []
    for i in range(0, len(seeds), 2):
        paired += [[seeds[i], seeds[i + 1]]]

    line = 2
    seed_to_soil, line = parse_map(data, line)
    soil_to_fertilizer, line = parse_map(data, line)
    fertilizer_to_water, line = parse_map(data, line)
    water_to_light, line = parse_map(data, line)
    light_to_temparature, line = parse_map(data, line)
    temparature_to_humidity, line = parse_map(data, line)
    humitidy_to_location, line = parse_map(data, line)

    min_location = float("inf")
    # pass down ranges from map to map
    for s, r in paired:
        for soil, soil_rng in lookup_map_2(seed_to_soil, s, r):
            for fertilizer, fertilizer_rng in lookup_map_2(soil_to_fertilizer, soil, soil_rng):
                for water, water_rng in lookup_map_2(fertilizer_to_water, fertilizer, fertilizer_rng):
                    for light, light_rng in lookup_map_2(water_to_light, water, water_rng):
                        for temparature, temperature_rng in lookup_map_2(light_to_temparature, light, light_rng):
                            for humidity, humidity_rng in lookup_map_2(temparature_to_humidity, temparature, temperature_rng):
                                for location, location_rng in lookup_map_2(humitidy_to_location, humidity, humidity_rng):
                                    print("location range found: %d, %d" % (location, location_rng))
                                    if (location != 0):
                                        min_location = min(min_location, location)

    return min_location

if __name__ == "__main__":
    with open("/Users/chou/source/workspace/aoc2023/day4/input1.txt", "r") as file:
        data = file.readlines()

    #print(solution(data))
    print(solution2(data))