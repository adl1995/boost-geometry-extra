/**
 * This script is designed to work with GeodTest dataset
 * associated with GeographicLib.
 *
 * Link: https://zenodo.org/record/32156
 *
 * Geodesic scale (M12) is absent in the above dataset. This script
 * computes M12 to add the missing values. 
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <numeric>
#include <iomanip>
#include <vector>

#include <GeographicLib/Geodesic.hpp>

using namespace GeographicLib;

int main() {

  // Objects for file reading.
  std::string line;
  std::ifstream infile("GeodTest-antipodal.dat");

  // This will temporarily hold the data values.
  double dataField;
  
  const Geodesic& geod = Geodesic::WGS84();

  double lat2, lon2, azi2, s12, m12, M12, M21, S12;

  std::cout << std::setprecision(25);
  while (std::getline(infile, line))
  {
    std::istringstream iss(line);

    // Push the space separated values in a vector.
    std::vector<double> geoData;
    while (iss >> dataField) { geoData.push_back(dataField); }

    // lat1 lon1 azi1 s12
    geod.Direct(geoData[0], geoData[1], geoData[2], geoData[6], lat2, lon2, azi2, m12, M12, M21, S12);

    // cout << lat2 << " " << lon2 << " " << azi2 << " " << m12 << " " << M12 << " " << M21 << std::endl;
    std::cout << M21 << std::endl;
  }

  // Reset the file buffer.
  infile.clear();
  infile.seekg(0, infile.beg);
}
