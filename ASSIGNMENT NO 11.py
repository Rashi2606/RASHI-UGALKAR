# Input parameters

influent_flow_rate = float(input("Enter influent flow rate (0) En MGD: ")) 
influent_BOD = float(input("Enter influent BOD (5 in) in mg/L: ")) 
waste_sludge_flow_rate = float(input("Enter waste sludge flow rate (W) in MGD: ")) 
biomass_concentration = float(input("Enter biomass concentration (X) in mg/L: ")) 
volume_areation_tank = float(input("Enter volume of areation tank (V) in m^3: ")) 
waste_sludge_suspended_solids = float(input("Enter waste sludge suspended solids (Xu) in mg/L: ")) 
effluent_suspended_solids = float(input("Enter effluent suspended soldis (Xe) in mg/L: "))
effluent_BOD= float(input("Enter effluent BOD (Ye) in mg/L: ")) 
#Calculate F/M Ratio 
FM_ratio = ((influent_BOD*influent_flow_rate)/(volume_areation_tank*biomass_concentration))

# Calculate MCRT
MCRT = (volume_areation_tank*biomass_concentration)/(((waste_sludge_flow_rate*waste_sludge_flow_rate)))

#Calculate HDT
HDT = (volume_areation_tank/influent_flow_rate)

#calculate BOD removal efficiency
efficiency = ((influent_BOD-effluent_BOD)/influent_BOD)*100

#Output results
print(f"1) Food to microorganism Ratio(F/M Ratio): {FM_ratio:.2f} g BOD/g MLSS/day")
print(f"2) Mean Cell Residence Time (MCRT): {MCRT:.2f} days")
print(f"3) Hydraulic Detention Time (HDT): {HDT:.2f} days")
print(f"4) B.O.D Removal Efficiency : {efficiency:.2f}%")