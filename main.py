import csv


class Animal_Info:
    
    def __init__(self):
        request = input("Please input an animal type (choose \"dogs\" or \"cats\"):  ")
        self.request = request
        try:
            with open(f'data/{self.request}.csv') as test_open:
                pass
        except:
            print(f"Sorry, we don\'t have any \"{self.request}\".")
            return
        self.get_animal_info()
                
    def get_animal_info(self):
        with open(f'data/{self.request}.csv') as csvfile:
            csv_reader = csv.DictReader(csvfile, skipinitialspace=True)
            for each_animal in csv_reader:
                print(f"{each_animal['name']} is a {each_animal['age']} year old {each_animal['breed']}")
                
Animal_Info()