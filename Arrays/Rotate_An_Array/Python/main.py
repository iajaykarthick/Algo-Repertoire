from rotateAnArray import RotateAnArray

def main():
    r = RotateAnArray()
    r.get_user_input()
    r.calc_subset_based_on_direction()
    r.rotate_array()
    r.print_array()
    
if __name__ == "__main__":
    main()