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
#     double lon2;
#     double lat2;
#     double reverse_azimuth;
#     double reduced_length;
#     // double geodesic_scale;
# };
#
# struct expected_results
# {
#     coordinates p1;
#     double distance;
#     double azimuth12;
#     expected_result karney;
# };
# 
# An example entry:
# 
#     {
#         { 0, 0 }, 250000, 0,
#         { 0.00000000000000000000, 2.26091191238511868278, 0.00000000000000000000, 249935.55905595037620514631, 0.99922674639115516282 },
#     }

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
f"""        {{ {values["lon1"]}, {values["lat1"]} }}, {values["distance"]}, {values["azi1"]},
        {{ {values["lon2"]}, {values["lat2"]}, {values["azi2"]}, {values["reduced_length"]}, {values["geodesic_scale"]} }}
    }},{{
"""
        print(out_entry, end="")

print("};", end="")
