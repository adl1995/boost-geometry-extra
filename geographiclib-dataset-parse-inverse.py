# Parse the GeodTest dataset for antipodal points
# 
# Input format: 
# 
# latitude1, longitude1, azimuth1, latitude2, longitude2, azimuth2, distance, arc distance, reduced length, area
# 
# An example entry:
# 
# 36.530042355041 0 176.125875162171 -48.164270779097768864 5.762344694676510456 175.334308316285410561 9398502.0434687 84.663858149358862201 6333544.7732452481809 -559418252332.321555
# 
# Output format:
# 
# struct coordinates
# {
#     double lon;
#     double lat;
# };
# 
# struct expected_result
# {
#     double distance;
#     double azimuth;
#     double reverse_azimuth;
#     double reduced_length;
#     double geodesic_scale;
# };
# 
# struct expected_results
# {
#     coordinates p1;
#     coordinates p2;
#     expected_result reference; // karney or vincenty
#     expected_result vincenty;
#     expected_result thomas;
#     expected_result andoyer;
# 
# };
# 
# An example entry:
# 
#    {
#        { 0, 31.394417440639 }, { 179.615601631202912322, -31.275540610835465807 },
#        { 19980218.4055399, 34.266322930672, 145.782701113414306756, 49490.8807994496209, -0.996116451012525883079717914370121434 }
#    }

keys = ["lat1", "lon1", "azi1", "lat2", "lon2", "azi2", "distance", "arc_distance", "reduced_length", "area", "geodesic_scale"]

var_declaration = """expected_results expected[] =
{
    {
"""
print(var_declaration, end="")

with open("GeodTest-antipodal.dat", "r") as in_file:
    for line in in_file:
        # Splits on " " by default.
        data = line.split()
        values = dict(zip(keys, data))

        out_entry = \
f"""        {{ {values["lon1"]}, {values["lat1"]} }}, {{ {values["lon2"]}, {values["lat2"]} }},
        {{ {values["distance"]}, {values["azi1"]}, {values["azi2"]}, {values["reduced_length"]}, {values["geodesic_scale"]} }}
    }},{{
"""
        print(out_entry, end="")

print("};", end="")
