# 6)Furniture:
# Household type, total area and furniture name list The new house has no furniture at all.
# Furniture has a name and area,
# of whichBed: 4 square metersWardrobe: 2 square metersTable:
# 1.5 square meters
# Add the above three pieces of furniture to the house
# When printing a house, output is required: household type, total area, remaining area,
# furniture name list.


class House:
    area = 120
    household_type = 'Full family '
    print(f"Household type: {household_type}")
    print("Total area of apartment: " + str(area))

    def __init__(self, furniture):
        self.all_furniture = furniture
        self.first_bed = all_furniture[0]
        self.second_bed = all_furniture[1]
        self.wardrope = all_furniture[2]
        self.table = all_furniture[3]
        self.chairs = all_furniture[4]
        self.total_area = 0
        self.type = " "
    
    def count_area(self,b1,b2,wrd,tbl,chrs):
        self.total_area = b1 + b2 + wrd + tbl + chrs
        print(f"Total furniture area: {self.total_area}")

    def final_output(self):
        self.household_type = "Full family "
        self.remaining_area = self.area - self.total_area
        return " - ".join((str(self.remaining_area), " - ".join(self.all_furniture), " ", self.type))

all_furniture = ["First bed", "Second bed", "Wardrope", "Table", "Chair"]
house = House(all_furniture)
house.count_area(4,5,2,1.5,1)

print("Remaining area: " + house.final_output())
