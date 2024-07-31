from shapely.geometry import Polygon

def get_filled_regions(input_path):
    filled_regions = []
    
    for region in input_path:
        is_enclosed = True
        for other_region in input_path:
            if region != other_region and region.within(other_region):
                is_enclosed = False
                break
        if is_enclosed:
            filled_regions.append(region)
    
    return filled_regions
