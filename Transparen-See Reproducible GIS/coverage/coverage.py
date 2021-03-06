# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# coverage.py
# Created on: 2022-02-24 15:57:49.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
test = "test"
test_Buffer3 = "C:\\Users\\Jli\\Documents\\ArcGIS\\Default.gdb\\test_Buffer3"
ndvp_edm_nooverlaps = "ndvp_edm_nooverlaps"
test_Buffer3_Intersect = "C:\\Users\\Jli\\Documents\\ArcGIS\\Default.gdb\\test_Buffer3_Intersect"
Test_Buffer_Intersect_Dissolve_shp = "C:\\Users\\Jli\\Desktop\\Ziwei\\Test Buffer Intersect Dissolve.shp"

# Process: Buffer
arcpy.Buffer_analysis(test, test_Buffer3, "700 Meters", "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Intersect
arcpy.Intersect_analysis("C:\\Users\\Jli\\Documents\\ArcGIS\\Default.gdb\\test_Buffer3 #;ndvp_edm_nooverlaps #", test_Buffer3_Intersect, "ALL", "", "INPUT")

# Process: Dissolve
arcpy.Dissolve_management(test_Buffer3_Intersect, Test_Buffer_Intersect_Dissolve_shp, "", "", "MULTI_PART", "DISSOLVE_LINES")

