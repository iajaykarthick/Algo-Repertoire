class Array:

    n = 0
    arr = []

    def print_array(self):
        print(self.arr)

    def get_user_input(self):
        self.n = int(input('Enter the size of array: '))
        print('Enter the elements of array in next line (space separated)')
        self.arr = list(map(int, input().split()))
