
def get_data():
    my_file = open('nationsPop.txt', 'r')
    lines = my_file.readlines()
    country_data = []
    for country_line in lines:
        country_line = country_line.strip()
        nation_pop_list = country_line.split(',')
        pop_dictionary = {'Name': nation_pop_list[0],
                          'pop': int(nation_pop_list[1]),
                          'change': float(nation_pop_list[2])
                          }
        country_data.append(pop_dictionary)
    return country_data

def print_menu():
    print("========Please select from the following=========")
    print("[1] Find the largest country")
    print("[2] Find the smallest country")
    print("[3] Add a new country")
    print("[4] Quit")
    print("=================================================")

def find_largest(country_data):
    largest_so_far = country_data[0]
    for current_country in country_data:
        if current_country['pop'] > largest_so_far['pop']:
            largest_so_far = current_country
    print("+++++++++++++++++")
    print(f"The largest country is {largest_so_far['Name']} with population {largest_so_far['pop']}")


def process_user_input(user_input, nations_pop):
    if user_input == '1':
        find_largest(nations_pop)
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input=='4':
        exit(0)
    else:
        print("Please select 1-4")

def main():
    country_list = get_data()
    while True:
        print_menu()
        user_choice = input("Please enter the number of your selection:")
        process_user_input(user_choice, country_list)
main()